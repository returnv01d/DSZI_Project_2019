from sprites.kitchenSprite import KitchenSprite
from model.order import Order
from model.move import Move

class Kitchen:
    def __init__(self, orders):
        self.sprite = None
        self.orders = orders
        self.given_orders = []

    def create_sprite(self, width, height):
        self.sprite = KitchenSprite(width, height)
        self.sprite.update_status(self.statuses())

    def __repr__(self):
        return "Kitchen"

    def __str__(self):
        return 'K'

    def give_order(self, order):
        order.is_taken_from_kitchen = True
        self.given_orders.append(order)
        self.orders.remove(order)
        self.sprite.update_status(self.statuses())

    def statuses(self):
        orders_as_strings = [repr(order) for order in self.orders if order.is_taken_from_kitchen == False]
        return orders_as_strings

    def waiting_orders(self):
        return [order for order in self.orders if order.is_taken_from_kitchen is False]

    def check_if_interaction_with_waiter_possible(self, waiter):
        if len(waiter.heldOrders) < 2 and self.orders:
            return True
        return False