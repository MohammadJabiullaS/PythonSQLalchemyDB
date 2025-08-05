Employee Database with SQLAlchemy
This project demonstrates how to use the SQLAlchemy library to interact with a SQLite database by building a simple Employee Management System.

📚 What You'll Learn
How to set up and connect to a SQLite database using SQLAlchemy

How to define a table schema using SQLAlchemy's ORM features

How to create a new database and table

How to add, update, and delete employee records

How to query and manipulate data using Python

⚙️ Features
Create a new SQLite database

Define an Employee table with SQLAlchemy

Insert a default employee record

Add new employees dynamically

Update existing employee data

Delete employee records

Test database connection

🧱 Technologies Used
Python 3

SQLAlchemy

SQLite (via sqlite3)

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/MohammadJabiullaS/PythonSQLalchemyDB.git
cd PythonSQLalchemyDB
2. Install Requirements
pip install sqlalchemy
3. Run the Script
python main.py
You can modify main.py to test different operations like adding, updating, or deleting records.

📂 Project Structure
PythonSQLalchemyDB/src/
│
├── SQLAlchemyConnection.py       # To Test the Database connection
├── CreateEmployeeTable.py        # SQLAlchemy model for the Employee table
├── CreateNewEmployee.py          # Insert new Employee Record
├── ReadEmployeeTable.py          # Read Employee Table Data
├── UpdateEmployeeRecord.py       # Update Employee Recordf fromTable
├── DeleteEmployeeRecord.py       # Delete Employee Record from Table
├── employee.sqlite               # Database file
└── README.md         # Project documentation
📝 Example: Adding an Employee
python
new_employee = Employee(id=2, name='Jane Doe', department='Engineering')
session.add(new_employee)
session.commit()
🙌 Contribution
Pull requests are welcome. 
