from __future__ import annotations
from abc import ABC
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem)
from PyQt5.QtGui import QColor

from game_state import GameState
from opponents.bot import Bot
from opponents.local_net import LocalNet
from opponents.on_this_pc import OnThisPC
from opponents.opponent import Opponent
from screens.button import Button


class Screen(ABC):
    def __init__(self, scr: Screen, parent: QWidget) -> None:
        super().__init__()
        self.next_screen = scr
        self.parent = parent

    def draw(self) -> None:
        ...

    def getWidget(self) -> QWidget:
        ...


# MARK: Title
class Title(Screen):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(self, parent)
        self.__board_size = (10, 10)
        self.title = "Title Screen"

        self.parent = QWidget()
        self.layout = QVBoxLayout()
        self.parent.setLayout(self.layout)
        # Might consider moving it to screen

        # self.__mode = Button(10, 10, 100, 50, "Mode", self.parent)
        # self.__mode.clicked.connect(self.__mode_clicked)

        self.__start = Button(10, 70, 100, 50, "Start", self.parent)
        self.__start.clicked.connect(self.__start_clicked)

        # self.__2player = Button(10, 130, 150, 50, "Two Players", self.parent)
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
        self.next_screen = Game(self.parent, self.__board_size, Bot())

    def __2p_clicked(self) -> None:
        print("clicked two players")
        self.next_screen = Multiplayer(self.parent, self.__board_size)

    def draw(self) -> None:
        self.parent.setWindowTitle(self.title)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parent.show()


# MARK: Multiplayer
# TODO: Make multiplayer work
class Multiplayer(Screen):
    def __init__(self, parent: QWidget,  size: tuple[int, int]) -> None:
        super().__init__(self, parent)
        self.__board_size = size

        self.title = "Multiplayer Screen"
        self.width, self.height = 400, 300

        # self.parent = QWidget()
        self.layout = QVBoxLayout()
        self.parent.setLayout(self.layout)
        # Might consider moving it to screen

        self.__local_net: Button = Button(0, 0, 0, 0,
                                          "Local net", self.parent)
        self.__one_pc: Button = Button(0, 0, 0, 0, "On this PC", self.parent)
        self.__local_net.clicked.connect(self.__clicked_local_net)
        self.__one_pc.clicked.connect(self.__clicked_one_pc)

        self.__buttons: list[Button] = [
            self.__local_net,
            self.__one_pc,
        ]

    def __clicked_local_net(self) -> None:
        print("clicked local network button")
        self.next_screen = Game(self.parent, self.__board_size, LocalNet())

    def __clicked_one_pc(self) -> None:
        print("clicked one pc")
        self.next_screen = Game(self.parent, self.__board_size, OnThisPC())

    def draw(self) -> None:
        self.parent.setWindowTitle(self.title)
        self.parent.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parent.show()


