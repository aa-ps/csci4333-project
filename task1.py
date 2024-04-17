import sqlite3
import csv
from tabulate import tabulate

con = sqlite3.connect("original_db.db")

cur = con.cursor()

CREATE_TABLE = '''CREATE TABLE no_town(
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
    data = [tuple(row) for row in reader]
    cur.executemany("INSERT INTO no_town VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

TEST = '''SELECT * FROM no_town WHERE date=2010'''

res = cur.execute(TEST)

relational_schema = [x[0] for x in res.description]

print(tabulate(res, headers=relational_schema))