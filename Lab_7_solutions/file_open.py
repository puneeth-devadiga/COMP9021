

with open('dictionary.txt') as f:
    for line in f:
        word = line.rstrip()
        print(word)
