import sqlite3
import re

def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the messages table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='messages'")
    table_exists = cursor.fetchone()

    # If the table doesn't exist, create it
    if not table_exists:
        cursor.execute('CREATE TABLE messages (name, content)')
        conn.commit()

    return conn

def write_db(conn, name, content):
    # insert data into the table
    conn.execute(f"INSERT INTO messages VALUES ({name}, {content})")
    # commit the changes and close the connection
    conn.commit()

def process_database_requests(response, conn):
    save_pattern = r"database save: (.*)(?=\s|$)"
    request_pattern = r"database request: (.*)(?=\s|$)"
    
    save_matches = re.findall(save_pattern, response)
    for match in save_matches:
        sql = match.strip()
        print(sql)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    request_matches = re.findall(request_pattern, response)
    search_results = []
    for match in request_matches:
        sql = match.strip()
        print(sql)
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        search_results.extend(results)
    return search_results