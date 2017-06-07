import unittest

from ginebig.geology import (Geology, InvalidHeadError,
                             InvalidDischargePotentialError)


class TestGeology(unittest.TestCase):
    """Test the Geology class."""

    # --------------------------------------------------------------------------
    def test_construction(self):
        """Test the initialization."""

        geo = Geology(1, 0.2, 3, 4)

        self.assertAlmostEqual(geo.hydraulic_conductivity, 1)
        self.assertAlmostEqual(geo.aquifer_porosity, 0.2)
        self.assertAlmostEqual(geo.aquifer_thickness, 3)
        self.assertAlmostEqual(geo.base_elevation, 4)

    # --------------------------------------------------------------------------
    def test_properties(self):
        """Test the properties retrival."""

        geo = Geology(1, 0.2, 3, 4)
        z = complex(0, 0)

        k, rho, H, b = geo.properties(z)

        self.assertAlmostEqual(k, 1)
        self.assertAlmostEqual(rho, 0.2)
        self.assertAlmostEqual(H, 3)
        self.assertAlmostEqual(b, 4)

    # --------------------------------------------------------------------------
    def test_head2Phi(self):
        """Test the head to discharge potential convertion."""

        geo = Geology(1, 0.2, 3, 4)
        z = complex(0, 0)

        self.assertRaises(InvalidHeadError, geo.head2Phi, 2, z)

        head = 5
        Phi = geo.head2Phi(head, z)
        head = geo.Phi2head(Phi, z)
        self.assertAlmostEqual(head, 5)

        head = 50
        Phi = geo.head2Phi(head, z)
        head = geo.Phi2head(Phi, z)
        self.assertAlmostEqual(head, 50)

    # --------------------------------------------------------------------------
    def test_Phi2head(self):
        """Test the discharge potential to head convertion."""

        geo = Geology(1, 0.2, 3, 4)
        z = complex(0, 0)

        self.assertRaises(InvalidDischargePotentialError, geo.Phi2head, -1, z)

        Phi = 5
        head = geo.Phi2head(Phi, z)
        Phi = geo.head2Phi(head, z)
        self.assertAlmostEqual(Phi, 5)

        Phi = 500
        head = geo.Phi2head(Phi, z)
        Phi = geo.head2Phi(head, z)
        self.assertAlmostEqual(Phi, 500)


if __name__ == '__main__':
    unittest.main()
