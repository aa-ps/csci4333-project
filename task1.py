import sqlite3
import csv

# Here we are using csv to read the file and create a large table with all the data from it.

with sqlite3.connect("original_db.db") as con:
    cur = con.cursor()

    with con:
        # Verbose names to avoid columns with the same name.
        CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS no_town(
            street_number TEXT,
            street_name TEXT,
            street_type TEXT,
            musician_name TEXT,
            musician_ssn TEXT,
            album_id INTEGER,
            album_title TEXT,
            album_date DATE,
            album_format TEXT,
            instrument_id INTEGER,
            instrument_name TEXT,
            instrument_key TEXT
        );'''

        cur.execute(CREATE_TABLE)
        
        with open("no_town.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
        
            # These are placeholders for our attributes, so we don't have to put the column names.
            # It goes in order from street_number to instrument_key
            insert_query = "INSERT INTO no_town VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            
            # The columns of the csv are in the same order as the columns of our table.
            data = [tuple(row) for row in reader]
            cur.executemany(insert_query, data)

    # To verify the data was transferred correctly.
    # Uncomment if needed.
    
    # TEST_QUERY = 'SELECT * FROM no_town'

    # res = cur.execute(TEST_QUERY).fetchall()

    # if res:
    #     relational_schema = [x[0] for x in cur.description]
    #     print(tabulate(res, headers=relational_schema))
    # else:
    #     print("No data available.")
