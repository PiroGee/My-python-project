import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",       # or your server IP
    user="root",            # replace with your MySQL username
    password="",            # replace with your MySQL password
    database="python"       # replace with your database name
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
)
""")

# Function to add student record
def add_student(name, age):
    sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
    values = (name, age)
    cursor.execute(sql, values)
    conn.commit()
    print(f"✅ Student {name} (Age {age}) added successfully!")

# Function to retrieve student records
def get_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("\n--- Student Records ---")
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")

# Function to update student record
def update_student(student_id, new_name, new_age):
    sql = "UPDATE students SET name=%s, age=%s WHERE id=%s"
    values = (new_name, new_age, student_id)
    cursor.execute(sql, values)
    conn.commit()
    print(f"✅ Student ID {student_id} updated successfully!")

# Function to delete student record
def delete_student(student_id):
    sql = "DELETE FROM students WHERE id=%s"
    cursor.execute(sql, (student_id,))
    conn.commit()
    print(f"🗑️ Student ID {student_id} deleted successfully!")

# Function to search by name
def search_by_name(name):
    sql = "SELECT * FROM students WHERE name LIKE %s"
    cursor.execute(sql, (f"%{name}%",))
    records = cursor.fetchall()
    print("\n--- Search Results by Name ---")
    if records:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")
    else:
        print("❌ No student found with that name.")

# Function to search by ID
def search_by_id(student_id):
    sql = "SELECT * FROM students WHERE id=%s"
    cursor.execute(sql, (student_id,))
    record = cursor.fetchone()
    print("\n--- Search Result by ID ---")
    if record:
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")
    else:
        print("❌ No student found with that ID.")

# Menu-driven system
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search by Name")
    print("6. Search by ID")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        add_student(name, age)
    elif choice == "2":
        get_students()
    elif choice == "3":
        student_id = int(input("Enter student ID to update: "))
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        update_student(student_id, new_name, new_age)
    elif choice == "4":
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)
    elif choice == "5":
        name = input("Enter name to search: ")
        search_by_name(name)
    elif choice == "6":
        student_id = int(input("Enter student ID to search: "))
        search_by_id(student_id)
    elif choice == "7":
        print("Exiting system...")
        break
    else:
        print("❌ Invalid choice, please try again.")

# Close connection
cursor.close()
conn.close()
