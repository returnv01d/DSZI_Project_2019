from sprites.basic_sprite import BasicSprite


class ObstacleSprite(BasicSprite):
    def __init__(self, width, height):
        image_path = "images/flower.png"
        BasicSprite.__init__(self, width, height, image_path)



