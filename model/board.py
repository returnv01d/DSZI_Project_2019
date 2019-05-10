import random
import pygame.sprite
from model.freeSpace import FreeSpace
from model.table import Table
from model.waiter import Waiter
from model.obstacle import Obstacle
from model.kitchen import Kitchen

class Board:
    def __init__(self, board_size, starting_waiter_x, starting_waiter_y):
        self.board_size = board_size
        self.starting_waiter_x = starting_waiter_x
        self.starting_waiter_y = starting_waiter_y
        self.objects = []


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


                if y == self.starting_waiter_y and x == self.starting_waiter_x:
                    print("creating waiter")
                    waiter = Waiter()
                    waiter.create_sprite(sprite_width, sprite_height)
                    sprites.add(waiter.sprite)
                    waiter.sprite.draw(x * sprite_width, current_height)
                    #sprites.change_layer(waiter.sprite, 1)

            current_height += sprite_height
        return sprites

    def generate_test_board(self):
        for i in range(0, self.board_size):
            row = []
            for j in range(0, self.board_size):
                new_object = None


                if (i == 0 and ((j == self.board_size - 1) or (j == self.board_size - 2))):
                    new_object = Kitchen()
                elif ((i + 8) % 12 == 0 and (j + 8) % 16 == 0):
                    new_object = Table()
                else:
                    if (random.randint(0, 30) != 30):
                        new_object = FreeSpace()
                    else:
                        new_object = Obstacle()

                row.append(new_object)
            self.objects.append(row)


