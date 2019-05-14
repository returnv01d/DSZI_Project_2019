import pygame
import sys
from model.table import Table
from model.carpet import Carpet
from model.kitchen import Kitchen
from model.freeSpace import FreeSpaceSprite, FreeSpace
from serialization.board_saver import BoardSaver
from serialization.board_loader import BoardLoader
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
BOARD_SIZE = 15

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_image = pygame.image.load("images/background_image.png").convert_alpha()

#background_image.set_alpha(255)
pygame.display.set_caption('Restaurant')

board = BoardLoader.load_board_from_file('boards/empty_board.txt')

sprites = board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)

#just a control print ;)
print("hello in شروانشاه restaurant!!")

DISPLAYSURF.blit(background_image, (0,0))

new_object = Table()

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                new_object = Table()
            elif event.key == pygame.K_k:
                new_object = Kitchen()
            elif event.key == pygame.K_c:
                new_object = Carpet()
            elif event.key == pygame.K_f:
                new_object = FreeSpace()
            elif event.key == pygame.K_s:
                print(board.objects)
                BoardSaver.save_board_to_file(board, 'boards/new_board.txt')

        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    x, y = event.pos

                for sprite in sprites:
                    if sprite.rect.collidepoint(x, y):
                        new_object.create_sprite(sprite.rect.width, sprite.rect.height)
                        new_object.sprite.rect.x = sprite.rect.x
                        new_object.sprite.rect.y = sprite.rect.y

                        if sprite.__class__.__name__ != FreeSpaceSprite.__name__:
                            sprites.remove(sprite)
                        board_x = int(x / sprite.rect.width)
                        board_y = int(y / sprite.rect.height)

                        board.objects[board_y][board_x] = new_object
                        sprites.add(new_object.sprite)


    sprites.draw(DISPLAYSURF)

    pygame.display.flip()
    fpsClock.tick(FPS)




