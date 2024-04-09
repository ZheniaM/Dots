from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, x: int, y: int,
                 width: int, height: int,
                 name: str) -> None:
        super().__init__(name, self)
        self.setGeometry(x, y, width, height)
