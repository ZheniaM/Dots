from __future__ import annotations
from abc import ABC


class Screen(ABC):
    def __init__(self, scr: Screen) -> None:
        super().__init__()
        self.next_screen = scr

    def draw(self) -> None:
        ...
