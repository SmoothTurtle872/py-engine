from types import NoneType

import pygame
from pygame import Surface

import time

from pyengine.types.rect import Rect
from pyengine.events import Event
import pyengine.events as events

class App:

    __slots__ = "width", "height", "running", "WIN", "FPS", "main_functions", "on_key_press", "on_init", "on_click", "on_event", "events", "auto_quit"
    width: int
    height: int
    running: bool
    WIN: Surface

    FPS: int
    CLOCK: pygame.time.Clock = pygame.time.Clock()

    auto_quit: bool

    main_functions: set[callable]
    on_key_press: set[callable]
    on_init: set[callable]
    on_click: set[callable]
    on_event: dict[int,callable]
    events: set[Event]

    def __init__(self, win_size: tuple[int, int], FPS: int = 30, auto_quit: bool = True) -> None:
        pygame.init()

        self.width = win_size[0]
        self.height = win_size[1]

        self.WIN = pygame.display.set_mode(win_size)

        self.FPS = FPS

        self.auto_quit = auto_quit

        self.main_functions = set()
        self.on_key_press = set()
        self.on_init = set()
        self.on_click = set()
        self.on_event = {}
        self.events = set()

    # Decorators

    def main(self, func) -> callable:
        self.main_functions.add(func)
        return func

    def onKeyPress(self, func) -> callable:
        self.on_key_press.add(func)
        return func

    def onInit(self, func) -> callable:
        self.on_init.add(func)
        return func

    def onClick(self, func) -> callable:
        self.on_click.add(func)
        return func

    def onEvent(self, event_type):
        def inner(func):
            self.on_event[event_type] = func
            return func
        return inner


    # Properties
    @property
    def mousePos(self) -> tuple[int,int]:
        return pygame.mouse.get_pos()

    # Functions to be run by user
    def sendEvent(self, event:int, data: None|list = None):
        """
        Sends an event
        :param event: The event type, a list of them can be found by importing ``pyengine.events``
        :param data: The data to be sent with the event, always includes a timestamp
        :return:
        """
        event_data: tuple = (time.time(),data)
        self.events.add(Event(event, event_data))

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
            if keys.count(True) > 0:
                if len(self.on_key_press) > 0:
                    for func in self.on_key_press:
                        func(self, keys)

            mouse_pressed = pygame.mouse.get_pressed()
            if True in set(mouse_pressed):
                if len(self.on_click) > 0:
                    for func in self.on_click:
                        func(self, mouse_pressed)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sendEvent(events.QUIT)

            if len(self.events) > 0:
                for event in self.events:
                    if self.on_event != {}:
                        if event.type in self.on_event:
                            self.on_event[event.type](self, event.data)
                    if event.type == events.QUIT and self.auto_quit:
                        self.running = False

                self.events = set()



        pygame.quit()


