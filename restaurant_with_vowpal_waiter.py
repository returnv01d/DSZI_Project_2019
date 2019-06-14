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
s.connect(("localhost", PORT))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        board = BoardLoader.load_board_from_file('data_learning_boards/board1.txt')
        Order.id = 0
        Table.id = 0
        move_counter = 0
        previous_move = Move(MoveType.EMPTY_MOVE)
        while not board.all_orders_served():
            possible_moves = board.get_possible_waiter_moves(previous_move)
            print(possible_moves)
            state = ""
            for i, movee in enumerate(board.get_possible_waiter_moves(previous_move)):
                if str(movee.type.value + 1) not in state:
                    state += f"{movee.type.value + 1} "
            state + repr(board.waiter)
            state += repr(board)
            state += "\n"
            print(f"state: {state}")
            s.send(bytes(f"{state}", 'utf-8'))
            print("wyslano")
            data = s.recv(1024).strip()

            print('Received', repr(data))
            data = int(data) - 1
            print(f"converted: {data}")
            move = [move for move in possible_moves if move.type.value == data][0]
            print(move)
            sprites = board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)
            pygame.display.set_caption(f"Restaurant - vowpal doing {move_counter} move: {move}")

            board.do(move)
            previous_move = move
            time.sleep(STEP_TIME)
            DISPLAYSURF.blit(background_image, (0, 0))
            sprites.draw(DISPLAYSURF)
            pygame.display.flip()
            fpsClock.tick(FPS)


