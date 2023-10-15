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
from step_2_my_classes import Alien, Rocket, Player

# Загрузка картинок
BG = pygame.image.load("images/bg1.jpeg")
ALIEN_IMG = pygame.image.load("images/alien_80px.png")
SHEEP = pygame.image.load("images/sheep2.png")

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

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
YELLOW = (255, 255, 0)

player = Player(300, 500, 100, 30, BLUE, SHEEP)
rockets = []  # Массив для ракет
alien = Alien(WIDTH // 2, 100, 1, ALIEN_IMG)
cnt = 0
lives = 3


def update_rockets_pos():
    """обновляет расположение всех ракет"""
    for r in rockets:
        r.update()
        if r.pos[1] <= 0:
            rockets.remove(r)


def set_text(counter):
    """Выводит на экран счетчик"""
    text_surface = font.render(f"{counter}", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() // 18, screen.get_height() // 18)
    screen.blit(text_surface, text_rect)


while True:  # Основной цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажал крестик - выходим из игры
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
            if len(rockets) < 4:
                cnt += 1
                mx, my = player.pos[0], player.pos[1]
                rocket = Rocket(mx + 20, my, 10, 30, YELLOW, 5)
                rockets.append(rocket)

    screen.blit(BG, (0, 0))  # Выводим фон

    set_text(cnt)  # вывод счетчика

    update_rockets_pos()  # обновляем положение всех ракет
    alien.update()

    for rocket in rockets:
        rocket.draw(screen)
    #player_heatbox = SHEEP.get_rect(topleft=(player.pos[0]))
    player.update(pygame.mouse.get_pos()[0])  # обновляем положение корабля
    screen.blit(player.img, player.pos)  # Прорисовывываем корабль на экране
    screen.blit(alien.img, alien.pos)

    pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация
