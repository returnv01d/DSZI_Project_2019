import pygame.sprite

from model.carpet import Carpet
from model.freeSpace import FreeSpace
from model.kitchen import Kitchen
from model.table import Table
from model.waiter import Waiter
from model.move import Move
from model.order import Order

class Board:
    def __init__(self, board_size):
        self.board_size = board_size

        self.objects = []
        self.waiter = None

    def to_sprite_group(self, window_width, window_height):
        sprite_width = int(window_width / self.board_size)
        sprite_height = int(window_height / self.board_size)

        sprites = pygame.sprite.Group()
        current_height = 0

        for row in self.objects:
            for j, obj in enumerate(row):
                if(obj.__class__.__name__ != Carpet.__name__ and obj.__class__.__name__ != FreeSpace.__name__):
                    floor = FreeSpace()
                    floor.create_sprite(sprite_width, sprite_height)
                    floor.sprite.draw(j * sprite_width, current_height)
                    sprites.add(floor.sprite)

                obj.create_sprite(sprite_width, sprite_height)
                obj.sprite.draw(j * sprite_width, current_height)
                sprites.add(obj.sprite)
            current_height += sprite_height
        self.waiter.create_sprite(sprite_width, sprite_height)

        self.waiter.sprite.draw(self.waiter.y * sprite_width, self.waiter.x * sprite_height)
        sprites.add(self.waiter.sprite)
        return sprites

    def take_dish(self):
        if len(self.waiter.heldOrders) == 0 and len(self.waiter.listOfOrders) != 0:
            # print(self.waiter.listOfOrders)
            # print(self.waiter.heldOrders)

            self.waiter.heldOrders.append(self.waiter.listOfOrders[0])
            self.waiter.listOfOrders.pop(0)
            self.waiter.sprite.update_image_waiter(1)

        elif len(self.waiter.heldOrders) == 1 and len(self.waiter.listOfOrders) != 0:
            # print(self.waiter.listOfOrders)
            # print(self.waiter.heldOrders)

            self.waiter.heldOrders.append(self.waiter.listOfOrders[0])
            self.waiter.listOfOrders.pop(0)
            self.waiter.sprite.update_image_waiter(2)

    def put_dish_on_table(self, table_id, next_object):
        for order in self.waiter.heldOrders:
            if order.table_id == table_id:
                self.waiter.heldOrders.remove(order)
                self.waiter.sprite.update_image_waiter(len(self.waiter.heldOrders))
                next_object.sprite.update_image()

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

        next_object = self.objects[new_x][new_y]

        if new_x >= 0 and new_x < self.board_size and new_y >= 0 and new_y < self.board_size:
            if next_object.__class__.__name__ == Carpet.__name__:
                self.waiter.x += board_move_x
                self.waiter.y += board_move_y
                self.waiter.update_sprite_position(board_move_y, board_move_x)
                # board.x is sprite.y because board.x means which row(height) we change.

            if next_object.__class__.__name__ == Kitchen.__name__:
                self.take_dish()

            if next_object.__class__.__name__ == Table.__name__:
                self.put_dish_on_table(next_object.id, next_object)

