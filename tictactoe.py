"""
Tic Tac Toe Player
"""

import math
import copy
from typing import final

X = "X"
O = "O"
EMPTY = None

# Game scores
X_WINS = 1
O_WINS = -1
DRAW = 0

MIN_VALUE = -2
MAX_VALUE = 2

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
    remainingMoves = sum(row.count(EMPTY) for row in board)
    if remainingMoves % 2 != 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = [(i, j) for i, row in enumerate(board) for j, value in enumerate(row) if value == EMPTY]
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    if indexOutOfBounds(i, board):
        raise Exception("Invalid index")

    j = action[1]
    arr = board[i]
    if indexOutOfBounds(j, arr):
        raise Exception("Invalid index")

    pos = arr[j]
    if pos != EMPTY:
        raise Exception("Invalid action")
    
    nextMove = player(board)

    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = nextMove
    
    return newBoard

def indexOutOfBounds(index, arr):
    return index not in range(-len(arr), len(arr))

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    movesOfX = [(i, j) for i, row in enumerate(board) for j, value in enumerate(row) if value == X]
    if checkWinPattern(movesOfX):
        return X

    movesOfO = [(i, j) for i, row in enumerate(board) for j, value in enumerate(row) if value == O]
    if checkWinPattern(movesOfO):
        return O

    return None

def checkWinPattern(moves):
    """
    Returns the winner of the game, if there is one.
    """
    winPatterns = [[(0,0), (0,1), (0,2)],
                   [(1,0), (1,1), (1,2)],
                   [(2,0), (2,1), (2,2)],
                   [(0,0), (1,0), (2,0)],
                   [(0,1), (1,1), (2,1)],
                   [(0,2), (1,2), (2,2)],
                   [(0,0), (1,1), (2,2)],
                   [(0,2), (1,1), (2,0)]]
    
    for pattern in winPatterns:
        if all(move in moves for move in pattern):
            return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    return sum(row.count(EMPTY) for row in board) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return X_WINS
    elif w == O:
        return O_WINS
    else:
        return DRAW


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    nextMove = player(board)
    
    if nextMove == X:
        v, action = maxValue(board)
        return action
    else:
        v, action = minValue(board)
        return action

def maxValue(board):

    value = MIN_VALUE
    finalAction = None

    if terminal(board):
        return utility(board), finalAction

    for action in actions(board):
        minV, a = minValue(result(board, action))

        # Since 1 is the max possible score, if we find that for max player no need to search further
        if minV == X_WINS:
            return minV, action
        elif minV > value:
            finalAction = action
            value = minV

    return value, finalAction

def minValue(board):

    value = MAX_VALUE
    finalAction = None

    if terminal(board):
        return utility(board), finalAction

    for action in actions(board):
        maxV, a = maxValue(result(board, action))

        # Since -1 is the min possible score, if we find that for min player no need to search further
        if maxV == O_WINS:
            return maxV, action
        elif maxV < value:
            finalAction = action
            value = maxV

    return value, finalAction