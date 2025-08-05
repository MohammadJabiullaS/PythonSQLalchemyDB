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

# Add a new employee
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
department = input("Enter department: ")
hireDate = input("Enter hire date (yyyy-mm-dd): ")
salary = float(input("Enter salary: "))

date_object = datetime.strptime(hireDate, "%Y-%m-%d")

new_employee = Employee(
    FirstName=firstName,
    LastName=lastName,
    Department=department,
    HireDate=date_object,
    Salary=salary,
)
session.add(new_employee)
session.commit()
session.close()

