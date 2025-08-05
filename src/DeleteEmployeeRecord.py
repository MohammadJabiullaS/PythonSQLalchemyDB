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
user_to_delete = session.query(Employee).filter(Employee.EmployeeID == empid).first()
if user_to_delete:
   session.delete(user_to_delete)
   print("Employee Records deleted")
else:
    print("Employee ID not found")

session.commit()
session.close()



