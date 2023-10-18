"""
Заготовка для игры "Space Invaders"
Корабль игрока двигается вдоль нижнего края поля, следуя за мышкой игрока.
По клику корабль выпускает ракету.
Ракета вылелетает вверх и исчезает, каснувшись края экрана.
ОДновремменно на экране могут существовать не больше 3х ракет

ТЗ:
Создать класс Player (аналог ракетки из Pong)

Создать класс ROCKET (прямоугольник с заданной скоростью)
class Rocket:
    def __init__(self, x, y, width, height, color, speed):
    def update(self):
        #Все время летит вверх
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))
"""

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

player = Player(300, 570, 100, 30, BLUE)
rockets = []  # Массив для ракет

while True:  # Основной цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажал крестик - выходим из игры
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # если нажата левая кнопка мыши
            # Создаем новый обьект ракеты и добавляем его в массив ракет
            pass

    screen.fill(WHITE)

    # TODO Для каждой ракеты обновляем ее положение
    # Если ракета улетела за пределы экрана - удаляем ее из массива

    # TODO Для каждой ракеты рисуем ее заново

    player.update(pygame.mouse.get_pos()[0])  # обновляем положение игрока
    player.draw(screen)  # Прорисовывываем корабль заново

    pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация
