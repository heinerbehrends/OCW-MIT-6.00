# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
##
##def join_strings(old_string, string_to_add):
##    new_string = old_string + string_to_add
##    return new_string

##print join_strings('ab', 'b')

def input_letter(input_message, error_message):
    """Asks for user input by input_message. Checks if a single ascii letter is input.
    Returns lower case letter if true, else will ask again."""
    while True:
        new_letter = string.lower(raw_input(input_message))
        letter_or_not = new_letter in string.ascii_letters and len(new_letter) == 1
        if letter_or_not == True:
            return new_letter
        else:
            print new_letter, 'is', error_message
            
##print input_letter("Please input a single letter \n", "not a valid letter")
##
##def play_hand_no_losing():
##    word_fragment = ''
##    print "Welcome to ghost"
##    print "Player 1 chooses the first letter"
##    word_fragment += input_letter("Player 1 says letter \n", "not a valid letter")
##    print 'current word fragment:', word_fragment
##    while True:
##        player_1 = False
##        word_fragment += input_letter("Player 2 says letter \n", "not a valid letter")
##        player_1 = True
##        print 'current word fragment:', word_fragment    
##        word_fragment += input_letter("Player 1 says letter \n", "not a valid letter")
##        print 'current word fragment:', word_fragment
        
##play_hand_no_losing()

def is_part_of_word(word_fragment, wordlist):
    """Returns True if word_fragment is the beginning of a word in wordlist.
    Returns False otherwise. Assumes word_fragment is a string."""
    for word in wordlist:
        is_part_of_list = word_fragment == word[:len(word_fragment)]
        if is_part_of_list == True:
            return True
    return False

##print is_part_of_word("ttt", wordlist)

def not_a_long_word(word, wordlist):
    """Returns True if word is not part of wordlist or less than 4 letters.
    Returns False if word is part of wordlist and longer than 3 letters."""
    if word in wordlist and len(word) > 3:
        return False
    else:
        return True

##print is_long_word('money', wordlist)

def play_ghost():
    word_fragment = ''
    player = "Player 1"
    valid_word = True
    not_a_valid_word = True
    print "Welcome to ghost"
    word_fragment += input_letter("Player 1 chooses the first letter: ", "not a valid letter")
    print 'current word fragment:', word_fragment
    while True:
        word_fragment += input_letter("Player 2 chooses the next letter: ", "not a valid letter")
        print 'Current word fragment:', word_fragment
        player = "Player 2"
        
        if is_part_of_word(word_fragment, wordlist) == False:
            print "Not a beginning of a valid word ", player, " loses."
            return
        
        if not_a_long_word(word_fragment, wordlist) == False:
            print word_fragment, 'is a valid word longer than 3 letters.', player, 'loses.'
            return
        
        word_fragment += input_letter("Player 1 chooses the next letter: ", "not a valid letter")
        print 'current word fragment:', word_fragment
        player = "Player 1"
        
        if is_part_of_word(word_fragment, wordlist) == False:
            print "Not a beginning of a valid word ", player, " loses."
            return
        
        if not_a_long_word(word_fragment, wordlist) == False:
            print word_fragment, 'is a valid word longer than 3 letters.', player, 'loses.'
            return
        
play_ghost()
