import pygame
import sys
from model.board import Board
from serialization.BoardToJson import BoardToJson
from model.waiter import Waiter
from model.table import Table
from model.carpet import Carpet
from model.kitchen import Kitchen
from model.freeSpace import FreeSpaceSprite
import model
from sprites.tableSprite import TableSprite
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
BOARD_SIZE = 15

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_image = pygame.image.load("images/background.png").convert_alpha()

#background_image.set_alpha(255)
pygame.display.set_caption('Restaurant')

board = Board(BOARD_SIZE, 5, 5)
board.generate_test_board()
sprites = board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)
#print(sprites.layers())
#just a control print ;)
print("hello in شروانشاه restaurant!!")


#sprites.draw(DISPLAYSURF),
s = pygame.sprite.Group()
k = Waiter()
k.create_sprite(100,100)
#k.sprite.draw(200,200)
s.add(k.sprite)
DISPLAYSURF.blit(background_image, (0,0))
img = pygame.image.load('images/waiter.png').convert_alpha()
new_object = Table()
DISPLAYSURF.blit(img, img.get_rect())
while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("s")
                new_object = Table()
            elif event.key == pygame.K_k:
                new_object = Kitchen()
            elif event.key == pygame.K_d:
                new_object = Carpet()

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
                        board_y = int(y / sprite.rect.width)

                        board.objects[board_y][board_x] = new_object
                        sprites.add(new_object.sprite)

    #Refresh Screen

    sprites.draw(DISPLAYSURF)
    # for o in sprites:
    #     DISPLAYSURF.blit(o.image, o.image.get_rect())
    #DISPLAYSURF.blit(background_image, (300, 300))
    pygame.display.flip()
    fpsClock.tick(FPS)




