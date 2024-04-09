from abc import ABC


class Opponent(ABC):
    def make_turn(self, board: list[list[int]]) -> tuple[int, int]:
        ...
