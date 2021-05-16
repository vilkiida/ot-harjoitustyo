import unittest
from othermodules.highscores_page import HighscorePage

class TestHighscorePage(unittest.TestCase):
    def setUp(self):
        self.easy = HighscorePage("easy")
        self.mhard = HighscorePage("mediumhard")
        self.expert = HighscorePage("expert")
    def test_setup_running_is_False(self):
        self.assertEqual(False, self.easy.running)
        self.assertEqual(False, self.mhard.running)
        self.assertEqual(False, self.expert.running)
    def test_click_on_back_button_makes_running_false(self):
        self.easy.running = True
        self.mhard.running = True
        self.expert.running = True
        self.easy.left_click((76,501))
        self.assertEqual(False, self.easy.running)
        self.mhard.left_click((76,501))
        self.assertEqual(False, self.mhard.running)
        self.expert.left_click((76,501))
        self.assertEqual(False, self.expert.running)
    def test_not_clicking_on_back_button_keeps_running_true(self):
        self.easy.running = True
        self.mhard.running = True
        self.expert.running = True
        self.easy.left_click((74,499))
        self.assertEqual(True, self.easy.running)
        self.mhard.left_click((74,499))
        self.assertEqual(True, self.mhard.running)
        self.expert.left_click((74,499))
        self.assertEqual(True, self.expert.running)