import pytest
import unittest

from dbm.models.discovery_system import CryptoTrackingPlatform, ScrapedToken, RawTokenToReview
from dbm.utils.tables import *
class TestDiscoverySystem(unittest.TestCase):

    def test_exist_table_CryptoTrackingPlatform(self):
        try:
            table_exists(CryptoTrackingPlatform)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)

    def test_exist_table_ScrapedToken(self):
        try:
            table_exists(ScrapedToken)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)
         
    def test_exist_table_raw_RawTokenToReview(self):
        try:
            table_exists(RawTokenToReview)
        except Exception as exc:
            pytest.fail(pytrace=True, reason=exc.__cause__)

if __name__ == '__main__':
    unittest.main()
