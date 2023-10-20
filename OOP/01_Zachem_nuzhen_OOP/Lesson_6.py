"""
Зачем нужно ООП?

Поздравляю, мы подобрались к самой сути ООП.
В прошлой программе мы хранили информацию про каждый мяч в словаре.
К сожалению, словарь может хранить только данные, а наши мячики должны выполнять действия,
например, обновлять свои координаты и прорисовывать себя на экране.

Сейчас вместо словаря мы создадим класс Ball и перенесем в него все данные и функции нашего мячика
- Изучите класс Ball
- Доработайте класс Ball, чтобы солкновения со стенами отрабатывались точнее.
- Реализуйте добавление новых мячей по клику. Новые мячики должны появляться в той точке, где кликнул пользователь
pygame.mouse.get_pos() возвращает кортеж с координатами клика
- Каждый новый мяч должен иметь случайный цвет из набора 10 цветов.

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


class Ball:  # Класс - это просто схема, которая описывает устройство какого-то обьекта, например, мяча.
    def __init__(self, x, y, r, speed, color):
        """Функцию внутри класса называют 'Метод' Данный метод называется 'конструктор'. Он выполняется в тот момент,
        когда мы создаем новый мяч (обьект класса)"""
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.color = color

    def update(self):
        """Этот метод будет обновлять координаты мяча и менять направление,
        если он столкнулся со стеной"""
        self.x += self.speed[0]
        self.y += self.speed[1]

        if self.x > WIDTH or self.x < 0:
            self.speed[0] = -self.speed[0]
        if self.y > HEIGHT or self.y < 0:
            self.speed[1] = -self.speed[1]

    def drow(self, screen):
        """Этот метод прорисовывает мяч на экране"""
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.r)



# С помощью класса мы описали, как должен выглядеть любой мяч и что он должен уметь.
# Теперь мы создадим наш первый мяч - обьект.
my_ball = Ball(400, 300, 20, [2,-3], RED)


# Готово! Запускаем игру
while True:
    # Если пользователь нажал крестик - выходим из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Заливаем фон белым цветом
    screen.fill(WHITE)

    # Обновим координаты мяча
    my_ball.update()

    # Рисуем мяч на экране
    my_ball.drow(screen)

    pygame.display.flip()  # Магическая команда
    pygame.time.delay(10)  # Магическая команда