import pyray

BLANK, UP, RIGHT, DOWN, LEFT = range(5)

WIDTH = 800
HEIGHT = 450

pyray.init_window(WIDTH, HEIGHT, "")

blank = pyray.load_texture_from_image(pyray.load_image("./tiles/blank.png"))
up = pyray.load_texture_from_image(pyray.load_image("./tiles/up.png"))
right = pyray.load_texture_from_image(pyray.load_image("./tiles/right.png"))
down = pyray.load_texture_from_image(pyray.load_image("./tiles/down.png"))
left = pyray.load_texture_from_image(pyray.load_image("./tiles/left.png"))

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
