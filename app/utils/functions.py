import os
import sqlite3

def get_database_connection():
    '''
        Creates a connection between selected database
    '''
    sqlite_file = 'classifier.db'
    file_exists = os.path.isfile(sqlite_file)
    conn = sqlite3.connect(sqlite_file)
    if not file_exists:
        create_sqlite_tables(conn)
    return conn


def create_sqlite_tables(conn):
    '''
        Creates a sqlite table as specified in schema_sqlite.sql file
    '''
    cursor = conn.cursor()
    with open('schema_sqlite.sql', 'r') as schema_file:
        cursor.executescript(schema_file.read())
    conn.commit()

def insert_into_details_table(category, description, quantity, amount):
    '''
        Inserts a new detail into the database
    '''

    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO details (category, description, quantity, amount) VALUES (?, ?, ?, ?)", (category, description, quantity, amount))
        conn.commit()
        cursor.close()
    except Exception as e:
        print('Error', e)
        cursor.close()

def get_category_by_description(description):
    '''
        Function for getting the data of all notes using user_id
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT category FROM details WHERE description LIKE ? COLLATE NOCASE', ('%'+description+'%', ))
        results = cursor.fetchall()
        cursor.close()
        if len(results) == 0:
            return None
        return results
    except Exception as e:
        print('Error', e)
        cursor.close()
