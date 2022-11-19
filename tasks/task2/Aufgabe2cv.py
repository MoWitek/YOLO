from random import seed, randint
from typing import List, Tuple, Any
from time import sleep

import cv2
import numpy as np

seed("YOLO")


# this creates one quarter of the diamond shape for the crystal
def create_slope(size, fill, back):
    ar = []
    for n in range(size):
        a2 = []
        a2.extend([fill for n in range(n + 1)])
        a2.extend([back for n in range(size - n - 1)])
        ar.append(a2)

    return ar


# make the board look ok
def print_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[y][x], end=" ")
        print()


# streches the diamond so you can add x and y growth multipliers
def strech_array(arr, strech_factor: int):
    mid = len(arr) // 2
    new_arr = []

    # if arr empty return
    if not arr:
        return arr

    # strech left side of the center
    for x in arr[:mid]:
        for _ in range(strech_factor):
            new_arr.append(x.copy())

    # copy center
    new_arr.append(arr[mid].copy())

    # strech right side of the center
    for x in arr[mid + 1:]:
        for _ in range(strech_factor):
            new_arr.append(x.copy())

    return new_arr


def rotate_array(array):
    return [list(v) for v in list(zip(*array[::-1]))]


# fuzes slopes into a diamond
def fuze_slopes(s, fill: Any = 1, back: Any = 0, xmul: int = 1, ymul: int = 1):
    # make slopes and oriante every in a diferent direction
    a1 = create_slope(s, fill, back)
    a2 = rotate_array(create_slope(s, fill, back))
    a3 = rotate_array(rotate_array(create_slope(s, fill, back)))
    a4 = rotate_array(rotate_array(rotate_array(create_slope(s, fill, back))))

    # FUZE
    arr = []
    for a, b in zip(a4, a1):
        arr.append([])
        arr[-1].extend(a)
        arr[-1].extend(b[1:])
    for c, d in zip(a3[1:], a2[1:]):
        arr.append([])
        arr[-1].extend(c)
        arr[-1].extend(d[1:])

    # adopt y growth multipliers
    if ymul != 1:
        arr = strech_array(arr, ymul)

    # adopt x growth multipliers
    if xmul != 1:
        arr = rotate_array(arr)
        arr = strech_array(arr, xmul)
        arr = rotate_array(arr)

    return arr


# easy board creation
def make_board(x, y, default_value=None):
    return [
        [
            default_value for _ in range(x)
        ] for _ in range(y)
    ]


# merge the diamonds into the board
def merge_arrays(main_arr, second, pos, criterium: callable = lambda v1, v2: v2 > v1):
    x, y = pos
    no_overrides = False

    # center the diamond on its center and not top left
    if second:
        x -= len(second[0]) // 2
    else:
        x -= 1 // 2
    y -= len(second) // 2

    for yp in range(len(second)):
        for xp in range(len(second[0])):
            # make sure crystals get indexes inside the board
            # / ->
            # |
            if y + yp >= len(main_arr):
                continue
            if x + xp >= len(main_arr[0]):
                continue

            # make sure crystals done get negative indexes
            #   <-
            # /\
            if y + yp < 0:
                continue
            if x + xp < 0:
                continue

            # dont overwrite spaces

            if criterium(main_arr[y + yp][x + xp], second[yp][xp]):
                main_arr[y + yp][x + xp] = second[yp][xp]
                no_overrides = True

    return no_overrides

# dataclass
class Crystal:
    def __init__(self, pos, colour: Tuple[int, int, int]=None, grow: tuple = (1, 1)):
        self.x, self.y = pos
        self.xg, self.yg = grow
        # random colour for the shade
        self.colour = [randint(0, 256) for _ in range(3)]


# main
def main(crystals: List[Crystal], board_size: Tuple[int, int], cv2_upscale=None):
    frames = []

    # mk board
    board_width, board_height = board_size
    b = make_board(board_width, board_height, [0, 0, 0])

    # crystals with higher growths get merged earlier
    crystals = sorted(crystals, key=lambda c: sum([c.xg, c.yg]), reverse=True)

    # convert the dataclass into raw data
    crystals = [(i, cry.colour, cry.x, cry.y, cry.xg, cry.yg) for i, cry in enumerate(crystals, 1)]

    burn_out_crystals = set()
    for n in range(max(list((board_width, board_height))) + 1):

        # create diamonds and merge them into the main baord
        for id, cc, cx, cy, cgx, cgy in crystals:
            if id not in burn_out_crystals:
                f = fuze_slopes(n, fill=cc, back=[0, 0, 0],  xmul=cgx, ymul=cgy)  # create diamon

                x = merge_arrays(b, f, (cx, cy), lambda v1, v2: v1 == [0, 0, 0])  # merging

                if not x and f != []:
                    burn_out_crystals.add(id)

        # displaying and stuff
        x = np.asarray(b, np.uint8)
        frames.append(x)
        if cv2_upscale:
            x = cv2.resize(x, cv2_upscale)
        cv2.imshow("frame", x)
        cv2.waitKey(2)
        sleep(1 / 24)

        if len(burn_out_crystals) == len(crystals):
            break

    return frames


# create random positions for crystals
def get_random_crystals(ammount, board_size):
    xb, yb = board_size
    crystals = []
    for _ in range(ammount):
        x = randint(0, xb - 1)
        y = randint(0, yb - 1)
        crystals.append(Crystal((x, y)))
    return crystals

def make_movie(frames):
    # len(frames) // clip_ln + 1
    vid = cv2.VideoWriter("crystals.mkv", cv2.VideoWriter_fourcc(*"PIM1"), 24, board_sz)  # DIVX PIM1 MJPG

    for f in frames:
        vid.write(f)
        vid.write(f)
        vid.write(f)

    vid.release()


if __name__ == '__main__':
    board_sz, crystals = (1024, 1024), 2058

    crys = get_random_crystals(crystals, board_sz)

    frames = main(crys, board_sz)

    make_movie(frames)

    cv2.waitKey(27)





