from random import choice
from opponents.opponent import Opponent
from game_state import GameState
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

    def __get_self_cells(self) -> Set[Tuple[int, int]]:
        self_cells: set[tuple[int, int]] = set()
        for y, line in enumerate(self.__board): 
            for x, cell in enumerate(line):
                if cell == 16:
                    self_cells.add((x, y))
        return self_cells

    def __get_bot_cells(self) -> Set[Tuple[int, int]]:
        bot_cells: set[tuple[int, int]] = set()
        for y, line in enumerate(self.__board): 
            for x, cell in enumerate(line):
                if cell == 32:
                    bot_cells.add((x, y))
        return bot_cells

    def __near_bot_cells(self) -> Set[Tuple[int, int]]:
        bot_cells = self.__get_bot_cells()
        near_bot_cells = GameState.get_neighbours(bot_cells)
        return near_bot_cells

    def __near_self_cells(self) -> Set[Tuple[int, int]]:
        self_cells = self.__get_self_cells()
        near_self_cells = GameState.get_neighbours(self_cells)
        return near_self_cells

    def make_turn(self, board: List[List[int]]) -> Tuple[int, int]:
        self.__board = board
        empty_cells = self.__get_empty_cells()
        self_cells = self.__get_self_cells()
        if len(self_cells) == 0:
            return choice(list(empty_cells))
        else:
            near_self_cells = list(self.__near_self_cells())
            near_bot_cells = list(self.__near_bot_cells())
            coordinates = []
            for i in near_bot_cells + near_self_cells:
                if i in empty_cells:
                    coordinates.append(i)
            return choice(coordinates)

