"""
Tic Tac Toe Player
"""
import copy
import math
from collections import Counter

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # In the initial game state, X gets the first move
    if board == initial_state():
        return X
    else:
        flattened_list = [cell for boardLine in board for cell in boardLine]
        count_dict = Counter(flattened_list)
        noX = count_dict[X]
        noO = count_dict[O]
        return X if noX <= noO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    admited_values = range(0, 3)
    if row not in admited_values or col not in admited_values:
        raise Exception('Forbidden action! Out of bounds.')
    selectedCell = board[row][col]
    if selectedCell != EMPTY:
        raise Exception('Forbidden action! The current action takes to a non-empty position on the board.')
    newBoard = copy.deepcopy(board)
    newBoard[row][col] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
