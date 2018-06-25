import tkinter
from threading import Timer
import time

from game import *
from const import *


class Form(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("PArkanoid")
        string_for_window = "{0}x{1}".format(WINDOW_HEIGHT, WINDOW_WIDTH)
        self.geometry(string_for_window)
        self.resizable(False, False)
        self.canvas = tkinter.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, background="blue")
        self.canvas.pack()
        self.game = Game()
        self.paint()
        self.canvas.bind('<Left>', self.move_left)
        self.canvas.bind('<Right>', self.move_right)
        self.canvas.bind('<space>', self.paint)


    def paint(self):
        self.ball = self.canvas.create_oval(self.game.ball.x,
                                            self.game.ball.y,
                                            self.game.ball.x + self.game.ball.diameter,
                                            self.game.ball.y + self.game.ball.diameter,
                                            fill='black',
                                            outline='yellow')

        self.paddle = self.canvas.create_rectangle(self.game.paddle.x,
                                                   self.game.paddle.y,
                                                   self.game.paddle.x + self.game.paddle.width,
                                                   self.game.paddle.y + self.game.paddle.height,
                                                   fill='black')
        for brick in self.game.bricks:
            brick.id = self.canvas.create_rectangle(brick.x,
                                                    brick.y,
                                                    brick.x + brick.width,
                                                    brick.y + brick.height,
                                                    fill = COLORS[brick.count_life],
                                                    outline='black')
    def start(self, e):
        timer = Timer(0.5, self.paint)
        timer.start()

    def move_right(self, e):
        self.game.paddle.move(10)

    def move_left(self, e):
        self.game.paddle.move(-10)

    def paint(self, *k):
        while True:
            self.game.ball.move()
            self.game.ball.hit_wall()
            self.canvas.coords(self.ball,
                               self.game.ball.x,
                               self.game.ball.y,
                               self.game.ball.x + self.game.ball.diameter,
                               self.game.ball.y + self.game.ball.diameter)

            self.canvas.coords(self.paddle,
                               self.game.paddle.x,
                               self.game.paddle.y,
                               self.game.paddle.x + self.game.paddle.width,
                               self.game.paddle.y + self.game.paddle.height)
            if self.ball in self.canvas.find_overlapping(self.game.paddle.x,
                                                         self.game.paddle.y,
                                                         self.game.paddle.x + self.game.paddle.width,
                                                         self.game.paddle.y + self.game.paddle.height):
                self.game.ball.hit_paddle(self.game.paddle)
            for brick in self.game.bricks:
                if self.ball in self.canvas.find_overlapping(brick.x,
                                                             brick.y,
                                                             brick.x + brick.width,
                                                             brick.y + brick.height):
                    self.game.ball.hit_brick(brick)
                    if self.game.destroy_brick(brick):
                        self.canvas.delete(brick.id)
                    else:
                        self.canvas.itemconfig(brick.id, fill = COLORS[brick.count_life])

            form.update()
            time.sleep(0.02)

if __name__ == '__main__':
    form = Form()
    form.mainloop()