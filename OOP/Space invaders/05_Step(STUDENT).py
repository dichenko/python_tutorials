"""

ТЗ:

- Добавить анимированный взрыв пришельца
- После 30 сбитых кораблей пришельцы меняют картинку. Теперь, чтобы сбить усиленного пришельца, требуется 2 попадания.
- Результат игры выводится на экран GameOver
- Игра хранит лучший результат и всегда показывает его на заставке Game Over:
    Твой результат: 56
    Лучший результат: 120
"""

import pygame
import sys
from step_5_my_classes import Alien, Rocket, Player, Explosion
from app.images import load_images, load_explosion_images

# Загрузка картинок


# Где храним лучший результат игры?


# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")

cnt = 0  # Счетчик сбитых пришельцев


def menu():
    pass

def game():
    # Загрузка звуков и фоновой музыки
    #  Создаем обьекты и списки обьектов
    # Создаем события и таймеры
    # Основной игровой цикл
    pass

def final():
    # Финальная заставка с рекордами



menu()
game()
final()
