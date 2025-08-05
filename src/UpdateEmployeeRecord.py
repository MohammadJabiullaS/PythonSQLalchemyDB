from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric
from datetime import date, datetime

#Define the Base
Base = declarative_base()

#Define the Table Class
class Employee(Base):
    __tablename__ = 'employee'
    EmployeeID = Column(Integer, primary_key=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Department = Column(String(50))
    HireDate = Column(Date)
    Salary = Column(Numeric(10, 2))

# Create an SQLite database (in-memory for demo, or use 'sqlite:///employees.db' for a file)
engine = create_engine('sqlite:///employee.sqlite')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query and update employee record
empid = int(input("Enter your employee ID to update: "))
user_to_update = session.query(Employee).filter(Employee.EmployeeID == empid).first()
if user_to_update:
    user_to_update.FirstName = input("Enter your first name: ")
    user_to_update.LastName = input("Enter your last name: ")
    user_to_update.Department = input("Enter your department: ")
    hireDate = input("Enter your hire date: ")
    date_object = datetime.strptime(hireDate, "%Y-%m-%d")
    user_to_update.HireDate = date_object
    user_to_update.Salary = input("Enter your salary: ")
    print("Employee Records updated")
else:
    print("Employee ID not found")

session.commit()
session.close()



