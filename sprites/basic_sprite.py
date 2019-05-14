import pygame
from PIL import Image,ImageDraw


class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, image_name):
        pygame.sprite.Sprite.__init__(self)
        self.image_name = image_name
        self.image = pygame.image.load("images/" + image_name)
        self.rect = self.image.get_rect()

        self.rect.width = width
        self.rect.height = height
        self.image = pygame.transform.scale(self.image, (width, height))
        pygame.image.save(self.image, "images/_temporary_" + self.image_name)
        self.update_status()

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update_status(self):
        image = Image.open("images/_temporary_" + self.image_name)
        draw = ImageDraw.Draw(image)
        draw.text((7, 7), str(self.status()))
        mode, size, data = image.mode, image.size, image.tobytes()

        self.image = pygame.image.frombuffer(data, size, mode)


    def status(self):
        return ""

