
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


for i in range(100, 1000):
    for j in range(10, 100):

        product1 = i * (j %10)
        if product1 < 1000:
            continue
        product2 = i * (j//10)
        
        if product2 >= 1000:
            continue

        total = product1 + (product2 * 10)
        if total >= 10000:
            continue

        the_sum = i%10 +  j%10 + product1%10 + total%10

        if (i//10%10) + (j//10) + (product1//10%10) + (product2%10) + (total//10%10) != the_sum:
            continue

        if (i//100%10) + (product1//100%10) + (product2//10%10) + (total//100%10) != the_sum:
            continue

        if (product1//1000) + (product2//100) + (total//1000) == the_sum:

            print('{} X {} = {} with the sum {}'.format(i, j, (i*j), the_sum))
        
        
