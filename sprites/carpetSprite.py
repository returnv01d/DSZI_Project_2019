from sprites.basic_sprite import BasicSprite


class CarpetSprite(BasicSprite):
    def __init__(self, width, height):
        image_path = "images/carpet.png"
        BasicSprite.__init__(self, width, height, image_path)




