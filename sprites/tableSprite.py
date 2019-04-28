from sprites.basic_sprite import BasicSprite


class TableSprite(BasicSprite):
    def __init__(self, width, height):
        image_path = "images/table.png"
        BasicSprite.__init__(self, width, height, image_path)





