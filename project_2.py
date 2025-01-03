'''
Brielle Foster
CSC110
Project -1
This program is creating a system to find grade results.
'''

def letter_grade(n):
    
    '''
    This function returns the letter grade.
    Args:
        The arguments are the percentages used to find the letter grade.
    Returns: 
        The letter grade.
    '''
     
    if 90 <= n <= 100:
        return "A"
    if 80<= n <= 90:
        return "B"
    if 70 <= n <= 80:
        return "C"
    if 60 <= n <= 70:
        return "D"
    if 0 <= n <= 60:
        return "E"
    else:
        return "X"
    
def pass_or_fail(letter):
    '''
    This function returns a pass or fail.
    Args: 
        The arguments are the letter grades that determine a pass or fail
    Returns:
        A pass or fail.
    '''

    if letter == "A":
        return "Pass"
    if letter == "B":
        return "Pass"
    if letter == "C":
        return "Pass"
    if letter == "D":
        return "Pass"
    if letter == "E":
        return "Fail"
    else:
        return "Error"
    
def point_grade(score, total_points):
    '''
    This function returns the point grade value. 
    Args:
        The arguments are the scores and total points
        used to calculate the point grade
    Returns:
        The point grade value.
    '''
    return round( (score/ total_points) * (100) , 2)

def get_grade_results(score, total_points):
    '''
    This function returns the final result.
    Args:
        The arguments are the scores and total points
        used to find the final result.
    Returns:
        The final result which is in a string.
    '''
    percentage = point_grade(score, total_points)
    # This variable is being used to find the letter grade and result.
    letter = letter_grade(percentage)
    result = pass_or_fail(letter)
    return "Your grade is " + (str(percentage)) + \
    " (" + (str(letter)) + " " + "- " + (str(result)) + ")"
