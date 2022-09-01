import pgzrun

WIDTH = 700
HEIGHT = 500

music.play('bgmusic')
# actor
p = Actor('char1', (50, 200))
c = Actor('char2', (200, 200))

speed = 3 # speed of movement
cspeed = 1

def draw():
    screen.fill('black')
    p.draw()
    c.draw()

def update():
    player_controls()
    player_controls_1()

def player_controls():
    if keyboard.UP and not p.top < 0:
        p.y += -speed
        p.angle = 0 
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
        p.angle = 0
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle = 10
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed
        p.angle = -10
    else:
        p.angle = 0

def player_controls_1():
    if keyboard.UP and not c.top < 0:
        c.y += -speed
        c.angle = 0 
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        c.y += speed
        c.angle = 0
    elif keyboard.LEFT and not p.left < 0:
        c.x += -speed
        c.angle = 10
    elif keyboard.RIGHT and not p.right > WIDTH:
        c.x += speed
        c.angle = -10
    else:
        c.angle = 0
pgzrun.go()