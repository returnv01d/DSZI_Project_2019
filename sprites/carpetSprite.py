from sprites.basic_sprite import BasicSprite


class CarpetSprite(BasicSprite):
    def __init__(self, width, height):
        self.image_name = "carpet.png"
        BasicSprite.__init__(self, width, height, self.image_name)




