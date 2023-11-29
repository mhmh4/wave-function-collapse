import pyray

pyray.init_window(800, 450, "")


blank = pyray.load_texture_from_image(pyray.load_image("./tiles/blank.png"))
up = pyray.load_texture_from_image(pyray.load_image("./tiles/up.png"))
right = pyray.load_texture_from_image(pyray.load_image("./tiles/right.png"))
down = pyray.load_texture_from_image(pyray.load_image("./tiles/down.png"))
left = pyray.load_texture_from_image(pyray.load_image("./tiles/left.png"))


while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.end_drawing()

pyray.close_window()
