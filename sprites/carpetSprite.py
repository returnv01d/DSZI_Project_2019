from sprites.basic_sprite import BasicSprite


class CarpetSprite(BasicSprite):
    def __init__(self, width, height):
        self.image_name = "carpet1.png"
        BasicSprite.__init__(self, width, height, self.image_name)




