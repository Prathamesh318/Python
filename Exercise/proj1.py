import sqlite3

# Connect to SQLite database (it will create a file if it doesn't exist)
conn = sqlite3.connect('python_db.db')
cursor = conn.cursor()

# Create Hospital Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Hospital (
    Hospital_Id INTEGER PRIMARY KEY,
    Hospital_Name TEXT NOT NULL,
    Bed_Count INTEGER NOT NULL
);
''')

# Create Doctor Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Doctor (
    Doctor_Id INTEGER PRIMARY KEY,
    Doctor_Name TEXT NOT NULL,
    Hospital_Id INTEGER NOT NULL,
    Joining_Date TEXT NOT NULL,
    Speciality TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Experience INTEGER,
    FOREIGN KEY (Hospital_Id) REFERENCES Hospital(Hospital_Id)
);
''')

# Insert data into Hospital Table
cursor.executemany('''
INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
VALUES (?, ?, ?);
''', [
    (1, "Mayo Clinic", 200),
    (2, "Cleveland Clinic", 400),
    (3, "Johns Hopkins", 1000),
    (4, "UCLA Medical Center", 1500)
])

# Insert data into Doctor Table
cursor.executemany('''
INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
VALUES (?, ?, ?, ?, ?, ?, ?);
''', [
    (101, "David", 1, "2005-02-10", "Pediatric", 40000, None),
    (102, "Michael", 2, "2018-07-23", "Oncologist", 20000, None),
    (103, "Susan", 2, "2016-05-19", "Garnaologist", 25000, None),
    (104, "Robert", 3, "2017-12-28", "Pediatric", 28000, None),
    (105, "Linda", 3, "2004-06-04", "Garnaologist", 42000, None),
    (106, "William", 4, "2006-04-11", "Dermatologist", 30000, None),
    (107, "Richard", 4, "2014-08-21", "Radiologist", 30000, None),
    (108, "Karen", 4, "2011-10-17", "Radiologist", 30000, None)
])

# Commit changes
conn.commit()

# Function to fetch hospital and doctor information using Hospital_Id and Doctor_Id
def fetch_hospital_and_doctor(hospital_id, doctor_id):
    cursor.execute('''
    SELECT h.Hospital_Name, h.Bed_Count, d.Doctor_Name, d.Speciality 
    FROM Hospital h 
    JOIN Doctor d ON h.Hospital_Id = d.Hospital_Id 
    WHERE h.Hospital_Id = ? AND d.Doctor_Id = ?;
    ''', (hospital_id, doctor_id))
    return cursor.fetchall()

# Function to fetch doctors by specialty and salary
def fetch_doctors_by_specialty_and_salary(specialty, min_salary):
    cursor.execute('''
    SELECT Doctor_Name, Speciality, Salary 
    FROM Doctor 
    WHERE Speciality = ? AND Salary >= ?;
    ''', (specialty, min_salary))
    return cursor.fetchall()

# Function to fetch doctors by hospital
def fetch_doctors_by_hospital(hospital_id):
    cursor.execute('''
    SELECT Doctor_Name, Speciality 
    FROM Doctor 
    WHERE Hospital_Id = ?;
    ''', (hospital_id,))
    return cursor.fetchall()

# Function to update doctor experience
def update_doctor_experience(doctor_id, experience):
    cursor.execute('''
    UPDATE Doctor 
    SET Experience = ? 
    WHERE Doctor_Id = ?;
    ''', (experience, doctor_id))
    conn.commit()

# Function to remove a hospital
def delete_hospital(hospital_id):
    cursor.execute('''
    DELETE FROM Hospital 
    WHERE Hospital_Id = ?;
    ''', (hospital_id,))
    conn.commit()

# Testing the functions
print("Fetching Hospital and Doctor Info (Hospital_Id: 1, Doctor_Id: 101):")
print(fetch_hospital_and_doctor(1, 101))

print("\nFetching Doctors by Specialty (Pediatric) and Salary >= 30000:")
print(fetch_doctors_by_specialty_and_salary("Pediatric", 30000))

print("\nFetching Doctors by Hospital (Hospital_Id: 4):")
print(fetch_doctors_by_hospital(4))

print("\nUpdating Doctor Experience (Doctor_Id: 101, Experience: 15 years):")
update_doctor_experience(101, 15)

print("\nDeleting Hospital (Hospital_Id: 3):")
delete_hospital(3)

# Verify hospital deletion
print("\nRemaining Hospitals:")
cursor.execute('SELECT * FROM Hospital')
print(cursor.fetchall())

# Close the connection
conn.close()
