import itertools

from model import waiter, move
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

    def get_moves_with_possible_combinations(self):
        listOfCombinations = self.get_possible_order_combinations(waiter)
        listOfMoves = []
        for i in range(len(listOfCombinations)):
            move.Move.first_order = listOfCombinations[i][0]
            move.Move.second_order = listOfCombinations[i][1]
            listOfMoves.append(move.Move)
        print(listOfMoves[1].first_order)

        return listOfMoves

