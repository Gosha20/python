
def get_chains(x, y, color, array, mode):
    array[x][y] = mode
    for shift_x in range(-1, 2):
        for shift_y in range(-1, 2):
            delta_x = x + shift_x
            delta_y = y + shift_y
            if -1 < delta_x < len(array) and -1 < delta_y < len(array[0]):
                if (array[delta_x][delta_y] == color) and not (shift_y == shift_x == 0) \
                        and (abs(shift_x * shift_y) != 1):
                    if delta_x == len(array):
                        continue
                    if delta_y == len(array[0]):
                        continue
                    get_chains(delta_x, delta_y, color, array, mode)
