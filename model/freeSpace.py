from sprites.freeSpaceSprite import FreeSpaceSprite

class FreeSpace:

    def __init__(self):
        self.sprite = None

    def create_sprite(self, width, height):
        self.sprite = FreeSpaceSprite(width, height)

    def __repr__(self):
        return "Free Space"