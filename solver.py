import numpy as np

N = 8

def transpose(table):
    """
    Uses numpy to return the transposed input table as a list of lists
    """
    return np.transpose(np.array(table)).tolist()

def count_rooks_at_row(board, row):
    """
    Given a board and a row, returns the number of rooks that exist in that row.
    """
    return board[row].count(1)

def count_rooks_at_col(board, col):
    """
    Given a board and a column, returns the number of rooks that exist in that column
    """
    return count_rooks_at_row(transpose(board), col)

def count_all_pieces(board):
    """
    Given a board, returns the number of rooks that exist in that board.
    Nice implementation yet never used since doesn't work for empty boards.
    """
    unique, counts = np.unique(np.array(board), return_counts=True)
    d = dict(zip(unique, counts))

    return d[1]

def count_all_rooks(board):
    """
    Given a board, returns the number of rooks that exist in that board.
    """
    count = 0
    for row in range(len(board)):
        count += count_rooks_at_row(board, row)
    return count

def print_board(board):
    """
    Returns a board as a string with the zeros and ones replaces so that it can be printed nicely.
    """
    return "\n".join([ " ".join(
        [ "R" if col == 1 else "C" if col == 1 else "·" for col in row ]
    ) for row in board])
    
def add_rook(board, row, col):
    """
    Given a board and a set of row, column coordinates, places a rook in the board at the coordinates,
    then returns the updated board.
    """
    board[row][col] = 1
    return board

def get_nrooks_states(board):
    """
    Given a board, returns all the possible subsequent states of the board.
    A subsequent state is a board with one more rook placed at a possible position.
    A given state can have multiple to none subsequent states.
    """
    # Checks whether the board is a complete board first
    if is_complete(board):
        return [board]

    # If not a complete board, then computes the subsequent states and returns them.
    num_rooks = count_all_rooks(board)
    if num_rooks < N and board != []:
        ans = []
        for col in range(0, num_rooks + 1):
            for row in range(0, N):
                if count_rooks_at_row(board, row) != 1 and count_rooks_at_col(board, col) != 1 and board[row][col] != 1:
                    ans.append(add_rook(board, row, col))
        return ans
    return []

def is_complete(board):
    """
    Checks whether the board has all the rooks in place
    """
    return count_all_rooks(board) == N 

def is_board_right(board):
    """
    Checks whether there is an issue with the input board.
    """
    # Checks whether the dims of the board are correct
    if len(board) != N or len(board[0]) != N:
        return "Error: Initial board dimensions not 8x8"
    # Checks whether the board has more than 8 rooks placed already, which is the limit
    elif count_all_rooks(board) > N:
        return "Error: There are more than 8 rooks in the initial board"
    # Checks whether initial board has a misplaced rook.
    for coordinate in range(len(board)):
        if count_rooks_at_row(board, coordinate) > 1:
            return "Error: More than one rook in a single row"
        if count_rooks_at_col(board, coordinate) > 1:
            return "Error: More than one rook in a single column"
    return ""

# Solve for n-rooks
def solve_nrooks(initial_board):
    """
    Given an initial board, runs DFS through the states until a first completed state shows up, if any.
    Starts from the assumption that all initial boards that are compliant with the rules have a solution
    """
    status = is_board_right(initial_board) 
    if not status:    
        states = [initial_board]
        while len(states) > 0:
            for s in get_nrooks_states(states.pop()):
                if is_complete(s):
                    return s, status
                states.append(s)
        return False, "No solution found, my bad..."
    return False, status