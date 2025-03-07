import pygame

from pyengine import App
from pyengine import Rect

APP = App((960,540))
test = Rect((0,0),(10,10),pygame.Color(255,0,0,255))

@APP.onKeyPress
def onPress(app, keys):
    if keys[pygame.K_DOWN]:
        test.y += 5
    elif keys[pygame.K_UP]:
        test.y -= 5

    if keys[pygame.K_RIGHT]:
        test.x += 5
    elif keys[pygame.K_LEFT]:
        test.x -= 5

    if test.x < 0:
        test.rect.x = 0
    elif test.x + test.width > app.width:
        test.rect.x = app.width - test.width

    if test.y < 0:
        test.rect.y = 0
    elif test.y + test.height > app.height:
        test.rect.y = app.height - test.height


@APP.main
def main(app):
    app.clearScreen()
    app.render(test)

@APP.onInit
def init(app):
    print("INITIALIZED APP")


APP.run()