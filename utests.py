import unittest
from game import *

class TestStringMethods(unittest.TestCase):

    def test_printing_emty_board(self):
        board = Board(10)
        board.draw_board()
        board.place_random_bomb(20)
        board.count_bobmbs_for_all()
        board.draw_board()







if __name__ == '__main__':
    unittest.main()