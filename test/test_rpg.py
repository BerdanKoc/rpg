import unittest
import sys
import os

# Ajouter le dossier racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.personnage import Personnage


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

    def test_regeneration_hp(self):
        personnage = Personnage()
        personnage.recevoir_attaque(None)  # Réduit les HP de 1
        personnage.regenerer(2)  # Régénère 2 HP
        self.assertEqual(10, personnage.get_hp())

    def test_armure_reduit_degats(self):
        attaquant = Personnage()
        defenseur = Personnage()
        
        defenseur.equiper_armure(2)  # Armure qui réduit de 2 les dégâts
        defenseur.recevoir_attaque(attaquant)
        
        # L'armure devrait absorber tout le dégât (1 point)
        self.assertEqual(10, defenseur.get_hp())


if __name__ == '__main__':
    unittest.main()
