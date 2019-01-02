# Written by Puneeth for COMP9021


'''
Decodes all multiplications of the form

                       *  *  *
                  x       *  *
                    ----------
                    *  *  *  *
                    *  *  *
                    ----------
                    *  *  *  *

such that the sum of all digits in all 4 columns is constant.
'''

for x in range(100, 1000):    
    for y in range(10, 100):
        product1 = x * (y%10)
        if product1 < 1000:
            continue
        product2 = x * (y // 10)
        if product2 >= 1000:
            continue
        total = product1 + product2 * 10
        if total >=10000:
            continue

        the_sum = x%10 + y%10 + product1%10 + total%10
        
        if x//10%10 + y//10 + product1//10%10 + product2%10 + total//10%10 != the_sum :
            continue

        if x//100 + product1//100%10 + product2//10%10 + total//100%10 != the_sum :
            continue

        if product1//1000 + product2//100 + total//1000 == the_sum:     
            print(f' {x} and {y} with the total sum {the_sum}') 
