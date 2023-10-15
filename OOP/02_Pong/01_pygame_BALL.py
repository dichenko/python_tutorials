"""Заготовка для игры PONG
Создаем мячик, который летает по экрану и отскакивает от стен.

ТЗ: доработать класс Ball

Класс Ball:
Инициализация:
- текущие координаты мяча по Х(int) и по Y(int)
- скорость мяча [по Х(int),  по Y(int)]
- радиус мячика, int
- цвет (кортеж RGB)
Метод update()
(Вычисляет новую координату мяча с учетом скорости.  Проверяет, не коснулся ли мяч стенки. Если да - меняет скорость на противоположную)
Метод draw()
(Рисует шарик на новых координатах)
"""


import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball with Paddle")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.pos = [x, y]
        self.radius = radius
        self.speed = speed
        self.color = color

    def update(self):
        pass
        # Обновить координаты мяча,в зависимости от скорости

        # Если мяч столкнулся с боковой стенкой - изменить скорость по X на противоположную по знаку

        # Если мяч столкнулся с верхней или нижней стенкой - изменить скорость по Y на противоположную по знаку

    def draw(self, screen): # Отрисовать мячик на экране
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


# Создаем обьект мячика
ball = Ball(400, 300, 20, [2, 2], RED)


while True: # Основной цикл игры
    for event in pygame.event.get(): #Если пользователь нажал крестик - выходим из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.update() # обновляем координаты мяча
    screen.fill(WHITE) # заполняем фон
    ball.draw(screen) # Прорисовывываем мяч заново
    pygame.display.flip() # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(10) # Задержка в мс, влияет на плавность анимации. Чем больше задержка, тем хуже анимация