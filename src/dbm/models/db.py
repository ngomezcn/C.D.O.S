from sqlalchemy import Column , create_engine, null, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, VARCHAR
SERVER = 'localhost'
DATABASE = 'postgres'
USERNAME = 'postgres'
PASSWORD = '1234'
DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}:5432/{DATABASE}'

#engine  = create_engine(DATABASE_CONNECTION)
#connection = engine.connect()
    
#Session = sessionmaker(bind=engine)
#session = Session()
#Base = declarative_base()

class DataBaseManager():
    connection = None
    engine = None

    def __init__(self, connection_url):
        try:
            self.engine = create_engine(connection_url)
        except Exception as e:
            print(e)
        
        try:
            self.connection = self.engine.connect()
        except Exception as e:
            print(e)

db = DataBaseManager(connection_url=DATABASE_CONNECTION)