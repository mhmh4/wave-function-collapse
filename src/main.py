import pyray

pyray.init_window(800, 450, "Hello")

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.WHITE)
    pyray.draw_text("Hello world", 190, 200, 20, pyray.VIOLET)
    pyray.end_drawing()

pyray.close_window()
