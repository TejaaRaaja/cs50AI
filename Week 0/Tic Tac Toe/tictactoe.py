"""
Tic Tac Toe Player
"""

import math
import copy

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
    # Change method to counting separately if not working
    empty_count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                empty_count += 1
    
    if empty_count % 2 == 0:
        return O
    return X
        

def actions(board):
    """
    Returns a set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    row, col = action
    new_board = copy.deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def checkRow(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    return False

def checkColoumn(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkFirstDig(board, player):
    count = 0
    for i in range(len(board)):
        if board[i][i] == player:
            count += 1
    if count == 3:
        return True
    return False


def checkSecDig(board, player):
    count = 0
    n = len(board)
    for i in range(n):
        if board[i][n - i - 1] == player:
            count += 1
    if count == 3:
        return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkColoumn(board, X) or checkFirstDig(board, X) or checkSecDig(board, X):
        return X
    elif checkRow(board, O) or checkColoumn(board, O) or checkFirstDig(board, O) or checkSecDig(board, O):
        return O
    return None


def EmptySquares(board):
    for row in board:
        for col in row:
            if col == EMPTY:
                return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    elif EmptySquares(board):
        return False
    return True #TIE
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append((min_value(result(board, action)), action))
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1] #Returning the optimal move
    
    else:
        plays = []
        for action in actions(board):
            plays.append((max_value(result(board, action)), action))
        return sorted(plays, key=lambda x: x[0])[0][1] #Returning the optimal move
    
