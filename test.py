import pygame

from pyengine import App
from pyengine import Rect

APP = App((960,540))
test = Rect((0,0),(10,10),pygame.Color(255,0,0,255))

@APP.main
def main(app):
    app.render(test)


APP.run()