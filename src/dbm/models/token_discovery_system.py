from select import select
import db
from sqlalchemy import Column , create_engine, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, VARCHAR


class CryptoTrackingPlatforms(db.Base):
    __tablename__  = 'crypto_tracking_platforms'
    
    ctp_id = Column(VARCHAR, primary_key=True)
    domain = Column(VARCHAR)
    ip = Column(VARCHAR(11))
    root_https = Column(VARCHAR)
     
    def __init__(self, ctp_id, domain, ip, root_https):
        self.ctp_id = ctp_id
        self.domain = domain
        self.ip = ip
        self.root_https = root_https

    def add(self):
        db.session.add(self)
        
    def commit(self):
        db.session.commit()
    
db.Base.metadata.create_all(db.engine)

cpt = CryptoTrackingPlatforms('coingecko', 'www.coingecko.com', '192.168.134.34', 'https://www.coingecko.com/')
cpt.add()
cpt.commit()

#doge = 
#session.add(doge)
#session.commit()