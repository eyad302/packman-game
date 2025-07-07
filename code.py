import pgzrun

WIDTH = 800 
HEIGHT = 600
score = 0
TITLE = "packman"
player = Actor ("pacman")
points = Actor ("points")
game_over = False
player.pos=500,400
points.pos = 300,200
def draw ():
    if not game_over:
        screeen .clear()
        screen .fill ((0,0,0))
        player.draw
        points.draw
        screen .draw.text('score = '+str(score), (10,10))
    else:
        screen .clear()
        screen.fill ("black")
        screen.draw.text("gg",(200,200))
        screen.draw.text("final score ="+str(score),(400,300))

