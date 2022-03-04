from dbm.models.discovery_system import *
from dbm.core.manager import db

def table_exists(table):
    try:
        db.session.query(table).count()
    except Exception as exc:
        print(exc)
        raise Exception