from opponents.local_net import LocalNet
from opponents.on_this_pc import OnThisPC
from screen import Screen
from screens.button import Button
from screens.game import Game


class Multiplayer(Screen):
    def __init__(self, size: tuple[int, int]) -> None:
        super().__init__(self)
        self.__board_size = size

        self.__local_net: Button = Button(0, 0, 0, 0, "Local net")
        self.__one_pc: Button = Button(0, 0, 0, 0, "On this PC")
        self.__local_net.clicked.connect(self.__clicked_local_net)
        self.__one_pc.clicked.connect(self.__clicked_one_pc)

    def __clicked_local_net(self) -> None:
        print("clicked local network button")
        self.next_screen = Game(self.__board_size, LocalNet())

    def __clicked_one_pc(self) -> None:
        print("clicked one pc")
        self.next_screen = Game(self.__board_size, OnThisPC())

    def draw(self) -> None:
        return super().draw()  # TODO
