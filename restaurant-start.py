import pygame
import sys
from model.board import Board
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

board = Board(BOARD_SIZE)
board.generate_test_board()
sprites = board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)

#just a control print ;)
print("hello in شروانشاه restaurant!!")



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



