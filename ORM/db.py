from sqlalchemy import Column , create_engine, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, VARCHAR

SERVER = 'localhost'
DATABASE = 'postgres'
USERNAME = 'postgres'
PASSWORD = '1234'
DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}:5432/{DATABASE}'
engine  = create_engine(DATABASE_CONNECTION)
#db.connect()

Session = sessionmaker(bind=engine )
session = Session()

Base = declarative_base()