from sprites.waiterSprite import WaiterSprite

class Waiter:
    def __init__(self):
        self.sprite = None

        self.step = 1
        self.barriers = []
        self.listOfOrders = []
        self.currentOrders = []

    def create_sprite(self, width, height):
        self.sprite = WaiterSprite(width, height)

    def addToCurrentOrders(self, meal):
        self.currentOrders.append(meal)


    def removeFromCurrentOrders(self, meal):
        self.currentOrders.remove(meal)

    def __repr__(self):
        return "Waiter"