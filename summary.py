import sqlite3
from tabulate import tabulate # I use tabulate to make the output easier to read. To install, run 'pip install tabulate' on the terminal to install the library.

# This function executes the query on the new_db.db and outputs the results with its count.
# Uses tabulate to format the output.
def execute_and_print_query(cur, query):
    res = cur.execute(query)
    rows = res.fetchall()
    relational_schema = [x[0] for x in res.description]
    print(tabulate(rows, headers=relational_schema))

# We could have just gotten the length of fetchall result from the function above, but here we are using the SQL COUNT().
def count_query_results(cur, count_query):
    count_res = cur.execute(count_query)
    count = count_res.fetchone()[0]
    return count


with sqlite3.connect("new_db.db") as con:
    cur = con.cursor()

    # Queries needed to get the information required for the summary.

    musician_query = "SELECT name, ssn FROM musician;"
    musician_count_query = "SELECT COUNT(*) FROM musician;"

    album_query = "SELECT title AS name, id FROM album;"
    album_count_query = "SELECT COUNT(*) FROM album;"

    instrument_query = "SELECT name, key, id FROM instrument;"
    instrument_count_query = "SELECT COUNT(*) FROM instrument;"

    album_count_by_musician_query = """
    SELECT m.*, COUNT(p.id) AS album_count
    FROM musician m
    JOIN produced p ON m.ssn = p.ssn 
    GROUP BY m.ssn;
    """

    # Execute each query and print its result.
    print("Musicians:")
    execute_and_print_query(cur, musician_query)
    print(f"Total Musicians: {count_query_results(cur, musician_count_query)}\n")

    print("Albums:")
    execute_and_print_query(cur, album_query)
    print(f"Total Albums: {count_query_results(cur, album_count_query)}\n")

    print("Instruments:")
    execute_and_print_query(cur, instrument_query)
    print(f"Total Instruments: {count_query_results(cur, instrument_count_query)}\n")

    # I am assuming an album played by a musician with different instruments counts as one album.
    print("Album Count by Musician:")
    execute_and_print_query(cur, album_count_by_musician_query)
