import sqlite3
from tabulate import tabulate

def execute_and_print_query(cur, query):
    res = cur.execute(query)
    rows = res.fetchall()
    relational_schema = [x[0] for x in res.description]
    print(tabulate(rows, headers=relational_schema))
    print(len(rows), "\n")

with sqlite3.connect("original_db.db") as con:
    cur = con.cursor()

    print("Musicians:")
    execute_and_print_query(cur, "SELECT name, ssn FROM musician")
    
    print("Albums:")
    execute_and_print_query(cur, "SELECT title, id FROM album")
    
    print("Instruments:")
    execute_and_print_query(cur, "SELECT name, key, id FROM instrument")
    
    print("Total Albums per Musician:")
    execute_and_print_query(cur, """
        SELECT name, COUNT(*) AS total_albums
        FROM musician NATURAL JOIN instrumentalbum
        GROUP BY(ssn)
    """)
