from random import choice, seed
from typing import List, Tuple

seed("YOLO")


def create_slope(sz, fill, back):
    ar = []
    for n in range(sz):
        a2 = []
        a2.extend([fill for n in range(n + 1)])
        a2.extend([back for n in range(sz - n - 1)])
        ar.append(a2)

    return ar


def print_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[y][x], end=" ")
        print()


def strech_array(arr, strech_factor: int):
    mid = len(arr) // 2
    new_arr = []

    if not arr:
        return arr

    for x in arr[:mid]:
        for _ in range(strech_factor):
            new_arr.append(x.copy())

    new_arr.append(arr[mid].copy())

    for x in arr[mid + 1:]:
        for _ in range(strech_factor):
            new_arr.append(x.copy())

    return new_arr


def rotate_array(array):
    return [list(v) for v in list(zip(*array[::-1]))]


def fuze_slopes(s, fill=1, back=0, xmul: int = 1, ymul: int = 1):
    a1 = create_slope(s, fill, back)
    a2 = rotate_array(create_slope(s, fill, back))
    a3 = rotate_array(rotate_array(create_slope(s, fill, back)))
    a4 = rotate_array(rotate_array(rotate_array(create_slope(s, fill, back))))

    arr = []
    for a, b in zip(a4, a1):
        arr.append([])
        arr[-1].extend(a)
        arr[-1].extend(b[1:])
    for c, d in zip(a3[1:], a2[1:]):
        arr.append([])
        arr[-1].extend(c)
        arr[-1].extend(d[1:])

    if ymul != 1:
        arr = strech_array(arr, ymul)

    if xmul != 1:
        arr = rotate_array(arr)
        arr = strech_array(arr, xmul)
        arr = rotate_array(arr)

    return arr


def make_board(x, y, default_value=None):
    return [
        [
            default_value for _ in range(x)
        ] for _ in range(y)
    ]


def merge_arrays(main_arr, second, pos, criterium: callable = lambda v1, v2: v2 > v1):
    x, y = pos

    if second:
        x -= len(second[0]) // 2
    else:
        x -= 1 // 2
    y -= len(second) // 2

    for yp in range(len(second)):
        for xp in range(len(second[0])):
            if y + yp >= len(main_arr):
                continue
            if x + xp >= len(main_arr[0]):
                continue
            if y + yp < 0:
                continue
            if x + xp < 0:
                continue

            if criterium(main_arr[y + yp][x + xp], second[yp][xp]):
                main_arr[y + yp][x + xp] = second[yp][xp]


class Crystal:
    def __init__(self, pos, colour=None, grow: tuple = (1, 1)):
        self.x, self.y = pos
        self.xg, self.yg = grow
        self.colour = colour if colour else choice(["\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"])


def main(crystals: List[Crystal], board_size: Tuple[int, int]):

    crystals = sorted(crystals, key=lambda c: sum([c.xg, c.yg]), reverse=True)

    crystals = [(f"{cry.colour}{i}\033[0m", cry.x, cry.y, cry.xg, cry.yg) for i, cry in enumerate(crystals, 1)]

    board_width, board_height = board_size
    b = make_board(board_width, board_height, 0)
    for n in range(max(list((board_width, board_height)))+1):
        for cid, cx, cy, cgx, cgy in crystals:
            f = fuze_slopes(n, cid, xmul=cgx, ymul=cgy)
            merge_arrays(b, f, (cx, cy), lambda v1, v2: v1 == 0)

        print_board(b)
        print()


if __name__ == '__main__':
    main([
        Crystal((2, 2)),
        Crystal((4, 7), grow=(2, 3)),
        Crystal((18, 4), "\033[95m", grow=(1, 4))
    ], (20, 20))

    arr = [
        [0, 1, 0],
        [2, 1, 2],
        [0, 1, 0],
    ]
