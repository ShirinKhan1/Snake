import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, png, number, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(png).convert_alpha()
        self.number = number
        self.color = color
        self.locate = 1
        self.rect = self.image.get_rect(center=(100, 800))

    def update(self, step):
        for _ in range(step):
            self.rect.x += 3

