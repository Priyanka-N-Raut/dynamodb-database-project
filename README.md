# 📌 AWS RDS – Intern Management Database Project

## 📖 Project Overview

This project demonstrates how to set up a Managed Relational Database Service (RDS) on AWS using MySQL.

We created a database to store intern information and connected it using:

✅ MySQL Workbench (SQL Client)

✅ Python Script (mysql-connector)

This project showcases hands-on experience with Cloud Database Management as a Cloud Intern.


## 🛠 Technologies Used

AWS RDS (MySQL)

EC2 Security Groups

MySQL Workbench

Python 3

mysql-connector-python


## 🏗 Architecture

Local Machine (Python / MySQL Client)
⬇
AWS RDS (MySQL Database)
⬇
Interns Table (Data Stored in Cloud)


## 🚀 Steps Performed
1️⃣ Create RDS Instance

Engine: MySQL

Instance type: db.t3.micro (Free Tier)

Public Access: Enabled

Port: 3306

Configured Security Group to allow My IP


## 1. Create Database & Table
CREATE DATABASE intern_management;
USE intern_management;

CREATE TABLE Interns (
    Name VARCHAR(100),
    Role VARCHAR(100),
    Email VARCHAR(100)
);

INSERT INTO Interns VALUES
('Priyanka Raut', 'Cloud Intern', 'priyanka@gmail.com'),
('Rahul Sharma', 'DevOps Intern', 'rahul@gmail.com');

## 2. Connect Using Python Script

Install dependency:

pip install mysql-connector-python

Python Code:

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

Run:

python app.py

## ✅ Output
('Priyanka Raut', 'Cloud Intern', 'priyanka@gmail.com')
('Rahul Sharma', 'DevOps Intern', 'rahul@gmail.com')

## 🔒 Security Configuration

Enabled Public Access (for testing)

Opened Port 3306 in Security Group

Restricted inbound access to My IP only


## 🎯 Learning Outcomes

Provisioned a managed database in AWS

Configured networking & security rules

Connected cloud database with local machine

Performed CRUD operations using SQL

Integrated AWS RDS with Python


## 👩‍💻 Author

Priyanka Raut
Cloud Computing Intern
