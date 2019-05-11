from sprites.carpetSprite import CarpetSprite

class Carpet:

    def __init__(self):
        self.sprite = None

    def create_sprite(self, width, height):
        self.sprite = CarpetSprite(width, height)

    def __repr__(self):
        return "Carpet"

    def __str__(self):
        return "C"