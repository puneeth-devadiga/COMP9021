

available_digits = int(input('Enter digits: '))
desired_sum = int(input('Enter the sum : '))

def solve(available_digits, desired_sum):
    if desired_sum < 0:
        return 0
    if available_digits == 0:
        if desired_sum == 0:
            return 1
        return 0

    return solve(available_digits//10, desired_sum) +\
           solve(available_digits//10, desired_sum - available_digits%10)

nb_of_solutions = solve(available_digits, desired_sum)
if nb_of_solutions == 0:
    print('There is no solution.')
elif nb_of_solutions == 1:
    print('There is a unique solution.')
else:
    print(f'There are {nb_of_solutions} solutions.')        
    
    
