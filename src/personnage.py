class Personnage:

    def __init__(self):
        self.hp = 10
        self.armure = 0
        self.force = 1  # Force de base

    def get_hp(self):
        return self.hp

    def recevoir_attaque(self, attaquant):
        if not self.estMort():
            
            degats = 1 if attaquant is None else max(attaquant.force - self.armure, 0)

            
            if self.armure > 10:  
                degats = degats // 2  
                self.armure -= 10  

            
            self.hp -= degats

    def estMort(self):
        return self.hp <= 0

    def regenerer(self, montant):
        if not self.estMort():
            self.hp = min(10, self.hp + montant)
        # Si le personnage est mort, ne rien faire

    def equiper_armure(self, valeur):
        if not self.estMort():
            self.armure = max(0, min(10, valeur))  # Limite l'armure entre 0 et 10

    def set_force(self, valeur):
        self.force = max(1, min(10, valeur))  # Force entre 1 et 10

    def combattre(self, autre_personnage):
        while not self.estMort() and not autre_personnage.estMort():
            autre_personnage.recevoir_attaque(self)
            if autre_personnage.estMort():
                break
            self.recevoir_attaque(autre_personnage)

    def attaquer_special(self, autre_personnage):
        if not self.estMort():
            
            autre_personnage.recevoir_attaque(self)
            autre_personnage.hp -= self.force  
            self.hp -= 2
    def defendre(self):
        if not self.estMort():
            self.armure += 10  