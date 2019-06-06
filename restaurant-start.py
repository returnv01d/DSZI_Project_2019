import sys
import time

import pygame
from pygame.locals import *

from algorithms.bfs import BFS
from algorithms.dfs import DFS
from machinelerning.decisionTree import DecisionTree
from model.move.move import Move
from model.move.move_type import MoveType
from model.order import Order
from model.table import Table
from serialization.board_loader import BoardLoader

pygame.init()

FPS = 30
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
BOARD_SIZE = 10
BOARD_PATH = "boards/board1.txt"
STEP_TIME = 0.6

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
background_image = pygame.image.load('images/background_image.png')

#0-FreeSpace, 1-Carpet, 2-Kitchen, 3-Table, 5-Waiter
#SVM.svm([1,1,1,0,5,0,0,3,0])
#
board = BoardLoader.load_board_from_file('boards/new_board.txt')
animation_board = BoardLoader.load_board_from_file('boards/new_board.txt')
sprites = animation_board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)

paths = []
paths.append([0,2,0,1,5,0,1,0,0])
paths.append([0,0,2,0,5,1,0,1,0])
paths.append([0,1,1,0,5,0,0,1,0])

for i in paths:
    move = Move(MoveType.UP)
    if DecisionTree.decisiontree([0,2,0,1,5,0,1,0,0]) == 'down':
        move = Move(MoveType.DOWN)
    elif DecisionTree.decisiontree([0,2,0,1,5,0,1,0,0]) == 'left':
        move = Move(MoveType.LEFT)
    elif DecisionTree.decisiontree([0,2,0,1,5,0,1,0,0]) == 'up':
        move = Move(MoveType.UP)
    elif DecisionTree.decisiontree([0,2,0,1,5,0,1,0,0]) == 'right':
        move = Move(MoveType.RIGHT)

    time.sleep(3.0)
    animation_board.do(move)
    time.sleep(STEP_TIME)

    DISPLAYSURF.blit(background_image, (0, 0))
    sprites.draw(DISPLAYSURF)
    pygame.display.flip()
    fpsClock.tick(FPS)
    time.sleep(3.0)

print(DecisionTree.decisiontree([0,0,2,0,5,1,0,1,0]))
print(DecisionTree.decisiontree([0,1,1,0,5,0,0,1,0]))
print(DecisionTree.decisiontree([0,1,0,0,5,0,0,3,0]))

# SVM.svm([0,2,0,1,5,0,1,0,0])
# SVM.svm([0,0,2,0,5,1,0,1,0])
# SVM.svm([0,1,1,0,5,0,0,1,0])
# SVM.svm([0,1,0,0,5,0,0,3,0])
