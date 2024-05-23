from abc import ABC
from typing import List, Tuple


class Opponent(ABC):
    def make_turn(self, board: List[List[int]]) -> Tuple[int, int]:
        ...
