import unittest
from cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell_with_a_mine=Cell(True, False, False)
        self.cell_without_a_mine=Cell(False, False, False)
    def test_cell_is_mine(self):
        self.assertEqual(self.cell_with_a_mine.bomb, True)
    def test_cell_is_empty(self):
        self.assertEqual(self.cell_without_a_mine.bomb,False)
