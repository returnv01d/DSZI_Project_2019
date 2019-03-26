import pygame
import sys
import random
from sprites.freeSpace import FreeSpace
from sprites.table import Table
from sprites.waiter import Waiter
from sprites.obstacle import Obstacle
from sprites.kitchen import Kitchen
from pygame.locals import *

pygame.init()


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
BOARD_SIZE = 30

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
background_image = pygame.image.load("images/background.png")
pygame.display.set_caption('Restaurant')

board = pygame.sprite.Group()

SPRITE_WIDTH = int(WINDOW_WIDTH / BOARD_SIZE)
SPRITE_HEIGHT = int(WINDOW_HEIGHT / BOARD_SIZE)
current_height = 0
for i in range(0, BOARD_SIZE):
    for j in range(0, BOARD_SIZE):
        new_sprite = None
        if (i == int(BOARD_SIZE / 2) and j == int(BOARD_SIZE/ 2)):
            new_sprite = Waiter()
        elif (i == 0 and ((j == BOARD_SIZE - 1) or (j == BOARD_SIZE - 2)) ):
            new_sprite = Kitchen()
        elif( (i + 8) % 12 == 0 and (j + 8) % 16 ==0):
            new_sprite = Table()
        else:
            if( random.randint(0, 30) != 30):
                new_sprite = FreeSpace()
            else:
                new_sprite = Obstacle()
        new_sprite.rect.x = j * SPRITE_WIDTH
        new_sprite.rect.y = current_height
        new_sprite.image = pygame.transform.scale(new_sprite.image,(SPRITE_WIDTH, SPRITE_HEIGHT))
        new_sprite.rect.width = SPRITE_WIDTH
        new_sprite.rect.height = SPRITE_HEIGHT
        print(new_sprite.rect.width)
        board.add(new_sprite)
    current_height += SPRITE_HEIGHT



#just a control print ;)
print("hello in شروانشاه restaurant!!")

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    board.update()

    DISPLAYSURF.blit(background_image, (0,0))
    board.draw(DISPLAYSURF)

    #Refresh Screen
    pygame.display.flip()
    fpsClock.tick(FPS)