import sqlite3
from tabulate import tabulate

with sqlite3.connect("original_db.db") as con:
    cur = con.cursor()
    
    CREATE_STATEMENTS = """
    CREATE TABLE IF NOT EXISTS musician(
        ssn TEXT,
        name TEXT,
        street_number TEXT,
        street_name TEXT,
        street_type TEXT,
        PRIMARY KEY(ssn)
    );
    
    CREATE TABLE IF NOT EXISTS instrument(
        id TEXT,
        name TEXT,
        key TEXT,
        PRIMARY KEY(id)
    );
    
    CREATE TABLE IF NOT EXISTS album(
        id TEXT,
        title TEXT,
        date INTEGER,
        format TEXT,
        PRIMARY KEY(id)
    );
    
    CREATE TABLE IF NOT EXISTS musicalbum(
        ssn TEXT,
        id TEXT,
        PRIMARY KEY(ssn, id),
        FOREIGN KEY(ssn) REFERENCES musician(ssn),
        FOREIGN KEY(id) REFERENCES album(id)
    );
    
    CREATE TABLE IF NOT EXISTS instrumentalbum(
        albumid TEXT,
        instrumentid TEXT,
        ssn TEXT,
        PRIMARY KEY(albumid, instrumentid, ssn),
        FOREIGN KEY(albumid) REFERENCES album(id),
        FOREIGN KEY(instrumentid) REFERENCES instrument(id),
        FOREIGN KEY(ssn) REFERENCES musician(ssn)
    );
    """
    
    cur.executescript(CREATE_STATEMENTS)
    
    res = cur.execute("SELECT * FROM no_town").fetchall()
    
def insert_into_table(cur, table, values):
    placeholders = ', '.join('?' * len(values))
    cur.execute(f"INSERT OR IGNORE INTO {table} VALUES ({placeholders})", values)
    
with con:
    for row in res:
        insert_into_table(cur, "musician", (row[4], row[3], row[0], row[1], row[2]))
        insert_into_table(cur, "instrument", (row[9], row[10], row[11]))
        insert_into_table(cur, "album", (row[5], row[6], row[7], row[8]))
        insert_into_table(cur, "musicalbum", (row[4], row[5]))
        insert_into_table(cur, "instrumentalbum", (row[5], row[9], row[4]))

