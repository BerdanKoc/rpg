class Personnage:

    def __init__(self):
        self.__hp = 10

    def get_hp(self):
        return self.__hp

    def recevoir_attaque(self, attaquant):
        self.__hp -= 1

    def estMort(self):
        return True
