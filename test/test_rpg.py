import unittest

from personnage import Personnage


class TestRpg(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personnage = Personnage()
        self.assertEqual(10, personnage.get_hp())


if __name__ == '__main__':
    unittest.main()
