import unittest
from menumodules.mainmenu import MainMenu

class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.mainmenu = MainMenu()
    def test_setup_makes_screensize_correct(self):
        self.assertEqual(600, self.mainmenu.screen_height)
        self.assertEqual(500, self.mainmenu.screen_width)
    def test_setup_makes_colors_correct(self):
        self.assertEqual((140, 140, 150), self.mainmenu.button_color)
        self.assertEqual((50, 50, 50), self.mainmenu.background_color)