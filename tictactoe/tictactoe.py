"""
Tic Tac Toe Player
"""
from copy import deepcopy #necessary because we have a list inside of a list
import math
win = ''
X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if [element for rows in board for element in rows].count(None) % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    x = set()
    for i, rows in enumerate(board):
        for j, box in enumerate(rows):
            if not box:
                x.add((i,j))
    return x

                     
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    diag, win = diagonal_is_crossed(board)
    if diag:
        return win
    col, win = column_is_crossed(board)
    if col:
        return win
    row,win = row_is_crossed(board)
    if row:
        return win
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or not None in [element for rows in board for element in rows]:
        return True
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    scores = {}
    
    # If players choose X, so AI is O, AI need to maximalize score so X wins
    if player(board) == O:
        for act in actions(board):
            temp = deepcopy(board)
            scores[act] = minimalize(result(temp,act))
        return max(scores,key = scores.get)
    
    # if players choose O, so AI is X, will go first and need to minimalize score
    for act in actions(board):
        temp = deepcopy(board)
        scores[act] = maximalize(result(temp,act)) 
    return min(scores,key = scores.get) 
    


"""
Helper functions
"""
def diagonal_is_crossed(board):
    if board[0][0] == board[1][1] == board[2][2] !=  None:
        win = board[0][0]
        return True,win
    elif board[2][0] == board[1][1] == board[0][2]  !=  None :
        win = board[2][0]
        return True,win
    return False, None

def column_is_crossed(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]  !=  None:
            win = board[i][0]
            return True,win
    return False, None

def row_is_crossed(board):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]  !=  None:
            win = board[0][i]
            return True,win
    return False, None

def minimalize(board, break_value = None):
    if terminal(board):
        return utility(board)
    x = 1
    for act in actions(board):
        temp = deepcopy(board)
        x = min(maximalize(result(temp,act),x), x) # supply x as the break value, because x is the smallest 
        
        # Alpha beta pruning
        if break_value: #if no break value supplied, don't stop the iteration
            if  x < break_value: 
                return x
    return x
        


def maximalize(board, break_value = None):
    if terminal(board):
        return utility(board)
    x = -1
    for act in actions(board):
        temp = deepcopy(board)
        x = max(minimalize(result(temp,act),x), x)
        
        # Alpha beta pruning
        if break_value: #if no break value supplied, don't stop the iteration
            if x > break_value:
                return x

    return x


