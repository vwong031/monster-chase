import pygame
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Monster Chase")
icon = pygame.image.load('monster.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 530
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('monster.png')
enemyX = 500
enemyY = 530
enemyX_change = -0.30

# Lives
num_of_lives = 3
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_lives(x, y):
    lives = font.render("Lives: " + str(num_of_lives), True, (255, 255, 255))
    screen.blit(lives, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))

    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.30
            if event.key == pygame.K_LEFT:
                playerX_change = -0.30
            if event.key == pygame.K_SPACE:
                playerY_change = -6
                jump_sound = mixer.Sound('jump.wav')
                jump_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                playerX_change = 0
                playerY_change = 6

    # Game boundaries for spaceship
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change
    if playerY >= 530:
        playerY = 530
    if playerY <= 400:
        playerY_change = 0.25

    enemyX += enemyX_change
    if enemyX <= -30:
        enemyX = 830

    collision = isCollision(enemyX, enemyY, playerX, playerY)
    if collision:
        num_of_lives += -1

        collide_sound = mixer.Sound('beep-buzz.mp3')
        collide_sound.play()

        enemyX = 830
        enemyY = 530

        if num_of_lives < 1:
            enemyX = 2000
            enemyY = 2000

    if enemyX >= 2000 or enemyY >= 2000:
        game_over_text()

    # Call Functions
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_lives(textX, textY)
    pygame.display.update()
