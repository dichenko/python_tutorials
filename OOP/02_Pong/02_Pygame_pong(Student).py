"""Игра Pong

Создаем игру, где мячик летает по экрану, игрок должен отбить мяч ракеткой. Ракетка следует за мышкой пользователя.

Класс Paddle:
Инициализация:
- текущие координаты ракетки по Х(int) и по Y(int)
- длина и ширина прямоугольника (int, int)
- цвет (кортеж RGB)
Метод update(x: int)
принимает координату Х от мышки и обновляет свои координаты на новые
Метод draw()
(Рисует ракетку на новых координатах)
Метод collide(ball)
Принимает обьект мяча, проверяет его координаты, и возвращает True, если мяч коснулся ракетки. Иначе False.


Добавить звуки столкновения мяча с ракеткой и со стенками
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
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= WIDTH:
            self.speed[0] = -self.speed[0]
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= HEIGHT:
            self.speed[1] = -self.speed[1]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


class Paddle:
    pass


ball = Ball(WIDTH // 2, HEIGHT // 2, 20, [2, 2], RED)
# <-----Создаем обьект ракетки


while True: # Основной цикл игры
    for event in pygame.event.get(): #Если пользователь нажал крестик - выходим из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.update() # обновляем положение мяча

    if paddle.collide(ball): # проверяем, что мяч коснулся ракетки
        pass #меняем направление мяча

    # обновляем положение ракетки pygame.mouse.get_pos()[0]

    screen.fill(WHITE)
    ball.draw(screen) # Прорисовывываем мяч заново
    # <-----------------Прорисовывываем ракетку заново
    pygame.display.flip() # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(15) # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация