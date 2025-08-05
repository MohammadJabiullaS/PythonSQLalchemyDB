import sqlalchemy as db
from sqlalchemy.exc import OperationalError

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#Creating connection to the database
try:
    engine = db.create_engine('sqlite:///employee.sqlite')
    # Attempt to connect to verify
    with engine.connect() as connection:
        print("Connection to the database successful!")
except OperationalError as ex:
    print(f"Connection could not be made due to the following error: \n {ex}")



