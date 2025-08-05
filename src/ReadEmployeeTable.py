from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric

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

# Query and display all employees
employees = session.query(Employee).all()
for emp in employees:
    print(f'ID: {emp.EmployeeID}, Name: {emp.FirstName} {emp.LastName}, '
          f'Department: {emp.Department}, Hire Date: {emp.HireDate}, Salary: {emp.Salary}')
session.commit()
session.close()