import pygame
import cfg
from Area import Area
from Player import Player
from kubik import Kubik
import logging
import random
from cfg import clock

pygame.init()
# W, H = 800, 600
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("images/snake.png"))
# clock = pygame.time.Clock()
bg = pygame.image.load('images/wallpaper_snake.png')
logging.basicConfig(filename='game.log', level=logging.INFO)
logger = logging.getLogger(__name__)

kubik = Kubik()

list_players = []
list_areas = []
selected_players = 0

# Шрифт для текста
font = pygame.font.Font(None, 36)


# Функция для создания кнопок
def create_button(text, x, y, width, height):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, cfg.cream, button_rect)
    pygame.draw.rect(screen, cfg.black, button_rect, 2)
    text_surface = font.render(text, True, cfg.black)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect


# Функция для отображения меню
def display_menu():
    screen.fill(cfg.black)
    b1 = create_button("2 игрока", 400, 300, 200, 100)
    b2 = create_button("3 игрока", 700, 300, 200, 100)
    b3 = create_button("4 игрока", 1000, 300, 200, 100)
    b4 = create_button("Играть", 700, 500, 200, 100)
    b5 = create_button("Новый год", 900, 650, 200, 100)
    b6 = create_button("Хеллоуин", 500, 650, 200, 100)
    pygame.display.flip()

    return b1, b2, b3, b4, b5, b6


# list_players = [Player(png, col, num) for png, col, num in zip(icons, colors, numbers)]
# MENU -------------------------------------------------------------------------------------------
button1, button2, button3, play_button, pack_ny, pack_hal = display_menu()
running = True
logger.info('Начало игры. Выбор игроков')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                selected_players = 2
            elif button2.collidepoint(event.pos):
                selected_players = 3
            elif button3.collidepoint(event.pos):
                selected_players = 4
            elif pack_ny.collidepoint(event.pos):
                cfg.icons = cfg.icons_christmas
            elif pack_hal.collidepoint(event.pos):
                cfg.icons = cfg.icons_halloween
            elif play_button.collidepoint(event.pos):
                if selected_players > 0:
                    running = False

    # logger.debug("Это сообщение с уровнем DEBUG")
    # logger.warning("Это предупреждение")
    # logger.error("Это сообщение об ошибке")
    # logger.critical("Это критическая ошибка")

    pygame.display.flip()
    # screen.blit(list_players[0].image, list_players[0].rect)
logger.info(f"Выбрано {selected_players}")
del button1, button2, button3, play_button
# MADE PLAYERS ----------------------------------------------------------
[list_players.append(
    Player(cfg.icons[i], cfg.numbers[i])
) for i in range(selected_players)]
# MADE AREAS ----------------------------------------------------------
[list_areas.append(
    Area(png=f'images/area/{i}r.png', number=i, tuple_=cfg.list_tuples[i - 1], question=cfg.bool_question(i))
) for i in range(1, cfg.COUNT_AREA + 1)]
# List_steps -------------------------------------------------------------
list_steps = [i for i in range(selected_players)]
random.shuffle(list_steps)
logger.info(f"Круг ходов {list_steps}")
k = 1  # For test, not necessary---------------------------------------


def start_():
    screen.blit(bg, (0, 0))
    for i in range(cfg.COUNT_AREA):  # init areas
        screen.blit(list_areas[i].image, (list_areas[i].x, list_areas[i].y))
    for i in range(selected_players):  # init players
        screen.blit(list_players[i].image, list_players[i].rect)
    pygame.display.update()


def start_locate():
    for i in range(selected_players):
        list_areas[0].add_player(list_players[i])


start_()
start_locate()
game_is_run = True
logger.info('Старт игры!')

while game_is_run:
    # start_()
    # pygame.display.update()
    # print(list_players[0].rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    now_playing = list_steps.pop(0)
    roll = kubik.roll()
    if list_players[now_playing].locate + roll >= cfg.COUNT_AREA - 1:
        game_is_run = False
        logger.info(f'Победил игрок {now_playing}')
        roll = cfg.COUNT_AREA - list_players[now_playing].locate - 1
    else:
        logger.info(f'Игрок номер {now_playing} походил на {roll} шагов')
    for _ in range(roll):
        clock.tick(cfg.FPS)
        list_areas[list_players[now_playing].locate].del_player(list_players[now_playing])
        list_players[now_playing].update(1)
        list_areas[list_players[now_playing].locate].add_player(list_players[now_playing])
        pygame.display.update()
        start_()
        pygame.display.update()
    start_()
    pygame.display.update()
    list_steps.append(now_playing)

    # if k == 2:  # test del_player------------------
    #     list_areas[0].del_player(list_players[0])
    #     k += 1

    # list_players[0].update(1)
    clock.tick(cfg.FPS)
