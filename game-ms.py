import pyglet

from pyglet.shapes import Rectangle, Circle
from pyglet.window import Window, key

# Window config
window_width = 800
window_height = 600
window = Window(height=window_height, width=window_width, caption="My Game")

keys = key.KeyStateHandler()
window.push_handlers(keys)

# Colors
GRAY=(170,170,170)
GREEN = (34,139,34)
WHITE = (255,255,255)
RED = (255,0,0)

# path config
path_width = 400
path_x = (window_width-path_width)/2
path = Rectangle(path_x,0,path_width,window_height,GRAY)

# backgronud
green_background = Rectangle(0,0, window_width, window_height, GREEN)

# player config
player_y = 100
player_x = window_width / 2
player_radius = 40

player = Circle(player_x,player_y,player_radius, color=WHITE )
player_speed = 150

obstacle_size = 40
obstacle_speed = 200

obstacles = []

def add_obstacle(dt):
    obstacle = Rectangle(250,window_height-obstacle_size, obstacle_size, obstacle_size,RED)
    obstacles.append(obstacle)

def update(dt):

    if keys[key.LEFT]:
        player.x -= player_speed * dt
    
    if keys[key.RIGHT]:
        player.x += player_speed * dt

    if player.x > path_width+path_x-player_radius:
        player.x =  path_width+path_x-player_radius

    if player.x < path_x+player_radius:
        player.x = path_x + player_radius
    
    for obstacle in obstacles[:]:
        obstacle.y -= obstacle_speed * dt
        if obstacle.y + obstacle_size < 0:
            obstacle.delete()
            obstacles.remove(obstacle)

    
@window.event
def on_draw():
    window.clear()
    green_background.draw()
    path.draw()
    player.draw()
    for obstacle in obstacles[:]:
        obstacle.draw()

add_obstacle(1)
pyglet.clock.schedule_interval(add_obstacle, 2)
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()