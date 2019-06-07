import sys
import time

import pygame
from pygame.locals import *

from machinelerning.decisionTree import DecisionTree
from machinelerning.svm import SVM
from model.move.move import Move
from model.move.move_type import MoveType
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


board = BoardLoader.load_board_from_file('boards/new_board.txt')
animation_board = BoardLoader.load_board_from_file('boards/new_board.txt')
sprites = animation_board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)

#you can change machinelearning: decision-tree, svm, svm-raport
machinelearning = 'decision-tree'

if machinelearning =='decision-tree':

    print("Decision tree - waiter moves: ")
    paths = []
    paths.append([0,2,0,1,5,1,0,0,0])
    paths.append([0,0,2,1,5,1,1,0,0])
    paths.append([0,0,0,0,5,1,0,1,0])
    paths.append([0,1,1,0,5,0,0,1,0])

    for i in range(0, 4):
        move = Move(MoveType.UP)
        if DecisionTree.decisiontree(paths[i]) == 'down':
            move = Move(MoveType.DOWN)
        elif DecisionTree.decisiontree(paths[i]) == 'left':
            move = Move(MoveType.LEFT)
        elif DecisionTree.decisiontree(paths[i]) == 'up':
            move = Move(MoveType.UP)
        elif DecisionTree.decisiontree(paths[i]) == 'right':
            move = Move(MoveType.RIGHT)

        time.sleep(2.0)
        animation_board.do(move)
        time.sleep(STEP_TIME)

        DISPLAYSURF.blit(background_image, (0, 0))
        sprites.draw(DISPLAYSURF)
        pygame.display.flip()
        fpsClock.tick(FPS)
        time.sleep(3.0)

    print(DecisionTree.decisiontree([0,2,0,1,5,1,0,0,0]))
    print(DecisionTree.decisiontree([0,0,2,1,5,1,1,0,0]))
    print(DecisionTree.decisiontree([0,0,0,0,5,1,0,1,0]))
    print(DecisionTree.decisiontree([0,1,1,0,5,0,0,1,0]))

elif machinelearning == 'svm':
    print("Support vestor machines - waiter moves: ")
    paths = []
    paths.append([0, 2, 0, 1, 5, 1, 0, 0, 0])
    paths.append([0, 0, 2, 1, 5, 1, 1, 0, 0])
    paths.append([0, 0, 0, 0, 5, 1, 0, 1, 0])
    paths.append([0, 1, 1, 0, 5, 0, 0, 1, 0])

    for i in range(0, 4):
        move = Move(MoveType.UP)
        if SVM.svm(paths[i]) == 'down':
            move = Move(MoveType.DOWN)
        elif SVM.svm(paths[i]) == 'left':
            move = Move(MoveType.LEFT)
        elif SVM.svm(paths[i]) == 'up':
            move = Move(MoveType.UP)
        elif SVM.svm(paths[i]) == 'right':
            move = Move(MoveType.RIGHT)

        time.sleep(2.0)
        animation_board.do(move)
        time.sleep(STEP_TIME)

        DISPLAYSURF.blit(background_image, (0, 0))
        sprites.draw(DISPLAYSURF)
        pygame.display.flip()
        fpsClock.tick(FPS)
        time.sleep(3.0)

    print(SVM.svm([0, 2, 0, 1, 5, 1, 0, 0, 0]))
    print(SVM.svm([0, 0, 2, 1, 5, 1, 1, 0, 0]))
    print(SVM.svm([0, 0, 0, 0, 5, 1, 0, 1, 0]))
    print(SVM.svm([0, 1, 1, 0, 5, 0, 0, 1, 0]))

elif machinelearning =='svm-raport':
    SVM.svm_raport([0, 2, 0, 1, 5, 1, 0, 0, 0])