import random
from collections import defaultdict
import support

class GameField(object):
    def __init__(self, weight=15, height=15):
        self.weight = weight
        self.height = height
        self.colors = {0: "white", 1: "red", 2: "blue", 3: "gold", 4: "black", 5: "green"}
        self.matrix_field = [[random.randrange(1, len(self.colors)) for j in range(weight)] for i in range(height)]
        self.score = 0
        self.count_colors_dictionary = defaultdict(int)
        self.set_count_dict()

    def set_count_dict(self):
        for key in self.count_colors_dictionary:
            self.count_colors_dictionary[key] = 0
        for line in self.matrix_field:
            for cell in line:
                self.count_colors_dictionary[cell] += 1

    def step(self, x, y):
        color = self.matrix_field[x][y]
        count = self.count_neighbors(x, y, color)
        if color != 0 and count == 1:
            self.get_chains(x, y, color)
            self.once_up_zero()
            self.left_zero()
            self.score_count()
            print(self.score)

    def score_count(self):
        full = 0
        for i in self.matrix_field:
            for j in i:
                if j == 0:
                    full += 1
        self.score = full

    def get_chains(self, x, y, color):
        support.get_chains(x, y, color, self.matrix_field, 0)

    def count_neighbors(self, x, y, color):
        if color != 0:
            for shift_x in range(-1, 2):
                for shift_y in range(-1, 2):
                    delta_x = x + shift_x
                    delta_y = y + shift_y
                    if -1 < delta_x < self.height and -1 < delta_y < self.weight:
                        if (self.matrix_field[delta_x][delta_y] == color) and not (shift_y == shift_x == 0) \
                                and (abs(shift_x*shift_y) != 1):
                            if delta_x == self.height:
                                continue
                            if delta_y == self.weight:
                                continue
                            return 1
        return 0

    def left_zero(self):
        y = 0
        while y < self.weight:
            if y+1 < self.weight and self.all_column_zero(y) and not self.all_column_zero(y+1):
                self.swap_columns(y)
                y = 0
                continue
            y += 1

    def all_column_zero(self, y):
        for j in range(self.height):
            if self.matrix_field[j][y] != 0:
                return False
        return True

    def swap_columns(self, x):
        for i in range(self.height):
            if x+1 < self.weight:
                color_left = self.matrix_field[i][x]
                self.matrix_field[i][x] = self.matrix_field[i][x + 1]
                self.matrix_field[i][x + 1] = color_left

    def once_up_zero(self):
        for x in range(self.height-1, -1, -1):
            for y in range(self.weight):
                current_x = x
                color = self.matrix_field[current_x][y]
                if current_x+1 < self.height and self.matrix_field[current_x + 1][y] == 0 and color != 0:
                    self.matrix_field[current_x+1][y] = self.matrix_field[current_x][y]
                    self.matrix_field[current_x][y] = 0

    def zero_below_color(self):
        for x in range(self.height-1, -1, -1):
            for y in range(self.weight):
                current_x = x
                color = self.matrix_field[current_x][y]
                if color == 0 and current_x - 1 > -1 and self.matrix_field[current_x - 1][y] != 0:
                    return True
        return False

    def refresh(self):
        self.matrix_field = [[random.randrange(1, len(self.colors)) for j in range(self.weight)] for i in range(self.height)]
        self.score = 0
        self.set_count_dict()

    def __print__(self):
        for line in self.matrix_field:
            print(line)

    def check_next_move(self):
        for i in range(self.height-1, -1, -1):
            for j in range(self.weight):
                color = self.matrix_field[i][j]
                if self.count_neighbors(i, j, color) == 1:
                    return True
        return False

