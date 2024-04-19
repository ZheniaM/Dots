from typing import Any, Generator

from opponents.opponent import Opponent
# from icecream.icecream import ic
import metadata


class GameState:
    def __init__(self, size: tuple[int, int], opponent: Opponent) -> None:
        self.size: tuple[int, int] = size
        self.__board: list[list[int]] = [
            [0 for j in range(self.size[1])]
            for i in range(self.size[0])
        ]
        self.opponent: Opponent = opponent
        self.__score: int = 0
        self.active: int = True

    def set_dot(self, x: int, y: int) -> None:
        if self.__board[y][x]:
            raise ValueError("Dot already exists")
        if self.active:
            self.__board[y][x] = metadata.first_p_dot
        else:
            self.__board[y][x] = metadata.second_p_dot
        self.active = not self.active

    def log(self) -> None:
        # ic(self.__board)
        ...

    def get_board(self):
        return self.__board

    def opponent_make_turn(self) -> None:
        x, y = self.opponent.make_turn(self.__board)
        self.set_dot(x, y)

    def __get_neighbours(self, x: int, y: int
                         ) -> Generator[tuple[int, int], Any, None]:
        x_size, y_size = self.size
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if 0 <= x + dx < x_size and 0 <= y + dy < y_size:
                yield (x + dx, y + dy)
