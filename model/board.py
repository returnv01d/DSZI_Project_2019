import pygame.sprite

from model.carpet import Carpet
from model.freeSpace import FreeSpace
from model.kitchen import Kitchen
from model.table import Table
from model.waiter import Waiter


class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.objects = []

    def to_sprite_group(self, window_width, window_height):
        sprite_width = int(window_width / self.board_size)
        sprite_height = int(window_height / self.board_size)

        sprites = pygame.sprite.Group()
        current_height = 0
        for row in self.objects:
            for j, obj in enumerate(row):
                obj.create_sprite(sprite_width, sprite_height)
                obj.sprite.draw(j * sprite_width, current_height)
                sprites.add(obj.sprite)
            current_height += sprite_height
        return sprites


    def generate_board(self):
        board = []
        flag = 0
        file = open("boards/board2.txt", "r")
        for line in file:
            fields = line.split(" ")
            new_object = None
            row = []
            if flag==0:
                board_size=fields[0]
                flag=1
            else:
                for j in range(0, int(board_size)):
                    new_object = fields[j].strip()
                    row.append(new_object)
                board.append(row)
        file.close()
        return board

    def draw_board(self):
        generatedBoard = Board.generate_board(self)
        current_height = 0
        board =[]
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                new_object = None
                if (generatedBoard[i][j] == 'F'):
                    new_object = FreeSpace()
                elif (generatedBoard[i][j] == 'W'):
                    new_object = Waiter()
                elif (generatedBoard[i][j] == 'C'):
                    new_object = Carpet()
                elif (generatedBoard[i][j] == 'T'):
                    new_object = Table()
                elif (generatedBoard[i][j] == 'K'):
                    new_object = Kitchen()
                row.append(new_object)
            self.objects.append(row)