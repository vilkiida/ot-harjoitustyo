import unittest
from highscores_menu import HighscoresMenu

class TestHighscoresMenu(unittest.TestCase):
    def setUp(self):
        self.hsmenu = HighscoresMenu()
    def test_setup_running_is_False(self):
        self.assertEqual(False, self.hsmenu.running)
    def test_click_on_back_button_makes_running_false(self):
        self.hsmenu.running = True
        self.hsmenu.click((76,501))
        self.assertEqual(False,self.hsmenu.running)
    def test_not_clicking_back_button_makes_running_true(self):
        self.hsmenu.running = True
        self.hsmenu.click((74,499))
        self.assertEqual(True, self.hsmenu.running)