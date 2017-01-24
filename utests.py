import unittest
from game import *

class TestStringMethods(unittest.TestCase):

    def test_printing_emty_board(self):
        board = Board(5)
        board.draw_board()
        board.add_bomb(1,2)
        board.add_bomb(1,3)
        board.draw_board()
        board.count_bobmbs_for_all()
        board.draw_board()







if __name__ == '__main__':
    unittest.main()