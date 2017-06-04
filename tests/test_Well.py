import unittest
from ginebig.analytic_element import AnalyticElement
from ginebig.well import Well

class TestWell(unittest.TestCase):
    """Test the Well class."""

    # preparing to test
    def setUp(self):
        pass

    # ending the test
    def tearDown(self):
        pass

    # test routine A
    def test_construction(self):
        w = Well(1,2,3)
        self.assertIsInstance(w, AnalyticElement)
        self.assertIsInstance(w, Well)

    # test routine B
    def test_B(self):
        """Test routine B"""
        print("TestWell:testB")
