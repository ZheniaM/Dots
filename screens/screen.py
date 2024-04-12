from __future__ import annotations
from abc import ABC
from PyQt5.QtWidgets import QPushButton


class Screen(ABC):
    def __init__(self, scr: Screen) -> None:
        super().__init__()
        self.next_screen = scr

    def draw(self, buttons: list) -> None:
        self.window.setWindowTitle(self.title)
        self.window.resize(self.width, self.height)
        for button in buttons:
            self.layout.addWidget(button)
        self.window.show()
