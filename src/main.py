import itertools
import random

import pyray

# this number is determined by each tile image's dimensions
IMAGE_SIZE = 30

N = 30

WIDTH = N * IMAGE_SIZE
HEIGHT = N * IMAGE_SIZE

BLANK, UP, RIGHT, DOWN, LEFT = range(5)

RULES = [
    [
        [BLANK, UP],
        [BLANK, RIGHT],
        [BLANK, DOWN],
        [BLANK, LEFT],
    ],
    [
        [RIGHT, LEFT, DOWN],
        [LEFT, UP, DOWN],
        [BLANK, DOWN],
        [RIGHT, UP, DOWN],
    ],
    [
        [RIGHT, LEFT, DOWN],
        [LEFT, UP, DOWN],
        [RIGHT, LEFT, UP],
        [BLANK, LEFT],
    ],
    [
        [BLANK, UP],
        [LEFT, UP, DOWN],
        [RIGHT, LEFT, UP],
        [RIGHT, UP, DOWN],
    ],
    [
        [RIGHT, LEFT, DOWN],
        [BLANK, RIGHT],
        [RIGHT, LEFT, UP],
        [UP, DOWN, RIGHT],
    ],
]

pyray.init_window(WIDTH, HEIGHT, "")

tiles = [
    pyray.load_texture_from_image(pyray.load_image(f))
    for f in (
        "./tiles/blank.png",
        "./tiles/up.png",
        "./tiles/right.png",
        "./tiles/down.png",
        "./tiles/left.png",
    )
]

grid = [
    {
        "collapsed": False,
        "options": [
            BLANK,
            UP,
            RIGHT,
            DOWN,
            LEFT,
        ],
    }
    for _ in range(N * N)
]


while not pyray.window_should_close():
    pyray.begin_drawing()

    w = WIDTH // N
    h = HEIGHT // N
    for j in range(N):
        for i in range(N):
            cell = grid[i + j * N]
            if cell["collapsed"] == True:
                index = cell["options"][0]
                pyray.draw_texture(tiles[index], i * w, j * h, pyray.WHITE)
            else:
                pyray.draw_rectangle(i * w, j * h, w, h, pyray.BLUE)

    pyray.end_drawing()

    # clone = list(
    #     sorted(
    #         list(itertools.chain.from_iterable(grid)),
    #         key=lambda cell: len(cell["options"]),
    #     )
    # )

    # candidates = list(
    #     filter(lambda cell: len(cell["options"]) == len(clone[0]["options"]), clone)
    # )

    # cell = random.choice(candidates)
    # cell["collapsed"] = True
    # cell["options"] = [random.choice(cell["options"])]


pyray.close_window()
