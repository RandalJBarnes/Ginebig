"""<well.py> implements the Well class.

This file is part of the Ginebig Project and is distributed under the
BSD-3-Clause license. See the accompanying LICENSE.txt file.

Copyright (c) 2017, Randal J. Barnes
"""

import cmath
import numpy

from ginebig.analytic_element import AnalyticElement

__version__ = '07 June 2017'


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
           z (complex): center of the well [L].
           Q (float): well discharge [L^3/T].
           r (float): well radius [L].

        Raises:
            well.Error: Base class for all exceptions raised by this
                module.
            well.InvalidRadiusError: The specified well radius was not
                strictly positive.
        """
        if r < numpy.finfo(float).eps:
            raise InvalidRadiusError

        self.z = z
        self.Q = Q
        self.r = r

    # --------------------------------------------------------------------------
    def __repr__(self):
        return 'Well({0.z!r},{0.Q!r},{0.r!r})'.format(self)

    # --------------------------------------------------------------------------
    def __str__(self):
        return 'Well(z={0.z!s},Q={0.Q!s},r={0.r!s})'.format(self)

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

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            float: divergence of the discharge at location <z> [L/T].

        Notes:
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
    def solve(self, geo, root):
        """
        """
        raise NotImplementedError('"solve" is not yet implemented.')
