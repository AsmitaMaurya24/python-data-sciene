import pgzrun 
from random import randint

WIDTH = 700
HEIGHT = 500

# our variables
p = Actor('char1', (50, 200)) 
c = Actor('char2', (50, 200)) 
speed = 3 # speed of movement

score = 0 # global varaible

def draw():
    screen.fill('black')
    p.draw()
    screen.draw.text(f'Score: {score}', (600,460), color = 'white', fontsize =30)
    c.draw()

def update():
    player_controls()
    check_score()

def check_score():
    global score
    if p.colliderect(c):
        score += 10
        c.pos = (randint(0, WIDTH), randint(0, HEIGHT))
        sounds.s1.play()

def player_controls(): 
    print(p.top, p.bottom)
    if keyboard.UP  and not p.top < 0:
        p.y += -speed
        p.anlge = 0
    elif keyboard.DOWN and not p.bottom > HEIGHT: 
        p.y += speed 
        p.angle = 0   

    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed 
        p.angle = -10

    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle = 10

pgzrun.go()
