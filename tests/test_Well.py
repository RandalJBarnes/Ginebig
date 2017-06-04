import unittest
import math
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

    # --------------------------------------------------------------------------
    def test_construction(self):
        """Test constructor."""
        w = Well(complex(1, 2), 3, 4)

        self.assertIsInstance(w, AnalyticElement)
        self.assertIsInstance(w, Well)

        self.assertAlmostEqual(w.z, complex(1, 2))
        self.assertAlmostEqual(w.q, 3)
        self.assertAlmostEqual(w.r, 4)

    # --------------------------------------------------------------------------
    def test_potential(self):
        """Test potential."""

        zo = complex(10, 10)
        we = Well(zo, 2*math.pi, 1)

        z = complex(10,20)
        Omega_true = complex(math.log(10),math.pi/2)
        self.assertAlmostEqual( Well.potential(we,z), Omega_true)

"""
        z = [ complex(20,10), complex(10,20) ]
        Omega_true = [ complex(log(10),0), complex(log(10),pi/2) ]
        self.assertAlmostEqual( potential(we,z), Omega_true)

        z = [ complex(20,10); complex(10,20) ]
        Omega_true = [ complex(log(10),0), complex(log(10),pi/2) ];
        self.assertAlmostEqual( potential(we,z), Omega_true)
"""

if __name__ == '__main__':
    unittest.main()
