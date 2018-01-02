
def update_hand(hand, word):
    x = 0
    for letter in word:
        hand[letter] = hand.get(letter, 0) -1
    return display_hand(hand)
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}

update_hand(hand, "quail")
