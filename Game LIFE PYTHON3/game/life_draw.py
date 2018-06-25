from tkinter import Tk, Canvas, Button, Frame, BOTH, NORMAL, HIDDEN
from life_func import GameField
import time

def draw_touch_mouse(e):
        ii = int(e.y / cell_size)
        jj = int(e.x / cell_size)
        if ii < game.hight and jj < game.weight:
            game.matrix_field[ii][jj] = 1
            paint()


def clear_touch_mouse(e):
    ii = int(e.y / cell_size)
    jj = int(e.x / cell_size)
    if ii < game.hight and jj < game.weight:
        game.matrix_field[ii][jj] = 0
        paint()


def clear():
    game.clear()
    paint()


def next_step():
    game.refresh()
    paint()


def play():
    game.play = True
    for r in range(1000):
        if game.play:
            game.refresh()
            window.update()
            paint()
            time.sleep(0.05)
        else:
            break


def stop():
    game.play = False


def addr(ii, jj):
    if ii < 0 or jj < 0 or ii >= game.hight or jj >= game.weight:
        return len(cell_matrix) - 1
    else:
        return ii * int(window_width / cell_size) + jj


def paint():
    for i in range(game.hight):
        for j in range(game.weight):
            square = cell_matrix[addr(i, j)]
            if game.matrix_field[i][j] == 0:
                canvas.itemconfig(square, state=HIDDEN, tags=('hid', '0'))
            if game.matrix_field[i][j] == 1:
                canvas.itemconfig(square, state=NORMAL, tags=('vis', '0'))


game = GameField(25, 25)
cell_size = 20
window = Tk()
window.title("Game Of Life")

window_height = cell_size*game.hight
window_width = cell_size*game.weight

string_for_window = "{0}x{1}".format(window_width, window_height+30)
window.geometry(string_for_window)
color_cells = "green"
canvas = Canvas(window, height=window_height, width=window_width)
canvas.pack(fill=BOTH)
cell_matrix = []

for i in range(game.hight):
    for j in range(game.weight):
        square = canvas.create_rectangle(cell_size * j,  cell_size * i, cell_size + cell_size * j,
                                         cell_size + cell_size * i, fill=color_cells)
        canvas.itemconfig(square, state=HIDDEN, tags=('hid', '0'))
        cell_matrix.append(square)

frame = Frame(window)

btn1 = Button(frame, text='Clear', command=clear)
btn2 = Button(frame, text='Next Step', command=next_step)
btn3 = Button(frame, text='Play', command=play)
btn4 = Button(frame, text='Stop', command=stop)

btn4.pack(side="right")
btn3.pack(side="right")
btn1.pack(side='left')
btn2.pack(side="right")

frame.pack(side='bottom')
canvas.bind('<Button-1>', draw_touch_mouse)
canvas.bind('<Button-3>', clear_touch_mouse)
canvas.bind('<B1-Motion>', draw_touch_mouse)
window.mainloop()
