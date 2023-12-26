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

def isEmpty(board):
    for i in range (0,3) :
        for j in range (0, 3 ) :
            if(board[i][j]!=EMPTY):
                return False
    return True

def countX(board):
    count = 0
    for i in range (0,3) :
        for j in range (0, 3 ) :
            if(board[i][j]==X):
                count+=1
    return count

def countO(board):
    count = 0
    for i in range (0,3) :
        for j in range (0, 3 ) :
            if(board[i][j]==O):
                count+=1
    return count

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if(countX(board)>countO(board)):
        return O
    return X






def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range (0,3) :
        for j in range (0, 3 ) :
            if(board[i][j]==EMPTY):
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resul = copy.deepcopy(board)

    try:
        if resul[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            # atualizando o valor
            resul[action[0]][action[1]] = player(board)
            print("==================")
            print(resul)
            print("==================")
            return resul
    # tratando o erro
    except IndexError:
        print('error')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range (0,3) :
        if(board[i][0]==board[i][1]==board[i][2]):
            return board[i][0]
        if(board[0][i]==board[1][i]==board[2][i]):
            return board[0][i]
    if(board[0][0]==board[1][1]==board[2][2]):
        return board[0][0]
    if(board[0][2]==board[1][1]==board[2][0]):
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    for i in range (0,3) :
        for j in range (0, 3 ) :
            if(board[i][j]==EMPTY):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if(win==X):
        return 1
    if(win==O):
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v_min = float('-inf')
            for possibiles in actions(board):
                i = min_value(result(board, possibiles))
                if i > v_min:
                    v_min = i
                    move = possibiles
        else:
            v_maximo = float('inf')
            for possibiles in actions(board):
                i = max_value(result(board, possibiles))
                # print(result(board,possibiles))
                # print(i)
                if i < v_maximo:
                    v_maximo = i
                    move = possibiles

    return move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
        if v == 1:
            return v
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
        if v == -1:
            return v
    return v