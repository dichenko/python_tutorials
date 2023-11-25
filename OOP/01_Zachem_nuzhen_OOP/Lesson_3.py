"""
Зачем нужно ООП?

Todo: допиши программу, чтобы мяч мог отскакивать от стен.

"""
# Импортируем библиотеку Pygame
import pygame

# Используем магическую команду
pygame.init()

# Задаем две константы - размеры окна с игрой
WIDTH, HEIGHT = 800, 600

# И создадим картинку на экране - screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Мяч будет красным, а экран - белым. Создадим две константы,
# которые будут хранить нужные нам цвета в формате RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Наш мяч - это просто круг.
# У него есть цвет, радиус, начальные координаты, на которых он появляется,
# и скорость, с которой он движется. Сохраним все эти данные в переменные.
ball_color = RED
ball_r = 20
ball_x = 400
ball_y = 300
ball_speed = 2

# Дальше идет основной игровой цикл, он работает пока не нажмешь не закроешь окно
while True:
    # Если пользователь нажал крестик - выходим из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Заливаем фон белым цветом
    screen.fill(WHITE)

    # Изменим координаты мяча
    ball_x += ball_speed

    if ball_x > WIDTH:
        ball_speed = -ball_speed

    # Рисуем круг с нужными характеристиками
    pygame.draw.circle(screen, ball_color, [ball_x, ball_y], ball_r)

    pygame.display.flip()  # Магическая команда
    pygame.time.delay(10)  # Магическая команда
