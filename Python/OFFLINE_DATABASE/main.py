
from connection import get_connection

def create_table():
    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STUDENT (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            subject VARCHAR(100),
            score INTEGER
        )
    ''')
    conn.commit() #save
    print("Table created successfully.")

    conn.close()

create_table()    