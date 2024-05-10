import sqlite3

# Here we create the small tables from the big table we created on task1.

with sqlite3.connect("new_db.db") as con:
    cur = con.cursor()
    
    # I decided to be more verbose with the attribute names to make it easier which attributes we are accessing.
    # UPDATE: Reverted the name to match the project.
    
    # I included "IF NOT EXISTS" in case the table is already created and to avoid errors.
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
        date DATE,
        format TEXT,
        PRIMARY KEY(id)
    );
    
    CREATE TABLE IF NOT EXISTS produced(
        ssn TEXT,
        id TEXT,
        PRIMARY KEY(ssn, id),
        FOREIGN KEY(ssn) REFERENCES musician(ssn),
        FOREIGN KEY(id) REFERENCES album(id)
    );
    
    CREATE TABLE IF NOT EXISTS used(
        album_id TEXT,
        instrument_id TEXT,
        PRIMARY KEY(album_id, instrument_id),
        FOREIGN KEY(album_id) REFERENCES album(id),
        FOREIGN KEY(instrument_id) REFERENCES instrument(id)
    );
    """
    
    cur.executescript(CREATE_STATEMENTS)
    
