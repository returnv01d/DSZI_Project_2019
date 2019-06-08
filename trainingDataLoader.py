import time

import pygame

from algorithms.bfs import BFS
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

labels = []
features = []
algorithms = [DFS]

print("hello in شروانشاه restaurant!!")

def convertMoveToLabel(move):
    moveType = move.type
    if moveType == moveType.LEFT:
        labels.append('left')
    elif moveType == moveType.RIGHT:
        labels.append('right')
    elif moveType == moveType.UP:
        labels.append('up')
    elif moveType == moveType.DOWN:
        labels.append('down')
    elif moveType == moveType.SERVE_ORDER:
        labels.append('serve_order')


for algo in algorithms:
    board = BoardLoader.load_board_from_file('boards/new_board.txt')
    if algo == DFS:
        DFS.dfs(board, [], Move(MoveType.EMPTY_MOVE))
    elif algo == BFS:
        BFS.bfs(board, [], Move(MoveType.EMPTY_MOVE))
    pygame.display.set_caption("Restaurant - doing {0}".format(algo.name))
    solution = algo.solution
    solution = list(reversed(solution))

    Order.id = 0
    Table.id = 0
    animation_board = BoardLoader.load_board_from_file('boards/new_board.txt')
    sprites = animation_board.to_sprite_group(WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.set_caption("Restaurant - finished {0}. Doing solution...".format(algo.name))
    move = Move(MoveType.EMPTY_MOVE)
    for i in range(len(solution)):
        previous_move = move
        move = solution.pop()
        pygame.display.set_caption("Restaurant - finished {0}. Doing solution....Current move: {1}".format(algo.name, move))
        convertMoveToLabel(move)
        if move.type != MoveType.EMPTY_MOVE and move.type != MoveType.TAKE_ORDER:
            features.append(board.get_training_set(move))
        animation_board.do(move)
        time.sleep(STEP_TIME)

        DISPLAYSURF.blit(background_image, (0, 0))
        sprites.draw(DISPLAYSURF)
        pygame.display.flip()
        fpsClock.tick(FPS)
    time.sleep(1.0)

labelsFile = open("trainingDataLabels.txt", "a")
for i in labels:
     labelsFile.write(i+"\n")

featuresFile = open("trainingFeatures.txt", "a")
for i in features:
    for j in i:
        featuresFile.write(str(j))
    featuresFile.write('\n')