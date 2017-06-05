"""
UniformFlow class for the Ginebig project.

Raises:
    uniform_flow.Error: Base class for all exceptions raised by this module.
"""

import cmath
import numpy

from ginebig.analytic_element import AnalyticElement

__version__ = '05 June 2017'


# ------------------------------------------------------------------------------
class Error(Exception):
    """Base class for all exceptions raised by this module."""


# ------------------------------------------------------------------------------
class UniformFlow(AnalyticElement):

    # --------------------------------------------------------------------------
    def __init__(self, Qo: float, alpha: float):
        """
        Intialize the attributes with minimal validation.

        Arguments:
           Qo (float): magnitude of the uniform flow [L^2/T].
           alpha (float): direction of the uniform flow [rad].

        """
        self.Qo = Qo
        self.alpha = alpha

    # --------------------------------------------------------------------------
    def __repr__(self):
        return 'UniformFlow({0.Qo!r},{0.alpha!r})'.format(self)

    # --------------------------------------------------------------------------
    def __str__(self):
        return 'UniformFlow(Qo={0.Qo!s},alpha={0.alpha!s})'.format(self)

    # --------------------------------------------------------------------------
    def complex_potential(self, z: complex) -> complex:
        """
        UniformFlow's complex potential at location <z>.

        Return the uniform flow's contribution to the complex potential,
        Omega(z) [L^3/T], evaluated at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            complex: complex potential at location <z> [L^3/T].

        Notes:
        -   The location <z> does not make any difference for uniform flow.

        """
        Omega = -self.Qo * cmath.exp(-complex(0, self.alpha)) * z
        return Omega

    # --------------------------------------------------------------------------
    def complex_discharge(self, z: complex) -> complex:
        """
        UniformFlow's complex discharge at location <z>.

        Return the unifrm flow's contribution to the complex discharge
        function, W(z) [L^2/T], at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            complex: complex discharge at location <z> [L^2/T].

        Notes:
        -   The location <z> does not make any difference for uniform flow.

        """
        W = self.Qo * cmath.exp(-complex(0, self.alpha))
        return W

    # --------------------------------------------------------------------------
    def abstraction(self):
        """
        UniformFlow's abstraction from the aquifer.

        Returns:
            float: abstraction from the aquifer [L^3/T].

        """
        return float(0)

    # --------------------------------------------------------------------------
    def divergence_discharge(self, z: complex) -> float:
        """
        UniformFlow's divergence of the discharge at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            float: divergence of the discharge at location <z> [L/T].

        Notes:
        -   The divergence of the discharge for UniformFlow is 0 everywhere.

        """
        return float(0)

    # --------------------------------------------------------------------------
    def jacobian_potential(self, z: complex) -> complex:
        """
        UniformFlow's Jacobian matrix of the complex potential for the free
        parameters

        Return the analytic element's dOmega/dP at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            numpy.array of complex128: empty array.

        Notes:
        -   Uniform flow has no free parameters, so there are no derivatives.

        """
        return numpy.array([], dtype=numpy.complex128)

    # --------------------------------------------------------------------------
    def jacobian_discharge(self, z: complex) -> complex:
        """
        UniformFlow's Jacobian matrix of the complex potential for the free
        parameters

        Return the analytic element's dOmega/dP at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            numpy.array of complex128: empty array.

        Notes
        -----
        -   Uniform flow has no free parameters, so there are no derivatives.

        """
        return numpy.array([], dtype=numpy.complex128)
