"""
Define the abstract base class AnalyticElement.

Notes
-----

References
----------


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
        """
        Return the element's complex potential, Omega(z), evaluated at
        locations <z>.

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
            not exist for the element, the missing component is set to NaN.
        """
        raise NotImplementedError('"potential" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def discharge(self, z):
        """
        Return the analytic element's contribution to the complex discharge
        function, W(z), at locations <z>.

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
            -   [L^3/T]
        """
        raise NotImplementedError('"discharge" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def total_discharge(self):
        """
        Return the analytic element's total discharge from the aquifer.

        Arguments
        ---------

        Returns
        -------
        Q : float64
            -   total discharge from the aquifer; e.g. the discharge from
                a well or the integrated discharge along a line sink.
            -   [L^3/T].
        """
        raise NotImplementedError('"total_discharge" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def jacobian_potential(self, z):
        """
        Return the analytic element's dOmega/dP at locations <z>.

        If either the discharge potential or the stream function does not
        exist for the element (e.g. the stream function does not exist for
        areal accretion), then the missing component is set to NaN.
        """
        raise NotImplementedError('jacobian_potential" must be implemented.')

    # --------------------------------------------------------------------------
    @abc.abstractmethod
    def jacobian_discharge(self, z):
        """
        Return the analytic element's dW/dP at locations <z>.
        """
        raise NotImplementedError('"jacobian_discharge" must be implemented.')
