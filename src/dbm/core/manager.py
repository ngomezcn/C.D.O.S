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

class DbmManagerConnection():
    connection = None
    engine = None
    connection_url = None
    
    def connect(self):
        try:
            self.engine = create_engine(self.connection_url)
            self.connection = self.engine.connect()     
        except Exception as exc:
            print(exc)
            raise Exception

    def __init__(self, connection_url):
        self.connection_url = connection_url
        return self.connect()

class DbmManagerSession(DbmManagerConnection):
    session = None
    dbase = None
    
    def __init__(self, connection_url):
        super().__init__(connection_url)
        
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.dbase = declarative_base()
     
class DbmManager(DbmManagerSession):
    
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
        
Base = declarative_base()
db = DbmManager(DATABASE_CONNECTION)