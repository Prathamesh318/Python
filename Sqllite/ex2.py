import sqlite3 as sq

# Database connection
conn = sq.connect('Student.db')
cur = conn.cursor()


# Function to create the table
def createTable():
    query = 'CREATE TABLE IF NOT EXISTS student(sid NUMBER, sname TEXT)'
    cur.execute(query)


# Function to add data
def addData():
    sid = int(input("Enter the student ID: "))
    sname = input("Enter the student name: ")
    query = "INSERT INTO student VALUES(?, ?)"
    cur.execute(query, (sid, sname))  # Parameterized query
    conn.commit()
    print(query)
    print("Data added successfully!")


# Function to retrieve data
def getData():
    query = "SELECT * FROM student"
    cur.execute(query)
    rows = cur.fetchall()
    if rows:
        print("Student Data:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}")
    else:
        print("No data found in the table.")


# Function to delete a record
def deleteData():
    sid = int(input("Enter the student ID to delete: "))
    query = "DELETE FROM student WHERE sid = ?"
    cur.execute(query, (sid,))
    conn.commit()
    print(f"Record with ID {sid} deleted successfully.")


# Function to validate student credentials
def validatestudent():
    sid = int(input("Enter the student ID: "))
    sname = input("Enter the student name: ")
    query = "SELECT * FROM student WHERE sid = ? AND sname = ?"
    cur.execute(query, (sid, sname))  # Parameterized query
    rows = cur.fetchall()

    if len(rows) == 0:
        print("Invalid User")
    else:
        print("Valid User")


# Check if the database is connected
if conn:
    print("Database was created successfully!")
    createTable()


# Menu-driven program
while True:
    print("\nMenu:")
    print("1. Add Data")
    print("2. Get Data")
    print("3. Delete Data")
    print("4. Validate Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addData()
    elif choice == 2:
        getData()
    elif choice == 3:
        deleteData()
    elif choice == 4:
        validatestudent()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
