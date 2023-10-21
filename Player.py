import pygame
import cfg


class Player(pygame.sprite.Sprite):
    def __init__(self, png, number):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(png).convert_alpha()
        self.number = number
        self.locate = 1
        self.rect = self.image.get_rect(center=(100, 800))

    def update(self, step):  # move player
        for _ in range(step):
            if self.rect.x < (cfg.area_len_px - 50) * 5:
                self.rect.x += cfg.area_len_px + 50
            else:
                self.rect.x = 60
                self.rect.y -= cfg.area_height_px
