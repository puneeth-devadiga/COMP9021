

max = 1000

for i in range(2, max):

    if 1 +sum(j for j in range(2, i//2+1) if i%j == 0)== i:
        print('Perfect number:', i)
    
