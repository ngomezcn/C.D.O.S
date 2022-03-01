import sys
import os
import unittest

from db.models.discovery_system import CryptoTrackingPlatform, ScrapedToken, RawTokenToReview
from db.utils.orm import table_exists

class TestModels(unittest.TestCase):

    def test_tables_exists(self):
        self.assertTrue(table_exists(CryptoTrackingPlatform))
        self.assertTrue(table_exists(ScrapedToken))
        self.assertTrue(table_exists(RawTokenToReview))


if __name__ == '__main__':
    unittest.main()


from pprint import pprint
