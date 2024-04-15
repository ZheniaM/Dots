from opponents.bot import Bot
from screens.multiplayer import Multiplayer
from screens.game import Game
from screens.screen import Screen
from button import Button
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class Title(Screen):
    def __init__(self) -> None:
        super().__init__(self)
        self.__board_size = (15, 15)
        self.title = "Title Screen"
        self.width, self.height = 400, 300

        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout)
        # Might consider moving it to screen

        self.__mode = Button(10, 10, 100, 50, "Mode")
        self.__mode.clicked.connect(self.__mode_clicked)

        self.__start = Button(10, 70, 100, 50, "Start")
        self.__start.clicked.connect(self.__start_clicked)

        self.__2player = Button(10, 130, 150, 50, "Two Players")
        self.__2player.clicked.connect(self.__2p_clicked)

        self.__buttons: list[Button] = [
            self.__mode,
            self.__start,
            self.__2player,
        ]

    def __mode_clicked(self) -> None:
        print("clicked mode")
        # TODO change board size

    def __start_clicked(self) -> None:
        print("clicked start")
        self.next_screen = Game(self.__board_size, Bot())

    def __2p_clicked(self) -> None:
        print("clicked two players")
        self.next_screen = Multiplayer(self.__board_size)

    def draw(self) -> None:
        self.window.setWindowTitle(self.title)
        self.window.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.window.show()
        # super().draw([self.__mode, self.__start, self.__2player])
