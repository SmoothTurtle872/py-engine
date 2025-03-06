import pygame
from pygame import Surface

class App:
    width: int
    height: int
    running: bool
    WIN: Surface

    main_functions:list[callable] = []

    def __init__(self, win_size: tuple[int, int]):
        self.width = win_size[0]
        self.height = win_size[1]

        self.WIN = pygame.display.set_mode(win_size)

        pygame.init()

    def main(self, func):
        self.main_functions.append(func)
        return func

    def run(self):
        self.running = True
        while self.running:
            if len(self.main_functions) > 0:
                for func in self.main_functions:
                    func(self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


        pygame.quit()


