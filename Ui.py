from Board import Board
from BoardHandler import BoardHandler
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text=" Hello Kivy World ")


TestApp().run()
boardHandler = BoardHandler()
boardHandler.board.printBoard()
