import sys
from screens.screen import Screen, Title
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication


# MARK: Dots
class Dots(QMainWindow):
    def __init__(self) -> None:
        super(Dots, self).__init__(None)
        self.setGeometry(500, 100, 0, 0)
        self.showMaximized()
        self.__screen: Screen = Title(self)
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__main)
        self.__timer.start(100)

    def __main(self) -> None:
        # print(self.__screen)
        self.__screen = self.__screen.next_screen
        self.setCentralWidget(self.__screen.parrent)
        self.__screen.draw()


# MARK: run
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dots()
    window.show()
    sys.exit(app.exec())
