from sprites.waiterSprite import WaiterSprite

class Waiter:
    def __init__(self):
        self.sprite = None

        self.step = 1
        self.barriers = []
        self.heldOrders = []
        self.x = None
        self.y = None

    def create_sprite(self, width, height):
        self.sprite = WaiterSprite(width, height)
        self.sprite.update_status(self.status())

    def add_to_current_orders(self, meal):
        self.heldOrders.append(meal)

    def update_sprite_position(self):
        self.sprite.rect.x = self.sprite.rect.width * self.y
        self.sprite.rect.y = self.sprite.rect.height * self.x

    def __repr__(self):
        return f"|Waiter ordersCount:{len(self.heldOrders)}"

    def num(self):
        return 4

    def give_order(self, order):
        my_order = [ord for ord in self.heldOrders if ord.table_id == order.table_id and ord.name == order.name][0]
        self.heldOrders.remove(my_order)
        self.update_status()

    def take_order(self, order):
        self.heldOrders.append(order)
        self.update_status()

    def status(self):
        status = ["Current orders: "]
        if len(self.heldOrders) == 0:
            status.append("None")
            return status
        else:
            for order in self.heldOrders:
                status.append(repr(order))
            return status

    def update_status(self):
        if self.sprite is not None:
            if len(self.heldOrders) == 0:
                self.sprite.update_image_waiter(0)
            if len(self.heldOrders) == 1:
                self.sprite.update_image_waiter(1)
            if len(self.heldOrders) == 2:
                self.sprite.update_image_waiter(2)

            self.sprite.update_status(self.status())
            self.update_sprite_position()