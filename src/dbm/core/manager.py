from tkinter import E, N
from traceback import print_tb
import traceback
from typing_extensions import Self
from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query, session
from crypto_scraper.crypto_scraper.utils.logger import sprint
from dbm.settings import DATABASE_CONNECTION
from psycopg2.errors import UniqueViolation

class Connect():
    connection = None
    engine = None
    connection_url = None

    def __init__(self, connection_url):
        self.connection_url = connection_url

    def connectToDatabase(self):
        try:
            self.engine = create_engine(self.connection_url)
            self.connection = self.engine.connect()     
            return True
        except Exception as exc:
            print(exc)
            raise Exception

class Session(Connect):
    session = None
    base = None
    
    def __init__(self, connection_url):
        super().__init__(connection_url)
        
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.base = declarative_base()
     
class DbInterface(Session):
    
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
        
        return self.session.query(table).get(param)
        
    def __init__(self, connection_url):
        super().__init__(connection_url)
    
dbase = declarative_base()    
dbm = DbInterface(DATABASE_CONNECTION)