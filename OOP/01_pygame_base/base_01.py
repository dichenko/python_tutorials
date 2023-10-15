"""На экране появляется мячик и движется в право
ТЗ
1) Изменить класс Ball так чтобы мячик мог лететь в любом направлении
2) Игра заканчивается, когда шарик касается края эрана

"""

import pygame
import sys

# Инициализация Pygame (заклинание)
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Заголовок окна
pygame.display.set_caption("Ball 01")

# Константы с цветами
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Ball:
    def __init__(self, x: int, y: int, radius: int, speed:int, color: tuple):
        self.pos = [x, y]
        self.radius = radius
        self.speed = speed
        self.color = color

    def update(self):
        """Расчитывает новые координаты мяча в зависимости от его скорости"""
        self.pos[0] += self.speed

    def draw(self, screen):
        """Рисует мяч на экране"""
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


ball = Ball(50, 300, 20, 1, RED) # Создаем обьект мячик

while True:  # Основной цикл игры
    for event in pygame.event.get():  # Проверяем все события в игровом цикле
        if event.type == pygame.QUIT: # Если пользователь нажал крестик - выходим из игры
            pygame.quit()
            sys.exit()

    ball.update()  # обновляем положение мяча
    screen.fill(WHITE) # Заливаем экран белой краской
    ball.draw(screen)  # Прорисовывываем мяч заново
    pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран (заклинание)
    pygame.time.delay(15)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация (заклинание)
