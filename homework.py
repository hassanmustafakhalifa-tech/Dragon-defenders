import pgzrun
import random

WIDTH = 1200
HEIGHT = 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
TITLE = 'Gallaga 2.0 Game'

score = 0
lives = 3
is_game_over = False
speed = 5
bullets = []
enemies = []

#create the ship
ship = Actor('crossbow.png')
ship.pos = (CENTER_X , CENTER_Y - 60)

#create the enemies
for i in range(8):
    enemy = Actor('evil_dragon.png')
    enemy.x = random.randint(0,WIDTH - 80)
    enemy.y = random.randint(-100, 0)
    enemies.append(enemy)

def display_score():
    screen.draw.text(f'Score:{score}',(50,30))
    screen.draw.text(f'Lives:{lives}',(50,60))

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor('bullet.png')
        bullet.x = ship.x
        bullet.y = ship.y - 50
        bullets.append(bullet)

#function to draw game 
def draw():
    if lives > 0:
        screen.clear()
        screen.fill('dark blue')
        ship.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        display_score()
    else:
        game_over_screen()

pgzrun.go()