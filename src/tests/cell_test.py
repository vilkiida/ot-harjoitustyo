import unittest
from gamemodules.cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()

    def test_is_a_mine_returns_true(self):
        self.cell.mine = True
        self.assertEqual(True, self.cell.is_a_mine())

    def test_is_a_mine_returns_false(self):
        self.assertEqual(False, self.cell.is_a_mine())

    def test_is_opened_returns_true(self):
        self.cell.opened = True
        self.assertEqual(True, self.cell.is_opened())

    def test_is_opened_returns_false(self):
        self.assertEqual(False, self.cell.is_opened())
    
    def test_is_flagged_returns_true(self):
        self.cell.flagged = True
        self.assertEqual(True, self.cell.is_flagged())
    
    def test_is_flagged_returns_false(self):
        self.assertEqual(False, self.cell.is_flagged())
    
    def test_is_not_marked_returns_true(self):
        self.assertEqual(True, self.cell.is_not_marked())

    def test_is_not_marked_returns_false(self):
        self.cell.flagged = True
        self.assertEqual(False, self.cell.is_not_marked())

    def test_is_questionmark_returns_true(self):
        self.cell.questionmark = True
        self.assertEqual(True, self.cell.is_questionmark())
    
    def test_is_questionmark_returns_false(self):
        self.assertEqual(False, self.cell.is_questionmark())
    
    def test_turn_into_a_mine_works(self):
        self.cell.turn_into_a_mine()
        self.assertEqual(True, self.cell.mine)
    
    def test_mark_neigbours_works(self):
        neighbours=[(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)]
        self.cell.mark_neighbours(neighbours)
        self.assertEqual(neighbours, self.cell.neighbours)
    
    def test_mark_neighbour_mines_works(self):
        neighbour_mines=5
        self.cell.mark_neigbour_mines(neighbour_mines)
        self.assertEqual(neighbour_mines, self.cell.neighbour_mines)
    
    def test_mark_flag_works(self):
        self.cell.mark_flagg()
        self.assertEqual(True, self.cell.flagged)
    
    def test_mark_questionmark_works(self):
        self.cell.mark_questionmark()
        self.assertEqual(True, self.cell.questionmark)
    
    def test_remove_markings_works(self):
        self.cell.questionmark = True
        self.cell.remove_markings()
        self.assertEqual(False, self.cell.questionmark)