from __future__ import annotations
from abc import ABC
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QMessageBox

from game_state import GameState
from opponents.bot import Bot
from opponents.local_net import LocalNet
from opponents.on_this_pc import OnThisPC
from opponents.opponent import Opponent
from screens.button import Button


class Screen(ABC):
    def __init__(self, scr: Screen, parrent: QWidget) -> None:
        super().__init__()
        self.next_screen = scr
        self.parrent = parrent

    def draw(self) -> None:
        ...

    def getWidget(self) -> QWidget:
        ...


# MARK: Title
class Title(Screen):
    def __init__(self, parrent: QWidget) -> None:
        super().__init__(self, parrent)
        self.__board_size = (10, 10)
        self.title = "Title Screen"

        self.parrent = QWidget()
        self.layout = QVBoxLayout()
        self.parrent.setLayout(self.layout)
        # Might consider moving it to screen

        # self.__mode = Button(10, 10, 100, 50, "Mode", self.parrent)
        # self.__mode.clicked.connect(self.__mode_clicked)

        self.__start = Button(10, 70, 100, 50, "Start", self.parrent)
        self.__start.clicked.connect(self.__start_clicked)

        # self.__2player = Button(10, 130, 150, 50, "Two Players", self.parrent)
        # self.__2player.clicked.connect(self.__2p_clicked)

        self.__buttons: list[Button] = [
            # self.__mode,
            self.__start,
            # self.__2player,
        ]

    def __mode_clicked(self) -> None:
        print("clicked mode")
        # TODO change board size

    def __start_clicked(self) -> None:
        print("clicked start")
        self.next_screen = Game(self.parrent, self.__board_size, Bot())

    def __2p_clicked(self) -> None:
        print("clicked two players")
        self.next_screen = Multiplayer(self.parrent, self.__board_size)

    def draw(self) -> None:
        self.parrent.setWindowTitle(self.title)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parrent.show()


# MARK: Multiplayer
# TODO: Make multiplayer work
class Multiplayer(Screen):
    def __init__(self, parrent: QWidget,  size: tuple[int, int]) -> None:
        super().__init__(self, parrent)
        self.__board_size = size

        self.title = "Multiplayer Screen"
        self.width, self.height = 400, 300

        # self.parrent = QWidget()
        self.layout = QVBoxLayout()
        self.parrent.setLayout(self.layout)
        # Might consider moving it to screen

        self.__local_net: Button = Button(0, 0, 0, 0,
                                          "Local net", self.parrent)
        self.__one_pc: Button = Button(0, 0, 0, 0, "On this PC", self.parrent)
        self.__local_net.clicked.connect(self.__clicked_local_net)
        self.__one_pc.clicked.connect(self.__clicked_one_pc)

        self.__buttons: list[Button] = [
            self.__local_net,
            self.__one_pc,
        ]

    def __clicked_local_net(self) -> None:
        print("clicked local network button")
        self.next_screen = Game(self.parrent, self.__board_size, LocalNet())

    def __clicked_one_pc(self) -> None:
        print("clicked one pc")
        self.next_screen = Game(self.parrent, self.__board_size, OnThisPC())

    def draw(self) -> None:
        self.parrent.setWindowTitle(self.title)
        self.parrent.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parrent.show()


