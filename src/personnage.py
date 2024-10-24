class Personnage:

    def __init__(self):
        self.__hp = 10
        self.__est_mort = False

    def get_hp(self):
        return self.__hp

    def recevoir_attaque(self, attaquant):
        if not self.__est_mort:
            self.__hp -= 1
            if self.__hp <= 0:
                self.__hp = 0
                self.__est_mort = True

    def estMort(self):
        return self.__est_mort
