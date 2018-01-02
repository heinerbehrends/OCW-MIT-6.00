def word_in_hand(word, hand):
    hand_local = hand
    for letter in word:
        hand_local[letter] = hand_local.get(letter, 0) -1
    for value in hand_local:
        if hand_local[value] < 0:
            return False
    return True
print word_in_hand("allew", {'a':1, 'x':2, 'l':3, 'e':1})
