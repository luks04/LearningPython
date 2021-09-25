import sqlite3

try:
    conn = sqlite3.connect("database_name")
    cursor = conn.cursor()
    print("Database connection and creation successful...")
    query = '''
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE
            );
            '''
    print("Executing query...")
    cursor.execute(query)
    cursor.close()
except sqlite3.Error as error:
    print("Error: ", error)
finally:
    if(conn):
        conn.close()
        print("Sqlite connection is closed...")