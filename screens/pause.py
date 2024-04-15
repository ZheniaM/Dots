from opponents.opponent import Opponent
from screens.screen import Screen
from screens.button import Button
from screens.game import Game
from screens.end import End
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class Pause(Screen):
    def __init__(self, game: Game,
                 size: tuple[int, int],
                 opponent: Opponent) -> None:
        super().__init__(self)
        self.__game: Game = game
        self.__size: tuple[int, int] = size
        self.__opponent: Opponent = opponent

        self.title = "Pause Screen"
        self.width, self.height = 400, 300

        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout)
        # Might consider moving it to screen

        self.__continue: Button = Button(20, 30, 50, 50, "continue")
        self.__surrender: Button = Button(100, 30, 50, 50, "surrender")
        self.__continue.clicked.connect(self.__continue_clicked)
        self.__surrender.clicked.connect(self.__surrender_clicked)

        self.__buttons: list[Button] = [
            self.__continue,
            self.__surrender
        ]

    def __continue_clicked(self) -> None:
        self.next_screen = self.__game

    def __surrender_clicked(self) -> None:
        self.next_screen = End(self.__size, self.__opponent)

    def draw(self) -> None:
        self.window.setWindowTitle(self.title)
        self.window.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.window.show()
