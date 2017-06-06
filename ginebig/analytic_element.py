"""
Abstract base class AnalyticElement.

The abstract base class AnalyticElement, defined in this module, serves as
the base class for ALL analytic elements in the Ginebig project.

Notes:
-   The notation, terminology, and formulation used in this project
    are based on Strack 1989 and on an pre-release version of Strack 2017.

References:
-   Otto D. L. Strack, 1989, Groundwater Mechanics, Prentice-Hall, Inc.,
    732 pp., ISBN-10: 0133654125.

-   Otto D. L. Strack, 2017, Analytical Groundwater Mechanics,  Cambridge
    University Press, 454 pp., ISBN-10: 1107148839.

"""

import abc

__version__ = '05 June 2017'


class AnalyticElement(abc.ABC):
    """
    Abstract base class for all analytic elements.

    Concrete methods:
        def activate(self)
        def deactivate(self)
        def isactive(self)

    Required abstract methods:
        def complex_potential(self, z)
        def complex_discharge(self, z)

        def abstraction(self)

        def divergence_discharge(self, z)
        def jacobian_potential(self, z)
        def jacobian_discharge(self, z)

        def solve(self, root)
        def boundary_conditions(self, root)

    """

    # --------------------------------------------------------------------------
    def activate(self):
        self.active = True

    # --------------------------------------------------------------------------
    def deactivate(self):
        self.active = False

    # --------------------------------------------------------------------------
    def isactive(self):
        return self.active

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def complex_potential(self, z: complex) -> complex:
        """
        Element's complex potential at location <z>.

        Return the analytic element's contribution to the complex potential,
        Omega(z) [L^3/T], evaluated at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            complex: complex potential at location <z> [L^3/T].

        Notes:
        -   The complex potential is defined by Omega(z) = Phi(z) + i*Psi(z),
            where Phi(z) is the discharge potential [L^3/T], and Psi(z) is the
            stream function [L^3/T].

        -   If either the discharge potential or the stream function does
            not exist for the element (e.g. a regional recharge element has
            no stream function) the missing component is set to NaN.

        """
        raise NotImplementedError('"complex_potential" is not implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def complex_discharge(self, z: complex) -> complex:
        """
        Element's complex discharge at location <z>.

        Return the analytic element's contribution to the complex discharge
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

        """
        raise NotImplementedError('"complex_discharge" is not implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def abstraction(self) -> float:
        """
        Element's abstraction from the aquifer.

        Return the analytic element's abstraction from the aquifer. The
        abstraction is the total quantity of water removed from the aquifer
        by the element per unit time [L^3/T].

        Returns:
            float: abstraction from the aquifer [L^3/T].

        Notes:
        -   For example, the discharge from a well or the integrated discharge
            along a line sink are abstrations.

        """
        raise NotImplementedError('"abstraction" is not implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def divergence_discharge(self, z: complex) -> float:
        """
        Element's divergence of the discharge at location <z>.

        The divergence of the discharge is the accretion at a point: the volume
        added to the aquifer per unit area [L/T].

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            float: divergence of the discharge at location <z> [L/T].

        Notes:
        -   The divergence of the discharge is the negative of the Laplacian
            of the discharge potential.

        """
        raise NotImplementedError('"divergence_discharge" not implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def jacobian_potential(self, z: complex):
        """
        Element's Jacobian matrix of the complex potential for the free
        parameters

        Return the analytic element's dOmega/dP at location <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns
            TODO: actually explain this method.

        Notes:
        -   If either the discharge potential or the stream function does not
            exist for the element (e.g. the stream function does not exist for
            areal accretion), then the missing component is set to NaN.

        """
        raise NotImplementedError('"jacobian_potential" is not implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def jacobian_discharge(self, z: complex):
        """
        Element's Jacobian matrix of the complex discharge for the free
        parameters

        Return the analytic element's dW/dP at locations <z>.

        Arguments:
            z (complex): 'little z' world coordinate location [L].

        Returns:
            TODO: actually explain this method.

        """
        raise NotImplementedError('"jacobian_discharge" is not implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def solve(self, root, geo):
        raise NotImplementedError('"solve" is not implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def boundary_conditions(self, root, geo):
        raise NotImplementedError('"boundary_conditions" is not implemented.')
