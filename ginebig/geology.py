"""
Geology class for the Ginebig project.

Raises:
    Error: Base class for all exceptions raised by this module.
    InvalidHydraulicConductivityError: The hydraulic conductivity
        must be strictly positive.
    InvalidPorosityError: The porosity must be strictly positive,
        but less than 1.
    InvalidAquiferThicknessError: The aquifer thickness must be
        strictly positive.
Notes:
    The Geology class is currently implemented for a homogeneous, isotropic
        aquifer. However, the hooks exist to allow for a future transition
        to piecewise constant aquifer properties.

"""

import numpy

__version__ = '05 June 2017'


# ------------------------------------------------------------------------------
class Error(Exception):
    """Base class for all exceptions raised by this module."""


class InvalidHydraulicConductivityError(Error):
    """The hydraulic conductivity must be strictly positive."""


class InvalidPorosityError(Error):
    """The porosity must be strictly positive, but less than 1."""


class InvalidAquiferThicknessError(Error):
    """The aquifer thickness must be strictly positive."""


class InvalidHeadError(Error):
    """The specified head is below the base of the aquifer."""


# ------------------------------------------------------------------------------
class Geology:

    # --------------------------------------------------------------------------
    def __init__(self, hydraulic_conductivity: float, porosity: float,
                 aquifer_thickness: float, base_elevation: float):
        """

        Arguments:
            hydraulic_conductivity (float):
            porosity (float):
            aquifer_thickness (float):
            base_elevation (float):

        """
        if hydraulic_conductivity < numpy.finfo(float).eps:
            raise InvalidHydraulicConductivityError

        if porosity < numpy.finfo(float).eps or porosity >= 1:
            raise InvalidPorosityError

        if aquifer_thickness < numpy.finfo(float).eps:
            raise InvalidAquiferThicknessError

        self.hydraulic_conductivty = hydraulic_conductivity
        self.porosity = porosity
        self.aquifer_thickness = aquifer_thickness
        self.base_elevation = base_elevation

    # --------------------------------------------------------------------------
    def __repr__(self):
        # TODO: add this code.
        return None

    # --------------------------------------------------------------------------
    def __str__(self):
        # TODO: add this code.
        return None

    # --------------------------------------------------------------------------
    def properties(self, z: complex):
        """
        """

        p = (
                self.hydraulic_conductivty,
                self.porosity,
                self.aquifer_thickness,
                self.base_elevation
            )
        return p

    # --------------------------------------------------------------------------
    def head2Phi(self, head: float, z: complex) -> float:
        """
        """

        k, rho, H, b = Geology.properties(self, z)

        if head >= b+H:
            Phi = k*H*(head-b) - 0.5*k*H**2
        elif head >= b:
            Phi = 0.5 * k * (head-b)**2
        else:
            raise InvalidHeadError('head below the base of the aquifer')

        return Phi

    # --------------------------------------------------------------------------
    def Phi2head(self, Phi: float, z: complex) -> float:
        """
        """

        # TODO: add this code.
        return None
