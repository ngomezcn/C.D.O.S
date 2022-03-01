import sys
import os
import unittest

from dbm.models.discovery_system import CryptoTrackingPlatform, ScrapedToken, RawTokenToReview
from dbm.utils.orm import table_exists

class TestModels(unittest.TestCase):

    def test_tables_exists(self):
        self.assertTrue(True)

    def test_tdds_exists(self):
        """This test comment should be with the Class color set as GREEN"""
        self.assertTrue(True)
        
        with self.subTest('hooola', i=5):
            self.assertFalse(False)



class BaseTestCases:
    
    class BaseTest(unittest.TestCase):


        def testCommon(self):
            print('Calling BaseTest:testCommon')
            value = 5
            self.assertEqual(value, 5)

class SubTest1(BaseTestCases.BaseTest):

    def testSub1(self):
        print('Calling SubTest1:testSub1')
        sub = 3
        self.assertEqual(sub, 3)

class SubTest2(BaseTestCases.BaseTest):

    def testSub2(self):
        print('Calling SubTest2:testSub2')
        sub = 4
        self.assertEqual(sub, 4)

print("gay")

if __name__ == '__main__':
    unittest.main()


from pprint import pprint
