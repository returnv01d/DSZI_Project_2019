from sprites.basic_sprite import BasicSprite
import pygame

class WaiterSprite(BasicSprite):
    def __init__(self, width, height):
        image_name = "waiter_none.png"
        BasicSprite.__init__(self, width, height, image_name)


    def update_image_waiter(self, number_of_meals):
        if number_of_meals == 0:
            self.image = pygame.image.load("images/waiter_none.png")
        elif number_of_meals == 1:
            self.image = pygame.image.load("images/waiter_one.png")
        elif number_of_meals == 2:
            self.image = pygame.image.load("images/waiter_two.png")

        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

