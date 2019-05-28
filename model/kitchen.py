import itertools

from model.move.move import Move
from model.move.move_type import MoveType
from sprites.kitchenSprite import KitchenSprite


class Kitchen:
    def __init__(self, orders):
        self.sprite = None
        self.orders = orders
        self.given_orders = []
        self.x = None
        self.y = None

    def create_sprite(self, width, height):
        self.sprite = KitchenSprite(width, height)
        self.sprite.update_status(self.statuses())

    def __repr__(self):
        return "Kitchen"

    def __str__(self):
        return 'K'

    def give_order(self, order):
        my_order = [ord for ord in self.orders if ord.id == order.id][0]
        my_order.is_taken_from_kitchen = True

        self.given_orders.append(my_order)
        self.orders.remove(my_order)
        self.update_status()

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
        listOfCombinations = []
        if len(waiter.heldOrders) == 0:
            listOfCombinations = set(list(itertools.combinations(self.orders, min([len(self.orders), 2]))))
        elif len(waiter.heldOrders) == 1:
            listOfCombinations = set(list(itertools.combinations(self.orders, 1)))
        return list(listOfCombinations)

    def get_possible_interactions_with_waiter(self, waiter):
        listOfCombinations = self.get_possible_order_combinations(waiter)
        listOfMoves = []
        for combination in listOfCombinations:
            if (len(combination) == 2):
                new_move = Move(MoveType.TAKE_ORDER, first_order=combination[0], second_order=combination[1])
            else:
                new_move = Move(MoveType.TAKE_ORDER, first_order=combination[0] )
            listOfMoves.append(new_move)

        return listOfMoves

    def update_status(self):
        if self.sprite is not None:
            self.sprite.update_status(self.statuses())


