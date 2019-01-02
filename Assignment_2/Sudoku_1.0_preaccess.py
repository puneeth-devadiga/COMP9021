import sys
fname = 'sudoku_4.txt'
grid = []

def pre_check(fname):   
    
    with open(fname) as f:
        content = list(line for line in (l.strip() for l in f) if line)

    given_grid = []
    # Checking for grid 9 X 9 and contains only digits
    try:
        if len(content) != 9:
            raise ValueError
        else:
            for i in content:
                i =i.replace(" ", "")
                if len(list(i)) == 9:
                    for x in i:
                        if x.isdigit() ==  False:
                            raise ValueError
                            break
                    given_grid.append(list(i))
                else:
                    raise ValueError
                    break
    except ValueError:
        print('Incorrect input')
        sys.exit()

    #print(given_grid)

    grid = []
    for row in given_grid:
        row = [int(e) for e in row]
        grid.append(row)

    #print(grid)
    return (grid)

grid = pre_check(fname)


def preassess(grid):


    # To check if there are repeats in a row
    
    for row in grid:
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
        for row in grid:            
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

    Box = []
    
    Box =   [[ grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2] ],
            [ grid[0][3], grid[0][4], grid[0][5], grid[1][3], grid[1][4], grid[1][5], grid[2][3], grid[2][4], grid[2][5] ],
            [ grid[0][6], grid[0][7], grid[0][8], grid[1][6], grid[1][7], grid[1][8], grid[2][6], grid[2][7], grid[2][8] ],
            [ grid[3][0], grid[3][1], grid[3][2], grid[4][0], grid[4][1], grid[4][2], grid[5][0], grid[5][1], grid[5][2] ],
            [ grid[3][3], grid[3][4], grid[3][5], grid[4][3], grid[4][4], grid[4][5], grid[5][3], grid[5][4], grid[5][5] ],
            [ grid[3][6], grid[3][7], grid[3][8], grid[4][6], grid[4][7], grid[4][8], grid[5][6], grid[5][7], grid[5][8] ],
            [ grid[6][0], grid[6][1], grid[6][2], grid[7][0], grid[7][1], grid[7][2], grid[8][0], grid[8][1], grid[8][2] ],
            [ grid[6][3], grid[6][4], grid[6][5], grid[7][3], grid[7][4], grid[7][5], grid[8][3], grid[8][4], grid[8][5] ],
            [ grid[6][6], grid[6][7], grid[6][8], grid[7][6], grid[7][7], grid[7][8], grid[8][6], grid[8][7], grid[8][8] ]]


    for i in range(9):
        temp2 = []
        for j in Box[i]:
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

preassess(grid)
    
    
