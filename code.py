import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
score = 0
TITLE = "Pac-Man Mini Game"
game_over = False

# Load sprites
player = Actor("pacman4.png")  # use pacman.png
points = Actor("points2.jpg")  # use points.webp
player.pos = 500, 400
points.pos = 300, 200

def draw():
    if not game_over:
        screen.clear()
        screen.fill("blue")
        player.draw()
        points.draw()
        screen.draw.text("Score: " + str(score), (10, 10), color="white", fontsize=40)
    else:
        screen.clear()
        screen.fill("black")
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=60, color="yellow")
        screen.draw.text("Final Score: " + str(score), center=(WIDTH // 2, HEIGHT // 2 + 20), fontsize=40, color="white")

def update():
    global score, game_over

    # Move Pac-Man
    if keyboard.right:
        player.x += 4
        if player.x > WIDTH: player.x = 0
    elif keyboard.left:
        player.x -= 4
        if player.x < 0: player.x = WIDTH
    elif keyboard.down:
        player.y += 4
        if player.y > HEIGHT: player.y = 0
    elif keyboard.up:
        player.y -= 4
        if player.y < 0: player.y = HEIGHT

    # Collision with point
    if player.colliderect(points):
        points.pos = randint(30, WIDTH - 30), randint(30, HEIGHT - 30)
        score += 1

    # Optional: Add end condition
    if score >= 100000000000000000000000000000:
        game_over = True

pgzrun.go()