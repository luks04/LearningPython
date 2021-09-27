import sqlite3

try:
    conn = sqlite3.connect("database_name")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name LIKE 'Ang%';"
    print("Executing query...")
    cursor.execute(query)
    rs = cursor.fetchone()
    for record in rs:
        print(str(record))
    cursor.close()
except sqlite3.Error as error:
    print("Error: ", error)
finally:
    if(conn):
        conn.close()
        print("Sqlite connection is closed...")