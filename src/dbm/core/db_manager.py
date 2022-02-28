from tkinter import N
from typing_extensions import Self
from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query, session
from settings import DATABASE_CONNECTION
from psycopg2.errors import UniqueViolation

class Connect():
    connection = None
    engine = None

    def __init__(self, connection_url):
        try:
            self.engine = create_engine(connection_url)
            self.connection = self.engine.connect()
        except Exception as e:
            print(e)

class Session(Connect):
    session = None
    base = None
    
    def __init__(self, connection_url):
        super().__init__(connection_url)
        
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.base = declarative_base()
     
class DBInterface(Session):
    
    def insert(self, obj):
        try:
            self.session.add(obj)
        except Exception as e:
            print(e)
        
    def commit(self):
        try:
            self.session.commit()
        except Exception as e:
            print(str(e.__cause__).replace('\n', '    ').replace(' ', ' '))
            self.session.rollback()
            
    def cinsert(self, obj):
        self.insert(obj)
        self.commit()
        
    def get(self, table, param):
        
        return db.session.query(table).get(param)
        
    def __init__(self, connection_url):
        super().__init__(connection_url)
    
Base = declarative_base()    
db = DBInterface(DATABASE_CONNECTION)