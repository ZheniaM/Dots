from opponents.opponent import Opponent
from screens.screen import Screen
from screens.button import Button
from screens.pause import Pause
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


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
        #Might consider moving it to screen

        self.__pause = Button(0, 0, 50, 50, "Pause")
        self.__pause.clicked.connect(self.__pause_clicked)

    def __pause_clicked(self) -> None:
        self.next_screen = Pause(self, self.__size, self.__opponent)

    def __make_turn(self) -> None:
        self.__score += 1
        print(f"{self.__score=}")

    def draw(self) -> None:
        super().draw([self.__pause])
