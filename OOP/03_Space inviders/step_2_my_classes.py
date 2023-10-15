import pygame


class Alien:
    def __init__(self, x, y, speed, img):
        self.pos = [x, y]
        self.img = img
        self.speed = speed

    def update(self):
        self.pos[1] = self.pos[1] + self.speed


class Player:
    def __init__(self, x, y, width, height, color, img):
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.color = color
        self.img = img

    def update(self, x):
        self.pos[0] = x - self.width // 2


class Rocket:
    def __init__(self, x, y, width, height, color, speed):
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def update(self):
        self.pos[1] = self.pos[1] - self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))
