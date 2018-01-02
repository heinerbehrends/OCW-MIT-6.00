 # 6.00 Problem Set 6
#
# The 6.00 Word Game
#

import random
import string
import time
from itertools import chain, combinations

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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


word_list = load_words()

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.   

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if len(word) == n:
        score += 50
    
    return score


def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
     """
    points_dict_temp = {}
    for word in word_list:
        points_dict_temp[word] = get_word_score(word, HAND_SIZE)
    return points_dict_temp

points_dict = get_words_to_points(word_list)


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char]-freq.get(char,0)
    return newhand
    #return dict( ( c, hand[c] - freq.get(c,0) ) for c in hand )
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return word in points_dict

def is_valid_word_hand_only(word, hand):
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return True

def get_time_limit(points_dict, k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
        end_time = time.time()
    return (end_time - start_time) * k

time_limit = get_time_limit(points_dict, 0.063)

##
##def get_possible_words(hand, points_dict):
##    possible_words = []
##    for key in points_dict:
##        if is_valid_word_hand_only(key, hand) == True:
##            possible_words.append(key)
##    return possible_words
##
##def pick_best_word(hand, points_dict):
##    possible_words = get_possible_words(hand, points_dict)
##    score_list = []
##    for word in possible_words:
##        score_list.append(points_dict[word])
####    print score_list
##    if len(score_list) == 0:
##        return '.'
##    max_score = max(score_list)
##    for word in possible_words:
##        if points_dict[word] == max_score:
##            return word

def get_word_rearrangements(word_list):
    rearrange_dict = {}
    for word in word_list:
        rearrange_dict[''.join(sorted(word))] = word
    return rearrange_dict

rearrange_dict = get_word_rearrangements(word_list)

def get_letters_of_hand_ordered(hand):
    word_as_list = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            word_as_list.append(letter)
    sorted_list = sorted(word_as_list)
    return sorted_list
##print get_letters_of_hand_ordered(hand)

##ordered_hand = get_letters_of_hand_ordered(hand)

def pick_best_word_faster(hand, rearrange_dict):
    possible_words = ()
    score_list = []
    ordered_hand = get_letters_of_hand_ordered(hand)
    for n in range(len(ordered_hand)+1):
        for tup in combinations(ordered_hand,n):
            if ''.join(sorted(tup)) in rearrange_dict:
                possible_words += (rearrange_dict[''.join(sorted(tup))],)     
    for word in possible_words:
        score_list.append(points_dict[word])
##    print score_list
    if len(score_list) == 0:
        return '.'
    max_score = max(score_list)
    for word in possible_words:
        if points_dict[word] == max_score:
            return word

##print get_all_subsets(ordered_hand)
##print pick_best_word_faster(hand, rearrange_dict)
#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list, time_limit):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """    
    total = 0.0
    initial_handlen = sum(hand.values())
    start_time = time.time()
    time_left = time_limit
    while sum(hand.values()) > 0:
        print 'Current Hand:',
        display_hand(hand)
        userWord = pick_best_word_faster(hand, rearrange_dict)
        if userWord == '.':
             break
        else:
            if not is_valid_word(userWord, hand, word_list):
                print 'Invalid word, please try again.'
            else:
                end_time = time.time()
                total_time = end_time - start_time
                time_left -= total_time
                if total_time == 0.0:
                    print '0.0 sec. Yeah! 100 bonus points'
                    points = get_word_score(userWord, initial_handlen)
                    points /= 0.01
                    total += points
                    total += 100
                    print '%s earned %.2f points. Total: %.2f points' % (userWord, points, total)
                    hand = update_hand(hand, userWord)
                    start_time = time.time()
                    break
                if time_left > 0:
                    print 'It took %.2f seconds to provide and answer. You have %.2f seconds left' % (total_time, time_left)
                    points = get_word_score(userWord, initial_handlen)
                    points /= float(total_time)
                    total += points
                    print '%s earned %.2f points. Total: %.2f points' % (userWord, points, total)
                    hand = update_hand(hand, userWord)
                    start_time = time.time()
                else:
                    print 'Total time exceeds %.2f seconds. You scored %.2f points.' % (time_limit, total)
                    break
    print 'Total score: %.2f points.' % total


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list, time_limit)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list, time_limit)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

        
hand = deal_hand(HAND_SIZE)


##possible_words = possible_words(hand, points_dict)
##points_dict = get_words_to_points(word_list)
##print hand, possible_words

##def best_choice(possible_words, points_dict):
##    score_list = []
##    for word in possible_words:
##        score_list.append(points_dict[word])
####    print score_list
##    max_score = max(score_list)
##    for word in possible_words:
##        if points_dict[word] == max_score:
##            return word
##
##print hand, best_choice(possible_words, points_dict)

