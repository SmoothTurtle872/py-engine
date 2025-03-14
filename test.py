import pygame
from pygame import Color

from pyengine import App
from pyengine import Rect
from pyengine.events import Event

APP = App((960,540), auto_quit=False)
test = Rect((0,0),(10,10),pygame.Color(255,0,0,255))

QUIT_RESPONSES = {0:"LOL! No more quitting!",
                  1:"I told you you won't be quitting",
                  2:"Please stop pressing the quit button",
                  3:"Windows is asking questions now",
                  4:"You really want to quit?",
                  5:"Why?",
                  6:"Please, don't kill me",
                  7:"I hear dying processes all the time, it's going to hurt",
                  8:"Fine if you really hate me",
                  9:"Goodbye..."}

quit_count = 0

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

@APP.onClick
def onClick(app, mouseBTNS):
    if mouseBTNS[0]:
        test.color = Color(255,0,0,255)
        app.sendEvent(Event(2,None))
    elif mouseBTNS[1]:
        test.color = Color(0,255,0,255)
    elif mouseBTNS[2]:
        test.color = Color(0,0,255,255)


@APP.main
def main(app):
    app.clearScreen()
    app.render(test)

@APP.onInit
def init(app):
    print("Hello")

@APP.onEvent(2)
def on_test(app, data):
    print(app.mousePos)

@APP.onEvent(1)
def on_test(app, data):
    global quit_count
    if quit_count < 10:
        print(QUIT_RESPONSES[quit_count])
        quit_count += 1
    else:
        app.running = False


APP.run()