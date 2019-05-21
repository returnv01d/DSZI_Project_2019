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

    def remove_from_current_orders(self, meal):
        self.heldOrders.remove(meal)

    def update_sprite_position(self, delta_x, delta_y):
        self.sprite.rect.x = self.sprite.rect.width * self.y
        self.sprite.rect.y = self.sprite.rect.height * self.x

    def __repr__(self):
        return "Waiter"

    def status(self):
        status = ["Current orders: "]
        if len(self.heldOrders) == 0:
            status.append("None")
            return status


    def put_order_on_the_table(self, idOrder):
        if len(self.heldOrders) != 0:
            #self.remove_from_current_orders(kitchen.Kitchen.orders[idOrder]) -- nie widzi kitchen
            self.remove_from_current_orders(idOrder) #usuwa samo idOrder, zamiast obiekt Order o takim id



    def get_order_from_kitchen(self, idOrder):
        #self.add_to_current_orders(kitchen.Kitchen.orders[idOrder]) -- nie widzi kitchen
        self.add_to_current_orders(idOrder) #dodaje samo idOrder, zamiast obiekt Order o takim id
