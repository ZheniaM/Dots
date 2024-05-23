from random import choice
from opponents.opponent import Opponent
from typing import Set, List, Tuple


class Bot(Opponent):
    def __init__(self) -> None:
        self.__board: list[list[int]]

    def __get_empty_cells(self) -> Set[Tuple[int, int]]:
        res: set[tuple[int, int]] = set()
        for y, line in enumerate(self.__board):
            for x, cell in enumerate(line):
                if not cell:
                    res.add((x, y))
        return res

    def make_turn(self, board: List[List[int]]) -> Tuple[int, int]:
        self.__board = board
        empty_cells = self.__get_empty_cells()
        return choice(list(empty_cells))
