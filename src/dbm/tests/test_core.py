import pytest
import unittest
from dbm.core.manager import DbmManager
from dbm.settings import DATABASE_CONNECTION
class TestCore(unittest.TestCase):

    def test_database_connection(self):
        try:
            DbmManager(DATABASE_CONNECTION)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)

if __name__ == '__main__':
    unittest.main()

