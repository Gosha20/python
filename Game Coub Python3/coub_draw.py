from tkinter import *
import copy

import support
from coub_func import GameField
import time
from tkinter import messagebox

pre_coords = [-1, -1]


def parse_coords_mouse(x):
    return int(x / cell_size)


def draw_touch_mouse(e):
        ii = parse_coords_mouse(e.y)
        jj = parse_coords_mouse(e.x)
        if ii < game.height and jj < game.weight:
            game_step(ii, jj)
        if not game.check_next_move():
            dialog()


def light_coub(temp_field):
    for x in range(game.height):
        for y in range(game.weight):
            if temp_field[x][y] == -1:
                canvas.itemconfig(matrix_rect[x][y], fill="dimgray")


def draw_motion_mouse(e):
    ii = parse_coords_mouse(e.y)
    jj = parse_coords_mouse(e.x)
    if pre_coords[0] != ii or pre_coords[1] != jj :
        paint()
        temp_field = copy.deepcopy(game.matrix_field)
        if ii < game.height and jj < game.weight and game.matrix_field[ii][jj] != 0\
                and game.count_neighbors(ii, jj, game.matrix_field[ii][jj]) == 1:

            support.get_chains(ii, jj, game.matrix_field[ii][jj], temp_field, -1)
            light_coub(temp_field)
        pre_coords[0] = ii
        pre_coords[1] = jj
    window.update()


def game_step(x, y):
        color = game.matrix_field[x][y]
        count = game.count_neighbors(x, y, color)
        if color != 0 and count == 1:

            game.get_chains(x, y, color)
            paint()
            window.update()
            while game.zero_below_color():
                time.sleep(0.1)
                game.once_up_zero()
                paint()
                window.update()

            time.sleep(0.2)
            game.left_zero()
            game.score_count()
            game.set_count_dict()
            paint()
            window.update()


def refresh_field():
    game.refresh()
    paint()


def paint():
    canvas.delete("all")
    paint_numbers()
    paint_rect()
    for i in range(game.height):
        for j in range(game.weight):
            color_cell = game.colors[game.matrix_field[i][j]]
            rect = canvas.create_rectangle(cell_size * j, cell_size * i, cell_size + cell_size * j, cell_size +
                                           cell_size * i, fill=color_cell)
            matrix_rect[i][j] = rect


def paint_numbers():
    j = 5
    canvas.create_text(window_weidth - 120, 25, anchor="nw", text='SCORE:', fill='black')
    canvas.create_rectangle(window_weidth - 80, 5 + 20, window_weidth - 58, 20 + 20, fill='white')
    for i in range(1, len(game.colors)):
        canvas.create_rectangle(window_weidth - 80, 25 + 20 * i + j, window_weidth - 59, 42 + 20 * i + j, fill='white')

        canvas.create_text(window_weidth - 77, 26 + 20 * i + j, anchor="nw", text=game.count_colors_dictionary[i],
                           fill='black')
        j += 5
    canvas.create_text(window_weidth - 77, 25, anchor="nw", text=game.score, fill='black')


def dialog():
    var = messagebox.askquestion("You lose", "Game Over \n Do you want refresh?")
    if var == 'yes':
        refresh_field()
    else:
        frame.quit()


def paint_rect():
    j = 0
    for i in range(1, len(game.colors)):
        canvas.create_rectangle(window_weidth - 100, 30 + 20 * i + j, window_weidth - 120, 50 + 20 * i + j, fill=game.colors[i])
        j += 5


game = GameField()

matrix_rect = [[0 for j in range(game.weight)] for i in range(game.height)]
cell_size = 20

window = Tk()
window.title("Coubs")
window_height = cell_size*game.height
window_weidth = cell_size * game.weight + 150
string_for_window = "{0}x{1}".format(window_weidth, window_height + 30)
window.geometry(string_for_window)
window.resizable(False, False)

canvas = Canvas(window, height=window_height, width=window_weidth)
canvas.pack(fill=BOTH)

frame = Frame(window)
btn1 = Button(frame, text='Refresh', command=refresh_field)

paint()

btn1.pack(side='left')
frame.pack(side='top')
canvas.bind('<Button-1>', draw_touch_mouse)
canvas.bind("<Motion>", draw_motion_mouse)
window.mainloop()

