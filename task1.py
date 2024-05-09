import sqlite3
import csv

with sqlite3.connect("original_db.db") as con:
    cur = con.cursor()

    with con:
        CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS no_town(
            street_number TEXT,
            street_name TEXT,
            street_type TEXT,
            musician_name TEXT,
            musician_ssn TEXT,
            album_id INTEGER,
            album_title TEXT,
            album_date INTEGER,
            album_format TEXT,
            instrument_id INTEGER,
            instrument_name TEXT,
            instrument_key TEXT
        );'''

        cur.execute(CREATE_TABLE)
        
        with open("no_town.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
        
            insert_query = "INSERT INTO no_town VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            
            data = [tuple(row) for row in reader]
            cur.executemany(insert_query, data)

    # To verify the data was transferred correctly.

    # TEST_QUERY = 'SELECT * FROM no_town'

    # res = cur.execute(TEST_QUERY).fetchall()

    # if res:
    #     relational_schema = [x[0] for x in cur.description]
    #     print(tabulate(res, headers=relational_schema))
    # else:
    #     print("No data available.")
