import pygame
import cfg
from Area import Area
from Player import Player

pygame.init()
# W, H = 800, 600
screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("images/snake.png"))
clock = pygame.time.Clock()
bg = pygame.image.load('images/wallpaper_snake.png')

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
    b1 = create_button("2 игрока", 500, 400, 200, 100)
    b2 = create_button("3 игрока", 800, 400, 200, 100)
    b3 = create_button("4 игрока", 1100, 400, 200, 100)
    b4 = create_button("Играть", 800, 600, 200, 100)
    pygame.display.flip()

    return b1, b2, b3, b4


# list_players = [Player(png, col, num) for png, col, num in zip(icons, colors, numbers)]
# MENU -------------------------------------------------------------------------------------------
button1, button2, button3, play_button = display_menu()
running = True
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
            elif play_button.collidepoint(event.pos):
                if selected_players > 0:
                    running = False

    pygame.display.flip()
    # screen.blit(list_players[0].image, list_players[0].rect)
del button1, button2, button3, play_button
# MADE PLAYERS ----------------------------------------------------------
[list_players.append(
    Player(cfg.icons[i], cfg.numbers[i])
) for i in range(selected_players)]
# MADE AREAS ----------------------------------------------------------
[list_areas.append(
    Area(png=f'images/area/{i}r.png', number=i, tuple_=cfg.list_tuples[i - 1], question=cfg.bool_question(i))
) for i in range(1, cfg.COUNT_AREA + 1)]
k = 1  # For test, not necessary---------------------------------------
while True:
    screen.blit(bg, (0, 0))
    for i in range(cfg.COUNT_AREA):  # init areas
        screen.blit(list_areas[i].image, (list_areas[i].x, list_areas[i].y))
    for i in range(selected_players):  # init players
        screen.blit(list_players[i].image, list_players[i].rect)
    pygame.display.update()
    # print(list_players[0].rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if k == 1:  # test add_player------------------
        list_areas[0].add_player(list_players[0])
        list_areas[0].add_player(list_players[1])
        list_areas[0].add_player(list_players[2])
        list_areas[0].add_player(list_players[3])

        k += 1
    if k == 2:  # test del_player------------------
        list_areas[0].del_player(list_players[0])
        k += 1
    list_players[0].update(1)
    clock.tick(cfg.FPS)
