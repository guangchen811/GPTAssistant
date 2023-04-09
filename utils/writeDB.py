import sqlite3

# create a new database file
conn = sqlite3.connect('DB/TextDatabase.db')

# create a table
conn.execute('CREATE TABLE contacts (name text, email text)')

# insert data into the table
conn.execute("INSERT INTO contacts VALUES ('John Doe', 'john@example.com')")
conn.execute("INSERT INTO contacts VALUES ('Jane Smith', 'jane@example.com')")

# commit the changes and close the connection
conn.commit()
conn.close()