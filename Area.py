import pygame
import Player

class Area(pygame.surface.Surface):
    def __init__(self, number, question, png, tuple_: tuple):
        # pygame.surface.Surface.__init__(self)
        super().__init__((271, 174))
        self.x, y = tuple_[0], tuple_[1]
        self.image = pygame.image.load(png).convert_alpha()
        self.number = number
        self.question = question
        self.people = []

    def update(self, player: Player):
        self.people.append(player)
