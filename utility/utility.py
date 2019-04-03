import random
from model.freeSpace import FreeSpace
from model.table import Table
from model.waiter import Waiter
from model.obstacle import Obstacle
from model.kitchen import Kitchen


class Utility:
    @staticmethod
    def generate_board(board_size, sprite_width, sprite_height):
        board = []
        current_height = 0
        for i in range(0, board_size):
            row = []
            for j in range(0, board_size):
                new_object = None
                if (i == int(board_size / 2) and j == int(board_size / 2)):
                    new_object = Waiter()

                elif (i == 0 and ((j == board_size - 1) or (j == board_size - 2))):
                    new_object = Kitchen()
                elif ((i + 8) % 12 == 0 and (j + 8) % 16 == 0):
                    new_object = Table()
                else:
                    if (random.randint(0, 30) != 30):
                        new_object = FreeSpace()
                    else:
                        new_object = Obstacle()
                new_object.create_sprite(sprite_width, sprite_height)
                new_object.sprite.draw(j * sprite_width, current_height)
                row.append(new_object)
            current_height += sprite_height
            board.append(row)
        return board