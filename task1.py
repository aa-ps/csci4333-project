import sqlite3
import csv
from tabulate import tabulate

with sqlite3.connect("original_db.db") as con:
    cur = con.cursor()

    with con:
        CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS no_town(
            num TEXT,
            street TEXT,
            street_type TEXT,
            name TEXT,
            ssn TEXT,
            album_id INTEGER,
            title TEXT,
            date INTEGER,
            album_type TEXT,
            instrument_id INTEGER,
            instrument_type TEXT,
            key TEXT
        );'''

        cur.execute(CREATE_TABLE)
        
        with open("no_town.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
        
            insert_query = "INSERT INTO no_town VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            
            data = [tuple(row) for row in reader]
            cur.executemany(insert_query, data)

    TEST_QUERY = 'SELECT * FROM no_town'

    res = cur.execute(TEST_QUERY).fetchall()

    if res:
        relational_schema = [x[0] for x in cur.description]
        print(tabulate(res, headers=relational_schema))
    else:
        print("No data available.")
