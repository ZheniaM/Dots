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

if __name__ == '__main__':
    unittest.main()