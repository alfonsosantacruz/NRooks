import numpy as np
import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import solver

N = 8

def check_completed_nrooks_compliant(board):
    """
    Given a solved board, checks that the solution is satisfiable.
    """
    for coordinate in range(len(board)):
        if solver.count_rooks_at_row(board, coordinate) != 1:
            return False
        if solver.count_rooks_at_col(board, coordinate) != 1:
            return False
    return True

def generate_random_board(num_rooks):
    """
    Given a number of rooks, returns a board with that amount of rooks 
    randomly placed at non-attacking positions

    If the number of rooks is larger than N, defaults to return an empty board.
    """
    board = np.zeros([N, N], dtype=int).tolist()
    if N >= num_rooks:
        rows, cols = list(range(0, N)), list(range(0, N))
        for _ in range(num_rooks):
            row, col = np.random.choice(rows), np.random.choice(cols)
            board[row][col] = 1
            rows.remove(row)
            cols.remove(col)
    return board