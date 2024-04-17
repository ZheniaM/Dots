from random import choice
from opponents.opponent import Opponent


class Bot(Opponent):
    def __init__(self) -> None:
        self.__board: list[list[int]]

    def __get_empty_cells(self) -> set[tuple[int, int]]:
        res: set[tuple[int, int]] = set()
        for y, line in enumerate(self.__board):
            for x, cell in enumerate(line):
                if not cell:
                    res.add((x, y))
        return res

    def make_turn(self, board: list[list[int]]) -> tuple[int, int]:
        self.__board = board
        empty_cells = self.__get_empty_cells()
        return choice(list(empty_cells))
