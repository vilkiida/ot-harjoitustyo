import unittest
from gamemodules.game import Game
from gamemodules.field import Field

class TestGame(unittest.TestCase):
    def setUp(self):
        self.field = Field(9,8,10)
        self.game = Game(self.field, 50, "testi")
    def test_setup_running_is_False(self):
        self.assertEqual(False, self.game.running)
    def test_setup_game_is_not_lost(self):
        self.assertEqual(False, self.game.game_lost)
    def test_setup_game_is_not_won(self):
        self.assertEqual(False, self.game.game_won)
    def test_setup_game_field_height_correct(self):
        self.assertEqual(9, self.game.field.height)
    def test_setup_game_field_width_correct(self):
        self.assertEqual(8, self.game.field.width)
    def test_setup_game_field_mine_amount_correct(self):
        self.assertEqual(10, self.game.field.how_many_mines)
    def test_setup_all_cells_are_unopened(self):
        all_closed=True
        for y in range(self.game.field_height):
            for x in range(self.game.field_width):
                if self.game.field.field[y][x].opened == True:
                    all_closed=False
        self.assertEqual(True, all_closed)
    def test_setup_screen_height_correct(self):
        height=50*9+50
        self.assertEqual(height, self.game.screen_height)
    def test_setup_screen_width_correct(self):
        width=50*8
        self.assertEqual(width, self.game.screen_width)
    def test_game_over_lost_makes_game_lost_true(self):
        self.game.game_over_lost(0,0)
        self.assertEqual(True, self.game.game_lost)
    def test_game_over_lost_makes_all_cells_open(self):
        self.game.game_over_lost(0,0)
        all_open=True
        for y in range(self.game.field_height):
            for x in range(self.game.field.width):
                if self.game.field.field[y][x].opened == False:
                    all_open=False
        self.assertEqual(True, all_open)
    def test_game_over_won_makes_game_won_true(self):
        self.game.end_time = 10320
        self.game.start_time = 10200
        self.game.game_over_won()
        self.assertEqual(True, self.game.game_won)
    def test_game_over_won_makes_all_cells_open(self):
        self.game.end_time = 10320
        self.game.start_time = 10200
        self.game.game_over_won()
        all_open=True
        for y in range(self.game.field_height):
            for x in range(self.game.field.width):
                if self.game.field.field[y][x].opened == False:
                    all_open=False
        self.assertEqual(True, all_open)
    def test_check_for_win_works_if_True(self):
        for y in range(self.game.field_height):
            for x in range(self.game.field_width):
                if self.game.field.field[y][x].mine == False:
                    self.game.field.field[y][x].opened = True
        self.assertEqual(True, self.game.check_for_win())
    def test_check_for_win_works_if_False(self):
        self.assertEqual(False, self.game.check_for_win())
    def test_left_click_opens_an_unopened_cell(self):
        self.game.left_click((40, 40))
        self.assertEqual(True, self.game.field.field[0][0].opened)
    def test_left_click_wont_open_a_flagged_cell_if_not_a_mine(self):
        self.game.field.field[0][0].mine = False
        self.game.field.field[0][0].flagged = True
        self.game.left_click((40, 40))
        self.assertEqual(False, self.game.field.field[0][0].opened)
    def test_left_click_wont_open_a_questionmarked_cell_if_not_a_mine(self):
        self.game.field.field[0][0].mine = False
        self.game.field.field[0][0].questionmark = True
        self.game.left_click((40, 40))
        self.assertEqual(False, self.game.field.field[0][0].opened)
    def test_left_click_wont_open_a_flagged_cell_if_a_mine(self):
        self.game.field.field[0][0].mine = True
        self.game.field.field[0][0].flagged = True
        self.game.left_click((40, 40))
        self.assertEqual(False, self.game.field.field[0][0].opened)
    def test_left_click_wont_open_a_questionmarked_cell_if_a_mine(self):
        self.game.field.field[0][0].mine = True
        self.game.field.field[0][0].questionmark = True
        self.game.left_click((40, 40))
        self.assertEqual(False, self.game.field.field[0][0].opened)
    def test_right_click_wont_mark_opened_cell_a_flag(self):
        self.game.field.field[0][0].opened = True
        self.game.right_click((40, 40))
        self.assertEqual(False, self.game.field.field[0][0].flagged)
    def test_right_click_wont_mark_opened_cell_a_questionmark(self):
        self.game.field.field[0][0].opened = True
        self.game.right_click((40, 40))
        self.assertEqual(False, self.game.field.field[0][0].questionmark)
    def test_right_click_marks_unopened_cell_a_flag(self):
        self.game.right_click((40, 40))
        self.assertEqual(True, self.game.field.field[0][0].flagged)
    def test_right_click_marks_flagged_cell_a_questionmarks(self):
        self.game.field.field[0][0].flagged = True
        self.game.right_click((40, 40))
        self.assertEqual(True, self.game.field.field[0][0].questionmark)
    def test_right_click_makes_questionmarked_cell_clear(self):
        self.game.field.field[0][0].questionmark = True
        self.game.right_click((40, 40))
        no_markings = True
        if self.game.field.field[0][0].flagged == True:
            no_markings = False
        if self.game.field.field[0][0].questionmark == True:
            no_markings = False
        self.assertEqual(True, no_markings)
    def test_is_first_move_returns_True_correctly(self):
        self.assertEqual(True, self.game.is_first_move())
    def test_is_first_move_return_False_correclty(self):
        for y in range(self.game.field_height):
            for x in range(self.game.field_width):
                if self.game.field.field[y][x].mine == False:
                    self.game.field.field[y][x].opened = True
        self.assertEqual(False, self.game.is_first_move())
    def test_handle_time_works_correctly(self):
        self.game.start_time = 10200
        self.game.end_time = 10320
        self.game.handle_time()
        self.assertEqual("0:2:0", self.game.time)
    def test_handle_time_works_correctly_if_no_end_time(self):
        self.game.start_time = 10200
        self.game.handle_time()
        self.assertEqual("NO TIME", self.game.time)
    def test_handle_time_works_correctly_if_no_start_time(self):
        self.game.end_time = 10320
        self.game.handle_time()
        self.assertEqual("NO TIME", self.game.time)
    def test_game_over_lost_makes_handle_time_work_correctly(self):
        self.game.start_time = 10200
        self.game.end_time = 10320
        self.game.game_over_lost(0,0)
        self.assertEqual("0:2:0", self.game.time)
    def test_game_over_won_makes_handle_time_work_correctly(self):
        self.game.start_time = 10200
        self.game.end_time = 10320
        self.game.game_over_won()
        self.assertEqual("0:2:0", self.game.time)
    def test_clicking_back_button_turns_running_false(self):
        self.game.running = True
        self.game.left_click((11,self.game.screen_height - 39))
    def test_count_found_mines_works(self):
        self.assertEqual(0, self.game.count_found_mines())
        self.game.field.field[0][0].flagged = True
        self.game.field.field[0][1].flagged = True
        self.assertEqual(2, self.game.count_found_mines())
        self.game.game_won = True
        self.assertEqual(10, self.game.count_found_mines())