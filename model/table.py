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

    def check_if_interaction_possible(self, waiter):
        if not set(waiter.heldOrders).isdisjoint(self.orders):
            return True
        return False


    def get_order_from_waiter(self, order):
        self.received_orders.append(order)
        self.orders.remove(order)
        if len(self.orders) == 0:
            self.received_all_orders = True



