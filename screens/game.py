from opponents.opponent import Opponent
from screens.end import End
from screens.screen import Screen
from screens.button import Button
# from screens.pause import Pause
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class Game(Screen):
    def __init__(self, size: tuple[int, int], opponent: Opponent) -> None:
        super().__init__(self)
        self.__size: tuple[int, int] = size
        # self.__board: list[list[Button]] = [
        #     [Button(20 + i * 3, 20 + j * 3, 4, 4, "") for j in range(size[1])]
        #     for i in range(size[0])
        # ]
        self.__opponent: Opponent = opponent
        self.__score: int = 0
        self.__active: bool = True

        self.title = "Game Screen"
        self.width, self.height = 400, 300

        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout)
        # Might consider moving it to screen

        self.__pause = Button(0, 0, 50, 50, "Pause")
        self.__pause.clicked.connect(self.__pause_clicked)

        self.__buttons: list[Button] = [self.__pause]

    def __pause_clicked(self) -> None:
        self.next_screen = Pause(self, self.__size, self.__opponent)

    def __make_turn(self) -> None:
        self.__score += 1
        print(f"{self.__score=}")

    def draw(self) -> None:
        self.window.setWindowTitle(self.title)
        self.window.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.window.show()


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
