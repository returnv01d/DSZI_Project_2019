import itertools

from model import waiter
from sprites.kitchenSprite import KitchenSprite
from model.order import Order
from model.move import Move

class Kitchen:
    def __init__(self):
        self.sprite = None
        self.orders = [Order]

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

    def waiting_orders(self):
        return [order for order in self.orders if order.is_taken_from_kitchen is False]

    def check_if_next_move_possible(self, previous_move):
        if previous_move.type == Move.TAKE_ORDER:
            return False
        return True

    def get_possible_order_combinations(self, waiter):
        ordersToServe = []
        listOfCombinations = []

        for i in range(len(self.orders)):
            if self.orders[i].is_taken_from_kitchen == False:
                ordersToServe.append(self.orders[i])

        if len(waiter.heldOrders) == 0:
            listOfCombinations = set(list(itertools.combinations(ordersToServe, 2)))
        elif len(waiter.heldOrders) == 1:
            listOfCombinations = set(list(itertools.combinations(ordersToServe, 1)))
        return list(listOfCombinations)