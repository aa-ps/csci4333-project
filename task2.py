import sqlite3
from tabulate import tabulate

con = sqlite3.connect("original_db.db")
cur = con.cursor()


CREATE_MUSICIANS = """
CREATE TABLE musician(
    ssn TEXT,
    name TEXT,
    street_number TEXT,
    street_name TEXT,
    street_type TEXT,
    PRIMARY KEY(ssn)
);
"""

CREATE_INSTRUMENTS = """
CREATE TABLE instrument(
    id TEXT,
    name TEXT,
    key TEXT,
    PRIMARY KEY(id)
);
"""

CREATE_ALBUMS = """
CREATE TABLE album(
    id TEXT,
    title TEXT,
    date INTEGER,
    format TEXT,
    PRIMARY KEY(id)
);
"""

CREATE_MUSICALBUMS = """
CREATE TABLE musicalbum(
    ssn TEXT,
    id TEXT,
    PRIMARY KEY(ssn, id),
    FOREIGN KEY(ssn) REFERENCES musician(ssn),
    FOREIGN KEY(id) REFERENCES album(id)
);
"""

CREATE_INSTRUMENTALBUMS = """
CREATE TABLE instrumentalbum(
    albumid TEXT,
    instrumentid TEXT,
    PRIMARY KEY(albumid, instrumentid),
    FOREIGN KEY(albumid) REFERENCES album(id),
    FOREIGN KEY(instrumentid) REFERENCES instrument(id)
);
"""

cur.execute(CREATE_MUSICIANS)
cur.execute(CREATE_INSTRUMENTS)
cur.execute(CREATE_ALBUMS)
cur.execute(CREATE_MUSICALBUMS)
cur.execute(CREATE_INSTRUMENTALBUMS)

con.commit()

res = cur.execute("SELECT * FROM no_town").fetchall()

def insert_into_table(cur, table, values):
    placeholders = ', '.join('?' * len(values))
    cur.execute(f"INSERT OR IGNORE INTO {table} VALUES ({placeholders})", values)


for row in res:
    musician_data = (row[4], row[3], row[0],
                     row[1], row[2])
    instrument_data = (row[9], row[10], row[11])
    album_data = (row[5], row[6], row[7], row[8])
    
    
    insert_into_table(cur, "musician", musician_data)
    insert_into_table(cur, "instrument", instrument_data)
    insert_into_table(cur, "album", album_data)


res = cur.execute("SELECT * FROM musician")
relational_schema = [x[0] for x in res.description]
print(tabulate(res, headers=relational_schema))

res = cur.execute("SELECT * FROM instrument")
relational_schema = [x[0] for x in res.description]
print(tabulate(res, headers=relational_schema))

res = cur.execute("SELECT * FROM album")
relational_schema = [x[0] for x in res.description]
print(tabulate(res, headers=relational_schema))