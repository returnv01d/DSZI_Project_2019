#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/flower.png")
        self.rect = self.image.get_rect()
