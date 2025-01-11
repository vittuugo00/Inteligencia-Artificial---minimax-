"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY,EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    count = 0
    for row in board:
        count += row.count(EMPTY)

    if count % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board):
        return None

    set_actions = set([])
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                set_actions.add((i,j))
    return set_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if isinstance(action, tuple) and len(action) == 2:
        i, j = action
    else:
        raise ValueError("Actions is not correct")

    board_copy = copy.deepcopy(board)

    if player(board) == X:
        board_copy[i][j] = X
    if player(board) == O:
        board_copy[i][j] = O

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    diagonally_left = board[0][0], board[1][1], board[2][2]
    diagonally_right = board[0][2], board[1][1], board[2][0]
    if X in diagonally_left and not (O in diagonally_left) and not (EMPTY in diagonally_left):
        winner = X
    elif O in diagonally_left and not (X in diagonally_left) and not (EMPTY in diagonally_left):
        winner = O
    if X in diagonally_right and not (O in diagonally_right) and not (EMPTY in diagonally_right):
        winner = X
    elif O in diagonally_right and not (X in diagonally_right) and not (EMPTY in diagonally_right):
        winner = O

    for column in zip(*board):
        if X in column and not (O in column) and not (EMPTY in column):
            winner = X
        elif O in column and not (X in column) and not (EMPTY in column):
            winner = O

    for row in board:
        if X in row and not (O in row) and not (EMPTY in row):
            winner = X
        elif O in row and not (X in row) and not (EMPTY in row):
            winner = O

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    finished = False
    emptys = 0

    for row in board:
        for cell in row:
            if cell == EMPTY:
                emptys += 1

    if not (winner(board) == None):
        return True
    if emptys == 0:
        return True

    return finished


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    util = winner(board)

    if util == X:
        return 1
    elif util == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        first_move = True
        for row in board:
            for cell in row:
                if cell != EMPTY:
                    first_move = False
        if first_move:
            return (1,1)

    if player(board) == X:
        v = float('-inf')
        for action in actions(board):
            value = min_value(result(board, action))
            if value > v:
                v = value
                best_action = action
        return best_action

    elif player(board) == O:
        v = float('inf')
        for action in actions(board):
            value = max_value(result(board, action))
            if value < v:
                v = value
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_func(value, max_value):
    if value > max_value:
        return value
    else:
        return max_value

def min_func(value, min_value):
    if value < min_value:
        return value
    else:
        return min_value