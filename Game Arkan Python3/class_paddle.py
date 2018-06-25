from const import *
class Paddle:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.height = h
        self.width = w

    def move(self,  delta):
        new_x = self.x + delta
        if new_x + self.width <= WINDOW_WIDTH and new_x >= 0:
            self.x = new_x