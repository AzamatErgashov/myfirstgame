# librarys
import pygame
import random 
import math
# initialize 
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# backround image
backround_iamge = pygame.image.load('image copy 3.png')

# title and icon
pygame.display.set_caption('my_first_game')
icon = pygame.image.load('im.png')
pygame.display.set_icon(icon)

# player
playerIMG = pygame.image.load('space-invaders.png')
playerX = 370 
playerY = 480
playerX_change = 0


# enemy or devil👿
enemyIMG = pygame.image.load('bomber.png')
enemyX = random.randint(0, 735) 
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

# bullet
bulletIMG = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

score = 0 

def player(x, y):
    screen.blit(playerIMG, (x, y))

def enemy(x, y):
    screen.blit(enemyIMG , (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x+16, y+10))

def toqnashuv(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
# game loop
running = True
while running:

    # RGB - RED GREEN BLUE
    screen.fill((0,0,0))
    # backround
    screen.blit(backround_iamge, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            # print(' a keystroke pressed')
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # cheking for boundries so it does;nt go out
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2 
        enemyY += enemyY_change
    
    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state ==  "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # toqnashuv
    collision = toqnashuv(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1 
        print(score)
        enemyX = random.randint(0, 735) 
        enemyY = random.randint(50,150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()