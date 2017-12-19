"""
scrabble_helper.py
Title: Scrabble Helper
Created By: Matthew Devaney
Description: find the best words that can be made from a list of Scrabble tiles
Why I Made This: I love Scrabble!
"""

import json

# make an empty list to hold words found
words_found = []

# open the scrabble dictionary
with open('scrabble_dictionary.json', 'r') as f:
    scrabble_dict = json.load(f)

# open the scrabble letters definition
with open('scrabble_letters.json', 'r') as f:
    scrabble_letters = json.load(f)

# ask the player to provide the letters in their rack
letters_in_rack = input('What letters do you want to make a word from? ')
print()

# get length of letters provided by the player
length_letters_in_rack = len(letters_in_rack)

# look at every word in the scrabble dictionary
for word in scrabble_dict.keys():

    check_letters = list(letters_in_rack)

    # look at every letter in each word
    for letter in word:
        if letter in check_letters:
            # remove the matching letter from the check letters list
            check_letters.remove(letter)
        else:
            break

        # add to found words list if a word can be made with letters in the rack
        if len(word) == length_letters_in_rack - len(check_letters):
            words_found.append((word, scrabble_dict[word]))
            break

# sort the list by the 2nd value in the tuple by descending order
words_found = sorted(words_found, key=lambda x: -x[1])

# print the list of words
for (word, points) in words_found:
    print('{}: {}'.format(word, points))
