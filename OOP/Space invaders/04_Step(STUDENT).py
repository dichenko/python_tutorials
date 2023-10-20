"""

ТЗ:

- Создайте картинку для заставки. При старте программы игрок видит заставку и кнопку PLAY
- Каждые 3 секунды появляется новый ряд пришельцев.
- Если любой из пришельцев касается нижней части экрана, игра показывает заставку GAME OVER

"""

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")


def menu():
    # Пока пользователь не кликнет по экрану, показываем заставку
    pass


def game():
    # основная игра
    # работает, пока пользователь не проиграет
    pass


def final():
    # Заставка gameover
    pass


# Вызываем функции по очереди
menu()
game()
final()
