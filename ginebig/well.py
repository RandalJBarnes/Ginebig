"""
Well class for the Ginebig project.

Raises:
    well.Error: Base class for all exceptions raised by this module.
    well.InvalidRadiusError: The specified well radius was not strictly
        positive.
"""

import cmath
import numpy
from ginebig.analytic_element import AnalyticElement

__version__ = '05 June 2017'


# ------------------------------------------------------------------------------
class Error(Exception):
    """Base class for all exceptions raised by this module."""


class InvalidRadiusError(Error):
    """The specified well radius was not strictly positive."""


# ------------------------------------------------------------------------------
class Well(AnalyticElement):

    # --------------------------------------------------------------------------
    def __init__(self, z: complex, Q: float, r: float):
        """
        Intialize the attributes with minimal validation.

        Arguments:
           z (complex): 'little z' world coordinate location [L].
           Q (float): well discharge [L^3/T].
           r (float): well radius [L].

        """
        if r < numpy.finfo(float).eps:
            raise InvalidRadiusError

        self.z = z
        self.Q = Q
        self.r = r

    # --------------------------------------------------------------------------
    def complex_potential(self, z: complex) -> complex:
        """
        Well's complex potential at location <z>.

        Return the well's contribution to the complex potential,
        Omega(z) [L^3/T], evaluated at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            complex: complex potential at location <z> [L^3/T].

        Notes:
        -   The complex potential is defined by Omega(z) = Phi(z) + i*Psi(z),
            where Phi(z) is the discharge potential [L^3/T], and Psi(z) is the
            stream function [L^3/T].

        -   If the location <z> is inside the radius of the well, the
            complex potential at the radius of the well is returned.

        """
        zz = z - self.z
        if abs(zz) >= self.r:
            Omega = self.Q/(2*cmath.pi) * cmath.log(zz)
        else:
            Omega = self.Q/(2*cmath.pi) * cmath.log(self.r)
        return Omega

    # --------------------------------------------------------------------------
    def complex_discharge(self, z: complex) -> complex:
        """
        Well's complex discharge at location <z>.

        Return the well's contribution to the complex discharge
        function, W(z) [L^2/T], at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            complex: complex discharge at location <z> [L^2/T].

        Notes:
        -   The complex discharge is defined by W(z) = Qx(z) - i*Qy(z),
            where Qx is the x-component of the vertically integrated specific
            discharge [L^2/T], and Qy is the y-component of the vertically
            integrated specific discharge [L^2/T].

        -   If the location <z> is inside the radius of the well, math.nan
            is returned.

        """
        zz = z - self.z
        if abs(zz) >= self.r:
            W = -self.Q/(2*cmath.pi) / zz
        else:
            W = complex(cmath.nan, cmath.nan)
        return W

    # --------------------------------------------------------------------------
    def abstraction(self):
        """
        Well's abstraction from the aquifer.

        Return the well's abstraction from the aquifer. The abstraction is the
        total quantity of water removed from the aquifer by the well per unit
        time [L^3/T].

        Returns:
            float: abstraction from the aquifer [L^3/T].

        """
        return self.Q

    # --------------------------------------------------------------------------
    def divergence_discharge(self, z: complex) -> float:
        """
        Well's divergence of the discharge at location <z>.

        The divergence of the discharge is the accretion at a point: the volume
        added to the aquifer per unit area [L/T].

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            float: divergence of the discharge at location <z> [L/T].

        Notes:
        -   The divergence of the discharge is the negative of the Laplacian
            of the discharge potential.

        -   If the location <z> is inside the radius of the well, math.nan
            is returned.

        """
        zz = z - self.z
        if abs(zz) >= self.r:
            div = float(0)
        else:
            div = cmath.nan
        return div

    # --------------------------------------------------------------------------
    def jacobian_potential(self, z: complex) -> complex:
        """
        Well's Jacobian matrix of the complex potential for the free
        parameters

        Return the analytic element's dOmega/dP at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            numpy.array of complex128: empty array.

        Notes:
        -   The well has no free parameters, so there are no derivatives.

        """
        return numpy.array([], dtype=numpy.complex128)

    # --------------------------------------------------------------------------
    def jacobian_discharge(self, z: complex) -> complex:
        """
        Well's Jacobian matrix of the complex potential for the free
        parameters

        Return the analytic element's dOmega/dP at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            numpy.array of complex128: empty array.

        Notes
        -----
        -   The well has no free parameters, so there are no derivatives.

        """
        return numpy.array([], dtype=numpy.complex128)
