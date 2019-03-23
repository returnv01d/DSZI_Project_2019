import pygame

class Waiter(pygame.sprite.Sprite):
    def __init__(self, x, y, window_width, window_height):
        pygame.sprite.Sprite.__init__(self)

        self.window_width = window_width
        self.window_height = window_height

        # Set height, width
        self.image = pygame.image.load("images/waiter.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
