import pygame
from Area import Area
from Player import Player

pygame.init()
# W, H = 800, 600
screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("images/snake.png"))
clock = pygame.time.Clock()
bg = pygame.image.load('images/wallpaper_snake.png')
FPS = 60
icons = [
    'images/frankenstein.png',
    'images/pumpkin.png',
    'images/witch.png',
    'images/candy-bag.png']
colors = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0]]
numbers = list(range(1, 5))

# Цвета
cream = (253, 244, 227)
black = (0, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 36)


# Функция для создания кнопок
def create_button(text, x, y, width, height):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, cream, button_rect)
    pygame.draw.rect(screen, black, button_rect, 2)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect


# Функция для отображения меню
def display_menu():
    screen.fill(black)
    button1 = create_button("2 игрока", 500, 400, 200, 100)
    button2 = create_button("3 игрока", 800, 400, 200, 100)
    button3 = create_button("4 игрока", 1100, 400, 200, 100)
    play_button = create_button("Играть", 800, 600, 200, 100)
    pygame.display.flip()

    return button1, button2, button3, play_button


# list_players = [Player(png, col, num) for png, col, num in zip(icons, colors, numbers)]
list_players = []
selected_players = 0
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
for i in range(selected_players):
    list_players.append(Player(icons[i], colors[i], numbers[i]))


while True:
    screen.blit(bg, (0, 0))
    screen.blit(list_players[0].image, list_players[0].rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)

    # list_players[0].update(1)
