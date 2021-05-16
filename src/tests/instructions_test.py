import unittest
from othermodules.instructions import Instruction

class TestGameMenu(unittest.TestCase):
    def setUp(self):
        self.instructions = Instruction()
    def test_setup_running_is_False(self):
        self.assertEqual(False, self.instructions.running)
    def test_click_on_back_button_makes_running_false(self):
        self.instructions.running = True
        self.instructions.left_click((76,501))
        self.assertEqual(False,self.instructions.running)
    def test_not_clicking_back_button_makes_running_true(self):
        self.instructions.running = True
        self.instructions.left_click((74,499))
        self.assertEqual(True, self.instructions.running)