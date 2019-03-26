#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys


class Table(pygame.sprite.Sprite):
    id = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/table.png")
        self.rect = self.image.get_rect()

        self.id = Table.id
        Table.id += 1
        self.listOfOrders = []
        self.received_orders = []



