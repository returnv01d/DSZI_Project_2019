import sys
import time

import pygame
from pygame.locals import *

from algorithms.dfs import DFS
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
algorithms = [DFS]

print("hello in شروانشاه restaurant!!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                board.do(Move(MoveType.UP))
            if event.key == K_DOWN:
                board.do(Move(MoveType.DOWN))
            if event.key == K_RIGHT:
                board.do(Move(MoveType.RIGHT))
            if event.key == K_LEFT:
                board.do(Move(MoveType.LEFT))
            if event.key == K_o:
                board.do(Move(MoveType.TAKE_ORDER, first_order=board.kitchen.orders[-1]))
            if event.key == K_p:
                print(DFS.dfs(board, [], Move(MoveType.EMPTY_MOVE)))

    for algo in algorithms:
        board = BoardLoader.load_board_from_file('boards/new_board.txt')

        if algo == DFS:
            DFS.dfs(board, [], Move(MoveType.EMPTY_MOVE))
        pygame.display.set_caption("Restaurant - doing {0}".format(algo.name))
        solution = algo.soulution
        solution = list(reversed(solution))
        print("otrzymana solucja: ")
        print(solution)
        Order.id = 0
        Table.id = 0

        animation_board = BoardLoader.load_board_from_file('boards/new_board.txt')
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

