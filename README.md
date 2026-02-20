# 📌 AWS DynamoDB – Intern Management System

## 📖 Project Overview

This project demonstrates how to set up a Managed NoSQL Database using Amazon DynamoDB on AWS.

We created a table named Interns, inserted dummy records, and connected it to a local Python script to verify data persistence.

This project showcases hands-on experience with serverless cloud databases as a Cloud Computing Intern.

## 🛠 Technologies Used

AWS DynamoDB

AWS IAM

Python 3

Boto3 (AWS SDK for Python)

## 🏗 Architecture

Local Machine (Python Script)
⬇
AWS DynamoDB (Managed NoSQL Database)
⬇
Interns Table (Stored Data)

## 🚀 Implementation Steps

1️⃣ Create DynamoDB Table

Service: DynamoDB

Table Name: interns

Partition Key: Email (String)

Region: us-east-1

## 2️⃣ Insert Dummy Records

Inserted sample records using AWS Console:

{
  "Email": "priyanka@gmail.com",
  "Name": "Priyanka Raut",
  "Role": "Cloud Intern"
}

Additional records:

{
  "Email": "rahul@gmail.com",
  "Name": "Rahul Sharma",
  "Role": "DevOps Intern"
}

## 3️⃣ Connect DynamoDB Using Python

Install boto3
pip install boto3
Configure AWS Credentials
aws configure

Provide:

AWS Access Key

AWS Secret Key

Region (us-east-1)

Output format (json)

## 4️⃣ Python Script to Fetch Data

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('interns')

response = table.scan()

print("Stored Items:\n")

for item in response['Items']:
    print(item)

Run:

## python dynamo_app.py

✅ Output
Stored Items:

{'Email': 'priyanka@gmail.com', 'Name': 'Priyanka Raut', 'Role': 'Cloud Intern'}
{'Email': 'rahul@gmail.com', 'Name': 'Rahul Sharma', 'Role': 'DevOps Intern'}

## 🔒 Key Features

Fully managed NoSQL database

Serverless architecture

High scalability and availability

Low latency performance

Secure access via IAM

## 🎯 Learning Outcomes

Created and configured DynamoDB table

Understood partition key concept

Inserted and retrieved data

Connected AWS services with Python

Implemented a serverless database solution

## 👩‍💻 Author

Priyanka Raut
Cloud Computing Intern
