import pyglet
from pyglet.shapes import Rectangle, Circle
from pyglet.window import key

# windows config
window_width = 800
window_height = 600
window = pyglet.window.Window(width=window_width, height=window_height, caption="My Game")

#color constants
GRAY = (169,169,169)
GREEN = (34,139,34)
WHITE = (255,255,255)

#player config
player_radius = 40
player_x = window_width / 2
player_y = 100
player_speed = 150

# This handles keyboard input
keys = key.KeyStateHandler()
window.push_handlers(keys)

player = Circle(player_x, player_y, player_radius, color=WHITE)

path_width = 400
path_x = (window_width - path_width)/2

background = Rectangle(0,0,window_width, window_height, GREEN )

path = Rectangle(path_x,0,path_width,window_height,GRAY)
dir = 'right'
def update(dt):
    global dir

    if keys[key.LEFT]:
        player.x -= player_speed * dt
    if keys[key.RIGHT]:
        player.x += player_speed * dt

    if player.x > path_width+path_x-player_radius:
        player.x =  path_width+path_x-player_radius

    if player.x < path_x+player_radius:
        player.x = path_x + player_radius


@window.event
def on_draw():
    window.clear()
    background.draw() 
    path.draw()  
    player.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()