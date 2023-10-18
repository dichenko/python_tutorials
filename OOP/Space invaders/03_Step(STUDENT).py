"""

ТЗ:

Создайте ряд пришельцев. Теперь пришельцы не падают вниз, а шагают вниз раз в 1 сек

Когда ракета попадает в пришельца они уничтожаются со взрывом. Добавьте звук и картинку взрыва.

Счетчик считает количество сбитих пришельцев.

"""

import pygame
import sys
from step_3_my_classes import Alien, Rocket, Player


# Загрузка картинок
BG = pygame.image.load("images/bg1.jpeg")
ALIEN_IMG = pygame.image.load("images/alien_80px.png")
SHEEP_IMG = pygame.image.load("images/sheep2.png")
ROCKET_IMG = pygame.image.load("images/Missile05_30x24.png")
EXPLODE_IMG = pygame.image.load("images/explosion_80.png")

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
explosion = pygame.mixer.Sound('sounds/explosion01.wav')

player = Player(300, 500, SHEEP_IMG)
rockets = []  # Массив для ракет
aliens = [ ] # Массив для пришельцев
cnt = 0  # Счетчик сбитых пришельцев

# Создаем событие для движения пришельцев каждую секунду
ALIEN_STEP = pygame.USEREVENT + 1
# Установим таймер который будет вызывать событие каждую секунду (1000 миллисекунд)
pygame.time.set_timer(ALIEN_STEP, 1000)


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
                mx, my = player.pos[0], player.pos[1]
                rocket = Rocket(mx + 20, my, 5, ROCKET_IMG)
                rockets.append(rocket)
                launch.play()
        elif event.type == ALIEN_STEP:  # Если сработало событие по таймеру ALIEN_STEP
            # print("Событие по таймеру сработало!")
            # обновляем положение пришельцев


    screen.blit(BG, (0, 0))  # Выводим фон

    set_text(cnt)  # вывод счетчика

    update_rockets_pos()  # обновляем положение всех ракет

    for rocket in rockets: # Рисуем все ракеты
        screen.blit(rocket.img, rocket.pos)

    player.update(pygame.mouse.get_pos()[0])  # обновляем положение корабля
    screen.blit(player.img, player.pos)  # Прорисовывываем корабль на экране

    # Создаем хитбоксы для всех пришельцев
    alien_heatboxes = [al.img.get_rect(topleft=(al.pos[0], al.pos[1])) for al in aliens]
    # Создаем хитбоксы для всех ракет
    rocket_heatboxes = [ro.img.get_rect(topleft=(ro.pos[0], ro.pos[1])) for ro in rockets]

    # Ищем, есть ли столкновения
    # if alien_heatbox.colliderect(rocket_heatbox):
    #   print("Сбил!")

    for al in aliens:
        screen.blit(al.img, al.pos)

    pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
    pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация
