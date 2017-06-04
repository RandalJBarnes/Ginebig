"""
Define the abstract base class AnalyticElement.

The abstract base class AnalyticElement, defined in this module, serves as
the base class for ALL analytic elements in the Ginebig project.


Notes
-----

-   The notation, terminology, and formulation used in this project
    are based on Strack 1989 and on an pre-release version of Strack 2017.


References
----------

-   Otto D. L. Strack, 1989, Groundwater Mechanics, Prentice-Hall, Inc.,
    732 pp., ISBN-10: 0133654125.

-   Otto D. L. Strack, 2017, Analytical Groundwater Mechanics,  Cambridge
    University Press, 454 pp., ISBN-10: 1107148839.

"""

import abc


class AnalyticElement(abc.ABC):
    """
    Abstract base class for all analytic elements.

    Required Methods
    ----------------
        def potential(self, z)
        def discharge(self, z)
        def total_discharge(self)
        def jacobian_potential(self, z)
        def jacobian_discharge(self, z)
    """

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def potential(self, z):
        """Complex potential at locations <z>.

        Return the analytic element's contribution to the complex potential,
        Omega(z) [L^3/T], evaluated at locations <z>.

        Arguments
        ---------
        z : numpy:array of complex128
            -   (PxQ) matrix of locations in "little z" world coordinates.
            -   <z> may be empty.
            -   [L]

        Returns
        -------
        Omega : numpy:array of complex128
            -   (PxQ) matrix of complex potentials at the <z> locations.
            -   If <z> is empty, then so is <Omega>.
            -   [L^3/T]

        Notes
        -----
        o   If either the discharge potential or the stream function does
            not exist for the element (e.g. a regional recharge element has
            no stream function) the missing component is set to NaN.
        """
        raise NotImplementedError('"potential" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def discharge(self, z):
        """Complex discharge at locations <z>.

        Return the analytic element's contribution to the complex discharge
        function, W(z) [L^2/T], at locations <z>.

        Arguments
        ---------
        z : numpy:array of complex128
            -   (PxQ) matrix of locations in "little z" world coordinates.
            -   <z> may be empty.
            -   [L]

        Returns
        -------
        W : numpy:array of complex128
            -   (PxQ) matrix of complex discharges at the <z> locations.
            -   If <z> is empty, then so is <W>.
            -   [L^2/T]
        """
        raise NotImplementedError('"discharge" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def total_discharge(self):
        """Total discharge from the aquifer.

        Return the analytic element's total discharge from the aquifer;
        e.g. the discharge from a well or the integrated discharge along a
        line sink.

        Arguments
        ---------

        Returns
        -------
        Q : float64
            -   total discharge from the aquifer.
            -   [L^3/T].
        """
        raise NotImplementedError('"total_discharge" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def jacobian_potential(self, z):
        """Jacobian of the complex potential.

        Return the analytic element's dOmega/dP at locations <z>.

        If either the discharge potential or the stream function does not
        exist for the element (e.g. the stream function does not exist for
        areal accretion), then the missing component is set to NaN.

        TODO: actually explain this method.
        """
        raise NotImplementedError('"jacobian_potential" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def jacobian_discharge(self, z):
        """Jacobian of the complex discharge.

        Return the analytic element's dW/dP at locations <z>.

        TODO: actually explain this method.
        """
        raise NotImplementedError('"jacobian_discharge" must be implemented.')
