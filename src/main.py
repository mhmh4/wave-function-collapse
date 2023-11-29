import pyray

BLANK, UP, RIGHT, DOWN, LEFT = range(5)

WIDTH = 800
HEIGHT = 450

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

N = 4

grid = [
    [
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
        for _ in range(N)
    ]
    for _ in range(N)
]
print(grid)

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.end_drawing()

pyray.close_window()
