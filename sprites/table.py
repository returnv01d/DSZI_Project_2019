#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys


class Table(pygame.sprite.Sprite):
    def __init__(self, x, y, id, listOfOrders, recived_orders):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/table.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = id
        
        self.listOfOrders = []
        self.recived_orders = []



