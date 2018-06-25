import random

from class_ball import *
from class_paddle import *
from class_briks import *


class Game:
    def __init__(self):
        self.ball = Ball(350, 437, 10, 3, 3)
        self.paddle = Paddle(300, 450, 20, 100)
        self.bricks = []
        self.set_bricks()

    def set_bricks(self):
        for i in range(10):
            self.bricks.append(Brick(40 + i * 40, 100, random.randint(1, 5)))
            self.bricks.append(Brick(40 + i * 40, 140, random.randint(1, 5)))
            self.bricks.append(Brick(40 + i * 40, 180, random.randint(1, 5)))

    def destroy_brick(self, brick):
        brick.count_life -= 1
        if brick.count_life <= 0:
            self.bricks.remove(brick)
            return True
        return False