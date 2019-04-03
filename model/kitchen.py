from sprites.kitchenSprite import KitchenSprite

class Kitchen:
    def __init__(self):
        self.sprite = None

    def create_sprite(self, width, height):
        self.sprite = KitchenSprite(width, height)

    def __repr__(self):
        return "Kitchen"