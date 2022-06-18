from Board import Board
from BoardHandler import BoardHandler

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class TestApp(App):
    def build(self):
        return Button(text=" Hello Kivy World ")

class TestWidget(Widget):
    pass


if __name__ == '__main__':
    TestApp().run()

boardHandler = BoardHandler()
boardHandler.board.printBoard()
