'''
Brielle Foster
CSC110
Project -8
This program checks for mispelled words and corrects them so that they will
be spelled correctly.
  
'''

def read_spellings():
    '''
    This function returns a dictionary with each misspelled word mapped to the 
    correct spelling of the word.
    Args:
        There are no arguments.
    Returns: 
        The dictionary where each misspelled word is mapped to the correct
        spelling of the word.
    '''
    file = open("misspellings.txt", "r")
    misspellings = {}
    for line in file:
        # This strips the line breaks and splits each word with an arrow.
        first_line = line.strip().split("->")
        # This maps the misspelled word (key) to the correctly spelled
        # word (value)
        misspellings[first_line[0]] = first_line[1]
    file.close()
    return misspellings

def correct_spelling(filename, dictionary):
    '''
    This function does not return anything. It just writes out a new file.
    Args:
        The arguments are the filename and the dictionary.
    Returns: 
        Nothing is returned.
    '''
    file1 = open(filename, "r")
    new_file = open("output_" + filename, "w")
    file = file1.readlines()
    for index in range(len(file)):
         # This strips the line breaks and splits each word with a space.
        line = file[index]
        first_line = line.strip().split(" ")
        for i in range(len(first_line)):
            words = first_line[i]
            variable = words
            # This checks if the first letter of the word is uppercase and if
            # it is then it is turned into lowercase.
            if words[0].isupper():
                words = words.lower()
            # This checks if the last index of the string has punctuation and
            # then removes it if it does.
            if words[-1] in ";.,?!":
                words = words[:-1]      
            if words in dictionary:
                words = dictionary[words]
            # The variable stores words so when we check if the first letter 
            # is uppercase we capitalize it since the original word was
            # capitilized.
            if variable[0].isupper():
                words = words.capitalize()
            # This also stores words and makes sure that if the original word
            # had puncuation then it would keep the puncuation.
            if variable[-1] in ";.,?!":
                words += variable[-1]
            first_line[i] = words
        new_string = ""
        for word in first_line:
            # This writes the new file with each word spaced out.
            new_string += (word + " ")
        new_string = new_string[:-1]
        if index == len(file) - 1:
            new_file.write(new_string)
        else:
            new_file.write(new_string + "\n")
    file1.close()
    new_file.close()

spell_dict = read_spellings()
correct_spelling("words_1.txt", spell_dict)