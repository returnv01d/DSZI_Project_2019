import pygame
from sprites.freeSpace import FreeSpace
from sprites.waiter import Waiter
from pygame.locals import *

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

#set up list of all orders- prototype
listOfOrders = [1, 2, 3]

#set up current orders- IDK for now how we'll do it officialy
currentOrders = [11, 22, 33, 44]

#set up waiter, for now left top corner
waiter = Waiter(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, barriers, listOfOrders, currentOrders)
all_sprites_list.add(waiter)

#WAITER TESTS: get and set order functions
waiter.addToCurrentOrders(55)
print(waiter.currentOrders)
waiter.removeFromCurrentOrders(22)
print(waiter.currentOrders)

#just a control print ;)
print("hello in شروانشاه restaurant!!")