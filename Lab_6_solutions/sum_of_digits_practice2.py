
available_digits = int(input('Enter digits: '))
desired_sum = int(input('Enter sum: '))

def solve(available_digits, desired_sum):
    if desired_sum < 0:
        return 0
    if available_digits == 0:
        if desired_sum == 0:
            return 1
        return 0
    return solve(available_digits//10, desired_sum) +\
           solve(available_digits//10, desired_sum - available_digits%10)

solutions = solve(available_digits, desired_sum)

if solutions == 0:
    print('No solutions available')
if solutions == 1:
    print('only one solution avaulble')
if solutions > 1:
    print('{} solutions are available'.format(solutions))
