import sys
from screens.screen import Screen
from screens.title import Title
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication


class Dots(QMainWindow):
    def __init__(self) -> None:
        self.__screen: Screen = Title()
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__main)

    def __main(self) -> None:
        self.__screen = self.__screen.next_screen
        self.__screen.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dots()
    window.show()
    sys.exit(app.exec())
