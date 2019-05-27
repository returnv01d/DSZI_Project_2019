from model.move.move import Move
from model.move.move_type import MoveType
from sprites.tableSprite import TableSprite

class Table:
    id = 0

    def __init__(self):
        self.id = Table.id
        Table.id += 1

        self.received_all_orders = False
        self.orders = []
        self.received_orders = []
        self.sprite = None

    def create_sprite(self, width, height):
        self.sprite = TableSprite(width, height)
        self.sprite.update_status(self.status())

    def __repr__(self):
        return "Table"

    def __str__(self):
        return 'T'

    def status(self):
        statuses = ["id: " + str(self.id)]
        for order in self.orders:
            statuses.append(repr(order) + " " + str(order.is_delivered))

        return statuses

    def check_if_interaction_with_waiter_possible(self, waiter):
        for order in waiter.heldOrders:
            for table_order in self.orders:
                if order.table_id == table_order.table_id and order.name == table_order.name:
                    return True
        return False

    def get_possible_interactions_with_waiter(self, waiter):
        this_table_orders = [order for order in waiter.heldOrders if order.table_id == self.id]

        if len(this_table_orders) == 2:
            possible_move = Move(MoveType.SERVE_ORDER, first_order=this_table_orders[0],
                                 second_order=this_table_orders[1], target_table_id=self.id)
        else:
            possible_move = Move(MoveType.SERVE_ORDER, first_order=this_table_orders[0],
                                 target_table_id=self.id)
        return  possible_move

    def take_order(self, order):
        this_table_order = [ord for ord in self.orders if ord.id == order.id][0]
        this_table_order.is_delivered = True
        self.received_orders.append(order)
        if len(self.orders) == len(self.received_orders):
            self.received_all_orders = True

        self.update_status()


    def update_status(self):
        if self.sprite is not None:
            self.sprite.update_status(self.status())

