import sys
import time

import pygame
from pygame.locals import *

from algorithms.bfs import BFS
from algorithms.dfs import DFS
from machinelerning.decisionTree import DecisionTree
from machinelerning.svm import SVM
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

# IMPORTANT! READ BEFORE ADDING YOUR ALGORITHM. ADD YOUR ALGORITHM CLASS, NOT FUNCTION.
# YOUR CLASS SHOULD HAVE "NAME" FIELD AND "SOLUTION" FIELD WHERE YOU MUST PUT YOUR LIST WITH SOLUTION MOVES.
# ADD YOU ALGORITHM CLASS HERE.
algorithms = [BFS]

print("hello in شروانشاه restaurant!!\n")

SVM.svm([1,1,1,0,5,0,0,3,0])
DecisionTree.decisiontree([1,1,1,0,5,0,0,3,0])