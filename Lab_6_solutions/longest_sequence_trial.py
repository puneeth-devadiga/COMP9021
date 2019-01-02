# Written by Eric Martin for COMP9021


'''
Prompts the user for a string w of lowercase letters and outputs the longest
sequence of consecutive letters that occur in w, but with possibly other letters
in between, starting as close as possible to the beginning of w.
'''


import sys


word = input('Please input a string of lowercase letters: ')
for c in word:
    if not c.islower():
        print('Incorrect input')
        sys.exit()

for c in word:
    print(f'{ord(c)}')
        
        
