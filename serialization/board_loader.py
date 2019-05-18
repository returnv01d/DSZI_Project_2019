from model.waiter import Waiter
from model.order import Order
from model.kitchen import Kitchen
from model.carpet import Carpet
from model.table import Table
from model.freeSpace import FreeSpace
from model.board import Board

class BoardLoader:

    @staticmethod
    def load_board_from_file(filepath):
        file = open(filepath, "r")
        board_size = int(file.readline())
        board = Board(board_size)
        y, x = map(lambda x: int(x), file.readline().split(" "))
        waiter = Waiter()

        waiter.x = x
        waiter.y = y

        orders=[]
        orders_size = int(file.readline())

        for k in range(0, orders_size):
            order = file.readline().split()
            orders.append(Order(int(order[0]), order[1]))

        loaded_objects = [[FreeSpace for _ in range(0, board_size)] for _ in range(0, board_size)]

        for i, line in enumerate(file):
            fields = line.split(" ")
            new_object = None

            for j in range(0, board_size):
                object_letter = fields[j].strip()
                new_object = FreeSpace()

                if object_letter == 'W':
                    new_object = Carpet()
                elif object_letter == 'C':
                    new_object = Carpet()
                elif object_letter == 'T':
                    new_object = Table()

                    this_table_orders = [order for order in orders if order.table_id == new_object.id]
                    new_object.orders.extend(this_table_orders)
                    board.tables.append(new_object)
                elif object_letter == 'K':
                    new_object = Kitchen(orders)
                    board.kitchen = new_object

                loaded_objects[i][j] = new_object

        print(loaded_objects)

        board.objects = loaded_objects
        board.waiter = waiter

        file.close()
        return board

