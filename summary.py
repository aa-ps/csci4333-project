import sqlite3
from tabulate import tabulate

con = sqlite3.connect("original_db.db")

cur = con.cursor()

QUERY_ONE = """SELECT name, ssn FROM no_town"""

res = cur.execute(QUERY_ONE)

rows = res.fetchall()

relational_schema = [x[0] for x in res.description]

print(tabulate(rows, headers=relational_schema))

print(len(rows))

QUERY_TWO = """SELECT name, ssn FROM no_town"""

res = cur.execute(QUERY_TWO)

rows = res.fetchall()

relational_schema = [x[0] for x in res.description]

print(tabulate(rows, headers=relational_schema))

print(len(rows))

QUERY_THREE = """SELECT name, ssn FROM no_town"""

res = cur.execute(QUERY_THREE)

rows = res.fetchall()

relational_schema = [x[0] for x in res.description]

print(tabulate(rows, headers=relational_schema))

print(len(rows))

QUERY_FOUR = """SELECT name, ssn FROM no_town"""

res = cur.execute(QUERY_FOUR)

rows = res.fetchall()

relational_schema = [x[0] for x in res.description]

print(tabulate(rows, headers=relational_schema))

print(len(rows))

con.close()
