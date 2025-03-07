import pygame

class Rect:
    rect: pygame.Rect
    color: pygame.Color

    def __init__(self, pos:tuple[int|float,int|float], size:tuple[int|float,int|float], color:pygame.Color):
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1],size[0], size[1])

    @property
    def x(self) -> int|float:
        return  self.rect.x

    @x.setter
    def x(self, value) -> None:
        self.rect.x = value

    @property
    def y(self) -> int|float:
        return  self.rect.y

    @y.setter
    def y(self, value) -> None:
        self.rect.y = value

    @property
    def width(self) -> int|float:
        return  self.rect.width

    @width.setter
    def width(self, value) -> None:
        self.rect.width = value

    @property
    def height(self) -> int|float:
        return  self.rect.height

    @height.setter
    def height(self, value) -> None:
        self.rect.height = value
