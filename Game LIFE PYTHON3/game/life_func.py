
class GameField(object):
    def __init__(self, weight=25, hight=25):
        self.matrix_field = [[0] * weight for i in range(hight)]
        self.weight = weight
        self.hight = hight
        self.play = True

    def clear(self):
        for x in range(0, self.weight):
            for y in range(0, self.hight):
                self.matrix_field[x][y] = 0

    def get_neighbors(self, x, y):
        neighbors = 0
        for shift_x in range(-1, 2):
            for shift_y in range(-1, 2):
                if not (shift_y == shift_x == 0):

                    delta_x = x + shift_x
                    delta_y = y + shift_y

                    if delta_x == self.hight:
                        delta_x = 0
                    if delta_y == self.weight:
                        delta_y = 0

                    if self.matrix_field[delta_x][delta_y] == 1:
                        neighbors += 1
        return neighbors

    def refresh(self):
        temp_matrix = [[0] * self.weight for i in range(self.hight)]
        for x in range(0, self.hight):
            for y in range(0, self.weight):
                if self.get_neighbors(x, y) == 3 or (self.get_neighbors(x, y) == 2 and self.matrix_field[x][y] == 1):
                    temp_matrix[x][y] = 1
                else:
                    temp_matrix[x][y] = 0
        self.matrix_field = None
        self.matrix_field = temp_matrix

    def print(self):
        for line in self.matrix_field:
            print(line)
