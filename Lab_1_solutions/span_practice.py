from random import seed, randint
import sys

try:
    arg_for_seed = int(input('Enter a seed: '))
    if arg_for_seed <= 0:
        raise exception
except:
    print('Not a valid input')
    sys.exit()

try:
    number_of_elements = int(input('Enter number of elements: '))
    if number_of_elements <= 0:
        raise exception
except:
    print('Not a valid input')
    sys.exit()

seed(arg_for_seed)

L = [randint(0, 99) for _ in range(number_of_elements)]

print('The list generated is: ', L)

max_element = 0
min_element = 99


for e in L:
    if e > max_element:
        max_element = e
    if e < min_element:
        min_element = e
min_max_diff = (max_element - min_element)
print(f'The difference between {max_element} and {min_element} is {min_max_diff}')

    
