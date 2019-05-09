from sprites.waiterSprite import WaiterSprite

class Waiter:
    def __init__(self):
        self.sprite = None

        self.step = 1
        self.barriers = []
        self.listOfOrders = []
        self.currentOrders = []
        self.x = None
        self.y = None

    def create_sprite(self, width, height):
        self.sprite = WaiterSprite(width, height)

    def add_to_current_orders(self, meal):
        self.currentOrders.append(meal)

    def remove_from_current_orders(self, meal):
        self.currentOrders.remove(meal)

    def update_sprite_position(self, delta_x, delta_y):
        print("{0} self.sprite.rect.x, {1} self.sprite.rect.y".format(self.sprite.rect.x, self.sprite.rect.y))
        self.sprite.rect.x = self.sprite.rect.width * self.y
        self.sprite.rect.y = self.sprite.rect.height * self.x
        print("{0} self.sprite.rect.x, {1} self.sprite.rect.y".format(self.sprite.rect.x, self.sprite.rect.y))


    def __repr__(self):
        return "Waiter"