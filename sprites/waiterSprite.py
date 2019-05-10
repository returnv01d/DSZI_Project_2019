import pygame

class WaiterSprite(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/waiter_none.png")
        self.rect = self.image.get_rect()

        self.rect.width = width
        self.rect.height = height

        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update_image_waiter(self, number_of_meals):
        if number_of_meals == 0:
            self.image = pygame.image.load("images/waiter_none.png")
        elif number_of_meals == 1:
            self.image = pygame.image.load("images/waiter_one.png")
        elif number_of_meals == 2:
            self.image = pygame.image.load("images/waiter_two.png")

        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))