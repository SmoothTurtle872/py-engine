import pygame
from pygame import Surface

from pyengine.types.rect import Rect

class App:

    __slots__ = "width", "height", "running", "WIN", "FPS", "main_functions", "on_key_press", "on_init"
    width: int
    height: int
    running: bool
    WIN: Surface

    FPS: int
    CLOCK: pygame.time.Clock = pygame.time.Clock()

    main_functions: set[callable]
    on_key_press: set[callable]
    on_init: set[callable]

    def __init__(self, win_size: tuple[int, int], FPS: int = 30) -> None:
        pygame.init()

        self.width = win_size[0]
        self.height = win_size[1]

        self.WIN = pygame.display.set_mode(win_size)

        self.FPS = FPS

        self.main_functions = set()
        self.on_key_press = set()
        self.on_init = set()

    def main(self, func) -> callable:
        self.main_functions.add(func)
        return func

    def onKeyPress(self, func) -> callable:
        self.on_key_press.add(func)
        return func

    def onInit(self, func) -> callable:
        self.on_init.add(func)
        return func

    def render(self, renderable: Rect) -> None:
        """
        Renders a renderable onto the screen
        :param renderable: The object to be rendered ``pyengine.types.rect.Rect``
        :return:
        """
        if type(renderable) == Rect:
            pygame.draw.rect(self.WIN,renderable.color,renderable.rect)

    def clearScreen(self, color:pygame.Color = pygame.Color(0,0,0,255)) -> None:
        """
        Fills the screen with a specific color
        :param color: The color to fill the screen with ``pygame.color``
        :return:
        """
        self.WIN.fill(color)

    def run(self) -> None:
        if len(self.on_init) > 0:
            for func in self.on_init:
                func(self)
        self.running = True
        while self.running:
            self.CLOCK.tick(self.FPS)
            if len(self.main_functions) > 0:
                for func in self.main_functions:
                    func(self)

            keys = pygame.key.get_pressed()
            if len(keys) > 1:
                if len(self.on_key_press) > 0:
                    for func in self.on_key_press:
                        func(self, keys)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


        pygame.quit()


