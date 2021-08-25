"""
Tic Tac Toe Player
"""

import math
import copy
import ipdb
from typing import final

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

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    
    nextMove = player(board)

    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = nextMove
    
    return newBoard


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
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    nextMove = player(board)
    
    if nextMove == X:
        print("X turn")
        v, action = maxValue(board)
        return action
    else:
        # ipdb.set_trace()
        print("O turn")
        v, action = minValue(board)
        return action

def maxValue(board):

    # ipdb.set_trace()

    value = -2
    finalAction = (0, 0)

    if terminal(board):
        return utility(board), finalAction

    for action in actions(board):
        minV, a = minValue(result(board, action))
        if minV == 1:
            return minV, action
        elif minV > value:
            finalAction = action
            value = minV

    return value, finalAction

def minValue(board):

    # ipdb.set_trace()

    value = 2
    finalAction = (0, 0)

    if terminal(board):
        return utility(board), finalAction

    for action in actions(board):
        maxV, a = maxValue(result(board, action))
        # if board == [[X, EMPTY, EMPTY],
        #     [X, X, EMPTY],
        #     [O, EMPTY, O]]:
        #     print("Outer function")
        if maxV == -1:
            return maxV, action
        elif maxV < value:
            finalAction = action
            value = maxV

    return value, finalAction

# if __name__ == "__main__":
#     # ipdb.set_trace()
#     board = initial_state()
#     # print(player(board))
#     # print(actions(board))
#     # board = result(board, (0,1))
#     # print(actions(board))
#     # print(board)
#     # print(player(board))
#     # board = result(board, (2,1))
#     # print(actions(board))
#     # print(board)
#     # print(player(board))
#     # board = result(board, (0,2))
#     # print(actions(board))
#     # print(board)
#     # print(player(board))
#     # board = result(board, (2,2))
#     # print(actions(board))
#     # print(board)
#     # print(terminal(board))
#     # board = result(board, (0,0))
#     # print(actions(board))
#     # print(terminal(board))
#     # board = result(board, (1,0))
#     # print(actions(board))
#     # board = result(board, (1,1))
#     # print(actions(board))
#     # board = result(board, (1,2))
#     # print(actions(board))
#     # board = result(board, (2,0))
#     # print(actions(board))
#     # print(terminal(board))
#     board =[[EMPTY, EMPTY, O],
#             [O, X, EMPTY],
#             [X, EMPTY, EMPTY]]
#     # print(winner(board))
#     print(minimax(board))