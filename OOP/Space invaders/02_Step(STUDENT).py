"""
ТЗ:
Создать класс Alien
(Пришелец летит сверху вниз, достигнув края исчезает)
Создать изображения для корабля, ракеты, пришельца
Создать фон
Добавить фоновую музыку и звуки запуска ракет
https://opengameart.org/

"""

import pygame
import sys

# Чтобы сделать программу компактнее, перенесем классы в другой файл
from my_classes import Alien, Rocket, Player

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")

# Загрузка фоновой музыки
pygame.mixer.music.load('sounds/theme.mp3')
# Создаем событие "Музыка закончилась"
pygame.mixer.music.set_endevent(pygame.USEREVENT)
# играть фоновую музыку бесконечно
pygame.mixer.music.play(-1)

# Загрузка картинок
BG_IMG = pygame.image.load("images/bg1.jpeg")
ALIEN_IMG = pygame.image.load("images/alien.png")
SHEEP_IMG = pygame.image.load("images/sheep.png")
ROCKET_IMG = pygame.image.load("images/missile.png")

# Загрузка звуков
launch = pygame.mixer.Sound('sounds/whoosh1.wav')
launch.set_volume(0.5)


class Player:
    def __init__(self, x, y, img):
        self.pos = [x, y]
        self.img = img

    def update(self, x):
        self.pos[0] = x - 25


player = Player(300, 500, SHEEP_IMG)
rockets = []  # Массив для ракет
alien = Alien(300, 100, 1, ALIEN_IMG)



while True:  # Основной цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажал крестик - выходим из игры
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
            pass  # Создаем новую ракету

     # обновляем положение всех ракет

    # обновляем положение пришельца

    # Прорисовываем все ракеты

    player.update(pygame.mouse.get_pos()[0])  # обновляем положение корабля
    screen.blit(player.img, player.pos)  # Прорисовывываем корабль на экране

    pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация
