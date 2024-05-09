import sqlite3

# Here we create the small tables from the big table we created on task1.

with sqlite3.connect("new_db.db") as con:
    cur = con.cursor()
    
    # I decided to be more verbose with the attribute names to make it easier which attributes we are accessing.

    CREATE_STATEMENTS = """
    CREATE TABLE IF NOT EXISTS musician(
        musician_ssn TEXT,
        musician_name TEXT,
        street_number TEXT,
        street_name TEXT,
        street_type TEXT,
        PRIMARY KEY(musician_ssn)
    );
    
    CREATE TABLE IF NOT EXISTS instrument(
        instrument_id TEXT,
        instrument_name TEXT,
        instrument_key TEXT,
        PRIMARY KEY(instrument_id)
    );
    
    CREATE TABLE IF NOT EXISTS album(
        album_id TEXT,
        album_title TEXT,
        album_date INTEGER,
        album_format TEXT,
        PRIMARY KEY(album_id)
    );
    
    CREATE TABLE IF NOT EXISTS produced(
        musician_ssn TEXT,
        album_id TEXT,
        PRIMARY KEY(musician_ssn, album_id),
        FOREIGN KEY(musician_ssn) REFERENCES musician(musician_ssn),
        FOREIGN KEY(album_id) REFERENCES album(album_id)
    );
    
    CREATE TABLE IF NOT EXISTS used(
        album_id TEXT,
        instrument_id TEXT,
        PRIMARY KEY(album_id, instrument_id),
        FOREIGN KEY(album_id) REFERENCES album(album_id),
        FOREIGN KEY(instrument_id) REFERENCES instrument(instrument_id)
    );
    """
    
    cur.executescript(CREATE_STATEMENTS)
    
