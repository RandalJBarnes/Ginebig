import unittest
import well

class TestWell(unittest.TestCase):
    """Test the Well class."""
    
    # preparing to test
    def setUp(self):
        print("TestWellsetUp_:begin")
        ## do something...
        print("TestWell:setUp_:end")
     
    # ending the test
    def tearDown(self):
        print("TestWelltearDown_:begin")
        ## do something...
        print("TestWell:tearDown_:end")
     
    # test routine A
    def test_construction(self):
        """Test routine A"""
        print("TestWell:testA")
        #w = Well()
        #assertIsInstance(w, 'AnalyticElement')
        #assertIsInstance(w, 'Well')
     
    # test routine B
    def test_B(self):
        """Test routine B"""
        print("TestWell:testB")
       
if __name__ == '__main__':
    unittest.main()     