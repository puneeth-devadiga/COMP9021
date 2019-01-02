
word = input('Enter a word: ')

ord_list = [ord(x) for x in word]

longest_length = 0
start = None
super_store = list()
for i in range(len(word)):
    required = 1
    for j in range(i+1, len(word)):
        if ord(word[i]) + required == ord(word[j]):
            required += 1
        store = list()
        store.append(x for x in range(ord(word[i]), ord(word[i + required])-1))
    super_store.append(store)
    if required > longest_length:
        longest_length = required
        start = ord_list[i]

print('The longest sequence is:', ''.join(chr(start+i) for i in range(longest_length)))
