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

class Coin(Base):
    __tablename__ = 'coin'
    
    coin_id = Column(VARCHAR(100), primary_key=True)
    fk_chain_id = Column(VARCHAR)
    coin_name = Column(VARCHAR(100))
    coin_price = Column(DOUBLE_PRECISION)
   
    def __init__(self, coin_id, fk_chain_id, coin_name, coin_price):
        self.coin_id = coin_id
        self.fk_chain_id = fk_chain_id
        self.coin_name = coin_name
        self.coin_price = coin_price
        
   
Base.metadata.create_all(engine)
    
#doge = Coin('dog', null(), 'doge', 1.1)
#session.add(doge)
#session.commit()

consulta = session.query(Coin)
for i in consulta:
    print(i.coin_price)

ob = session.query(Coin).get('dog')

print(ob)

'''
class doit(Base):
    __tablename__ = 'doit'
    
    name = Column(VARCHAR, primary_key=True)
    
    def __init__(self, name):
        self.name = name
        
Base.metadata.create_all(engine)
doge = doit('dog')
session.add(doge)
session.commit()
'''