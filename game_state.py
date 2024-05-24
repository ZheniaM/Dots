from typing import Any, Generator, Tuple, Set

from opponents.opponent import Opponent
# from icecream.icecream import ic
import metadata


class GameState:
    def __init__(self, size: Tuple[int, int], opponent: Opponent) -> None:
        self.size: tuple[int, int] = size
        self.__board: list[list[int]] = [
            [0 for j in range(self.size[1])]
            for i in range(self.size[0])
        ]
        self.opponent: Opponent = opponent
        self.__score: int = 0
        self.active: int = True
        self.empty_spaces = size[0] * size[1]

    def set_dot(self, x: int, y: int) -> None:
        if self.__board[y][x]:
            raise ValueError("Dot already exists")
        if self.active:
            self.__board[y][x] = metadata.first_p_dot
        else:
            self.__board[y][x] = metadata.second_p_dot
        self.empty_spaces -= 1
        self.active = not self.active

    def log(self) -> None:
        # ic(self.__board)
        ...

    def get_board(self):
        return self.__board

    def opponent_make_turn(self) -> None:
        x, y = self.opponent.make_turn(self.__board)
        self.set_dot(x, y)

    def get_neighbours(points: Set[Tuple[int, int]]
                         ) -> Generator[Tuple[int, int], Any, None]:
        x_size = 10
        y_size = 10
        for x, y in points:
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= x + dx < x_size and 0 <= y + dy < y_size:
                    yield (x + dx, y + dy)
