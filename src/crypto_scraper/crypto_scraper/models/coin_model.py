from sqlite3 import Date
from tokenize import String
from datetime import datetime

class Coin():
    name = String
    href = String
    id = String
    tracking_date = Date
    network = String
    contract = String

    def __init__(self, name, id, href):
            self.name = name
            self.id = id
            self.href = href
            self.tracking_date = datetime.now()
            
    def tracked_time(self):
        return (datetime.now()- self.tracking_date).total_seconds()