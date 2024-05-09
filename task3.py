import sqlite3


def insert_into_table(cur, table, query, original_db_cur):
    original_db_cur.execute(query)
    rows = original_db_cur.fetchall()
    for row in rows:
        placeholders = ', '.join('?' * len(row))
        cur.execute(f"INSERT OR IGNORE INTO {table} VALUES ({placeholders})", row)


with sqlite3.connect("new_db.db") as new_db_con:
    new_db_cur = new_db_con.cursor()

    with sqlite3.connect("original_db.db") as original_db_con:
        original_db_cur = original_db_con.cursor()

        musician_query = """
        SELECT DISTINCT musician_ssn, musician_name, street_number, street_name, street_type
        FROM no_town
        """
        insert_into_table(new_db_cur, "musician", musician_query, original_db_cur)

        instrument_query = """
        SELECT DISTINCT instrument_id, instrument_name, instrument_key
        FROM no_town
        """
        insert_into_table(new_db_cur, "instrument", instrument_query, original_db_cur)

        album_query = """
        SELECT DISTINCT album_id, album_title, album_date, album_format
        FROM no_town
        """
        insert_into_table(new_db_cur, "album", album_query, original_db_cur)

        produced_query = """
        SELECT DISTINCT musician_ssn, album_id
        FROM no_town
        """
        insert_into_table(new_db_cur, "produced", produced_query, original_db_cur)

        used_query = """
        SELECT DISTINCT album_id, instrument_id
        FROM no_town
        """
        insert_into_table(new_db_cur, "used", used_query, original_db_cur)

    new_db_con.commit()
