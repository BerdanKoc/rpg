import unittest

from personnage import Personnage


class TestRpg(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personnage = Personnage()
        self.assertEqual(10, personnage.get_hp())

    def test_attaquer_enleve_1_hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_attaque(attaquant)
        self.assertEqual(9, defenseur.get_hp())

    def test_attaquer_enleve_2_hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_attaque(attaquant)
        defenseur.recevoir_attaque(attaquant)
        self.assertEqual(8, defenseur.get_hp())

    def test_attaquer_10_fois_tue(self):
        attaquant = Personnage()
        defenseur = Personnage()

        for i in range(0,10):
            defenseur.recevoir_attaque(attaquant)
        self.assertTrue(defenseur.estMort())

    def test_attaquer_9_fois_ne_tue(self):
        attaquant = Personnage()
        defenseur = Personnage()

        for i in range(0,9):
            defenseur.recevoir_attaque(attaquant)
        self.assertFalse(defenseur.estMort())

    def test_personnage_mort_reste_mort_apres_attaque(self):
        attaquant = Personnage()
        defenseur = Personnage()
        for i in range(10):
            defenseur.recevoir_attaque(attaquant)
        defenseur.recevoir_attaque(attaquant)
        self.assertEqual(0, defenseur.get_hp())
        self.assertTrue(defenseur.estMort())


if __name__ == '__main__':
    unittest.main()
