#/usr/bin/env python3


import unittest
import battleship as battle


class BattleshipTest(unittest.TestCase):

    def test_ship(self):

        my_ship = battle.Ship(1, 2)
        self.assertEqual(True, True)


if __name__ == '__main__':
        unittest.main()
