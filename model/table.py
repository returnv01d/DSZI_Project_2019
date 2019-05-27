from model.move import Move
from model.move_type import MoveType
from sprites.tableSprite import TableSprite

class Table:
    id = 0

    def __init__(self, x, y):
        self.id = Table.id
        Table.id += 1

        self.received_all_orders = False
        self.orders = []
        self.received_orders = []
        self.sprite = None
        self.x = x
        self.y = y
        # print(self.x, self,y)


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

    def check_if_interaction_possible(self, waiter):
        if not set(waiter.heldOrders).isdisjoint(self.orders):
            return True
        return False

    def get_move_with_possible_combination(self, waiter):

        ordersToThisTable = []

        for i in range(len(waiter.heldOrders)):
            if waiter.heldOrders[i].table_id == self.id:
                ordersToThisTable.append(waiter.heldOrders[i])

        if len(ordersToThisTable) == 1:
            move = Move(MoveType.SERVE_ORDER, ordersToThisTable[0], None, self.id)
        elif len(ordersToThisTable) == 2:
            move = Move(MoveType.SERVE_ORDER, ordersToThisTable[0], ordersToThisTable[1], self.id)

        return move


    def get_order_from_waiter(self, order):
        self.received_orders.append(order)
        self.orders.remove(order)
        if len(self.orders) == 0:
            self.received_all_orders = True




