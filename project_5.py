'''
Brielle Foster
CSC110
Project -5
This program is creating a simplified version of chess where the king and
knights can only move specific ways and at the end there is a winner.
'''

def create_board():
    '''
    This function returns the list of the chess board.
    Args:
        There are no arguments within this function.
    Returns: 
        The list of the chess board.
    '''
    list = ["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY","BKn", "BKn", "BKi"]
    return list

def printable_board(board):
    '''
    This function returns physical chess board.
    Args:
        The arguments is the chess board that will be used for the game.
    Returns: 
        The physical chess board.
    '''
    string = ""
    string += "+-----------------------------------------------------+\n"

    index = 0
    while index < len(board):
        piece = board[index]
        if piece == "EMPTY":
            string += "| " + "   " + " "
        else:
            string += "| " + piece + " "
        index += 1
    string += "|\n+-----------------------------------------------------+"
    return string

def is_valid_move(board, position, player):
    '''
    This function returns True or False depending on if the moves that are made
    during the game are valid.
    Args:
        The arguments are the board, the position, and the player.
    Returns: 
        This returns True or False depending on if the moves made during the 
        game are valid moves.
    '''
    # This checks if the pieces are staying in bounds.
    if 0 <= position < 9:
        if board[position] == "WKi" or board[position] == "WKn" and\
        player == "WHITE":
            return True
        if board[position] == "BKi" or board[position] == "BKn" and\
        player == "BLACK":
            return True
        else:
            return False
    else: 
        return False
    
def move_king(board, position, direction):
    '''
    This function returns the board where the king is able to move correctly.
    Args:
        The arguments are the board, position, and direction of the king.
    Returns: 
        The board where the king stays in bonds and moves only one space to
        the left or right
    '''
    # This checks if the king is staying in bounds and moving correctly.
    piece = board[position]
    if direction == "LEFT":
        left_index = position - 1
        while left_index > 0 and board[left_index] == "EMPTY":
            left_index -= 1
        if left_index < 0:
            left_index = 0
        board[position] = "EMPTY"
        board[left_index] = piece
            
    else:
        right_index = position + 1
        while right_index < len(board) - 1 and board[right_index] == "EMPTY":
            right_index += 1
        if right_index >= len(board):
            right_index = len(board) - 1
        board[position] = "EMPTY"
        board[right_index] = piece
    
    return board

def move_knight(board, position, direction):
    '''
    This function returns the board where the knight is able to move correctly.
    Args:
        The arguments are the board, position, and direction of the knight.
    Returns: 
        The board where the knight stays in bonds and moves only two spaces to
        the left or right
    '''
    # This checks if the knight is staying in bounds and moving correctly.
    piece = board[position]
    if direction == "LEFT":
        new_index = position - 2

    else:
        new_index = position + 2
    if new_index >= 0 and new_index < len(board):
        board[position] = "EMPTY"
        board[new_index] = piece
    return board

def move(board, position, direction):
    '''
    This function determines if the king or knight is being moved.
    Args:
        The arguments are the board, position, and direction of the pieces.
    Returns: 
        It returns if the move_king or move_knight function should be called
        depending on if the king or knight are being used.
    '''
    # This makes sure that the right pieces are being moved on the board.
    if "WKi" in board[position] or "BKi" in board[position]:
        move_king(board, position, direction)
    elif "WKn" in board[position] or "BKn" in board[position]:
        move_knight(board, position, direction)

def is_game_over(board):
    '''
    This function returns True or False depending on if the game is over or
    not.
    Args:
        The argument is the board.
    Returns: 
        It returns True or False depending on if the game is over or not and
        if the game is over then it prints out the winner of the game.
    '''
    # This checks if the game is over or not.
    if "WKi" not in board:
        print("Black wins!",end="")
        return True 
    elif "BKi" not in board:
        print("White wins!",end="")
        return True
    else:
        return False