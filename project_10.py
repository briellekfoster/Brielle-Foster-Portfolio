'''
Brielle Foster
CSC110
Project -10
This program creates a puzzle game called mine sweeper that generates
coordinates to a square on a board. If an X is revealed then the player loses.
Otherwise, an integer will be revealed that shows the number of adjacent mines.
  
'''

def read_file(filename):
    '''
    This function returns a list of a grid.
    Args:
        The argument is a file name.
    Returns: 
        A list of a grid which holds each line split by a comma where each 1 is
        turned into an X on the grid.
    '''
    file = open(filename, "r")
    grid = []
    for line in file:
        # This strips the line breaks and adds a comma between each number in
        # the list.
        first_line = line.strip().split(",")
        if len(first_line) > 1:
            grid.append(first_line)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # This checks if there is a space or not and then replaces the 
                # 1 with an X.
                if grid[i][j] == " 1" or grid[i][j] == "1":
                    grid[i][j] = "X"
                # This checks if there is an extra space and if there is then 
                # it removes the space.
                if grid[i][j] == " 0":
                    grid[i][j] = "0"
    return grid

def make_empty_grid(grid):
    '''
    This function returns a new list of a grid.
    Args:
        The argument is a list of a grid.
    Returns: 
        A new list of a grid where each element in the list is now and empty
        string.
    '''
    new_grid = []
    for sublist in grid:
        sub = []
        for i in range(len(sublist)):
            # This turns each element in the grid into an empty string.
            sub.append(' ')
        new_grid.append(sub)
    return new_grid

def within_limits(two_d_list, y , x):
    '''
    This function does not return anything.
    Args:
        The argument is a 2D list, a y value, and an x value.
    Returns: 
        It does not return anything. It just checks if the grid is staying in
        bounds.
    '''
    # This checks if this is out of bounds.
    if y < 0 or y >= len(two_d_list):
        return False
    if x < 0 or x >= len(two_d_list[0]):
        return False
    # This checks if this is in bounds.
    else:
        return True

def update_grid(grid):
    '''
    This function returns the grid.
    Args:
        The argument is a grid.
    Returns: 
        A grid where the adjacent mines are now shown.
    '''
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            # This creates a count variable if X is not at the specific index.
            if grid[row][column] != "X":
                count = 0
                for i in range(row-1, row+2):
                    for j in range(column-1, column+2):
                        # This checks if it is within limits.
                        bounds2 = within_limits(grid, i, j)
                        # This makes sure that it is in limits and if X is at
                        # that specific index before adding 1 to the count.
                        if bounds2 == True and grid[i][j] == "X":
                            count += 1
                grid[row][column] = count
    return grid

def letter_to_index(letter):
    '''
    This function is a helper function for the dig function that returns
    the letter changed to an index.
    Args:
        The argument is a letter.
    Returns: 
        It returns the letter changed to an index.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        # This makes sure that the letter is equal to the alphabet at that
        #specific index and if it is then the index is returned.
        if letter == alphabet[i]:
            return i

def dig(grid, moves, user_view):
    '''
    This function prints the grid.
    Args:
        The arguments are the grid, the moves, and the user view.
    Returns: 
        Nothing is returned but the grid is printed with the adjacent numbers
        added to the grid in the correct spots.
    '''
    column = letter_to_index(moves[0])
    string = ""
    for i in range(1, len(moves)):
        string += moves[i]
    string = int(string)
    row = len(grid) - string - 1
    user_view[row][column] = grid[row][column]
    # This checks if the user view at that specific place is not equal to X
    # and if this is true then we call our other function to reveal the spaces.
    if user_view[row][column] != "X":
        reveal_spaces(grid, user_view, row, column)
    print_grid(user_view)

def reveal_spaces(grid, user_view, x, y):
    '''
    This function is a helper function that returns nothing.
    Args:
        The arguments are the grid, user view, x, and y.
    Returns: 
        Nothing is returned.
    '''
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if within_limits(grid, i, j):
                # This checks if the grid at that specific place is not equal
                # to X and if it is then the user view at that specific place
                # will be set equal to the grid at that specifc place to
                # reveal the spaces.
                if grid[i][j] != "X":
                    user_view[i][j] = grid[i][j]

def count_total_moves(grid, user_view):
    '''
    This function returns the count of the total moves.
    Args:
        The arguments are a grid and user view.
    Returns: 
        A count of the total moves made.
    '''
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # This checks if the user view at that specific place is empty
            # and if the grid at that specific place is not equal to X and if
            # both of these are true then 1 is added to the count.
            if user_view[i][j] == ' ' and grid[i][j] != "X":
                count += 1
    return count 
    
def print_grid(grid):
    '''
    This function prints the grid.
    Args:
        The arguments are the grid, the moves, and the user_view.
    Returns: 
        The grid is returned with the numbers going down and the
        alphabet on the bottom going to the right.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = len(grid[0])
    height = len(grid) -1
    for sublist in grid:
        # This is used to correctly format the numbers.
        print("{:2}".format(height),end="")
        for item in sublist:
            print("[{0}]".format(item),end="")
        print()
        height -= 1
    print("  ",end="")
    for i in range(width):
        # This is used to format the letters at the bottom correctly.
        print(" {} ".format(alphabet[i]),end="")
    print(" ")

def determine_game_status(grid, user_view):
    '''
    This function returns true or false.
    Args:
        The arguments are the grid and the user view.
    Returns: 
        True is returned if the game should continue and False is returned if
        the game is over.
    '''
    # This checks if the count is equal to 0 and if it is then the game is
    # over.
    if count_total_moves(grid, user_view) == 0:
        return False
    for row in user_view:
    # This checks if X is in the row and if it is then the game is over.
        if "X" in row:
            return False
    # This checks if otherwise and if this is the case then the game will 
    # continue.
    return True