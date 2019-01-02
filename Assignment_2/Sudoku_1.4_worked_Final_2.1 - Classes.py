
import sys
from collections import Counter
from collections import defaultdict

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message

class Sudoku:
    def __init__(self, fname):
        self.fname = fname

        with open(self.fname) as f:
            content = list(line for line in (l.strip() for l in f) if line)

        given_grid = []
        #Checking for grid 9 X 9 and contains only digits
    
        if len(content) != 9:
            raise SudokuError('Incorrect input')
        else:
            for i in content:
                i =i.replace(" ", "")
                if len(list(i)) == 9:
                    for x in i:
                        if x.isdigit() ==  False:
                            raise SudokuError('Incorrect input')
                    given_grid.append(list(i))
                else:
                    raise SudokuError('Incorrect input')

        self.grid = []
        for row in given_grid:
            row = [int(e) for e in row]
            self.grid.append(row)


        self.Box =  [[ self.grid[0][0], self.grid[0][1], self.grid[0][2], self.grid[1][0], self.grid[1][1], self.grid[1][2], self.grid[2][0], self.grid[2][1], self.grid[2][2] ],
                    [ self.grid[0][3], self.grid[0][4], self.grid[0][5], self.grid[1][3], self.grid[1][4], self.grid[1][5], self.grid[2][3], self.grid[2][4], self.grid[2][5] ],
                    [ self.grid[0][6], self.grid[0][7], self.grid[0][8], self.grid[1][6], self.grid[1][7], self.grid[1][8], self.grid[2][6], self.grid[2][7], self.grid[2][8] ],
                    [ self.grid[3][0], self.grid[3][1], self.grid[3][2], self.grid[4][0], self.grid[4][1], self.grid[4][2], self.grid[5][0], self.grid[5][1], self.grid[5][2] ],
                    [ self.grid[3][3], self.grid[3][4], self.grid[3][5], self.grid[4][3], self.grid[4][4], self.grid[4][5], self.grid[5][3], self.grid[5][4], self.grid[5][5] ],
                    [ self.grid[3][6], self.grid[3][7], self.grid[3][8], self.grid[4][6], self.grid[4][7], self.grid[4][8], self.grid[5][6], self.grid[5][7], self.grid[5][8] ],
                    [ self.grid[6][0], self.grid[6][1], self.grid[6][2], self.grid[7][0], self.grid[7][1], self.grid[7][2], self.grid[8][0], self.grid[8][1], self.grid[8][2] ],
                    [ self.grid[6][3], self.grid[6][4], self.grid[6][5], self.grid[7][3], self.grid[7][4], self.grid[7][5], self.grid[8][3], self.grid[8][4], self.grid[8][5] ],
                    [ self.grid[6][6], self.grid[6][7], self.grid[6][8], self.grid[7][6], self.grid[7][7], self.grid[7][8], self.grid[8][6], self.grid[8][7], self.grid[8][8] ]]
        

    def preassess(self):    

    # To check if there are repeats in a row   
        for row in self.grid:
            temp = []
            for e in row:
                if e == 0:
                    temp.append(e)
                    continue
                elif e not in temp:
                    temp.append(e)
                else:
                    print('There is clearly no solution.')
                    sys.exit()

        # To check if there are repeats in a column
        for x in range(9):
            temp = []
            for row in self.grid:            
                #f = int(row[x])
                if row[x] == 0:
                    temp.append(row[x])
                    continue
                elif row[x] not in temp:
                    temp.append(row[x])
                    continue
                else:
                    print('There is clearly no solution.')
                    sys.exit()

        # To check if there are repeats in box

        for i in range(9):
            temp2 = []
            for j in self.Box[i]:
                #j = int(j)
                if j == 0:
                    temp2.append(j)
                    continue
                elif j not in temp2:
                    temp2.append(j)
                else:
                    print('There is clearly no solution.')
                    sys.exit()
                
        print('There might be a solution.')
