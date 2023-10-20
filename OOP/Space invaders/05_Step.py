"""

ТЗ:

- Добавить анимированный взрыв пришельца
- После 30 сбитых кораблей пришельцы меняют картинку. Теперь, чтобы сбить усиленного пришельца, требуется 2 попадания.
- Результат игры выводится на экран GameOver
- Игра хранит лучший результат и всегда показывает его на заставке Game Over:
    Твой результат: 56
    Лучший результат: 120
"""

import pygame
import sys
from step_5_my_classes import Alien, Rocket, Player, Explosion
from app.images import load_images, load_explosion_images

# Загрузка картинок
START_BG_IMG, BG_IMG, ALIEN1_IMG, ALIEN2_IMG, SHIP_IMG, ROCKET_IMG, EXPLODE_IMG, GAMEOVER_IMG = load_images()
explode_images = load_explosion_images()

SCORE_PATH = 'saves/score.txt'

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")

cnt = 0  # Счетчик сбитых пришельцев


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
    player = Player(300, 500, SHIP_IMG)
    rockets = []  # Массив для ракет
    alien_images = [ALIEN1_IMG, ALIEN2_IMG]
    level = 1
    aliens_list = [Alien(x, -50, 20, alien_images, level) for x in range(10, WIDTH, WIDTH // 8)]

    explosions_list = []

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

    def drow_rockets():
        for rocket in rockets:
            screen.blit(rocket.img, rocket.pos)

    def check_explode():
        global cnt
        # Создаем хитбоксы для всех пришельцев
        alien_heatboxes = [al.get_image().get_rect(topleft=(al.pos[0], al.pos[1])) for al in aliens_list]
        # Создаем хитбоксы для всех ракет
        rocket_heatboxes = [ro.img.get_rect(topleft=(ro.pos[0], ro.pos[1])) for ro in rockets]

        # Ищем, есть ли столкновения ракет с пришельцами
        for al in alien_heatboxes:
            for ro in rocket_heatboxes:
                if al.colliderect(ro):
                    explosion.play()
                    ### Создаем обьект взрыва
                    x = ro.x
                    y = ro.y
                    explosions_list.append(Explosion(explode_images, (x - 50, y - 50)))
                    ### Создали

                    # Удаляем ракету и пришельца
                    lives = aliens_list[alien_heatboxes.index(al)].boom()
                    if not lives:
                        aliens_list.pop(alien_heatboxes.index(al))
                        cnt += 1
                    rockets.pop(rocket_heatboxes.index(ro))


    def drow_explosions():
        for explo in explosions_list:
            img = explo.get_image()
            if img:
                screen.blit(img, explo.pos)
            else:
                explosions_list.remove(explo)

    def drow_aliens_list():
        for al in aliens_list:
            screen.blit(al.get_image(), al.pos)

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
                for al in aliens_list:  # обновляем положение пришельцев
                    al.update()
                    if al.pos[1] > 500:
                        running = False
            elif event.type == ALIEN_ROW:  # Если пришло время добавить ряд пришельцев
                if cnt > 40:
                    level = 2
                aliens_list += [Alien(x, -50, 20, alien_images, level) for x in range(10, WIDTH, WIDTH // 8)]

        screen.blit(BG_IMG, (0, 0))  # Выводим фон

        drow_explosions()  # Рисуем все взрывы

        update_rockets_pos()  # обновляем положение всех ракет

        drow_rockets()  # Рисуем ракеты

        player.update(pygame.mouse.get_pos()[0])  # обновляем положение корабля
        screen.blit(player.img, player.pos)  # Прорисовывываем корабль на экране

        check_explode()  # Проверяем сбитых пришельцев

        drow_aliens_list()

        set_text(cnt)  # вывод счетчика

        pygame.display.flip()  # Чтобы все изменения стали видны, нужно флипнуть игровой экран
        pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация


def final():
    def set_text(counter, best_score):
        """Выводит на экран счетчик"""
        font = pygame.font.Font(None, 36)
        text_surface1 = font.render(f"Your score: {counter} ", True, (255, 255, 255))
        text_surface2 = font.render(f" Best score: {best_score}", True, (255, 255, 255))
        rect_surface2 = pygame.Surface((250, 110))
        rect_surface1 = pygame.Surface((270, 130))
        rect_surface2.fill((28, 29, 85))
        rect_surface1.fill((252, 71, 60))
        screen.blit(rect_surface1, (270, 420))
        screen.blit(rect_surface2, (280, 430))
        screen.blit(text_surface1, (300, 450))
        screen.blit(text_surface2, (300, 500))

    def update_score(path):
        global cnt
        with open(path) as f:
            best_score = int(f.read())

        if cnt > best_score:
            best_score = cnt
            with open(path, "w") as f:
                f.write(f'{cnt}')
        return best_score

    best_score = update_score(SCORE_PATH)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если пользователь нажал крестик - выходим из игры
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        screen.blit(GAMEOVER_IMG, (0, 0))  # Выводим фон

        set_text(cnt, best_score)  # Выводим счет
        pygame.display.flip()  # Чтобы все изменения стали видны, нужно update игровой экран
        pygame.time.delay(10)  # Задержка, влияет на плавность анимации. Чем больше, тем хуже анимация


menu()
game()
final()
