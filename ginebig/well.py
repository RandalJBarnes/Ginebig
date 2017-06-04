"""
Well class for the Ginebig project.
"""
import numpy
import math
from ginebig.analytic_element import AnalyticElement


class Well(AnalyticElement):

    # --------------------------------------------------------------------------
    def __init__(self, z: complex, q: float, r: float):
        """
        Intialize the attributes without validating.

        Arguments:

        """
        self.z = z
        self.q = q
        self.r = r

    # --------------------------------------------------------------------------
    def potential(self, z: complex) -> complex:
        """
            Return the well's contribution to the complex potential
            at location z, $\Omnega(z)$.
        """
        return complex(0, 0)

    # --------------------------------------------------------------------------
    def discharge(self, z: complex) -> complex:
        """
        Return the well's contribution to the complex discharge
        at location z, $\W(z)$.
        """
        return complex(math.nan, math.nan)

    # --------------------------------------------------------------------------
    def total_discharge(self):
        """
        Return the well's total discharge from the aquifer.
        """
        return 0

    # --------------------------------------------------------------------------
    def jacobian_potential(self, z: complex) -> complex:
        """
        Return the well's $dOmega/dP$ at location z.
        """
        return complex(math.nan, math.nan)

    # --------------------------------------------------------------------------
    def jacobian_discharge(self, z: complex) -> complex:
        """
        Return the well's $dW/dP$ at location z.
        """
        return complex(math.nan, math.nan)
