import math
from const import *

class Ball:
    def __init__(self, x, y, diameter, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.diameter = diameter

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def hit_wall(self):
        if self.x < 0:
            self.dx = -self.dx
        if self.x >= WINDOW_WIDTH:
            self.dx = -self.dx
        if self.y < 0:
            self.dy = -self.dy
        if self.y >= WINDOW_HEIGHT:
            self.dy = -self.dy
    """придумать формулу отскока """
    def hit_paddle(self, paddle):
        self.dy = -self.dy

    def hit_brick(self, brick):
        if self.y + self.diameter <= brick.y + brick.height / 2 or self.y > brick.y + brick.height / 2:
            self.dy = -self.dy
        else:
            self.dx = -self.dx