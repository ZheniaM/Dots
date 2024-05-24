import unittest
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from screens.screen import Title, Multiplayer, Game, Pause, End
from game_state import GameState
from opponents.bot import Bot

class TestScreens(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_title_screen(self):
        title_screen = Title(QWidget())
        self.assertEqual(title_screen.title, "Title Screen")
        self.assertIsInstance(title_screen.parent, QWidget)
        self.assertIsInstance(title_screen.layout, QVBoxLayout)

    def test_multiplayer_screen(self):
        multiplayer_screen = Multiplayer(QWidget(), (10, 10))
        self.assertEqual(multiplayer_screen.title, "Multiplayer Screen")
        self.assertIsInstance(multiplayer_screen.parent, QWidget)
        self.assertIsInstance(multiplayer_screen.layout, QVBoxLayout)
        
    def test_game_screen(self):
        game_state = GameState((10, 10), Bot())
        game_screen = Game(QWidget(), (10, 10), Bot(), game_state)
        self.assertEqual(game_screen.title, "Game Screen")
        self.assertIsInstance(game_screen.parent, QWidget)
        self.assertIsInstance(game_screen.layout, QVBoxLayout)

    def test_pause_screen(self):
        game_state = GameState((10, 10), Bot())
        game_screen = Game(QWidget(), (10, 10), Bot(), game_state)
        pause_screen = Pause(QWidget(), game_screen, game_state)
        self.assertEqual(pause_screen.title, "Pause Screen")
        self.assertIsInstance(pause_screen.parent, QWidget)
        self.assertIsInstance(pause_screen.layout, QVBoxLayout)

    def test_end_screen(self):
        end_screen = End(QWidget(), (10, 10), Bot())
        self.assertEqual(end_screen.title, "End Screen")
        self.assertIsInstance(end_screen.parent, QWidget)
        self.assertIsInstance(end_screen.layout, QVBoxLayout)

    def tearDown(self):
        self.app.quit()


class TestBot(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = Bot()

    def test_get_empty_cells(self):
        board = [
            [0, 0, 16],
            [32, 16, 0],
            [0, 0, 0]
        ]
        self.bot._Bot__board = board
        empty_cells = self.bot._Bot__get_empty_cells()
        expected_empty_cells = {(0, 0), (1, 0), (2, 2), (0, 2), (1, 2), (2, 2), (2, 1)}
        self.assertEqual(empty_cells, expected_empty_cells)

    def test_get_self_cells(self):
        board = [
            [0, 0, 16],
            [32, 16, 0],
            [0, 0, 0]
        ]
        self.bot._Bot__board = board
        self_cells = self.bot._Bot__get_self_cells()
        expected_self_cells = {(2, 0), (1, 1)}
        self.assertEqual(self_cells, expected_self_cells)

    def test_get_bot_cells(self):
        board = [
            [0, 0, 16],
            [32, 16, 0],
            [0, 0, 0]
        ]
        self.bot._Bot__board = board
        bot_cells = self.bot._Bot__get_bot_cells()
        expected_bot_cells = {(0, 1)}
        self.assertEqual(bot_cells, expected_bot_cells)

    def test_near_bot_cells(self):
        board = [
            [0, 0, 16],
            [32, 16, 0],
            [0, 0, 0]
        ]
        self.bot._Bot__board = board
        near_bot_cells = set(self.bot._Bot__near_bot_cells())
        expected_near_bot_cells = {(0, 0), (0, 2), (1, 1)}
        self.assertEqual(near_bot_cells, expected_near_bot_cells)

    def test_near_self_cells(self):
        board = [
            [0, 0, 16],
            [32, 16, 0],
            [0, 0, 0]
        ]
        self.bot._Bot__board = board
        near_self_cells = set(self.bot._Bot__near_self_cells())
        expected_near_self_cells = {(1, 0), (2, 1), (0, 1), (1, 2), (3, 0)}
        self.assertEqual(near_self_cells, expected_near_self_cells)

if __name__ == '__main__':
    unittest.main()