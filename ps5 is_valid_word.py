def is_valid_word(word, hand, word_list):
    if word_in_hand(word, hand) == True and word_in_wordlist(word, wordlist) == True:
        return True
    else:
        return False

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

wordlist = load_words()
    
def word_in_wordlist(word, wordlist):
    if word in wordlist:
        return True
    else:
        return False
print word_in_wordlist("vet", wordlist)
