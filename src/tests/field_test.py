import unittest
from field import Field

class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field(9,8,10)
    def test_setup_height_correct(self):
        self.assertEqual(9, self.field.height)
    def test_setup_width_correct(self):
        self.assertEqual(8, self.field.width)
    def test_setup_mine_amount_correct(self):
        self.assertEqual(10, self.field.how_many_mines)
    def test_field_has_correct_height(self):
        self.assertEqual(9, len(self.field.field))
    def test_field_has_correct_width(self):
        self.assertEqual(8, len(self.field.field[0]))
    def test_field_has_correct_amount_of_mines(self):
        amount=0
        for y in range(0, self.field.height):
            for x in range(0, self.field.width):
                if self.field.field[y][x].mine:
                    amount += 1
        self.assertEqual(10, amount)
    def test_find_neighbours_finds_correct_cell1(self):
        self.assertEqual([(0,1), (1,0), (1,1)],self.field.field[0][0].neighbours)
    
    def test_is_cell_opened_works_if_True(self):
        self.field.field[0][0].opened = True
        self.assertEqual(True, self.field.is_cell_opened(0,0))
    def test_is_cell_opened_works_if_False(self):
        self.assertEqual(False, self.field.is_cell_opened(0,0))
    def test_is_cell_a_mine_works_if_True(self):
        self.field.field[0][0].mine = True
        self.assertEqual(True, self.field.is_cell_a_mine(0,0))
    def test_is_cell_a_mine_works_if_False(self):
        self.field.field[0][0].mine = False
        self.assertEqual(False, self.field.is_cell_a_mine(0,0))
    def test_mark_a_cell_makes_flagged_if_cell_unmarked(self):
        self.field.mark_a_cell(0,0)
        self.assertEqual(True, self.field.field[0][0].flagged)
    def test_mark_cell_makes_questionmark_if_cell_flagged(self):
        self.field.field[0][0].flagged = True
        self.field.mark_a_cell(0,0)
        self.assertEqual(True, self.field.field[0][0].questionmark)
    def test_mark_a_cell_makes_not_flagged_if_cell_questionmark(self):
        self.field.field[0][0].questionmark = True
        self.field.mark_a_cell(0,0)
        self.assertEqual(False, self.field.field[0][0].flagged)
    def test_mark_a_cell_makes_not_questionmark_if_cell_questionmark(self):
        self.field.field[0][0].questionmark = True
        self.field.mark_a_cell(0,0)
        self.assertEqual(False, self.field.field[0][0].questionmark)
    def test_open_all_works(self):
        self.field.open_all()
        all_open=True
        for y in range(self.field.height):
            for x in range(self.field.width):
                if self.field.field[0][0].opened == False:
                    all_open=False
        self.assertEqual(True, all_open)
    