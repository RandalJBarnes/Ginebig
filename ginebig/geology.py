"""<geology.py> implements the Geology class.

This file is part of the Ginebig Project and is distributed under the
BSD-3-Clause license. See the accompanying LICENSE.txt file.

Copyright (c) 2017, Randal J. Barnes
"""

import math

__version__ = '06 June 2017'


# ------------------------------------------------------------------------------
class Error(Exception):
    """Base class for all exceptions raised by this module."""


class InvalidHeadError(Error):
    """The head must be above the base of the aquifer."""


class InvalidDischargePotentialError(Error):
    """The discharge potential must be positive."""


# ------------------------------------------------------------------------------
class Geology(object):
    """The Geology class is the librarian for the hydrogeology.

    The Geology class organizes, maintains, and serves the hydrogeologic
    parameters. The Geology class provides methods to convert between
    physically measurable head and the mathematically useful discharge
    potential Phi.

    The Geology class is currently implemented for a homogeneous, isotropic
    aquifer. However, the hooks exist to allow for a future transition to
    piecewise constant aquifer properties.

    Raises:
        Error: Base class for all exceptions raised by this module.
    """

    # --------------------------------------------------------------------------
    def __init__(self,
                 hydraulic_conductivity: float,
                 aquifer_porosity: float,
                 aquifer_thickness: float,
                 base_elevation: float):
        """Initialize the Geology class.

        Arguments:
            hydraulic_conductivity (float): The homogeneous, isotropic
                aquifer hydraulic conductivity [L/T].
            aquifer_porosity (float): The homogeneous aquifer porosity [].
            aquifer_thickness (float): The homogeneous aquifer thickness [L].
            base_elevation (float): The homogeneous base elevation [L].
        """

        self.hydraulic_conductivity = hydraulic_conductivity
        self.aquifer_porosity = aquifer_porosity
        self.aquifer_thickness = aquifer_thickness
        self.base_elevation = base_elevation

    # --------------------------------------------------------------------------
    def __repr__(self):
        return 'Geology({0.hydraulic_conductivity!r},' \
               '{0.aquifer_porosity!r},{0.aquifer_thickness!r},' \
               '{0.base_elevation!r})'.format(self)

    # --------------------------------------------------------------------------
    def __str__(self):
        str = 'GEOLOGY\n\t' + self.__repr__()
        # TODO: improve this.
        return str

    # --------------------------------------------------------------------------
    def properties(self, z: complex):
        """Return all of the hydrogeologic properties as a tuple."""
        p = (
                self.hydraulic_conductivity,
                self.aquifer_porosity,
                self.aquifer_thickness,
                self.base_elevation
            )
        return p

    # --------------------------------------------------------------------------
    def head2Phi(self, head: float, z: complex) -> float:
        """Convert the head to a discharge potential.

        Raises:
            InvalidHeadError: The head must be above the base of the aquifer.
        """

        k, rho, H, b = self.properties(z)

        if head >= b+H:
            Phi = k*H*(head-b) - 0.5*k*H**2
        elif head > b:
            Phi = 0.5 * k * (head-b)**2
        else:
            raise InvalidHeadError

        return Phi

    # --------------------------------------------------------------------------
    def Phi2head(self, Phi: float, z: complex) -> float:
        """Convert the discharge potential to a head.

        Raises:
            InvalidDischargePotentialError: The discharge potential must be
                positive.
        """

        k, rho, H, b = self.properties(z)

        if Phi >= 0.5*k*H**2:
            head = Phi/(k*H) + H/2 + b
        elif Phi > 0:
            head = math.sqrt(2*Phi/k) + b
        else:
            raise InvalidDischargePotentialError

        return head
