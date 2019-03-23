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

#set up barriers and add to all_sprites_list
barriers = []

for barrier in barriers:
    all_sprites_list.add(barrier)

#set up current orders- IDK for now how we'll set if officialy
currentOrders = [1,2,3,4]

#set up waiter, for now left top corner
waiter = Waiter(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, barriers, currentOrders)
all_sprites_list.add(waiter)

#just a control print ;)
print("hello in شروانشاه restaurant!!")
