import unittest

class TestAnalyticElement(unittest.TestCase):
    """Test the AnalyticElement class."""
    
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print("TestAnalyticElement:setUp_:begin")
        ## do something...
        print("TestAnalyticElement:setUp_:end")
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print("TestAnalyticElement:tearDown_:begin")
        ## do something...
        print("TestAnalyticElement:tearDown_:end")
     
    # test routine A
    def test_A(self):
        """Test routine A"""
        print("TestAnalyticElement:testA")
     
    # test routine B
    def test_B(self):
        """Test routine B"""
        print("TestAnalyticElement:testB")
       
if __name__ == '__main__':
    unittest.main()     