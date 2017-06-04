""" 
Well class for the Ginebig project.
"""
import numpy
import analytic_element


class Well(analytic_element.AnalyticElement):
    
    # --------------------------------------------------------------------------
    def __init__(self, z: complex, Q, r):
        """
        Intialize the attributes without validating.
        """
        self.z = z
        self.Q = Q
        self.r = r

    # --------------------------------------------------------------------------
    def complex_potential(self, z: complex) -> complex:
        """
            Return the well's contribution to the complex potential
            at location z, $\Omnega(z)$.
        """
        return complex(math.nan, math.nan)
    
    # --------------------------------------------------------------------------
    def complex_discharge(self, z: complex) -> complex:
        """
        Return the well's contribution to the complex discharge
        at location z, $\W(z)$.
        """
        return complex(math.nan, math.nan)

    # --------------------------------------------------------------------------
    def accretion(self):
        """
        Return the Well's accretion at location z.
        """
        return math.nan

    # --------------------------------------------------------------------------
    def total_discharge(self):
        """
        Return the well's total discharge from the aquifer.
        """
        raise NotImplementedError('Method "total_discharge" must be implemented.')

    # --------------------------------------------------------------------------
    def domegadp(self, z: complex) -> complex:
        """
        Return the well's $dOmega/dP$ at location z.
        """
        return complex(math.nan, math.nan)

    # --------------------------------------------------------------------------
    def dwdp(self, z: complex) -> complex:
        """
        Return the well's $dW/dP$ at location z.
        """
        return complex(math.nan,math.nan)