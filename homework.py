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
crossbow = Actor('crossbow.png')
crossbow.pos = (CENTER_X , HEIGHT - 60)

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
        bullet.x = crossbow.x
        bullet.y = crossbow.y - 50
        bullets.append(bullet)

def draw():
    if lives > 0:
        screen.clear()
        screen.fill('dark blue')
        crossbow.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        display_score()
    else:
        game_over_screen()

def update():
    global score , lives
    if keyboard.left :
        crossbow.x -= speed 
        if crossbow.x <= 0 :
            crossbow.x = 0
    elif keyboard.right:
        crossbow.x += speed
        if crossbow.x >= WIDTH:
            crossbow.x = WIDTH
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    for enemy in enemies:
        enemy.y += 5
        if enemy.y >= HEIGHT:
            enemy.x = random.randint(0,WIDTH - 80)
            enemy.y = random.randint(-100,0)
        for bullet in bullets :
            if enemy.colliderect(bullet):
                score += 100
                sounds.eep.play()
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                break
        if enemy.colliderect(crossbow):
            lives -= 1
            if enemy in enemies:
                enemies.remove(enemy)
            if lives == 0:
                game_over()
    if len(enemies)  < 8:
         enemy = Actor('evil_dragon.png')
         enemy.x = random.randint(0,WIDTH - 80)
         enemy.y = random.randint(-100, 0)
         enemies.append(enemy)

def game_over():
    global is_game_over
    is_game_over = True

def game_over_screen():
    screen.clear()
    screen.fill('#D90429')
    screen.draw.text(f'Game Over!!!',(CENTER_X - 150, CENTER_Y), fontsize = 60, color = 'white')
    screen.draw.text(f'Score : {score}',(CENTER_X - 150, CENTER_Y + 50),fontsize = 40, color = 'white')
    screen.draw.text(f'Press space to restart.',(CENTER_X - 150, CENTER_Y + 100),fontsize = 40, color = 'white')
    if keyboard.SPACE:
        restart_game()
    
def restart_game():
     global lives, score, enemies, bullets
     score = 0
     lives = 3
     enemies = []
     bullets = []
     for i in range(8):
        enemy = Actor('evil_dragon.png')
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100, 0)
        enemies.append(enemy)
    


pgzrun.go()