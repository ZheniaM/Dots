from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


class Button(QPushButton):
    def __init__(self, x: int, y: int,
                 width: int, height: int,
                 name: str, parrent: QWidget) -> None:
        super().__init__(name, parrent)
        self.setGeometry(x, y, width, height)
