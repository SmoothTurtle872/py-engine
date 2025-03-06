from app import App

APP = App((960,540))

@APP.main
def test():
    print("YAY")

APP.run()