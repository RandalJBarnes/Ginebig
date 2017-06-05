import unittest
from ginebig.analytic_element import AnalyticElement


class TestAnalyticElement(unittest.TestCase):
    """Test the AnalyticElement class."""

    # --------------------------------------------------------------------------
    def test_must_not_instantiate(self):
        """Test must not instantiate an AnalyticElement."""
        self.assertRaises(TypeError, AnalyticElement)


if __name__ == '__main__':
    unittest.main()