# MARK: Game
class Game(Screen):
    def __init__(self, parent: QWidget,
                 size: tuple[int, int] = (25, 25),
                 opponent: Opponent = Bot(),
                 game_state: GameState | None = None) -> None:
        super().__init__(self, parent)
        self.__game_state: GameState
        if game_state is None:
            self.__game_state = GameState(size, opponent)
        else:
            self.__game_state = game_state

        self.title = "Game Screen"
        self.width, self.height = 400, 300

        self.parent = QWidget()
        self.layout = QVBoxLayout()
        self.parent.setLayout(self.layout)

        # self.__surround: Button = Button(0, 0, 0, 0, "Surround", self.parent)
        # self.__surround.clicked.connect(self.__surround_clicked)
        self.__b_pause: Button = Button(0, 0, 50, 50, "Pause", self.parent)
        self.__b_pause.clicked.connect(self.__pause_clicked)

        self.__le_xy: QLineEdit = QLineEdit(self.parent)
        self.__le_xy.setInputMask("00 00;_")
        self.__le_xy.returnPressed.connect(self.__xy_return_pressed)

        self.__table = QTableWidget()

        self.__widgets: list[Button] = [
            self.__b_pause,
            self.__le_xy,
            self.__table
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
        self.next_screen = Pause(self.parent, self, self.__game_state)

    def __make_turn(self, x: int = 0, y: int = 0) -> None:
        if self.__game_state.active:
            try:
                self.__game_state.set_dot(x, y)
                if self.__game_state.empty_spaces == 0:
                    self.next_screen = End(self.parent,
                                           self.__game_state.size,
                                           self.__game_state.opponent)
            except ValueError:
                ...

        else:
            self.__game_state.opponent_make_turn()

        self.__game_state.log()
        self.set_table()

    def draw(self) -> None:
        self.parent.setWindowTitle(self.title)
        self.parent.resize(self.width, self.height)
        for widget in self.__widgets:
            self.layout.addWidget(widget)
        self.parent.show()

    def set_table(self):
        data = self.__game_state.get_board()
        self.__table.setRowCount(len(data))
        self.__table.setColumnCount(len(data[0]))
        # cell_width = 20
        # cell_height = 20
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str("*"))
                if val == 16:
                    color = QColor("blue")
                elif val == 32:
                    color = QColor("red")
                else:
                    color = QColor("white")
                item.setForeground(color)

                self.__table.setItem(i, j, item)
                # for i in range(len(data)):
                #    self.__table.setRowHeight(i, cell_height)
                # for j in range(len(data[0])):
                #    self.__table.setColumnWidth(j, cell_width)


# MARK: Pause
class Pause(Screen):
    def __init__(self, parent: QWidget, game: Game,
                 game_state) -> None:
        super().__init__(self, parent)
        self.__game: Game = game
        self.__game_state: GameState = game_state

        self.title = "Pause Screen"
        self.width, self.height = 400, 300

        self.parent = QWidget()
        self.layout = QVBoxLayout()
        self.parent.setLayout(self.layout)
        # Might consider moving it to screen

        self.__continue: Button = Button(
            20, 30, 50, 50, "Continue", self.parent)
        self.__surrender: Button = Button(
            100, 30, 50, 50, "Surrender", self.parent)
        self.__continue.clicked.connect(self.__continue_clicked)
        self.__surrender.clicked.connect(self.__surrender_clicked)

        self.__buttons: list[Button] = [
            self.__continue,
            self.__surrender
        ]

    def __continue_clicked(self) -> None:
        self.next_screen = Game(self.parent, game_state=self.__game_state)

    def __surrender_clicked(self) -> None:
        self.next_screen = End(self.parent,
                               self.__game_state.size,
                               self.__game_state.opponent)

    def draw(self) -> None:
        self.parent.setWindowTitle(self.title)
        self.parent.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parent.show()
# MARK: Continue doesn't return game properly


# MARK: End
class End(Screen):
    def __init__(self, parent: QWidget,
                 size: tuple[int, int], opponent: Opponent) -> None:
        super().__init__(self, parent)
        self.__size: tuple[int, int] = size
        self.__opponent: Opponent = opponent

        self.title = "End Screen"
        self.width, self.height = 400, 300

        self.parent = QWidget()
        self.layout = QVBoxLayout()
        self.parent.setLayout(self.layout)
        # Might consider moving it to screen

        self.__exit: Button = Button(0, 0, 0, 0, "Exit", self.parent)
        self.__try_over: Button = Button(0, 0, 0, 0, "Try again", self.parent)
        self.__to_title: Button = Button(
            0, 0, 0, 0, "Go to title screen", self.parent)

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
        self.next_screen = Game(self.parent, self.__size, self.__opponent)

    def __to_title_clicked(self) -> None:
        print("to title clicked")
        self.next_screen = Title(self.parent)

    def draw(self) -> None:
        self.parent.setWindowTitle(self.title)
        self.parent.resize(self.width, self.height)
        for button in self.__buttons:
            self.layout.addWidget(button)
        self.parent.show()
