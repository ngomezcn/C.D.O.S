import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, VARCHAR, TIMESTAMP, MONEY
from dbm.core.manager import Base

class PriceTrackedTokens(Base):
    __tablename__  = 'price_tracked_tokens'
    
    token_contract = Column(VARCHAR, primary_key=True)
    ptp_id = Column(VARCHAR)
    tracked_since = Column(TIMESTAMP)
    last_update = Column(TIMESTAMP)
           
    def __init__(self, token_contract, ptp_id, tracked_since, last_update):
        self.token_contract = token_contract
        self.ptp_id = ptp_id
        self.tracked_since = tracked_since
        self.last_update = last_update
        
        
        