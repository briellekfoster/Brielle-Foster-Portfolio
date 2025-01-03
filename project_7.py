'''
Brielle Foster
CSC110
Project -7
This program is a program that reads a data set and prints out the
plot of first-digits to determine if it conforms to Benford's law.
  
'''

def csv_to_list(filename):
    '''
    This function returns a new list with only numbers from the file and then
    strips and splits the data with commas.
    Args:
        The argument the filename which is the name of the file being used.
    Returns: 
        The new list containing only numbers from the file and then
    stripped and split with commas.
    '''
    new_list = []
    file = open(filename, "r")
    # This iterates through the list, strips the lines, and splits them with
    # commas.
    for line in file:
        list = line.strip().split(",")
        # This iterates through the list.
        for n in list:
            # This checks if each element in the list is 1,2,3,4,5,6,7,8, or 9.
            # If they are then they are appended to the new list.
            if n[0] in "123456789":
                new_list.append(n)   
    file.close()    
    return new_list

def count_start_digits(digits):
    '''
    This function returns a new dictionary that counts the digits in the list.
    Args:
        The argument is the digits.
    Returns: 
        The count of each of the digits.
    '''
    count_digits = {1: 0, 2: 0,3 :0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 }
    # This iterates through the digits in the dictionary.
    for i in digits:
        # These if statements check if the digits should be counted or not.
        if int(str(i[0])) != 0:
            if int(str(i[0])) in count_digits:
                count_digits[int(str(i[0]))] += 1
    return count_digits

def digit_percentages(count):
    '''
    This function returns a new dictionary that changes the values of the keys
    into percentages by doing a calculation.
    Args:
        The argument is the count.
    Returns: 
        The new dictionary that has the key and its value which is now a 
        percentage.
    '''
    total = 0
    # This iterates through everything and then adds up the values.
    for values in count.values():
        total += values
    new_dict = {}
    # This iterates through everything and finds the keys
    for key, values in count.items():
        # This checks if the key is in the new dictionary and then calculates
        # the percentages and creates the new dictionary with the
        # percentages.
        if key not in new_dict:
            percentage = ((values/ total) * (100))
            new_dict[key] = round(percentage,2)
    return new_dict

def print_plot(percentages):
    '''
    This function returns a plot with printed out hashtags that correspond to
    the percentages in the dictionary.
    Args:
        The argument is the percentages.
    Returns: 
        The printed out hash tags that correspond to the percentages in the 
        dictionary.
    '''
    # This iterates through everything and then prints a plot depending on the
    # percentages in the dictionary.
    for key, values in percentages.items():
        print(str(key) + " | " + "#" * int(values))

def check_benfords_law(percentages):
    '''
    This function returns True or False while determining if it conforms
    to Benford's law or not. 
    Args:
        The argument is the percentages.
    Returns: 
        It returns True if it conforms to Benford's law and False if it
        does not. 
    '''
    law_percent = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
    # This iterates through everything.
    for key, values in percentages.items():
        # These check if the values are less or greater than the law percent
        # at a key - 5 and + 10 which will determine True or False.
        if values < (law_percent[key]- 5):
            return False
        if values > (law_percent[key] + 10):
            return False
    return True