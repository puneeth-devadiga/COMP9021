
import sys

fname = 'sudoku_4.txt'
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


def bare_tex_output(grid):

    latex = ['\\documentclass[10pt]{article}\n', '\\usepackage[left=0pt,right=0pt]{geometry}\n',\
             '\\usepackage{tikz}\n', '\\usetikzlibrary{positioning}\n', '\\usepackage{cancel}\n', \
             '\\pagestyle{empty}\n', '\n', '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n',\
             ' label=above right:{\\tiny #2},\n', ' label=below left:{\\tiny #3},\n',\
             ' label=below right:{\\tiny #4}]{#5};}}\n', '\n', '\\begin{document}\n',\
             '\n', '\\tikzset{every node/.style={minimum size=.5cm}}\n', '\n', '\\begin{center}\n',\
             '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n',\
             '% Line 1\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n',\
             '% Line 2\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n',\
             '% Line 3\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n','\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n', '\n',\
             '% Line 4\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n','\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n',\
             '% Line 5\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n',
             '% Line 6\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n', '\n',
             '% Line 7\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n','\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', \
             '% Line 8\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n','\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', \
             '% Line 9\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n','\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n', \
             '\\end{tabular}\n', '\\end{center}\n', '\n', '\\end{document}\n']



        
        # finding the index to add grid elements
    for row in range(9):
        for string in range(len(latex)):
            if latex[string] == '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n' and\
               (latex[string+2]== '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n' or\
                latex[string+2]== '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n'):
                
                
                if grid[row][0] != 0:
                    latex[string] = latex[string][:11] + str(grid[row][0]) + latex[string][11:]
                else:
                    latex[string] = latex[string][:11] + ' ' + latex[string][11:]
                if grid[row][3] != 0:
                    latex[string+1] = latex[string+1][:11] + str(grid[row][3]) + latex[string+1][11:]
                else:
                    latex[string+1] = latex[string+1][:11] + ' ' + latex[string+1][11:]
                if grid[row][6] != 0:
                    latex[string+2] = latex[string+2][:11] + str(grid[row][6]) + latex[string+2][11:]
                else:
                    latex[string+2] = latex[string+2][:11] + ' ' + latex[string+2][11:]
                    
                if grid[row][1] != 0:
                    latex[string] = latex[string][:27] + str(grid[row][1]) + latex[string][27:]
                else:
                    latex[string] = latex[string][:27] + ' ' + latex[string][27:]
                    
                if grid[row][4] != 0:
                    latex[string+1] = latex[string+1][:27] + str(grid[row][4]) + latex[string+1][27:]
                else:
                    latex[string+1] = latex[string+1][:27] + ' ' + latex[string+1][27:]
                    
                if grid[row][7] != 0:
                    latex[string+2] = latex[string+2][:27] + str(grid[row][7]) + latex[string+2][27:]
                else:
                    latex[string+2] = latex[string+2][:27] + ' ' + latex[string+2][27:]

                if grid[row][2] != 0:
                    latex[string] = latex[string][:43] + str(grid[row][2]) + latex[string][43:]
                else:
                    latex[string] = latex[string][:43] + ' ' + latex[string][43:]
                    
                if grid[row][5] != 0:
                    latex[string+1] = latex[string+1][:43] + str(grid[row][5]) + latex[string+1][43:]
                else:
                    latex[string+1] = latex[string+1][:43] + ' ' + latex[string+1][43:]
                    
                if grid[row][8] != 0:
                    latex[string+2] = latex[string+2][:43] + str(grid[row][8]) + latex[string+2][43:]
                else:
                    latex[string+2] = latex[string+2][:43] + ' ' + latex[string+2][43:]

                #print(row)
                break

    for i in range(len(latex)):
        for j in range(len(latex[i])):
            try:
                if latex[i][j] == '{' and latex[i][j+1] == ' ' and latex[i][j+2] == '}':
                    latex[i] = latex[i][:j+1] + latex[i][j+2:]
            except IndexError:
                pass
            
    with open('filename_bare.tex','w+') as bare:      
        for line in latex:
            bare.write(line)
            print(line)
    
bare_tex_output(grid)


    
        
        
    
    
