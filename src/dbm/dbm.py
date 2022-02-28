from sqlalchemy import table
from models.discovery_system import *
from core.db_manager import db
from datetime import datetime
from utils.models import *



#new_ctp = CryptoTrackingPlatform('coingecko', 'coingecko.com', '104.148.544.127', 'httpsdf://www.coingecko.com/')
#db.cinsert(new_ctp)
#ctp = db.session.query(CryptoTrackingPlatform).get("coingecko")
#print(ctp.domain)

#db.session.query(ScrapedToken).count()
#ScrapedToken('tesfgdddfssdffgfdsdfft1/dffgdffssdfdgadfsdftest1','ddgfdsfdfdfsdffgd', cpt.ctp_id, datetime.now(), datetime.now())
#test = RawTokenToReview(uri='es/tokens/doge', token_id='doge', ctp_id=ctp.ctp_id, token_name='dogecoin', discovery_timestamp=datetime.now(), contract='0x124sdfsdf', chain_name='hdl', value=0.000134, listed_timestamp=datetime.now())
#db.cinsert(test)
#test1 = ScrapedToken('tesfgdddfssdffgfdsdfft1/dffgdffssdfdgadfsdftest1','ddgfdsfdfdfsdffgd', cpt.ctp_id, datetime.now(), datetime.now())
#db.cinsert(test1)
#test2 = ScrapedToken('tesfgd234fgsdffasdfadffgf324t5/tgdfesdasdffsdffgtfff3123','dsfsfsdfdfffadfgsfgd', a.ctp_id, datetime.now(), datetime.now())
#db.cinsert(test2)
