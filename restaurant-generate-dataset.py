import sys
import time

import pygame
from pygame.locals import *

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
files.append('boards/board3.txt')
files.append('boards/board5.txt')
files.append('boards/board6.txt')
files.append('boards/board1.txt')
files.append('boards/board7.txt')
files.append('boards/board8.txt')
files.append('boards/board9.txt')
files.append('boards/board10.txt')
files.append('boards/board11.txt')
files.append('boards/board12.txt')
files.append('boards/board13.txt')
files.append('boards/board2.txt')
files.append('boards/board4.txt')
files.append('boards/board14.txt')
files.append('boards/board15.txt')
files.append('boards/board16.txt')
files.append('boards/board17.txt')
files.append('boards/board18.txt')
files.append('boards/board19.txt')
files.append('boards/board20.txt')


# IMPORTANT! READ BEFORE ADDING YOUR ALGORITHM. ADD YOUR ALGORITHM CLASS, NOT FUNCTION.
# YOUR CLASS SHOULD HAVE "NAME" FIELD AND "SOLUTION" FIELD WHERE YOU MUST PUT YOUR LIST WITH SOLUTION MOVES.
# ADD YOU ALGORITHM CLASS HERE.


print("hello in شروانشاه restaurant!!")

testing_data = open("boards/testing_data.txt", "w")

for file in files:
    print()
    board = None
    solution = None
    Order.id = 0
    Table.id = 0
    board = BoardLoader.load_board_from_file(file)

    DFS.dfs(board, [], Move(MoveType.EMPTY_MOVE), "")
    pygame.display.set_caption("Restaurant - doing {0}".format(DFS.name))

    solution = DFS.soulution
    print(solution)
    solution = list(reversed(solution))
    solution.pop()

    Order.id = 0
    Table.id = 0

    DFS.found_solution = None
    DFS.soulution = None

    for move_and_state in solution:
        testing_data.write(f"{move_and_state[0].type.value} |Possible_moves {move_and_state[1]}")
        testing_data.write("\n")
        print(f"{move_and_state[0].type.value} |Possible_moves {move_and_state[1]}")

    print("otrzymana solucja: ")
    print(solution)


    animation_board = BoardLoader.load_board_from_file(file)
    sprites = animation_board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.set_caption("Restaurant - finished {0}. Doing solution...".format(DFS.name))

    for i in range(len(solution)):
        move = solution.pop()
        move = move[0]

        print(move)
        pygame.display.set_caption("Restaurant - finished {0}. Doing solution....Current move: {1}".format(DFS.name, move))
        animation_board.do(move)
        time.sleep(STEP_TIME)

        DISPLAYSURF.blit(background_image, (0, 0))
        sprites.draw(DISPLAYSURF)
        pygame.display.flip()
        fpsClock.tick(FPS)
    time.sleep(1.0)



testing_data.close()