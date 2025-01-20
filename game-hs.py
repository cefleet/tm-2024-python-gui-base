import pyglet
from pyglet.shapes import Rectangle

window_width = 800
window_height = 600
window = pyglet.window.Window(width=window_width, height=window_height, caption="My Game")

GRAY = (169,169,169)
GREEN = (34,139,34)

path_width = 400
path_left_width = (window_width - path_width)/2

left_side = Rectangle(0,0,path_left_width, window_height, GREEN )
right_side = Rectangle()

path = Rectangle(path_left_width,0,path_width,window_height,GRAY)

@window.event
def on_draw():
    window.clear()
    path.draw()  
    left_side.draw()  
    right_side.draw()
pyglet.app.run()