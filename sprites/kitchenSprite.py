from sprites.basic_sprite import BasicSprite


class KitchenSprite(BasicSprite):
    def __init__(self, width, height):
        image_path = "images/kitchen.png"
        BasicSprite.__init__(width, height, image_path)


