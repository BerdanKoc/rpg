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


if __name__ == '__main__':
    unittest.main()
