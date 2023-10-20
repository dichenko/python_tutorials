import pygame


class Alien:
    def __init__(self, x, y, speed, img: list, level):
        self.pos = [x, y]
        self.img = img
        self.speed = speed
        self.level = level
        self.lives = level

    def update(self):
        self.pos[1] = self.pos[1] + self.speed

    def get_image(self):
        return self.img[self.level-1]

    def boom(self):
        if self.lives > 0:
            self.lives -= 1
            return self.lives
        else:
            return  None


class Player:
    def __init__(self, x, y, img):
        self.pos = [x, y]
        self.img = img

    def update(self, x):
        self.pos[0] = x-25


class Rocket:
    def __init__(self, x, y, speed, img):
        self.pos = [x, y]
        self.speed = speed
        self.img = img

    def update(self):
        self.pos[1] = self.pos[1] - self.speed


class Explosion:
    def __init__(self, images: list, coord: tuple):
        self.pos = coord
        self.images = images
        self.counter = 0
        self.freq = 5 # Частота обновления кадров

    def get_image(self):
        '''Первые 10 обращений класс выдает первую картинку, вторые 10 обращений выдает вторую итд'''
        self.counter += 1
        index = self.counter // self.freq
        if index < len(self.images):
            return self.images[index]
        return None


