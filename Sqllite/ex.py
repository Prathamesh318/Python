import sqlite3

# Step 1: Connect to SQLite database (creates the file if it doesn't exist)
connection = sqlite3.connect("example.db")

# Step 2: Create a cursor object
cursor = connection.cursor()

# Step 3: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Step 4: Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

# Step 5: Commit the changes
connection.commit()

# Step 6: Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Step 7: Close the connection
connection.close()
