import json
import solver
import copy

# To run all unit tests before the execution of the app
# import os
# os.system('python3 -m unittest discover tests')

print("\n\nSubmit your board as a list of lists with zeroes and ones, where one represents a rook and zero represents an empty space.")
print("Remember that your board should be contained in one line, since zsh might consider it a bad pattern.\n\n")
board = json.loads(input())

print("\n\n")

solved_board, status = solver.solve_nrooks(copy.deepcopy(board))
print("Initial board:\n\n" + solver.print_board(board) + "\n\nSolving...\n\n")
print(solver.print_board(solved_board) if solved_board else status)

print("\n\n")