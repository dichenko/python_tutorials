import pygame


class Alien:
    def __init__(self, x, y, speed, img):
        self.pos = [x, y]
        self.img = img
        self.speed = speed

    def update(self):
        self.pos[1] = self.pos[1] + self.speed


class Player:
    def __init__(self, x, y, color, img):
        self.pos = [x, y]
        self.color = color
        self.img = img

    def update(self, x):
        self.pos[0] = x-25


class Rocket:
    def __init__(self, x, y, color, speed, img):
        self.pos = [x, y]
        self.color = color
        self.speed = speed
        self.img = img

    def update(self):
        self.pos[1] = self.pos[1] - self.speed

