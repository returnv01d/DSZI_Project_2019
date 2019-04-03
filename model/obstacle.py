from sprites.obstacleSprite import ObstacleSprite

class Obstacle:

    def __init__(self):
        self.sprite = None

    def create_sprite(self, width, height):
        self.sprite = ObstacleSprite(width, height)

    def __repr__(self):
        return "Waiter"
