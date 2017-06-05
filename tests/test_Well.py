import unittest
import cmath
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
        self.assertAlmostEqual(w.Q, 3)
        self.assertAlmostEqual(w.r, 4)

    # --------------------------------------------------------------------------
    def test_complex_potential(self):
        """Test complex potential."""

        zo = complex(10, 10)
        we = Well(zo, 2*cmath.pi, 1)

        z = complex(10, 20)
        Omega_true = complex(cmath.log(10), cmath.pi/2)
        Omega = Well.complex_potential(we, z)
        self.assertAlmostEqual(Omega, Omega_true)

        z = complex(20, 20)
        Omega_true = complex(cmath.log(10*cmath.sqrt(2)), cmath.pi/4)
        Omega = Well.complex_potential(we, z)
        self.assertAlmostEqual(Omega, Omega_true)

    # --------------------------------------------------------------------------
    def test_complex_discharge(self):
        """Test complex discharge."""

        zo = complex(10, 10)
        we = Well(zo, 2*cmath.pi, 1)

        z = complex(20, 10)
        W_true = -1/complex(10, 0)
        W = Well.complex_discharge(we, z)
        self.assertAlmostEqual(W, W_true)

        z = complex(10, 20)
        W_true = -1/complex(0, 10)
        W = Well.complex_discharge(we, z)
        self.assertAlmostEqual(W, W_true)

    # --------------------------------------------------------------------------
    def test_abstraction(self):
        """Test abstraction."""
        assert(False)

    # --------------------------------------------------------------------------
    def test_divergence_discharge(self):
        """Test divergence discharge."""
        assert(False)

    # --------------------------------------------------------------------------
    def test_jacobian_potential(self):
        """Test jacobian potential."""
        assert(False)

    # --------------------------------------------------------------------------
    def test_jacobian_discharge(self):
        """Test jacobian discharge."""
        assert(False)


if __name__ == '__main__':
    unittest.main()
