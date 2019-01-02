
import sys

word = input('Enter a word: ')

ord_list = [ord(x) for x in word]
longest_length = 0
start = None

for i in range(len(word)):
    required = 1
    for j in range(i+1, len(word)):
        if ord(word[i]) + required == ord(word[j]):
            required += 1
    if required > longest_length:
        longest_length = required
        start = ord_list[i]

print('Longest sequence is: ',''.join(chr(start+x) for x in range(longest_length)))


    
