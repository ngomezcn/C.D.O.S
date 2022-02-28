import sys
import os
sys.path.append( os.path.realpath(__file__)+ "\\..\\..\\")
import unittest
from utils.models import table_exists
from models.discovery_system import *
from utils.models import table_exists

class TestModels(unittest.TestCase):

    def test_tables_exists(self):
        self.assertTrue(table_exists(CryptoTrackingPlatform))
        self.assertTrue(table_exists(ScrapedToken))
        self.assertTrue(table_exists(RawTokenToReview))


if __name__ == '__main__':
    unittest.main()


from pprint import pprint
