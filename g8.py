# inhertiance
import pgzrun
HEIGHT = 500
WIDTH = 500

class Player(Actor):
    pass
    vx = 3
    vy = 3

    
    def control(self):
        pass
        if keyboard.RIGHT:
            self.x += self.vx
        if keyboard.LEFT:
            self.x += -self.vx
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = HEIGHT

class Enemy(Actor):
    pass

# game code starts here
p = Player('char1', pos = (WIDTH//2, HEIGHT//2))

def draw():
    screen.clear()
    p.draw()

def update():
    p.control()

pgzrun.go()