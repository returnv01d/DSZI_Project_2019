from sprites.basic_sprite import BasicSprite
import pygame

class TableSprite(BasicSprite):
    def __init__(self, width, height):
        image_path = "images/table2.png"
        BasicSprite.__init__(self, width, height, image_path)

    def update_image(self):
        self.image = pygame.image.load("images/table3.png")
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
