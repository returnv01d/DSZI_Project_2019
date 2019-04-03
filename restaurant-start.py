import pygame
import sys
from utility.utility import Utility
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
BOARD_SIZE = 15

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
background_image = pygame.image.load("images/background.png")
pygame.display.set_caption('Restaurant')

SPRITE_WIDTH = int(WINDOW_WIDTH / BOARD_SIZE)
SPRITE_HEIGHT = int(WINDOW_HEIGHT / BOARD_SIZE)
board = Utility.generate_board(BOARD_SIZE, SPRITE_WIDTH, SPRITE_HEIGHT)
print(board)

#just a control print ;)
print("hello in شروانشاه restaurant!!")

sprites = pygame.sprite.Group()
all_sprites = []
all_objects = []
for row in board:
    all_objects.extend(row)
all_sprites = [obj.sprite for obj in all_objects]
for sprite in all_sprites:
    sprites.add(sprite)

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background_image, (0,0))
    sprites.draw(DISPLAYSURF)

    #Refresh Screen
    pygame.display.flip()
    fpsClock.tick(FPS)




