"""

ТЗ:

Создать класс Alien
Пришелец летит сверху вниз, достигнув края исчезает


Создать изображения для корабля, ракеты, пришельца
Создать фон

Добавить фоновую музыку и звуки запуска ракет



"""

import pygame
import sys
from step_2_my_classes import Alien, Rocket, Player

# Загрузка картинок
BG = pygame.image.load("images/bg1.jpeg")
ALIEN_IMG = pygame.image.load("images/alien_80px.png")
SHEEP = pygame.image.load("images/sheep2.png")
ROCKET_IMG = pygame.image.load("images/Missile05_30x24.png")




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

# Загрузка фоновой музыки
pygame.mixer.music.load('sounds/theme.mp3')
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play(-1)

# Загрузка звуков
launch = pygame.mixer.Sound('sounds/whoosh1.wav')
launch.set_volume(0.5)

player = Player(300, 500, BLUE, SHEEP)
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
                rocket = Rocket(mx + 20, my, YELLOW, 5, ROCKET_IMG)
                rockets.append(rocket)
                launch.play()


    screen.blit(BG, (0, 0))  # Выводим фон

    set_text(cnt)  # вывод счетчика

    update_rockets_pos()  # обновляем положение всех ракет

    alien.update() #обновляем положение пришельцев

    for rocket in rockets:
        screen.blit(rocket.img, rocket.pos)

    #alien_heatbox = ALIEN_IMG.get_rect(topleft=(alien.pos[0], alien.pos[1]))
    #rocket.heatbox = ...
    #if alien_heatbox.colliderect(rocket_heatbox):
    #   print("Сбил!")



    player.update(pygame.mouse.get_pos()[0])  # обновляем положение корабля
    screen.blit(player.img, player.pos)  # Прорисовывываем корабль на экране
    screen.blit(alien.img, alien.pos)

    pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация
