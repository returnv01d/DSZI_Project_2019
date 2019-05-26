import itertools

from model import waiter, move
from model.move_type import MoveType
from sprites.kitchenSprite import KitchenSprite
from model.order import Order
from model.move import Move

class Kitchen:
    def __init__(self, orders):
        self.sprite = None
        self.waiting_orders = orders
        self.taken_orders = []


    def create_sprite(self, width, height):
        self.sprite = KitchenSprite(width, height)
        self.sprite.update_status(self.statuses())

    def __repr__(self):
        return "Kitchen"

    def __str__(self):
        return 'K'

    def statuses(self):
        orders_as_strings = [repr(order) for order in self.waiting_orders]
        return orders_as_strings

    def waiting_orders(self):
        return [order for order in self.waiting_orders if order.is_taken_from_kitchen is False]

    def check_if_next_move_possible(self, waiter):
        if len(waiter.heldOrders) == 2 or not self.waiting_orders:
            return False
        return True

    def get_possible_order_combinations(self, waiter):
        ordersToServe = []
        listOfCombinations = []

        for i in range(len(self.waiting_orders)):
            if self.waiting_orders[i].is_taken_from_kitchen == False:
                ordersToServe.append(self.waiting_orders[i])

        if len(waiter.heldOrders) == 0:
            if len(ordersToServe) > 1:
                listOfCombinations = set(list(itertools.combinations(ordersToServe, 2)))
            else:
                listOfCombinations = set(list(itertools.combinations(ordersToServe, 1)))
        elif len(waiter.heldOrders) == 1:
            listOfCombinations = set(list(itertools.combinations(ordersToServe, 1)))

        return list(listOfCombinations)

    def get_moves_with_possible_combinations(self, waiter):
        listOfCombinations = self.get_possible_order_combinations(waiter)
        listOfMoves = []
        for i in range(len(listOfCombinations)):
            move = Move(MoveType.TAKE_ORDER, listOfCombinations[i][0], listOfCombinations[i][1])
            listOfMoves.append(move)
        print(listOfMoves)

        return listOfMoves