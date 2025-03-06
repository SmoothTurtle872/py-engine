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

    @property
    def y(self) -> int|float:
        return  self.rect.y

    @property
    def width(self) -> int|float:
        return  self.rect.width

    @property
    def height(self) -> int|float:
        return  self.rect.height
