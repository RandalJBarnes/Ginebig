"""<reference_point.py> implements the ReferencePoint class.

This file is part of the Ginebig Project and is distributed under the
BSD-3-Clause license. See the accompanying LICENSE.txt file.

Copyright (c) 2017, Randal J. Barnes
"""

from ginebig.analytic_element import AnalyticElement

__version__ = '07 June 2017'


# ------------------------------------------------------------------------------
class Error(Exception):
    """Base class for all exceptions raised by this module."""


# ------------------------------------------------------------------------------
class ReferencePoint(AnalyticElement):

    # --------------------------------------------------------------------------
    def __init__(self, z: complex, head: float):
        """
        Intialize the attributes with minimal validation.

        Arguments:
           z (complex): 'little z' world coordinate location [L].
           head (float): head at the reference point [L].

        """

        self.z = z
        self.head = head

    # --------------------------------------------------------------------------
    def __repr__(self):
        return 'ReferencePoint({0.z!r},{0.head!r})'.format(self)

    # --------------------------------------------------------------------------
    def __str__(self):
        return 'ReferencePoint(z={0.z!s},head={0.Q!s})'.format(self)

    # --------------------------------------------------------------------------
    def complex_potential(self, z: complex) -> complex:
        """
        ReferencePoint's complex potential at location <z>.

        Return the reference point's contribution to the complex potential,
        Omega(z) [L^3/T], evaluated at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            complex: complex potential at location <z> [L^3/T].

        """
        return complex(0, 0)

    # --------------------------------------------------------------------------
    def complex_discharge(self, z: complex) -> complex:
        """
        ReferencePoint's complex discharge at location <z>.

        Return the reference point's contribution to the complex discharge
        function, W(z) [L^2/T], at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            complex: complex discharge at location <z> [L^2/T].

        """
        return complex(0, 0)

    # --------------------------------------------------------------------------
    def abstraction(self):
        """
        ReferencePoint's abstraction from the aquifer.

        Return the reference point's abstraction from the aquifer. The
        abstraction is the total quantity of water removed from the aquifer by
        the reference point per unit time [L^3/T].

        Returns:
            float: abstraction from the aquifer [L^3/T].

        """
        return float(0)

    # --------------------------------------------------------------------------
    def divergence_discharge(self, z: complex) -> float:
        """
        ReferencePoint's divergence of the discharge at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            float: divergence of the discharge at location <z> [L/T].

        """
        return float(0)

    # --------------------------------------------------------------------------
    def solve(self, geo, root):
        """
        """
        raise NotImplementedError('"solve" is not yet implemented.')
