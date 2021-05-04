import unittest
from menumodules.gamemenu import GameMenu

class TestGameMenu(unittest.TestCase):
    def setUp(self):
        self.gamemenu = GameMenu()
    def test_setup_running_is_False(self):
        self.assertEqual(False, self.gamemenu.running)
    def test_click_on_back_button_makes_running_false(self):
        self.gamemenu.running = True
        self.gamemenu.click((76,501))
        self.assertEqual(False,self.gamemenu.running)
    def test_not_clicking_back_button_makes_running_true(self):
        self.gamemenu.running = True
        self.gamemenu.click((74,499))
        self.assertEqual(True, self.gamemenu.running)
    