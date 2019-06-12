import copy
import sys
import time

import pygame
from pygame.locals import *

from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.best_first_search import BestFirstSearch
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
STEP_TIME = 0.1

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
background_image = pygame.image.load('images/background_image.png')



files = []
files.append('boards/board5.txt')
files.append('boards/board3.txt')
files.append('boards/board6.txt')

# IMPORTANT! READ BEFORE ADDING YOUR ALGORITHM. ADD YOUR ALGORITHM CLASS, NOT FUNCTION.
# YOUR CLASS SHOULD HAVE "NAME" FIELD AND "SOLUTION" FIELD WHERE YOU MUST PUT YOUR LIST WITH SOLUTION MOVES.
# ADD YOU ALGORITHM CLASS HERE.
algorithms = [DFS, BFS, BestFirstSearch]

print("hello in شروانشاه restaurant!!")

while True:
    for file in files:

        for algo in algorithms:
            board = None
            solution = None
            Order.id = 0
            Table.id = 0
            board = copy.deepcopy(BoardLoader.load_board_from_file(file))
            print(algo)
            if algo == DFS:
                print("dfsik")
                DFS.dfs(board, [], Move(MoveType.EMPTY_MOVE))
                solution = DFS.soulution
                DFS.found_solution = None
                DFS.soulution = None
            elif algo == BFS:
                BFS.bfs(board, [], Move(MoveType.EMPTY_MOVE))
                solution = BFS.soulution
                BFS.soulution = None
                BFS.found_solution = None
            elif algo == BestFirstSearch:
                BestFirstSearch.best_first(board, [], [], Move(MoveType.EMPTY_MOVE))
                solution = BestFirstSearch.soulution
                BestFirstSearch.soulution = None
                BestFirstSearch.found_solution = None

            pygame.display.set_caption("Restaurant - doing {0}".format(algo.name))
            solution = list(reversed(solution))
            print("otrzymana solucja: ")
            print(list(reversed(solution)))
            Order.id = 0
            Table.id = 0
            animation_board = BoardLoader.load_board_from_file(file)
            sprites = animation_board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)
            pygame.display.set_caption("Restaurant - finished {0}. Doing solution...".format(algo.name))
            for i in range(len(solution)):
                move = solution.pop()
                pygame.display.set_caption("Restaurant - finished {0}. Doing solution....Current move: {1}".format(algo.name, move))
                animation_board.do(move)
                time.sleep(STEP_TIME)

                DISPLAYSURF.blit(background_image, (0, 0))
                sprites.draw(DISPLAYSURF)
                pygame.display.flip()
                fpsClock.tick(FPS)
            time.sleep(1.0)