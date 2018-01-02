# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
word_list = loadWords()
letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# your code begins here!

def printLetters(letter_list):
    for letter in letter_list:
        print letter,
    print ''

def gameOver():
    return None
    
def playGame():
    word_to_guess = chooseWord(word_list)
    guesses_left = 10
    letters_guessed = []
    letters_correct = []
    letters_left = letter_list

    for letter in word_to_guess:
        letters_correct.append('_')
    
    print 'Welcome to the game. I am thinking of a word', \
         'that is %i letters long.' %(len(word_to_guess), )
    printLetters(letters_correct)
    
    while ''.join(letters_correct) != word_to_guess and guesses_left > 0:
        print 'You have %i guesses left.\nAvailable letters:' %(guesses_left)
        printLetters(letters_left)
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
            
        try:
            letters_left.remove(guess)
            if guess in word_to_guess:
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                               letters_correct[i] = word_to_guess[i]
                print 'Good guess.'
                printLetters(letters_correct)            
            else:
                print 'Oops. That letter is not in my word.'
                printLetters(letters_correct)
            guesses_left -= 1

        except ValueError:
            print 'You already tried %s or %s is not a valid character.' %(guess, guess)

        
    if ''.join(letters_correct) == word_to_guess:
        print 'Congratulations. You won'
    else:
        print 'You lost. The right answer was %s.' %(word_to_guess)
    
    
    return
print 'a' in letter_list 
playGame()
