import unittest
from coub_func import *


class TestLifeFunc(unittest.TestCase):

    def test_default_creation(self):
        game = GameField()
        self.assertEqual(game.weight, 15)
        self.assertEqual(game.height, 15)
        self.assertEqual(len(game.matrix_field), 15)
        self.assertEqual(len(game.matrix_field[0]), 15)

    def test_custom_creation(self):
        game = GameField(24, 10)
        self.assertEqual(game.weight, 24)
        self.assertEqual(game.height, 10)
        self.assertEqual(len(game.matrix_field), 10)
        self.assertEqual(len(game.matrix_field[0]), 24)

    def test_swap_columns(self):
        game = GameField(5, 5)
        for i in range(game.height):
            game.matrix_field[i][0] = 1
        for i in range(game.height):
            game.matrix_field[i][1] = 2
        game.swap_columns(0)
        for i in range(game.height):
            self.assertEqual(game.matrix_field[i][0], 2)
            self.assertEqual(game.matrix_field[i][1], 1)

    def test_left_zero(self):
        game = GameField(5, 5)
        for i in range(game.height):
            game.matrix_field[i][0] = 0
            game.matrix_field[i][2] = 0
            game.matrix_field[i][1] = 0
            game.matrix_field[i][3] = 2
        game.left_zero()
        for i in range(game.height):
            self.assertEqual(game.matrix_field[i][0], 2)

    def test_once_up_zero(self):
        game = GameField(5, 5)
        for i in range(game.height):
            for j in range(game.weight):
                game.matrix_field[i][j] = 5
        game.matrix_field[4][4] = 0
        game.matrix_field[4][0] = 0
        game.once_up_zero()

        self.assertEqual(game.matrix_field[0][4], 0)
        self.assertEqual(game.matrix_field[0][0], 0)
        self.assertEqual(game.matrix_field[2][2], 5)
        self.assertEqual(game.matrix_field[2][3], 5)
        self.assertEqual(game.matrix_field[1][2], 5)
        self.assertEqual(game.matrix_field[1][3], 5)

    def test_get_chains(self):
        game = GameField(5, 5)
        for i in range(game.height):
            for j in range(game.weight):
                game.matrix_field[i][j] = 5
        for i in range(1, 4):
            game.matrix_field[2][i] = 2
            game.matrix_field[i][2] = 2
        game.get_chains(1, 2, game.matrix_field[1][2])

        for i in range(1, 4):
            self.assertEqual(game.matrix_field[2][i], 0)
            self.assertEqual(game.matrix_field[i][2], 0)

    def test_check_next_move(self):
        game = GameField(5, 5)
        for i in range(game.height):
            for j in range(game.weight):
                game.matrix_field[i][j] = 0
        for i in range(game.height):
            game.matrix_field[4][i] = i
        self.assertEqual(False, game.check_next_move())
        game.matrix_field[0][0] = 1
        game.matrix_field[0][1] = 1
        self.assertEqual(True, game.check_next_move())

    def test_all_column_zero(self):
        game = GameField(5, 5)
        for j in range(game.height):
            game.matrix_field[j][1] = 0
        self.assertEqual(False, game.all_column_zero(2))
        self.assertEqual(True, game.all_column_zero(1))

    def test_count_neighbors(self):
        game = GameField(5, 5)
        for j in range(game.height):
            game.matrix_field[j][1] = 0
        game.matrix_field[0][0] = 5
        game.matrix_field[1][1] = 5
        self.assertEqual(0, game.count_neighbors(0, 0, 5))
        game.matrix_field[0][1] = 5
        self.assertEqual(1, game.count_neighbors(0, 0, 5))

if __name__ == "__main__":
    unittest.main()
