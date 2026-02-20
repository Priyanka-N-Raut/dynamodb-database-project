import mysql.connector

connection = mysql.connector.connect(
    host="your-rds-endpoint",
    user="admin",
    password="your-password",
    database="intern_management"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM Interns")

for row in cursor.fetchall():
    print(row)

connection.close()
