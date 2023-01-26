"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    counter = 0

    for row in board:
        for item in row:
            if item is not None:
                counter += 1

    if counter % 2 == 0:
        return 'X'
    else:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not None:
        raise Exception("Board cell already filled.")
    board_copy = deepcopy(board)
    board_copy[action[0]][action[1]] = player(board_copy)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] != None:
                return row[0]
            else:
                return None

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != None:
                return board[0][i]
            else:
                return None

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            return board[0][0]
        else:
            return None

    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != None:
            return board[2][0]
        else:
            return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for row in board:
            for item in row:
                if item == None:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) and winner(board) == X:
        return 1
    elif winner(board) and winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # if the board is terminal return None, no actions to take
    if terminal(board):
        return None

    # a list of all the possible actions with their values
    possible_actions = []

    for action in actions(board):
        # we iterate through all the possible actions and get the according value
        # depending on max or min player, then we append the tuple to the array
        if player(board) == X:
            # if it is the max player, we get the minimum value of the action,
            # because it will be the min player's turn
            possible_actions.append((min_value(result(board, action)), action))
        elif player(board) == O:
            # if it is the max player, we get the maximum value of the action,
            # because it will be the max player's turn
            possible_actions.append((max_value(result(board, action)), action))

    # we return the action with the most priority value depending if
    # it is the min or max player.
    if player(board) == X:
        return max(possible_actions, key=lambda tup: tup[0])[1]
    elif player(board) == O:
        return min(possible_actions, key=lambda tup: tup[0])[1]


def min_value(board):
    value = math.inf

    if terminal(board):
        # if terminal board, we return the utility value of the board
        return utility(board)

    for action in actions(board):
        # we iterate again through the possible actions and return the lowest value.
        value = min(value, max_value(result(board, action)))

    return value


def max_value(board):
    value = -math.inf

    if terminal(board):
        # if terminal board, we return the utility value of the board
        return utility(board)

    for action in actions(board):
        # we iterate again through the possible actions and return the highest value.
        value = max(value, min_value(result(board, action)))

    return value
