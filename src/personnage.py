class Personnage:

    def __init__(self):
        self.hp = 10
        self.armure = 0

    def get_hp(self):
        return self.hp

    def recevoir_attaque(self, attaquant):
        if not self.estMort():
            degats = max(1 - self.armure, 0)  # Les dégâts ne peuvent pas être négatifs
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
