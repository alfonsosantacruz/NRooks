import unittest
import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import solver

class TestInput(unittest.TestCase):
    def test_input_board_with_diff_dims(self):
        """
        Unit test to determine whether the solver can handle input with incorrect dimensions
        """
        test_boards = [
            [
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            [
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0]
            ]
        ]

        for tboard in test_boards:
            solved_board, status = solver.solve_nrooks(tboard)
            self.assertFalse(solved_board, "Should be False")
            self.assertEqual(status, "Error: Initial board dimensions not 8x8", "Should be an empty String")

if __name__ == '__main__':
    unittest.main()