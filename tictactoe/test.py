"""
Tic Tac Toe Player
"""
import copy
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
    temp = board.copy()
    temp[action[0]][action[1]] = player(temp)
    return temp
    


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
    score = {}
    temp = copy.deepcopy(board)
    temp[0][2] = 'X'
    print(temp)
    print(board)
    acts = actions(temp) 
    for act in acts:
        score[act]= minimax_derivative(result(temp,act))
    return min(score, key = score.get)
    


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

def minimax_derivative(board):
    temp = copy.deepcopy(board)
    acts = actions(temp)
    x = utility(temp)
    scores = []
    if x == 0:
        if not acts:
            return x
        for act in acts:
            scores.append(minimax_derivative(result(temp,act)))
        return min(scores)
    return x


x = initial_state()
x[0][0] = 'X'
act = minimax(x)
print(act)
x = result(x,act)
print(x)

