import sqlite3

try:
    conn = sqlite3.connect("database_name")
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE name = 'Bob';"
    print("Executing query...")
    cursor.execute(query)
    conn.commit()
    cursor.close()
except sqlite3.Error as error:
    conn.rollback()
    print("Error: ", error)
finally:
    if(conn):
        conn.close()
        print("Sqlite connection is closed...")