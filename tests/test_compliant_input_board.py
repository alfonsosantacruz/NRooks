#!/usr/bin/python

import unittest
import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import solver

class TestCompliance(unittest.TestCase):

    def test_non_compliant_board_on_col(self):
        """
        Unit test to determine whether the solver can flag inputs with mistakenly placed rooks on columns
        """
        test_board = [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0]
        ]

        solved_board, status = solver.solve_nrooks(test_board)
        self.assertFalse(solved_board, "Should be False")
        self.assertEqual(status, "Error: More than one rook in a single column", "Should be an empty String")

    def test_non_compliant_board_on_row(self):
        """
        Unit test to determine whether the solver can flag inputs with mistakenly placed rooks on rows
        """

        test_board = [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1]
        ]

        solved_board, status = solver.solve_nrooks(test_board)
        self.assertFalse(solved_board, "Should be False")
        self.assertEqual(status, "Error: More than one rook in a single row", "Should be an empty String")

if __name__ == '__main__':
    unittest.main()