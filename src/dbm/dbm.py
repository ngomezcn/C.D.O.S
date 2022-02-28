from sqlalchemy import table
from models.discovery_system import *
from core.db_manager import db

cpt = CryptoTrackingPlatform('acoidfngsdfecko', 'www.coinsdfgecko.com', '193.168.134.34', 'httpsdf://www.coingecko.com/')
#a = db.session.query(CryptoTrackingPlatform).
#a = db.engine.execute('select * from crypto_tracking_platforms;')
#query = db.session.query(table=CryptoTrackingPlatform).get()

for instance in db.session.query(CryptoTrackingPlatform.name.label('name_label')).all():    
    print(instance.domain, instance.ip)

#for i in a:
#    for b in i:
#        print(b)

#print(a)

#print(db.get(CryptoTrackingPlatform, "coingecko").domain)