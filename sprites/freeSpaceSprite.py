from sprites.basic_sprite import BasicSprite


class FreeSpaceSprite(BasicSprite):
    def __init__(self, width, height):
        self.image_name = "floor1.png"
        BasicSprite.__init__(self, width, height, self.image_name)



