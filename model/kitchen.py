from sprites.kitchenSprite import KitchenSprite
from model.order import Order
class Kitchen:
    def __init__(self):
        self.sprite = None
        self.orders = []
        order1 = Order(0, 'bliny')
        order2 = Order(1, 'schabowy')
        order3 = Order(2, 'przepiorka')
        self.orders.append(order1)
        self.orders.append(order2)
        self.orders.append(order3)

    def create_sprite(self, width, height):
        self.sprite = KitchenSprite(width, height)
        self.sprite.update_status(self.statuses())

    def __repr__(self):
        return "Kitchen"

    def __str__(self):
        return 'K'

    def statuses(self):
        orders_as_strings = [repr(order) for order in self.orders]
        return orders_as_strings