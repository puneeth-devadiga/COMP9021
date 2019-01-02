# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.

S = [None] * 2001 #This is needed for 100 to 999. We waste 0 to 99

for a in range(0,32):
    for b in range(0,32):
        if (a**2 + b**2) < 100 or (a**2 + b**2)  > 1000: # If sum is 3 digits
            continue        
        else:
            S[(a**2)+(b**2)] = (a,b)


for i in range(100, 997 + 1):
    if None not in (S[i],S[i+1],S[i+2]):

        
        print('({}, {}, {}) (equal to ({}^2+{}^2, {}^2+{}^2, {}^2+{}^2)) is a solution.' \
              .format(i, i+1, i+2, S[i][0], S[i][1], S[i+1][0], S[i+1][1], S[i+2][0], S[i+2][1])) 
            
