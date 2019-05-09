import pygame

class FreeSpaceSprite(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/Empty.png")
        self.rect = self.image.get_rect()

        self.rect.width = width
        self.rect.height = height

        self.image = pygame.transform.scale(self.image, (width, height))



    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y


