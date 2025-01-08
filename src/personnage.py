class Personnage:

    def __init__(self):
        self.hp = 10

    def get_hp(self):
        return self.hp

    def recevoir_attaque(self, attaquant):
        if not self.estMort():
            self.hp -= 1

    def estMort(self):
        return self.hp <= 0

    def regenerer(self, montant):
        if not self.estMort():
            self.hp = min(10, self.hp + montant)
