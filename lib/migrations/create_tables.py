import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from lib.models import Base, Freebie, Company, Dev

engine = create_engine('sqlite:///freebies.db')

Base.metadata.create_all(engine)
print("Tables created successfully.")