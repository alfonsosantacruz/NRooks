import numpy as np
import unittest
from utils import generate_random_board, check_completed_nrooks_compliant
import sys, os
import copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import solver

class TestSolution(unittest.TestCase):
    def test_multiple_random_boards(self):
        """
        Unit test that generates multiple random 8x8 boards with different number of rooks on it.
        Then, it solves the boards and asserts whether the solution is valid.

        It also prints the initial in solved boards around 50% percent of the time.
        """
        N = 8
        
        for i in range(N):
            board = generate_random_board(N, i)
            solved_board, status = solver.solve_nrooks(copy.deepcopy(board))
            
            if np.random.random() > 0.5:
                print(f"Number of rooks in initial board: {i}")
                print("Initial board:\n" + solver.print_board(board) + "\n\n")
                print ("Solved board:\n" + solver.print_board(solved_board) + "\n\n")

            self.assertTrue(check_completed_nrooks_compliant(solved_board), "Should be True")
            self.assertEqual(status, "", "Should be an empty String")

if __name__ == '__main__':
    unittest.main()