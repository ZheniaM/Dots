from opponents.opponent import Opponent
from typing import List, Tuple


class LocalNet(Opponent):
    def __init__(self) -> None:
        super().__init__()

    def make_turn(self, board: List[List[int]]) -> Tuple[int, int]:
        return super().make_turn(board)  # TODO
