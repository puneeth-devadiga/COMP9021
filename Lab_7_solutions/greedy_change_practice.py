

face_values = [1, 2, 5, 10, 20, 50, 100]

amount = int(input('Enter given amount: '))
bank_notes = list()
amount_left = amount

while amount_left:
    value = face_values.pop()
    if amount_left >= value:
        bank_notes.append((value, amount_left//value))
        amount_left %= value

no_of_notes = sum(bank_note[1] for bank_note in bank_notes)

print('No notes: {}'.format(no_of_notes))

for bank_note in bank_notes:
    print('{:>4}:{}'.format('$'+str(bank_note[0]), bank_note[1]))
        
    
