from datetime import datetime


def get_timestamp():
    return datetime.now().replace(microsecond=0)
    