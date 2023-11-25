"""
Зачем нужно ООП?

Пока мячиков было мало, никаких проблем у нас не возникало.

А теперь задача стоит так:
Каждый раз, когда пользователь кликает по экрану, на этом месте появляется новый мячик и начинает летать по экрану.
Мячиков может быть сколько угодно.

Мы все еще ничего не знаем про ООП, поэтому данные каждого мячика нужно будет хранить в словаре.

"""
# Импортируем библиотеку Pygame
import pygame

# Используем магическую команду
pygame.init()

# размеры окна с игрой
WIDTH, HEIGHT = 800, 600

# И создадим картинку на экране - screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

ball_1 = {"color": RED,
          "r": 20,
          "x": 400,
          "y": 300,
          "speed": [2, 3]}

ball_2 = {"color": BLUE,
          "r": 20,
          "x": 400,
          "y": 300,
          "speed": [-1, 3]}

# В этом списке будут храниться словари для всех мячиков
balls = [ball_1, ball_2]

# Дальше идет основной игровой цикл, он работает пока не нажмешь не закроешь окно
while True:
    # Если пользователь нажал крестик - выходим из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif pygame.event == pygame.MOUSEBUTTONDOWN:  # Если пользователь кликнул мышкой по экрану
            pass  # Нужно создать новый мячик и добавить его в массив к остальным мячикам

    # Заливаем фон белым цветом
    screen.fill(WHITE)

    # Обновим координаты мячей
    for ball in balls:
        ball["x"] += ball["speed"][0]
        ball["y"] += ball["speed"][1]

    # Если мяч столкнулся со стеной - отскок
    for ball in balls:
        if ball["x"] > WIDTH or ball["x"] < 0:
            ball["speed"][0] = -ball["speed"][0]
        if ball["y"] > HEIGHT or ball["y"] < 0:
            ball["speed"][1] = -ball["speed"][1]

    # Рисуем круги с нужными характеристиками
    for ball in balls:
        pygame.draw.circle(screen, ball["color"], [ball['x'], ball["y"]], ball['r'])

    pygame.display.flip()  # Магическая команда
    pygame.time.delay(10)  # Магическая команда
