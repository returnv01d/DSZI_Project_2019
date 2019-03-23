import pygame
import time

from sprites.freeSpace import FreeSpace
from sprites.waiter import Waiter

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 640

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Restaurant')

all_sprites_list = pygame.sprite.Group()

elsa = Waiter(0,0, WINDOW_WIDTH, WINDOW_HEIGHT)

print("hello in شروانشاه restaurant!!")
