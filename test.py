from app import App

APP = App((960,540))

@APP.main
def test(app:App):
    print(app.width)

APP.run()