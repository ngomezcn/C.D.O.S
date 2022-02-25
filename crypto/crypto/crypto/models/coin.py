from sqlite3 import Date
from tokenize import String

class Coin():
    name = String
    href = String
    id = String
    tracking_time = Date
    network = String
    contract = String

    def __init__(self, name, id, href):
            self.name = name
            self.id = id
            self.href = href