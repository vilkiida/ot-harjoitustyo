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
    
    # ...