import pygame
import sys
from model.board import Board
from pygame.locals import *
from model.move import Move
from serialization.board_loader import BoardLoader

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
BOARD_SIZE = 10
BOARD_PATH = "boards/board1.txt"


DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
background_image = pygame.image.load('images/background_image.png')
pygame.display.set_caption('Restaurant')

board = BoardLoader.load_board_from_file('boards/new_board.txt')

sprites = board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)
print("hello in شروانشاه restaurant!!")


while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                board.move_waiter(Move.UP)
            if event.key == K_DOWN:
                board.move_waiter(Move.DOWN)
            if event.key == K_RIGHT:
                board.move_waiter(Move.RIGHT)
            if event.key == K_LEFT:
                board.move_waiter(Move.LEFT)

    DISPLAYSURF.blit(background_image, (0,0))
    sprites.draw(DISPLAYSURF)

    #Refresh Screen
    pygame.display.flip()
    fpsClock.tick(FPS)




