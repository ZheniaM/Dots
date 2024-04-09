from opponents.bot import Bot
from screens.multiplayer import Multiplayer
from screens.button import Button
from screens.game import Game
from screens.screen import Screen


class Title(Screen):
    def __init__(self) -> None:
        super().__init__(self)
        self.__board_size = (15, 15)

        # TODO sizes and locations
        self.__mode: Button = Button(0, 0, 0, 0, "Mode")
        self.__start: Button = Button(0, 0, 0, 0, "Start")
        self.__2player: Button = Button(0, 0, 0, 0, "Two Players")

        self.__mode.clicked.connect(self.__mode_clicked)
        self.__start.clicked.connect(self.__start_clicked)
        self.__2player.clicked.connect(self.__2p_clicked)

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
        return super().draw()  # TODO
