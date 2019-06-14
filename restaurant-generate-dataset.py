import os
import time
from pathlib import Path
import pygame
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
STEP_TIME = 0.02

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
background_image = pygame.image.load('images/background_image.png')
paths = []
testing_data = open("boards/testing_data.txt", "w")
directory = os.fsencode("data_learning_boards")


for file in os.listdir(directory):
     filenam = os.fsdecode(file)
     paths.append(filenam)

print(paths)

for filename in list(sorted(paths)):

    board = None
    solution = None
    Order.id = 0
    Table.id = 0
    board = BoardLoader.load_board_from_file("data_learning_boards" + os.sep + filename)

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
        testing_data.write(f"{move_and_state[0].type.value + 1} |Possible_moves {move_and_state[1]}")
        testing_data.write("\n")
        print(f"{move_and_state[0].type.value} |Possible_moves {move_and_state[1]}")

    print("otrzymana solucja: ")
    print(solution)


    animation_board = BoardLoader.load_board_from_file("data_learning_boards" + os.sep + filename)
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
    time.sleep(0.2)



testing_data.close()