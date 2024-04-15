from opponents.opponent import Opponent
from screens.button import Button
from screens.game import Game
from screens.screen import Screen
from screens.title import Title
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class End(Screen):
    def __init__(self, size: tuple[int, int], opponent: Opponent) -> None:
        super().__init__(self)
        self.__size: tuple[int, int] = size
        self.__opponent: Opponent = opponent

        self.title = "End Screen"
        self.width, self.height = 400, 300

        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout)
        # Might consider moving it to screen

        self.__exit: Button = Button(0, 0, 0, 0, "Exit")
        self.__try_over: Button = Button(0, 0, 0, 0, "Try again")
        self.__to_title: Button = Button(0, 0, 0, 0, "Go to title screen")

        self.__exit.clicked.connect(self.__exit_clicked)
        self.__try_over.clicked.connect(self.__try_over_clicked)
        self.__to_title.clicked.connect(self.__to_title_clicked)

        self.__buttons: list[Button] = [
            self.__exit,
            self.__try_over,
            self.__to_title
        ]

    def __exit_clicked(self) -> None:
        print("exit clicked")
        exit(0)  # TODO : Find a better way of closing the program

    def __try_over_clicked(self) -> None:
        print("try over clicked")
        self.next_screen = Game(self.__size, self.__opponent)

    def __to_title_clicked(self) -> None:
        print("to title clicked")
        self.next_screen = Title()

    def draw(self, bu) -> None:
        self.window.setWindowTitle(self.title)
        self.window.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.window.show()
