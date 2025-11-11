import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

cursor = conn.cursor()

# Function to insert student record
def add_students(name, age, grade):
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(sql, values)
    conn.commit()
    print("Student record added successfully!")

# Example usage
add_students("John Doe", 18, "A")
add_students("Jane Smith", 17, "B")

# Fetch and display records
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
