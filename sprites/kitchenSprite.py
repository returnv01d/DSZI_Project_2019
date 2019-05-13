from sprites.basic_sprite import BasicSprite


class KitchenSprite(BasicSprite):
    def __init__(self, width, height):
        self.image_name = "kitchen4.png"
        BasicSprite.__init__(self, width, height, self.image_name)



