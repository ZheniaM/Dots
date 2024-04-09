from opponents.opponent import Opponent


class OnThisPC(Opponent):
    def __init__(self) -> None:
        super().__init__()

    def make_turn(self, board: list[list[int]]) -> tuple[int, int]:
        return super().make_turn(board)  # TODO
