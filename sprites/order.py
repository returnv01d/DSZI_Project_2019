import pygame

class Order(pygame.sprite.Sprite):
    def __init__(self, table_id, order_name):
        pygame.sprite.Sprite.__init__(self)

        self.table_id = table_id
        self.order_name = order_name
        self.is_delivered = False