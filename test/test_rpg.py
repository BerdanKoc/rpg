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

    def test_personnage_mort_ne_peut_pas_regenerer(self):
        personnage = Personnage()
        # Tuer le personnage
        for i in range(10):
            personnage.recevoir_attaque(None)
        
        # Essayer de régénérer
        personnage.regenerer(5)
        
        # Le personnage devrait rester mort avec 0 HP
        self.assertEqual(0, personnage.get_hp())
        self.assertTrue(personnage.estMort())

    def test_personnage_mort_ne_peut_pas_equiper_armure(self):
        personnage = Personnage()
        # Tuer le personnage
        for i in range(10):
            personnage.recevoir_attaque(None)
            
        # Essayer d'équiper une armure
        personnage.equiper_armure(5)
        
        # L'armure ne devrait pas être équipée (devrait rester à 0)
        self.assertEqual(0, personnage.armure)

    def test_armure_maximum_10(self):
        personnage = Personnage()
        
        # Essayer d'équiper une armure supérieure à 10
        personnage.equiper_armure(15)
        
        # L'armure devrait être limitée à 10
        self.assertEqual(10, personnage.armure)

    def test_armure_ne_peut_pas_etre_negative(self):
        personnage = Personnage()
        
        # Essayer d'équiper une armure négative
        personnage.equiper_armure(-5)
        
        # L'armure ne devrait pas être négative (minimum 0)
        self.assertEqual(0, personnage.armure)

    def test_force_augmente_degats(self):
        attaquant = Personnage()
        defenseur = Personnage()
        
        # Augmenter la force de l'attaquant
        attaquant.set_force(3)
        
        # Une attaque devrait faire 3 points de dégâts
        defenseur.recevoir_attaque(attaquant)
        self.assertEqual(7, defenseur.get_hp())  # 10 HP - 3 dégâts
    def test_initier_combat(self):
        attaquant = Personnage()
        defenseur = Personnage()
        
        attaquant.combattre(defenseur)
        self.assertTrue(True)
    def test_combat_reduit_hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        
        # Simuler un combat
        attaquant.combattre(defenseur)
        
        # Vérifier que le défenseur a perdu des HP
        self.assertLess(defenseur.get_hp(), 10)
    def test_combat_tours_multiples(self):
        attaquant = Personnage()
        defenseur = Personnage()

        attaquant.combattre(defenseur)
        self.assertTrue(attaquant.estMort() or defenseur.estMort())
    def test_attaquer_special_reduit_hp_attaquant_et_inflige_degats_doubles(self):
        attaquant = Personnage()
        defenseur = Personnage()

        # Lancer une attaque spéciale
        attaquant.attaquer_special(defenseur)
        self.assertEqual(defenseur.get_hp(), 8)  

        self.assertEqual(attaquant.get_hp(), 8)  
    def test_defendre_reduit_degats(self):
        attaquant = Personnage()
        defenseur = Personnage()

        defenseur.defendre()

        attaquant.set_force(5)
        defenseur.recevoir_attaque(attaquant)

        self.assertEqual(defenseur.get_hp(), 8)  



if __name__ == '__main__':
    unittest.main()
