#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Waiter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        # Set height, width
        self.image = pygame.image.load("images/waiter.png")

        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()

        self.step = 1
        self.barriers = []
        self.listOfOrders = []
        self.currentOrders = []

    def addToCurrentOrders(self, meal):
        self.currentOrders.append(meal)
        
    def removeFromCurrentOrders(self, meal):
        self.currentOrders.remove(meal)

    def move_right(self):
        if self.rect.x + self.rect.width + self.step <= self.window_width:
            self.rect.x += self.step
            collision = False
            for barrier in self.barriers:
                if self.rect.colliderect(barrier.rect):
                    self.rect.x -= self.step
                    collision = True
                    break
            if collision:
                print("collision!")
            else:
                print("no collision")

    def move_left(self):
        if self.rect.x >= self.step:
            self.rect.x -= self.step
            collision = False
            for barrier in self.barriers:
                if self.rect.colliderect(barrier.rect):
                    self.rect.x += self.step
                    collision = True
                    break
            if collision:
                print("collision!")
            else:
                print("no collision")

    def move_down(self):
        if self.rect.y + self.rect.height + self.step <= self.window_height:
            self.rect.y += self.step
            collision = False
            for barrier in self.barriers:
                if self.rect.colliderect(barrier.rect):
                    self.rect.y -= self.step
                    collision = True
                    break
            if collision:
                print("collision!")
            else:
                print("no collision")

    def move_up(self):
        if self.rect.y >= self.step:
            self.rect.y -= self.step
            collision = False
            for barrier in self.barriers:
                if self.rect.colliderect(barrier.rect):
                    self.rect.y += self.step
                    collision = True
                    break
            if collision:
                print("collision!")
            else:
                print("no collision")

    def reset(self):
        self.rect.x = 0
        self.rect.y = 0