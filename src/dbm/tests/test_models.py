import pytest
import unittest

#from dbm.models.discovery_system import CryptoTrackingPlatform, ScrapedToken, RawTokenToReview

from dbm.utils.tables import table_exists
from dbm.models import tables
class TestDiscoverySystem(unittest.TestCase):

    def test_exist_table_CryptoTrackingPlatform(self):
        try:
            table_exists(tables.crypto_tracking_platform)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)

    def test_exist_table_ScrapedToken(self):
        try:
            table_exists(tables.scraped_token)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)
         
    def test_exist_table_RawTokenToReview(self):
        try:
            table_exists(tables.raw_token_to_review)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)

class TestTrackingSystem(unittest.TestCase):
    
    def test_price_tracked_tokens(self):
        try:
            table_exists(tables.price_tracked_tokens)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)
            
    def test_price_tracked_tokens(self):
        try:
            table_exists(tables.price_tracking_platforms)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)
    
if __name__ == '__main__':
    unittest.main()
