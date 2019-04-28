import pygame

class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.width = width
        self.rect.height = height
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y


