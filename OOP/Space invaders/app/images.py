import pygame


def load_images():
    BG_IMG = pygame.image.load("images/bg1.jpeg")
    ALIEN_IMG = pygame.image.load("images/alien_80px.png")
    SHEEP_IMG = pygame.image.load("images/sheep2.png")
    ROCKET_IMG = pygame.image.load("images/Missile05_30x24.png")
    EXPLODE_IMG = pygame.image.load("images/explosion_80.png")
    START_BG_IMG = pygame.image.load('images/start_bg.jpeg')
    GAMEOVER_IMG = pygame.image.load('images/gameover.jpeg')
    return START_BG_IMG, BG_IMG, ALIEN_IMG, SHEEP_IMG, ROCKET_IMG, EXPLODE_IMG, GAMEOVER_IMG
