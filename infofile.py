'''
Brielle Foster
CSC110
Project -9
This program creates dictionaries, writes files, and produces an information
file based on the text.
  
'''

def text_to_list(filename):
    '''
    This function returns a list with each word split between commas
    Args:
        The argument is a file name.
    Returns: 
        A list which each word from the text with commas in between each
        word.
    '''
    file = open(filename, "r").readlines()
    new_list = []
    for line in file:
        # This strips the line breaks and splits each word with a space.
        first_line = line.strip().split(" ")
        for word in first_line:
            # This appends each word to the new list.
            new_list.append(word)
    return new_list

def count_words(list):
    '''
    This function returns a dictionary where each word in the list is counted.
    Args:
        The argument is a list.
    Returns: 
        The dictionary where each word is mapped to a value representing how
        many times it has been counted.
    '''
    dictionary = {}
    for word in list:
        if len(word) > 0:
        # This adds one to the value of the key if the word is in the
        # dictionary.
            if word in dictionary:
                dictionary[word] += 1
        # This sets the word equal to one if it has not been seen in the list
        # yet.
            else:
                dictionary[word] = 1
    return dictionary

def most_frequent(dictionary):
    '''
    This function returns the value of each small, medium, and large key.
    Args:
        The argument is a dictionary.
    Returns: 
        The dictionary where the amount of small words, medium words, and
        large words are counted with they keys mapped to each value.
    '''
    small = 0
    medium = 0
    large = 0
    for key, value in dictionary.items():
        if len(key) <= 4 and value > small:
            # This checks if the value is considered small.
            small = value
            small_key = key
        elif 5 <= len(key) <= 7 and value > medium:
            # This checks if the value is considered medium.
            medium = value
            medium_key = key
        elif len(key) > 7 and value > large:
            # This checks if the value is considered large.
            large = value
            large_key = key
    return small_key, medium_key, large_key

def count_capitalized(dictionary):
    '''
    This function returns the value of each capitalized and uncapitalized word.
    Args:
        The argument is a dictionary.
    Returns: 
        The dictionary where the amount of capitalized and uncapitalized words
        are counted with they keys mapped to each value.
    '''
    capitalized = 0
    uncapitalized = 0
    for key in dictionary.keys():
        if len(key) > 0:
        # This checks if the first letter of the key is capitalized and if it
        # is then the value of 1 is added to the count.
            if key[0].isupper():
                capitalized += 1
        # This checks if the first letter of the key is uncapitalized and if it
        # is then the value of 1 is added to the count.
            else:
                uncapitalized += 1
    return capitalized, uncapitalized

def count_punctuated(dictionary):
    '''
    This function returns the value of each puncuated and unpuncuated word.
    Args:
        The argument is a dictionary.
    Returns: 
        The dictionary where the amount of puncuated and unpuncuated words
        are counted with they keys mapped to each value.
    '''
    punctuated = 0
    unpunctuated = 0
    for key in dictionary.keys():
        if len(key) > 0:
        # This checks if the last index of the key has a . or , and if it does
        # then the value of 1 is added to the count.
            if key[-1] in ".,":
                punctuated += 1
        # This checks if otherwise and if so then the value of 1 is added to
        # the count.
            else:
                unpunctuated += 1
    return punctuated, unpunctuated

def count_sizes(dictionary):
    '''
    This function returns the count of how many small, medium, and large
    words there are.
    Args:
        The argument is a dictionary.
    Returns: 
        The dictionary where the small, medium, and large words are counted
        where each key is mapped to its value depending on how many times it 
        was counted.
    '''
    small = 0
    medium = 0
    large = 0
    for key in dictionary:
        if len(key) > 0:
        # This determines if it is a small word and adds it to the count.
            if len(key) <= 4:
                small += 1
        # This determines if it is a medium word and adds it to the count.
            elif len(key) <= 7:
                medium += 1
        # This determines if it is a large word and adds it to the count.
            elif len(key) > 7:
                large += 1
    return small, medium, large

def write_results(dictionary, filename):
    '''
    This function writes the output file of the input file.
    Args:
        The argument is a dictionary and a filename.
    Returns: 
        The output file which includes the total number of unique words,
        most frequent words, 
    '''
    file = open(filename[:-4] + "_results" + filename[-4:], "w")
    file.write("Total number of unique words: " + str(len(dictionary)))
    file.write("\n" + "Most frequent words by size:")

    frequency = most_frequent(dictionary)
    file.write("\n* Small: " + frequency[0])
    file.write("\n* Medium: " + frequency[1])
    file.write("\n* Large: " + frequency[2])

    length = count_sizes(dictionary)
    total = length[0] + length[1] + length[2]
    small_count = length[0]/total * 50
    medium_count = length[1]/total * 50
    large_count = length[2]/total * 50
    file.write("\n\nLength:")
    file.write("\n* Small: " + str(length[0]))
    file.write(" (" + str(round(length[0]/total * 100,2)) + "%)")
    file.write("\n* Medium: " + str(length[1]))
    file.write(" (" + str(round(length[1]/total * 100,2)) + "%)")
    file.write("\n* Large: " + str(length[2]))
    file.write(" (" + str(round(length[2]/total * 100,2)) + "%)")
    file.write("\n" + round(small_count) * "#" + round(medium_count) * "%" +\
    round(large_count) * "*")
    


    capital = count_capitalized(dictionary)
    total = capital[0] + capital[1]
    capitalized = capital[0]/total * 50
    uncapitalized = capital[1]/total * 50
    file.write("\n\nCapitalization:")
    file.write("\n* Capitalized: " + str(capital[0]))
    file.write(" (" + str(round(capital[0]/total * 100,2)) + "%)")
    file.write("\n* Non-capitalized: " + str(capital[1]))
    file.write(" (" + str(round(capital[1]/total * 100,2)) + "%)")
    file.write("\n" + round(capitalized) * "#" + round(uncapitalized) * "%")


    punctuation = count_punctuated(dictionary)
    total = punctuation[0] + punctuation[1]
    puncuated_count = punctuation[0]/total * 50
    unpuncuated_count = punctuation[1]/total * 50
    file.write("\n\nPunctuation:")
    file.write("\n* Punctuated: " + str(punctuation[0]))
    file.write(" (" + str(round(punctuation[0]/total * 100,2)) + "%)")
    file.write("\n* Non-punctuated: " + str(punctuation[1]))
    file.write(" (" + str(round(punctuation[1]/total * 100,2)) + "%)")
    file.write("\n" + round(puncuated_count) * "#" + round(unpuncuated_count)\
     * "%")


            
word_list = text_to_list("poem.txt")
    
word_counts = count_words(word_list)    
    
print(most_frequent(word_counts) )
print(count_capitalized(word_counts) )
print(count_punctuated(word_counts) )
print(count_sizes(word_counts))
    
print(write_results(word_counts, "poem.txt"))