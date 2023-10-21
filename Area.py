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

    def add_player(self, player: Player):   # sort in area
        sort_plat_xy = [(self.x + 70, self.y + 30),
                        (self.x + 160, self.y + 30),
                        (self.x + 70, self.y + 100),
                        (self.x + 160, self.y + 100)]

        self.__people.append(player)
        for i in range(len(self.__people)):
            self.__people[i].rect.x, self.__people[i].rect.y = sort_plat_xy[i][0],sort_plat_xy[i][1]

    def del_player(self, player: Player):
        for i in range(len(self.__people)):
            if self.__people[i].number == player.number:
                self.__people.pop(i)
                break
        player.rect.x = 60
        player.rect.y = self.y + 50

