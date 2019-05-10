import pygame.sprite

from model.carpet import Carpet
from model.freeSpace import FreeSpace
from model.kitchen import Kitchen
from model.table import Table
from model.waiter import Waiter
from model.move import Move


class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.objects = []
        self.waiter = None


    def to_sprite_group(self, window_width, window_height):
        sprites = pygame.sprite.Group()
        sprite_width = int(window_width / self.board_size)
        sprite_height = int(window_height / self.board_size)

        current_height = 0

        for y, row in enumerate(self.objects):
            for x, obj in enumerate(row):
                obj.create_sprite(sprite_width, sprite_height)
                obj.sprite.draw(x * sprite_width, current_height)
                sprites.add(obj.sprite)
            current_height += sprite_height
        self.waiter.create_sprite(sprite_width, sprite_height)

        self.waiter.sprite.draw(self.waiter.y * sprite_width, self.waiter.x * sprite_height)
        sprites.add(self.waiter.sprite)
        return sprites


    def generate_board(self):
        board = []
        flag = 0
        file = open("boards/board1.txt", "r")
        board_size = int(file.readline())
        y, x = map(lambda x: int(x), file.readline().split(" "))
        self.waiter = Waiter()

        self.waiter.x = x
        self.waiter.y = y

        for line in file:
            fields = line.split(" ")
            new_object = None
            row = []

            for j in range(0, board_size):
                new_object = fields[j].strip()
                row.append(new_object)
            board.append(row)
        file.close()
        return board

    def draw_board(self):
        generatedBoard = Board.generate_board(self)
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                new_object = None
                if (generatedBoard[i][j] == 'F'):
                    new_object = FreeSpace()
                elif (generatedBoard[i][j] == 'W'):
                    new_object = Carpet()
                elif (generatedBoard[i][j] == 'C'):
                    new_object = Carpet()
                elif (generatedBoard[i][j] == 'T'):
                    new_object = Table()
                elif (generatedBoard[i][j] == 'K'):
                    new_object = Kitchen()
                row.append(new_object)
            self.objects.append(row)

    def move_waiter(self, move):
        board_move_x = 0
        board_move_y = 0

        if move == Move.UP:
            board_move_x = -1
        elif move == Move.DOWN:
            board_move_x = 1
        elif move == Move.RIGHT:
            board_move_y = 1
        elif move == Move.LEFT:
            board_move_y = -1

        new_x = self.waiter.x + board_move_x
        new_y = self.waiter.y + board_move_y

        if new_x >= 0 and new_x < self.board_size and new_y >= 0 and new_y < self.board_size:
            if self.objects[new_x][new_y].__class__.__name__ == Carpet.__name__:
                self.waiter.x += board_move_x
                self.waiter.y += board_move_y
                self.waiter.update_sprite_position(board_move_y, board_move_x)
                # board.x is sprite.y because board.x means which row(height) we change.


