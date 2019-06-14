import socket
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

PORT = 26542
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("localhost", PORT))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        board = BoardLoader.load_board_from_file('boards/new_board.txt')
        Order.id = 0
        Table.id = 0
        move_counter = 0
        previous_move = Move(MoveType.EMPTY_MOVE)
        while not board.all_orders_served():
            possible_moves = board.get_possible_waiter_moves(previous_move)
            state = ""
            for i, movee in enumerate(board.get_possible_waiter_moves(previous_move)):
                if str(movee.type.value) not in state:
                    state += f"{movee.type.value} "
            state += repr(board)
            state += "\n"
            print(state)
            s.send(bytes(f"{state}", 'utf-8'))
            print("wyslano")
            data = s.recv(1024).strip()

            print('Received', repr(data))
            sprites = board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)
            #pygame.display.set_caption(f"Restaurant - vowpal doing {move_counter} move: {move}")

            #board.do(move)

            time.sleep(STEP_TIME)
            DISPLAYSURF.blit(background_image, (0, 0))
            sprites.draw(DISPLAYSURF)
            pygame.display.flip()
            fpsClock.tick(FPS)