# MARK: Game
class Game(Screen):
    def __init__(self, parrent: QWidget,
                 size: tuple[int, int] = (25, 25),
                 opponent: Opponent = Bot(),
                 game_state: GameState | None = None) -> None:
        super().__init__(self, parrent)
        self.__game_state: GameState
        if game_state is None:
            self.__game_state = GameState(size, opponent)
        else:
            self.__game_state = game_state

        self.title = "Game Screen"
        self.width, self.height = 400, 300

        self.parrent = QWidget()
        self.layout = QVBoxLayout()
        self.parrent.setLayout(self.layout)

        # self.__surround: Button = Button(0, 0, 0, 0, "Surround", self.parrent)
        # self.__surround.clicked.connect(self.__surround_clicked)
        self.__b_pause: Button = Button(0, 0, 50, 50, "Pause", self.parrent)
        self.__b_pause.clicked.connect(self.__pause_clicked)

        self.__le_xy: QLineEdit = QLineEdit(self.parrent)
        self.__le_xy.setInputMask("00 00;_")
        self.__le_xy.returnPressed.connect(self.__xy_return_pressed)

        self.__widgets: list[Button] = [
            self.__b_pause,
            self.__le_xy,
        ]

        self.__box_error: QMessageBox = QMessageBox()
        self.__box_error.setIcon(QMessageBox.Critical)
        self.__box_error.setWindowTitle("Error")

    def __xy_return_pressed(self) -> None:
        x, y = map(lambda x: int(x) - 1, self.__le_xy.text().split())
        try:
            if not (0 <= x < self.__game_state.size[0] and
                    0 <= y < self.__game_state.size[1]):
                raise ValueError("Coordinates out of the field.")
            self.__make_turn(x, y)
            self.__make_turn()
        except ValueError as e:
            self.__box_error.setInformativeText(str(e))
            self.__box_error.exec()

    def __pause_clicked(self) -> None:
        self.next_screen = Pause(self.parrent, self, self.__game_state)

    def __make_turn(self, x: int = 0, y: int = 0) -> None:
        if self.__game_state.active:
            self.__game_state.set_dot(x, y)
        else:
            self.__game_state.opponent_make_turn()

        self.__game_state.log()

    def draw(self) -> None:
        self.parrent.setWindowTitle(self.title)
        self.parrent.resize(self.width, self.height)
        for widget in self.__widgets:
            self.layout.addWidget(widget)
        self.parrent.show()


# MARK: Pause
class Pause(Screen):
    def __init__(self, parrent: QWidget, game: Game,
                 game_state) -> None:
        super().__init__(self, parrent)
        self.__game: Game = game
        self.__game_state: GameState = game_state

        self.title = "Pause Screen"
        self.width, self.height = 400, 300

        self.parrent = QWidget()
        self.layout = QVBoxLayout()
        self.parrent.setLayout(self.layout)
        # Might consider moving it to screen

        self.__continue: Button = Button(
            20, 30, 50, 50, "Continue", self.parrent)
        self.__surrender: Button = Button(
            100, 30, 50, 50, "Surrender", self.parrent)
        self.__continue.clicked.connect(self.__continue_clicked)
        self.__surrender.clicked.connect(self.__surrender_clicked)

        self.__buttons: list[Button] = [
            self.__continue,
            self.__surrender
        ]

    def __continue_clicked(self) -> None:
        self.next_screen = Game(self.parrent, game_state=self.__game_state)

    def __surrender_clicked(self) -> None:
        self.next_screen = End(self.parrent,
                               self.__game_state.size,
                               self.__game_state.opponent)

    def draw(self) -> None:
        self.parrent.setWindowTitle(self.title)
        self.parrent.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parrent.show()


# MARK: End
class End(Screen):
    def __init__(self, parrent: QWidget,
                 size: tuple[int, int], opponent: Opponent) -> None:
        super().__init__(self, parrent)
        self.__size: tuple[int, int] = size
        self.__opponent: Opponent = opponent

        self.title = "End Screen"
        self.width, self.height = 400, 300

        self.parrent = QWidget()
        self.layout = QVBoxLayout()
        self.parrent.setLayout(self.layout)
        # Might consider moving it to screen

        self.__exit: Button = Button(0, 0, 0, 0, "Exit", self.parrent)
        self.__try_over: Button = Button(0, 0, 0, 0, "Try again", self.parrent)
        self.__to_title: Button = Button(
            0, 0, 0, 0, "Go to title screen", self.parrent)

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
        self.next_screen = Game(self.parrent, self.__size, self.__opponent)

    def __to_title_clicked(self) -> None:
        print("to title clicked")
        self.next_screen = Title(self.parrent)

    def draw(self) -> None:
        self.parrent.setWindowTitle(self.title)
        self.parrent.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parrent.show()
