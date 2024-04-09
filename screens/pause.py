from opponents.opponent import Opponent
from screen import Screen
from screens.button import Button
from screens.game import Game
from screens.end import End


class Pause(Screen):
    def __init__(self, game: Game,
                 size: tuple[int, int],
                 opponent: Opponent) -> None:
        super().__init__(self)
        self.__game: Game = game
        self.__size: tuple[int, int] = size
        self.__opponent: Opponent = opponent

        self.__continue: Button = Button(0, 0, 0, 0, "continue")
        self.__surrender: Button = Button(0, 0, 0, 0, "surrender")
        self.__continue.clicked.connect(self.__continue_clicked)
        self.__surrender.clicked.connect(self.__surrender_clicked)

    def __continue_clicked(self) -> None:
        self.next_screen = self.__game

    def __surrender_clicked(self) -> None:
        self.next_screen = End(self.__size, self.__opponent)

    def draw(self) -> None:
        return super().draw()  # TODO
