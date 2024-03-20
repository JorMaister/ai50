"""
Tic Tac Toe Player
"""
import copy
import math
import random
from collections import Counter

X = "X"
O = "O"
EMPTY = None
board_dim = 3


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
        _, x_list, o_list = parse_board(board)
        return X if len(x_list) <= len(o_list) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions, _, _ = parse_board(board)
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
    _, x_pos_list, o_pos_list = parse_board(board)
    noX = len(x_pos_list)
    noO = len(o_pos_list)
    if noX < 3 and noO < 3:
        return None
    # Check the X player
    if isAWin(x_pos_list):
        return X
    if isAWin(o_pos_list):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        if len(actions(board)) == 0:
            return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_result = winner(board)
    if game_result == X:
        return 1
    elif game_result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Given a state s
    # The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
    # The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).
    current_player = player(board)
    if current_player == X:
        _, act = min_value(board)
    else:
        _, act = max_value(board)
    return act


# Aux functions
def parse_board(board):
    """
    Returns two lists with the (i, j) position for empty, X, and O values
    """
    empty_pos_list = set()
    x_pos_list = set()
    o_pos_list = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            current_val = board[i][j]
            current_ind = (i, j)
            if current_val == X:
                x_pos_list.add(current_ind)
            elif current_val == O:
                o_pos_list.add(current_ind)
            else:
                empty_pos_list.add(current_ind)

    return empty_pos_list, x_pos_list, o_pos_list


def isAWin(positions):
    """
    Checks if the given positions correspond to a win
    """
    # Look for vertical and horizontal winning lines
    rows, cols = zip(*positions)
    rows_count_dict = Counter(rows)
    cols_count_dict = Counter(cols)
    for i in range(board_dim):
        if rows_count_dict[i] == board_dim or cols_count_dict[i] == board_dim:
            return True

    # Look for diagonal winning lines
    diagonal_win_up = [(0, 0), (1, 1), (2, 2)]
    diagonal_win_down = [(2, 0), (1, 1), (0, 2)]
    for pos in positions:
        if pos in diagonal_win_down:
            diagonal_win_down.remove(pos)
        if pos in diagonal_win_up:
            diagonal_win_up.remove(pos)
        if len(diagonal_win_up) == 0 or len(diagonal_win_down) == 0:
            return True

    return False


def max_value(board):
    if terminal(board):
        return utility(board), None
    # Initialization
    value = -math.inf
    # Possible actions
    action_list = actions(board)
    for current_action in action_list:
        resulting_board = result(board, current_action)
        current_value, _ = min_value(resulting_board)
        value = max(value, current_value)
        return value, current_action


def min_value(board):
    if terminal(board):
        return utility(board), None
    # Initialization
    value = math.inf
    # Possible actions
    action_list = actions(board)
    for current_action in action_list:
        resulting_board = result(board, current_action)
        current_value, _ = max_value(resulting_board)
        value = min(value, current_value)
        return value, current_action  # Break the loop if the min val is found

