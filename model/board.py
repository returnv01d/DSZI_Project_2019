import pygame.sprite
from model.move.move_filter import MoveFilter
from model.carpet import Carpet
from model.freeSpace import FreeSpace
from model.kitchen import Kitchen
from model.move.move import Move
from model.move.move_type import MoveType
from model.table import Table


class Board:
    def __init__(self, board_size):
        self.board_size = board_size

        self.objects = []
        self.waiter = None
        self.kitchen = None
        self.tables = []

    def __repr__(self):
        s = "|Environment "
        s += self.get_waiter_environment(3, 3)
        #s += repr(self.waiter)
        #s += repr(self.kitchen)
        #s += "|Tables "
        #for table in self.tables:
            #s += repr(table)

        return s

    def to_sprite_group(self, window_width, window_height):
        sprite_width = int(window_width / self.board_size)
        sprite_height = int(window_height / self.board_size)

        sprites = pygame.sprite.Group()
        current_height = 0

        for row in self.objects:
            for j, obj in enumerate(row):
                if obj.__class__.__name__ != Carpet.__name__ and obj.__class__.__name__ != FreeSpace.__name__:
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
        orders = [move.first_order, move.second_order]
        for order in orders:
            if order is not None:
                self.waiter.take_order(order)
                self.kitchen.give_order(order)

    def serve_dish_to_table_from_waiter(self, move):
        table = [table for table in self.tables if move.target_table_id == table.id][0]
        orders = [move.first_order, move.second_order]

        for order in orders:

            if order is not None:
                self.waiter.give_order(order)
                table.take_order(order)
                order.is_delivered = True



    def get_possible_waiter_fields(self, previous_move):
        x = self.waiter.x
        y = self.waiter.y

        fields = {"LEFT": self.object_at(x, y - 1), "RIGHT": self.object_at(x, y + 1),
                  "DOWN": self.object_at(x + 1, y), "UP": self.object_at(x - 1, y)}

        filtered = MoveFilter.filter_possible_moves(fields, previous_move, self.waiter)
        return filtered

    def get_possible_waiter_moves(self, previous_move):
        possible_moves = []
        fields = self.get_possible_waiter_fields(previous_move)
        for direction, field in fields.items():
            if field.__class__.__name__ == Carpet.__name__:
                possible_moves.append(Move(MoveType[direction]))
            elif field.__class__.__name__ == Kitchen.__name__:
                possible_moves.extend(self.kitchen.get_possible_interactions_with_waiter(self.waiter))
            elif field.__class__.__name__ == Table.__name__:
                possible_moves.append(field.get_possible_interactions_with_waiter(self.waiter))

        return possible_moves

    def all_orders_served(self):
        if not self.waiter.heldOrders:  # if waiter don't have any orders

            if all(table.received_all_orders is True for table in self.tables):  # and if all tables have their orders
                if not self.kitchen.waiting_orders():  # and if there isn't any waiting order in kitchen
                    return True
        return False

    def object_at(self, x, y):
        if x >= self.board_size or x < 0 or y >= self.board_size or y < 0:
            return None

        return self.objects[x][y]

    def move_waiter(self, move):
        board_move_x = 0
        board_move_y = 0

        if move == MoveType.UP:
            board_move_x = -1
        elif move == MoveType.DOWN:
            board_move_x = 1
        elif move == MoveType.RIGHT:
            board_move_y = 1
        elif move == MoveType.LEFT:
            board_move_y = -1

        self.waiter.x += board_move_x
        self.waiter.y += board_move_y
        if self.waiter.sprite is not None:
            self.waiter.update_sprite_position()
        # board.x is sprite.y because board.x means which row(height) we change.

    def do(self, move):
        # print("dostaje move: {0}".format(move))
        if 0 <= move.type.value <= 4:
            self.move_waiter(move.type)

        if move.type == MoveType.TAKE_ORDER:
            self.take_dish_from_kitchen_to_waiter(move)

        if move.type == MoveType.SERVE_ORDER:
            self.serve_dish_to_table_from_waiter(move)
        # print(move)
        # for table in self.tables:
        #     print("table {0}: is interaction possible? {1}".format(table.id,
        #                                                            table.check_if_interaction_with_waiter_possible(self.waiter)))
        #
        # print("kitchen: is interaction possible? {0}".format(self.kitchen.check_if_interaction_with_waiter_possible(self.waiter)))
        # print("possible moves:")
        # print(self.get_possible_waiter_moves(move))
        return self

    def get_waiter_environment(self, width, height):
        env = ""
        for i in range(2 * height + 1):
            for j in range(2 * width + 1):
                obj_pos_x = self.waiter.x - height + i
                obj_pos_y = self.waiter.y - width + j
                obj = self.object_at(obj_pos_x, obj_pos_y)
                if width - i == 0 and height - j == 0:
                    obj = self.waiter
                env += f"{width - i}_{height - j}:{obj.num() if obj is not None else -1} "

        return env