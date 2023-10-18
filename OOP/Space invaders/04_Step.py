"""

ТЗ:

Создайте картинку для заставки. При старте программы игрок видит заставку и кнопку PLAY
Каждые 3 секунды появляется новый ряд пришельцев.
Если любой из пришельцев касается нижней части экрана, игра показывает заставку GAME OVER
"""

import pygame
import sys
from step_4_my_classes import Alien, Rocket, Player
from app.images import load_images

# Загрузка картинок
START_BG_IMG, BG_IMG, ALIEN_IMG, SHEEP_IMG, ROCKET_IMG, EXPLODE_IMG, GAMEOVER_IMG = load_images()

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")


def menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если пользователь нажал крестик - выходим из игры
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        screen.blit(START_BG_IMG, (0, 0))  # Выводим фон
        pygame.display.flip()  # Чтобы все изменения стали видны, нужно update игровой экран
        pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация


def game():
    # Загрузка звуков
    launch = pygame.mixer.Sound('sounds/whoosh1.wav')
    launch.set_volume(0.05)
    explosion = pygame.mixer.Sound('sounds/explosion01.wav')
    launch.set_volume(0.5)

    #  Создаем обьекты
    player = Player(300, 500, SHEEP_IMG)
    rockets = []  # Массив для ракет
    aliens = [Alien(x, -50, 20, ALIEN_IMG) for x in range(10, WIDTH, WIDTH // 8)]
    cnt = 0  # Счетчик сбитых пришельцев

    # Создаем событие для движения пришельцев каждую секунду
    ALIEN_STEP = pygame.USEREVENT + 1
    # Установим таймер который будет вызывать событие каждую секунду (1000 миллисекунд)
    pygame.time.set_timer(ALIEN_STEP, 1000)

    # Создаем событие для появления нового ряда пришельцев каждые 3 сек
    ALIEN_ROW = pygame.USEREVENT + 2
    # Установим таймер который будет вызывать событие каждые 3 секунды
    pygame.time.set_timer(ALIEN_ROW, 3000)

    # Загрузка фоновой музыки
    pygame.mixer.music.load('sounds/theme.mp3')
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play(-1)

    def set_text(counter):
        """Выводит на экран счетчик"""
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"{counter}", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen.get_width() // 18, screen.get_height() // 18)
        screen.blit(text_surface, text_rect)

    def update_rockets_pos():
        """обновляет расположение всех ракет"""
        for r in rockets:
            r.update()
            if r.pos[1] <= 0:
                rockets.remove(r)

    # Основной игровой цикл
    running = True
    while running:
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
                for al in aliens:  # обновляем положение пришельцев
                    al.update()
                    if al.pos[1] > 500:
                        running = False
            elif event.type == ALIEN_ROW:  # Если пришло время добавить ряд пришельцев
                aliens += [Alien(x, -50, 20, ALIEN_IMG) for x in range(10, WIDTH, WIDTH // 8)]

        screen.blit(BG_IMG, (0, 0))  # Выводим фон

        set_text(cnt)  # вывод счетчика

        update_rockets_pos()  # обновляем положение всех ракет

        for rocket in rockets:
            screen.blit(rocket.img, rocket.pos)

        player.update(pygame.mouse.get_pos()[0])  # обновляем положение корабля
        screen.blit(player.img, player.pos)  # Прорисовывываем корабль на экране

        # Создаем хитбоксы для всех пришельцев
        alien_heatboxes = [al.img.get_rect(topleft=(al.pos[0], al.pos[1])) for al in aliens]
        # Создаем хитбоксы для всех ракет
        rocket_heatboxes = [ro.img.get_rect(topleft=(ro.pos[0], ro.pos[1])) for ro in rockets]

        # Ищем, есть ли столкновения ракет с пришельцами
        for al in alien_heatboxes:
            for ro in rocket_heatboxes:
                if al.colliderect(ro):
                    explosion.play()
                    screen.blit(EXPLODE_IMG, aliens[alien_heatboxes.index(al)].pos)
                    aliens.pop(alien_heatboxes.index(al))
                    rockets.pop(rocket_heatboxes.index(ro))
                    cnt += 1

        for al in aliens:
            screen.blit(al.img, al.pos)

        pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
        pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация


def final():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если пользователь нажал крестик - выходим из игры
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        screen.blit(GAMEOVER_IMG, (0, 0))  # Выводим фон
        pygame.display.flip()  # Чтобы все изменения стали видны, нужно update игровой экран
        pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация


menu()
game()
final()
