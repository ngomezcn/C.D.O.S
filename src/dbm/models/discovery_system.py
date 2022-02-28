from select import select
from sqlalchemy import Column , create_engine, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, VARCHAR
from core.db_manager import db, Base

class CryptoTrackingPlatform(Base):
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


class ScrapedTokens(Base):
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
                                    



                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
