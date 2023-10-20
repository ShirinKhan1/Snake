import pygame
import Player


class Area(pygame.surface.Surface):
    def __init__(self, number: int, question: bool, png: str, tuple_: tuple):
        # pygame.surface.Surface.__init__(self)
        super().__init__((271, 174))
        self.x, self.y = tuple_[0], tuple_[1]
        self.image = pygame.image.load(png).convert_alpha()
        self.number = number
        self.question = question
        self.__people = []

    def add_player(self, player: Player):
        self.__people.append(player)

    def del_player(self, player: Player):
        return self.__people.remove(player)
