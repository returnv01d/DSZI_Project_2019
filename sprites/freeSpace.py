#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class FreeSpace(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.image.load("images/floor1.png")
        self.rect = self.image.get_rect()

    def update(self):
        print("nothing yet")