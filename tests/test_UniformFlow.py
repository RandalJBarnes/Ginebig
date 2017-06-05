import unittest
import cmath
import numpy

from ginebig.analytic_element import AnalyticElement
from ginebig.uniform_flow import UniformFlow


class TestUniformFlow(unittest.TestCase):
    """Test the UniformFlow class."""

    # --------------------------------------------------------------------------
    def test_construction(self):
        """Test constructor."""

        uf = UniformFlow(1, cmath.pi/4)

        self.assertIsInstance(uf, AnalyticElement)
        self.assertIsInstance(uf, UniformFlow)

        self.assertAlmostEqual(uf.Qo, 1)
        self.assertAlmostEqual(uf.alpha, cmath.pi/4)

    # --------------------------------------------------------------------------
    def test_complex_potential(self):
        """Test complex potential."""

        uf = UniformFlow(2, cmath.pi/6)

        z = complex(cmath.sqrt(3), 1)
        Omega_true = complex(-4, 0)
        Omega = UniformFlow.complex_potential(uf, z)
        self.assertAlmostEqual(Omega, Omega_true)

        z = complex(1, -1)
        Omega_true = complex(-0.732050807568878, 2.73205080756888)
        Omega = UniformFlow.complex_potential(uf, z)
        self.assertAlmostEqual(Omega, Omega_true)

    # --------------------------------------------------------------------------
    def test_complex_discharge(self):
        """Test complex discharge."""

        uf = UniformFlow(2, cmath.pi/6)

        z = complex(cmath.sqrt(3), 1)
        W_true = complex(cmath.sqrt(3), -1)
        W = UniformFlow.complex_discharge(uf, z)
        self.assertAlmostEqual(W, W_true)

        z = complex(1, -1)
        W_true = complex(cmath.sqrt(3), -1)
        W = UniformFlow.complex_discharge(uf, z)
        self.assertAlmostEqual(W, W_true)

    # --------------------------------------------------------------------------
    def test_abstraction(self):
        """Test abstraction."""

        uf = UniformFlow(2, cmath.pi/6)

        ab = UniformFlow.abstraction(uf)
        self.assertAlmostEqual(ab, float(0))

    # --------------------------------------------------------------------------
    def test_divergence_discharge(self):
        """Test divergence discharge."""

        uf = UniformFlow(2, cmath.pi/6)

        z = complex(10, 20)
        div = UniformFlow.divergence_discharge(uf, z)
        self.assertAlmostEqual(div, float(0))

    # --------------------------------------------------------------------------
    def test_jacobian_potential(self):
        """Test jacobian potential."""

        uf = UniformFlow(2, cmath.pi/6)

        z = complex(10, 20)
        jac = UniformFlow.jacobian_discharge(uf, z)
        self.assertTrue(numpy.size(jac) == 0)

    # --------------------------------------------------------------------------
    def test_jacobian_discharge(self):
        """Test jacobian discharge."""

        uf = UniformFlow(2, cmath.pi/6)

        z = complex(10, 20)
        jac = UniformFlow.jacobian_discharge(uf, z)
        self.assertTrue(numpy.size(jac) == 0)


if __name__ == '__main__':
    unittest.main()
