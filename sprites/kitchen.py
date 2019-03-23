import pygame

class Kitchen(pygame.sprite.Sprite):
    def __init__(self, x, y, window_width, window_height, ready_orders):
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.window_width = window_width
        self.window_height = window_height

        #Set image
        self.image = pygame.image.load("images/kitchen.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ready_orders = ready_orders
