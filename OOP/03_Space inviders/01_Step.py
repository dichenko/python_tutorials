"""
Игрок двигается вдоль нижнего края поля, преследуя мышь.
По клику он выпускает ракету.
Ракета долетает до конца экрана и исчезает

ТЗ:
Создать класс Player
Создать класс ROCKET
"""

import pygame
import sys
from step_1_my_classes import *

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")

# Загрузка шрифта
font = pygame.font.Font(None, 36)

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

player = Player(300, 570, 100, 30, BLUE)
rockets = []  # Массив для ракет
cnt = 0

while True:  # Основной цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажал крестик - выходим из игры
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
            if len(rockets) < 3:
                cnt += 1
                mx, my = player.pos[0], player.pos[1]
                rocket = Rocket(mx+(player.width//2), my, 10, 30, BLACK, 5)
                rockets.append(rocket)

     # Создание текстовой поверхности
    text_surface = font.render(f"{cnt}", True, (0, 0, 0))
    # Положение текста на экране
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() // 18, screen.get_height() // 18)

    screen.fill(WHITE)

    screen.blit(text_surface, text_rect)


    for rocket in rockets:
        rocket.update()
        if rocket.pos[1] <= 0:
            rockets.remove(rocket)

    for rocket in rockets:
        rocket.draw(screen)

    player.update(pygame.mouse.get_pos()[0])  # обновляем положение игрока
    player.draw(screen)  # Прорисовывываем ракетку заново
    pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация
