'''
Brielle Foster
CSC110
Project -6
This program is creating a cross stitch pattern using random shapes.
'''
import random

random.seed(123)
SYMBOLS = [" ◎ ", " △ ", " ▞ ", " ● ", " ▣ ", 
           " ▤ ", " ▲ ", " ▼ ", " * ", " < ",
           " > ", " = ", " ≡ ", " ☼ ", " ♦ ",
           " ◭ ", " ► ", " ◘ ", " ◓ ", " ▌ "]


def print_pattern(pattern):
    '''
    This function prints the pattern of the cross stitch.
    Args:
        The argument is the pattern.
    Returns: 
        The pattern of the cross stitch.
    '''
    width = len(pattern[0])  - 1
    top_line = "┌" + "───┬" * width + "───┐"
    print(top_line)
    for i in range(len(pattern)):
        new_row = "│"
        for j in range(len(pattern[i])):
            new_row += pattern[i][j] + "│"
        print(new_row)
        if i != len(pattern) - 1:
            print("├" + "───┼" * width + "───┤")
    bottom_line = "└" + "───┴" * width + "───┘"
    print(bottom_line)

def create_background(w,l,numbers):
    '''
    This function returns a list that creates the random background of the
    cross stitch pattern.
    Args:
        The arguments are the width of the pattern, length of the pattern, and
        the number of colors which creates the amount of symbols in the 
        pattern.
    Returns: 
        The list that creates the random background of the cross stitch
        pattern.
    '''
    random.seed(123)
    list = []
    # These for loops check if the length and width are in range of variables
    # index and j to append a sublist to a list.
    for index in range(l):
        sublist = []
        for j in range(w):
            randnum = SYMBOLS[random.randint(0,numbers - 1)]
            sublist.append(randnum)
        list.append(sublist)
    return list

def add_v_stripe(pattern, start, width, symbol_index):
    '''
    This function returns a pattern of a vertical stripe.
    Args:
        The arguments are the pattern, the start of the pattern, the width of 
        the pattern, and the symbol at a specific index.
    Returns: 
        The pattern of a vertical stripe.
    '''
    # These for loops check if the rows are in range and columns are in range
    # of the pattern and goes to the index of the row and then the column in 
    # that row to create the shape.
    for r in range(len(pattern)):
        for c in range(start,start + width):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape
    return pattern

def add_h_stripe(pattern, start, length, symbol_index):
    '''
    This function returns a pattern of a horizontal stripe.
    Args:
        The arguments are the pattern, the start of the pattern, the width of 
        the pattern, and the symbol at a specific index.
    Returns: 
        The pattern of a horizontal stripe.
    '''
    # These for loops check if the rows are in range between the starting
    # point and the starting point added to the legnth. It also checks if
    # the columns are in range of the length of the pattern. Then it goes to 
    # the index of the row and then the column in that row to create the shape.
    for r in range(start, start + length):
        for c in range(len(pattern[0])):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape
    return pattern
         
def add_square(pattern, x, y, size, symbol_index):
    '''
    This function returns a pattern of a square.
    Args:
        The arguments are the pattern, the x position, the y position, the 
        size of the pattern of the square, and the symbol at a specific index.
    Returns: 
        The pattern of a square.
    '''
    # These for loops check if the rows are in range between the x positon 
    # and x position added to the size. It also checks if the columns are in
    # range between the y position and the y position added to the size. Then 
    # it goes to the index of the row and then the column in that row to create
    # the shape.
    for r in range(x, x + size):
        for c in range(y, y + size):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape
    return pattern

def add_rectangle(pattern, x, y, width, height, symbol_index):
    '''
    This function returns a pattern of a rectangle.
    Args:
        The arguments are the pattern, the x position, the y position, the 
        width of the rectangle, the height of the rectangle, and the symbol
        at a specific index.
    Returns: 
        The pattern of a rectangle.
    '''
    # These for loops check if the rows are in range between the x positon 
    # and x position added to the height. It also checks if the columns are in
    # range between the y position and the y position added to the width. Then 
    # it goes to the index of the row and then the column in that row to create
    # the shape.
    for r in range(x, x + height):
        for c in range(y, y + width):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape
    return pattern

def add_triangle_a(pattern, x, y, size, symbol_index):
    '''
    This function returns a pattern of a normal triangle.
    Args:
        The arguments are the pattern, the x position, the y position, the 
        size of the pattern of the triangle, and the symbol at a specific 
        index.
    Returns: 
        The pattern of a normal triangle.
    '''
    position = 0
    # These for loops check if the rows are in range between the y positon 
    # subtracted by 1 and y position added to the size. It also checks if the 
    # columns are in range between the x position and the x position added to
    # the position. Then it goes to the index of the row, then the column
    # in that row and increments 1 each time to create the shape.
    for r in range(y - 1, y + size):
        for c in range(x, x + position):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape    
        position += 1  
    return pattern  

def add_triangle_b(pattern, x, y, size, symbol_index):
    '''
    This function returns a pattern of a normal triangle that has been flipped
    on its' y axis.
    Args:
        The arguments are the pattern, the x position, the y position, the 
        size of the pattern of the triangle, and the symbol at a specific 
        index.
    Returns: 
        The pattern of a normal triangle flipped
        on its' y axis.
    '''
    position = 0
    # These for loops check if the rows are in range between the y positon 
    # subtracted by 1 and y position added to the size. It also checks if the 
    # columns are in range between the x position added to the size, subtracted
    # to one and the x position added to the size, subtracted by the position, 
    # subtracted by 1. Then it goes to the index of the row, then the column
    # in that row and increments 1 each time to create the shape.
    for r in range(y - 1, y + size):
        for c in range(x + size - 1, x + size - position - 1, - 1):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape    
        position += 1  
    return pattern

def add_triangle_c(pattern, x, y, size, symbol_index):
    '''
    This function returns a pattern of a normal triangle that has been flipped
    upside down on its' x axis.
    Args:
        The arguments are the pattern, the x position, the y position, the 
        size of the pattern of the triangle, and the symbol at a specific 
        index.
    Returns: 
        The pattern of a normal triangle flipped upside down on
        its' x axis.
    '''
    position = size
    # These for loops check if the rows are in range between the y positon 
    # and y position added to the size. It also checks if the 
    # columns are in range between the x position and the x position added to
    # the position Then it goes to the index of the row, then the column
    # in that row and decrements 1 each time to create the shape.
    for r in range(y, y + size):
        for c in range(x, x + position):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape    
        position -= 1  
    return pattern

def add_triangle_d(pattern, x, y, size, symbol_index):
    '''
    This function returns a pattern of a normal triangle that has been flipped 
    on its's y axis and upside down on its' x axis.
    Args:
        The arguments are the pattern, the x position, the y position, the 
        size of the pattern of the triangle, and the symbol at a specific 
        index.
    Returns: 
        The pattern of a normal triangle flipped on its's y axis and
        upside down on its' x axis.
    '''
    position = size
    # These for loops check if the rows are in range between the y positon 
    # and y position added to the size. It also checks if the 
    # columns are in range between the x position added to the size subtracted
    # by 1 and the x position added to size subtracted by the position
    # subtracted by 1. Then it goes to the index of the row, then the column
    # in that row and decrements 1 each time to create the shape.
    for r in range(y, y + size):
        for c in range(x + size - 1, x + size - position - 1, -1):
            shape = SYMBOLS[symbol_index]
            pattern[r][c] = shape    
        position -= 1  
    return pattern