import pytest
import unittest
from sqlalchemy.ext.declarative import declarative_base
from dbm.core.manager import *

class TestCore(unittest.TestCase):

    def test_database_connection(self):
        try:
            dbm.connectToDatabase()
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)

if __name__ == '__main__':
    unittest.main()

