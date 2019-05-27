import pygame.sprite

from model.carpet import Carpet
from model.freeSpace import FreeSpace
from model.kitchen import Kitchen
from model.table import Table
from model.waiter import Waiter
from model.move_filter import MoveFilter
from model.move import Move
from model.move_type import MoveType
from model.order import Order

class Board:
    def __init__(self, board_size):
        self.board_size = board_size

        self.objects = []
        self.waiter = None
        # self.kitchen = []
        self.kitchen = None
        self.tables = []

    def to_sprite_group(self, window_width, window_height):
        sprite_width = int(window_width / self.board_size)
        sprite_height = int(window_height / self.board_size)

        sprites = pygame.sprite.Group()
        current_height = 0

        for row in self.objects:
            for j, obj in enumerate(row):
                if(obj.__class__.__name__ != Carpet.__name__ and obj.__class__.__name__ != FreeSpace.__name__):
                    # draw floor first under kitchen and table
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

    def take_dish_from_kitchen_to_waiter(self, move):

        if self.kitchen.check_if_next_move_possible(self.waiter) == True:
            self.waiter.heldOrders.append(move.first_order)
            self.kitchen.waiting_orders.remove(move.first_order)
            self.kitchen.taken_orders.append(move.first_order)
            # print(self.waiter.heldOrders)

            if len(move.items) == 1:
                move.items[0].is_taken_from_kitchen = True
            elif len(move.items) == 2:
                move.items[0].is_taken_from_kitchen = True
                move.items[1].is_taken_from_kitchen = True


            if len(self.waiter.heldOrders) == 1:
                self.waiter.sprite.update_image_waiter(1)

            if len(self.waiter.heldOrders) == 2:
                self.waiter.sprite.update_image_waiter(2)

    def serve_dish_to_table_from_waiter(self, move):
        table = move.target_table
        # order = items[1]

        if table.check_if_interaction_possible(self.waiter) == True:

            self.waiter.heldOrders.remove(move.first_order)
            move.first_order.is_delivered = True

            if len(self.waiter.heldOrders) == 0:
                self.waiter.sprite.update_image_waiter(0)

            if len(self.waiter.heldOrders) == 1:
                self.waiter.sprite.update_image_waiter(1)

    # def take_dish(self):
    #     if len(self.waiter.heldOrders) == 0:
    #         self.waiter.heldOrders.append()
    #         self.waiter.listOfOrders.pop(0)
    #         self.waiter.sprite.update_image_waiter(1)
    #
    #     elif len(self.waiter.heldOrders) == 1 and len(self.waiter.listOfOrders) != 0:
    #         self.waiter.heldOrders.append(self.waiter.listOfOrders[0])
    #         self.waiter.listOfOrders.pop(0)
    #         self.waiter.sprite.update_image_waiter(2)

    # def put_dish_on_table(self, table_id, next_object):
    #     for order in self.waiter.heldOrders:
    #         if order.table_id == table_id:
    #             self.waiter.heldOrders.remove(order)
    #             self.waiter.sprite.update_image_waiter(len(self.waiter.heldOrders))
    #             next_object.sprite.update_image()

    def get_possible_waiter_fields(self, previous_move):
        x = self.waiter.x
        y = self.waiter.y

        fields = {"LEFT" : self.object_at(x, y - 1), "RIGHT" : self.object_at(x, y + 1), "DOWN":self.object_at(x + 1, y ), "UP":self.object_at(x - 1, y)}
        filtered = MoveFilter.filter_possible_moves(fields, previous_move)
        return filtered

    def get_possible_waiter_moves(self, previous_move):
        possible_moves = []
        fields = self.get_possible_waiter_fields(previous_move)

        for j in fields:
            if str(fields[j]) == "K":
                possible_moves.extend(fields[j].get_moves_with_possible_combinations(self.waiter))
            elif str(fields[j]) == "T":
                possible_moves.append(fields[j].get_move_with_possible_combination(self.waiter))
            elif str(fields[j]) == "C" and j == "DOWN":
                move = Move(MoveType.DOWN)
                possible_moves.append(move)
            elif str(fields[j]) == "C" and j == "UP":
                move = Move(MoveType.UP)
                possible_moves.append(move)
            elif str(fields[j]) == "C" and j == "RIGHT":
                move = Move(MoveType.RIGHT)
                possible_moves.append(move)
            elif str(fields[j]) == "C" and j == "LEFT":
                move = Move(MoveType.LEFT)
                possible_moves.append(move)
        # print(possible_moves)
        return possible_moves


    def all_orders_served(self):
        if not self.waiter.heldOrders: # if waiter dont have any orders
            print("I dont have any orders")
            for table in self.tables:
                print("table")
                print(table.received_orders)
            if all(table.received_all_orders is True for table in self.tables): # and if all tables have their orders
                if not self.kitchen.waiting_orders(): # and if there isn't any waiting order in kitchen
                    return True
        return False


    def object_at(self, x, y):
        if x >= self.board_size or x < 0 or y >= self.board_size or y < 0:
            return None

        return self.objects[x][y]

    def move_waiter(self, move_type):
        board_move_x = 0
        board_move_y = 0

        if move_type == MoveType.UP:
            board_move_x = -1
        elif move_type == MoveType.DOWN:
            board_move_x = 1
        elif move_type == MoveType.RIGHT:
            board_move_y = 1
        elif move_type == MoveType.LEFT:
            board_move_y = -1

        new_x = self.waiter.x + board_move_x
        new_y = self.waiter.y + board_move_y


        if new_x >= 0 and new_x < self.board_size and new_y >= 0 and new_y < self.board_size:
            next_object = self.objects[new_x][new_y]
            if next_object.__class__.__name__ == Carpet.__name__:
                self.waiter.x += board_move_x
                self.waiter.y += board_move_y
                self.waiter.update_sprite_position(board_move_y, board_move_x)
                # board.x is sprite.y because board.x means which row(height) we change.


            # if next_object.__class__.__name__ == Kitchen.__name__:
            #     self.take_dish()
            #
            # if next_object.__class__.__name__ == Table.__name__:
            #     self.put_dish_on_table(next_object.id, next_object)

            # print(self.get_possible_waiter_fields())

    def do(self, move):
        if move.type == MoveType.UP:
            self.move_waiter(move.type)

        if move.type == MoveType.DOWN:
            self.move_waiter(move.type)

        if move.type == MoveType.RIGHT:
            self.move_waiter(move.type)

        if move.type == MoveType.LEFT:
            self.move_waiter(move.type)

        if move.type == MoveType.TAKE_ORDER:
            self.take_dish_from_kitchen_to_waiter(move)

        if move.type == MoveType.SERVE_ORDER:
            self.serve_dish_to_table_from_waiter(move)

        return self

