from models.discovery_system import *
from core.db_manager import db
from sqlalchemy import false, table, true

def table_exists(table):
    try:
        db.session.query(table).count()
        return True
    except Exception as e:
        print(e)
        return False