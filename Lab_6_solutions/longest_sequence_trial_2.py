# Written by Eric Martin for COMP9021


'''
Prompts the user for a string w of lowercase letters and outputs the longest
sequence of consecutive letters that occur in w, but with possibly other letters
in between, starting as close as possible to the beginning of w.
'''


word = input('Enter a word: ')

longest_length = 0
start = None

ord_list = [ord(x) for x in word]

for i in range(len(word)):
    required = 1
    for j in range(i+1, len(word)):
        if ord(word[i])+required == ord(word[j]):
            required += 1
        if required > longest_length:
            longest_length = required
            start = ord_list[i]

print('The longest sequence is: ',''.join(chr(start + i) for i in range(longest_length)))
