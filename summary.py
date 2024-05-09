import sqlite3
from tabulate import tabulate # I use tabulate to make the output easier to read. To install, run 'pip install tabulate' on the terminal to install the library.

# This function executes the query on the new_db.db and outputs the results with its count.
# Uses tabulate to format the output.
def execute_and_print_query(cur, query):
    res = cur.execute(query)
    rows = res.fetchall()
    relational_schema = [x[0] for x in res.description]
    print(tabulate(rows, headers=relational_schema))
    print("Total Records:", len(rows), "\n")

with sqlite3.connect("new_db.db") as con:
    cur = con.cursor()

    # Queries needed to get the information required for the summary.
    musician_query = "SELECT musician_name, musician_ssn FROM musician;"
    album_query = "SELECT album_title, album_id FROM album;"
    instrument_query = "SELECT instrument_name, instrument_key, instrument_id FROM instrument;"
    album_count_by_musician_query = """
    SELECT m.*, COUNT(p.album_id) AS album_count
    FROM musician m
    JOIN produced p ON m.musician_ssn = p.musician_ssn 
    GROUP BY m.musician_ssn;
    """

    # Execute each query and print its result.
    print("Musicians:")
    execute_and_print_query(cur, musician_query)

    print("Albums:")
    execute_and_print_query(cur, album_query)

    print("Instruments:")
    execute_and_print_query(cur, instrument_query)

    print("Album Count by Musician:")
    execute_and_print_query(cur, album_count_by_musician_query)
