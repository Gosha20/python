import unittest
from life_func import *


class TestLifeFunc(unittest.TestCase):

    def test_default_creation(self):
        game = GameField()
        self.assertEqual(game.weight, 25)
        self.assertEqual(game.hight, 25)
        self.assertEqual(len(game.matrix_field), 25)
        self.assertEqual(len(game.matrix_field[0]), 25)

    def test_custom_creation(self):
        game = GameField(2, 1)
        self.assertEqual(game.weight, 2)
        self.assertEqual(game.hight, 1)
        self.assertEqual(len(game.matrix_field), 1)
        self.assertEqual(len(game.matrix_field[0]), 2)

    def test_get_neighbors(self):
        game = GameField(5, 5)
        game.matrix_field[2][1] = 1
        game.matrix_field[3][1] = 1
        game.matrix_field[1][1] = 1
        game.matrix_field[3][3] = 1
        self.assertEqual(game.get_neighbors(3, 3), 0)
        self.assertEqual(game.get_neighbors(2, 1), 2)
        self.assertEqual(game.get_neighbors(1, 1), 1)
        self.assertEqual(game.get_neighbors(3, 1), 1)

    def test_infinity_field(self):
        game = GameField(5, 5)
        game.matrix_field[2][0] = 1
        game.matrix_field[3][0] = 1
        game.matrix_field[1][0] = 1
        game.refresh()
        self.assertEqual(game.matrix_field[2][4], 1)

    def test_custom_creation_refresh(self):
        game = GameField(7, 5)
        game.matrix_field[2][0] = 1
        game.matrix_field[3][0] = 1
        game.matrix_field[1][0] = 1
        game.refresh()
        self.assertEqual(game.matrix_field[2][0], 1)
        self.assertEqual(game.matrix_field[1][0], 0)
        self.assertEqual(game.matrix_field[3][0], 0)
        self.assertEqual(game.matrix_field[2][1], 1)
        self.assertEqual(game.matrix_field[2][6], 1)

    def test_clear_field(self):
        game = GameField(5, 5)
        for x in range(5):
            for y in range(5):
                game.matrix_field[x][y] = 1
        game.clear()
        for x in range(5):
            for y in range(5):
                self.assertEqual(game.matrix_field[x][y], 0)

    def test_refresh_tri_line(self):
        game = GameField(5, 5)
        game.matrix_field[2][0] = 1
        game.matrix_field[3][0] = 1
        game.matrix_field[1][0] = 1
        game.refresh()
        self.assertEqual(game.matrix_field[2][0], 1)
        self.assertEqual(game.matrix_field[1][0], 0)
        self.assertEqual(game.matrix_field[3][0], 0)
        self.assertEqual(game.matrix_field[2][1], 1)
        self.assertEqual(game.matrix_field[2][4], 1)

    def test_refresh_coub(self):
        game = GameField(5, 5)
        game.matrix_field[0][0] = 1
        game.matrix_field[1][0] = 1
        game.matrix_field[1][1] = 1
        game.matrix_field[0][1] = 1
        game.refresh()
        self.assertEqual(game.matrix_field[1][0], 1)
        self.assertEqual(game.matrix_field[0][0], 1)
        self.assertEqual(game.matrix_field[1][1], 1)
        self.assertEqual(game.matrix_field[0][1], 1)

    def test_refresh_solo_cell(self):
        game = GameField(5, 5)
        game.matrix_field[0][0] = 1
        game.refresh()
        self.assertEqual(game.matrix_field[0][0], 0)

    def test_refresh_double_cell(self):
        game = GameField(5, 5)
        game.matrix_field[0][0] = 1
        game.matrix_field[0][1] = 1
        game.refresh()
        self.assertEqual(game.matrix_field[0][0], 0)
        self.assertEqual(game.matrix_field[0][1], 0)


unittest.main()
