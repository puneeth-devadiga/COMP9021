# Written by Eric Martin for COMP9021


'''
Prints out a conversion table of temperatures from Celsius to Fahrenheit degrees,
the former ranging from 0 to 100 in steps of 10.
'''


min_temperature = 0
max_temperature = 100
step = 10

print('Celsius\tFahrenheit')
for celsius in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    fahrenheit = celsius // 5 * 9 + 32
    print(f'{celsius:7d}\t{fahrenheit:10d}')
