from sprites.basic_sprite import BasicSprite

class FreeSpaceSprite(BasicSprite):
    def __init__(self, width, height):
        image_path = "images/floor1.png"
        BasicSprite.__init__(width, height, image_path)

