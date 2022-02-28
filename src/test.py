from dbm import CryptoTrackingPlatform, db

new_ctp = CryptoTrackingPlatform('coingecko', 'coingecko.com', '104.148.544.127', 'https://www.coingecko.com/')
db.cinsert(new_ctp)
#ctp = db.session.query(CryptoTrackingPlatform).get("coingecko")
#print(ctp.domain)


