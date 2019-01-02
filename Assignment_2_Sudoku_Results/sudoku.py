import sys
from collections import Counter
from collections import defaultdict
from copy import deepcopy

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

        self.given_grid = deepcopy(self.grid)
        
        self.Box =  [[ self.grid[0][0], self.grid[0][1], self.grid[0][2], self.grid[1][0], self.grid[1][1], self.grid[1][2], self.grid[2][0], self.grid[2][1], self.grid[2][2] ],
                    [ self.grid[0][3], self.grid[0][4], self.grid[0][5], self.grid[1][3], self.grid[1][4], self.grid[1][5], self.grid[2][3], self.grid[2][4], self.grid[2][5] ],
                    [ self.grid[0][6], self.grid[0][7], self.grid[0][8], self.grid[1][6], self.grid[1][7], self.grid[1][8], self.grid[2][6], self.grid[2][7], self.grid[2][8] ],
                    [ self.grid[3][0], self.grid[3][1], self.grid[3][2], self.grid[4][0], self.grid[4][1], self.grid[4][2], self.grid[5][0], self.grid[5][1], self.grid[5][2] ],
                    [ self.grid[3][3], self.grid[3][4], self.grid[3][5], self.grid[4][3], self.grid[4][4], self.grid[4][5], self.grid[5][3], self.grid[5][4], self.grid[5][5] ],
                    [ self.grid[3][6], self.grid[3][7], self.grid[3][8], self.grid[4][6], self.grid[4][7], self.grid[4][8], self.grid[5][6], self.grid[5][7], self.grid[5][8] ],
                    [ self.grid[6][0], self.grid[6][1], self.grid[6][2], self.grid[7][0], self.grid[7][1], self.grid[7][2], self.grid[8][0], self.grid[8][1], self.grid[8][2] ],
                    [ self.grid[6][3], self.grid[6][4], self.grid[6][5], self.grid[7][3], self.grid[7][4], self.grid[7][5], self.grid[8][3], self.grid[8][4], self.grid[8][5] ],
                    [ self.grid[6][6], self.grid[6][7], self.grid[6][8], self.grid[7][6], self.grid[7][7], self.grid[7][8], self.grid[8][6], self.grid[8][7], self.grid[8][8] ]]

        self.P_Box =  [[ self.given_grid[0][0], self.given_grid[0][1], self.given_grid[0][2], self.given_grid[1][0], self.given_grid[1][1], self.given_grid[1][2], self.given_grid[2][0], self.given_grid[2][1], self.given_grid[2][2] ],
                    [ self.given_grid[0][3], self.given_grid[0][4], self.given_grid[0][5], self.given_grid[1][3], self.given_grid[1][4], self.given_grid[1][5], self.given_grid[2][3], self.given_grid[2][4], self.given_grid[2][5] ],
                    [ self.given_grid[0][6], self.given_grid[0][7], self.given_grid[0][8], self.given_grid[1][6], self.given_grid[1][7], self.given_grid[1][8], self.given_grid[2][6], self.given_grid[2][7], self.given_grid[2][8] ],
                    [ self.given_grid[3][0], self.given_grid[3][1], self.given_grid[3][2], self.given_grid[4][0], self.given_grid[4][1], self.given_grid[4][2], self.given_grid[5][0], self.given_grid[5][1], self.given_grid[5][2] ],
                    [ self.given_grid[3][3], self.given_grid[3][4], self.given_grid[3][5], self.given_grid[4][3], self.given_grid[4][4], self.given_grid[4][5], self.given_grid[5][3], self.given_grid[5][4], self.given_grid[5][5] ],
                    [ self.given_grid[3][6], self.given_grid[3][7], self.given_grid[3][8], self.given_grid[4][6], self.given_grid[4][7], self.given_grid[4][8], self.given_grid[5][6], self.given_grid[5][7], self.given_grid[5][8] ],
                    [ self.given_grid[6][0], self.given_grid[6][1], self.given_grid[6][2], self.given_grid[7][0], self.given_grid[7][1], self.given_grid[7][2], self.given_grid[8][0], self.given_grid[8][1], self.given_grid[8][2] ],
                    [ self.given_grid[6][3], self.given_grid[6][4], self.given_grid[6][5], self.given_grid[7][3], self.given_grid[7][4], self.given_grid[7][5], self.given_grid[8][3], self.given_grid[8][4], self.given_grid[8][5] ],
                    [ self.given_grid[6][6], self.given_grid[6][7], self.given_grid[6][8], self.given_grid[7][6], self.given_grid[7][7], self.given_grid[7][8], self.given_grid[8][6], self.given_grid[8][7], self.given_grid[8][8] ]]


        self.latex = ['\\documentclass[10pt]{article}\n', '\\usepackage[left=0pt,right=0pt]{geometry}\n', '\\usepackage{tikz}\n', '\\usetikzlibrary{positioning}\n', '\\usepackage{cancel}\n', '\\pagestyle{empty}\n', '\n', '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n', '                               label=above right:{\\tiny #2},\n', '                               label=below left:{\\tiny #3},\n', '                               label=below right:{\\tiny #4}]{#5};}}\n', '\n', '\\begin{document}\n', '\n', '\\tikzset{every node/.style={minimum size=.5cm}}\n', '\n', '\\begin{center}\n', '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n', '% Line 1\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', '% Line 2\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', '% Line 3\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n', '\n', '% Line 4\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', '% Line 5\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', '% Line 6\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n', '\n', '% Line 7\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', '% Line 8\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n', '\n', '% Line 9\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n', '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n', '\\end{tabular}\n', '\\end{center}\n', '\n', '\\end{document}\n'] 

        self.forced_latex = deepcopy(self.latex)
#------Flow---------------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.run_bare()
        self.run_forced()
        self.run_marked()
        

        self.marked_grid = deepcopy(self.grid)  # Saving Copy of grid after MARKED to compare with WORKED
        
        self.new_grid = deepcopy(self.grid) # copy of marked grid to be used in WORKED
           
        self.marked_latex = self.get_marked_latex() # Because self.grid will be lost here as its used for LATEX

        self.new_column = deepcopy(self.grid_to_col())
        self.new_Box = deepcopy(self.grid_to_box())
        self.run_worked()
        self.worked_latex = self.get_worked_latex()        
#-------Methods----------------------------------------------------------------------------------------------------------------------------------------------------

    def grid_to_col(self):
        self.new_column =[]
        for i in range(9):
            c = [self.new_grid[x][i] for x in range(9)]
            self.new_column.append(c)
        return self.new_column

    def col_to_grid(self):
        self.new_grid = []
        for i in range(9):
            g = [self.new_column[x][i] for x in range(9)]
            self.new_grid.append(g)
        return self.new_grid
            
    def grid_to_box(self):
        Box =[[ self.new_grid[0][0], self.new_grid[0][1], self.new_grid[0][2], self.new_grid[1][0], self.new_grid[1][1], self.new_grid[1][2], self.new_grid[2][0], self.new_grid[2][1], self.new_grid[2][2] ],
              [ self.new_grid[0][3], self.new_grid[0][4], self.new_grid[0][5], self.new_grid[1][3], self.new_grid[1][4], self.new_grid[1][5], self.new_grid[2][3], self.new_grid[2][4], self.new_grid[2][5] ],
              [ self.new_grid[0][6], self.new_grid[0][7], self.new_grid[0][8], self.new_grid[1][6], self.new_grid[1][7], self.new_grid[1][8], self.new_grid[2][6], self.new_grid[2][7], self.new_grid[2][8] ],
              [ self.new_grid[3][0], self.new_grid[3][1], self.new_grid[3][2], self.new_grid[4][0], self.new_grid[4][1], self.new_grid[4][2], self.new_grid[5][0], self.new_grid[5][1], self.new_grid[5][2] ],
              [ self.new_grid[3][3], self.new_grid[3][4], self.new_grid[3][5], self.new_grid[4][3], self.new_grid[4][4], self.new_grid[4][5], self.new_grid[5][3], self.new_grid[5][4], self.new_grid[5][5] ],
              [ self.new_grid[3][6], self.new_grid[3][7], self.new_grid[3][8], self.new_grid[4][6], self.new_grid[4][7], self.new_grid[4][8], self.new_grid[5][6], self.new_grid[5][7], self.new_grid[5][8] ],
              [ self.new_grid[6][0], self.new_grid[6][1], self.new_grid[6][2], self.new_grid[7][0], self.new_grid[7][1], self.new_grid[7][2], self.new_grid[8][0], self.new_grid[8][1], self.new_grid[8][2] ],
              [ self.new_grid[6][3], self.new_grid[6][4], self.new_grid[6][5], self.new_grid[7][3], self.new_grid[7][4], self.new_grid[7][5], self.new_grid[8][3], self.new_grid[8][4], self.new_grid[8][5] ],
              [ self.new_grid[6][6], self.new_grid[6][7], self.new_grid[6][8], self.new_grid[7][6], self.new_grid[7][7], self.new_grid[7][8], self.new_grid[8][6], self.new_grid[8][7], self.new_grid[8][8] ]]
        return Box

    
    def box_to_grid(self):
        self.new_grid = [[ self.new_Box[0][0], self.new_Box[0][1], self.new_Box[0][2], self.new_Box[1][0], self.new_Box[1][1], self.new_Box[1][2], self.new_Box[2][0], self.new_Box[2][1], self.new_Box[2][2] ],
                    [ self.new_Box[0][3], self.new_Box[0][4], self.new_Box[0][5], self.new_Box[1][3], self.new_Box[1][4], self.new_Box[1][5], self.new_Box[2][3], self.new_Box[2][4], self.new_Box[2][5] ],
                    [ self.new_Box[0][6], self.new_Box[0][7], self.new_Box[0][8], self.new_Box[1][6], self.new_Box[1][7], self.new_Box[1][8], self.new_Box[2][6], self.new_Box[2][7], self.new_Box[2][8] ],
                    [ self.new_Box[3][0], self.new_Box[3][1], self.new_Box[3][2], self.new_Box[4][0], self.new_Box[4][1], self.new_Box[4][2], self.new_Box[5][0], self.new_Box[5][1], self.new_Box[5][2] ],
                    [ self.new_Box[3][3], self.new_Box[3][4], self.new_Box[3][5], self.new_Box[4][3], self.new_Box[4][4], self.new_Box[4][5], self.new_Box[5][3], self.new_Box[5][4], self.new_Box[5][5] ],
                    [ self.new_Box[3][6], self.new_Box[3][7], self.new_Box[3][8], self.new_Box[4][6], self.new_Box[4][7], self.new_Box[4][8], self.new_Box[5][6], self.new_Box[5][7], self.new_Box[5][8] ],
                    [ self.new_Box[6][0], self.new_Box[6][1], self.new_Box[6][2], self.new_Box[7][0], self.new_Box[7][1], self.new_Box[7][2], self.new_Box[8][0], self.new_Box[8][1], self.new_Box[8][2] ],
                    [ self.new_Box[6][3], self.new_Box[6][4], self.new_Box[6][5], self.new_Box[7][3], self.new_Box[7][4], self.new_Box[7][5], self.new_Box[8][3], self.new_Box[8][4], self.new_Box[8][5] ],
                    [ self.new_Box[6][6], self.new_Box[6][7], self.new_Box[6][8], self.new_Box[7][6], self.new_Box[7][7], self.new_Box[7][8], self.new_Box[8][6], self.new_Box[8][7], self.new_Box[8][8] ]]
        return self.new_grid
    
    def col_to_Box(self):
        self.new_grid = []
        for i in range(9):
            g = [self.new_column[x][i] for x in range(9)]
            self.new_grid.append(g)

        Box =[[ self.new_grid[0][0], self.new_grid[0][1], self.new_grid[0][2], self.new_grid[1][0], self.new_grid[1][1], self.new_grid[1][2], self.new_grid[2][0], self.new_grid[2][1], self.new_grid[2][2] ],
              [ self.new_grid[0][3], self.new_grid[0][4], self.new_grid[0][5], self.new_grid[1][3], self.new_grid[1][4], self.new_grid[1][5], self.new_grid[2][3], self.new_grid[2][4], self.new_grid[2][5] ],
              [ self.new_grid[0][6], self.new_grid[0][7], self.new_grid[0][8], self.new_grid[1][6], self.new_grid[1][7], self.new_grid[1][8], self.new_grid[2][6], self.new_grid[2][7], self.new_grid[2][8] ],
              [ self.new_grid[3][0], self.new_grid[3][1], self.new_grid[3][2], self.new_grid[4][0], self.new_grid[4][1], self.new_grid[4][2], self.new_grid[5][0], self.new_grid[5][1], self.new_grid[5][2] ],
              [ self.new_grid[3][3], self.new_grid[3][4], self.new_grid[3][5], self.new_grid[4][3], self.new_grid[4][4], self.new_grid[4][5], self.new_grid[5][3], self.new_grid[5][4], self.new_grid[5][5] ],
              [ self.new_grid[3][6], self.new_grid[3][7], self.new_grid[3][8], self.new_grid[4][6], self.new_grid[4][7], self.new_grid[4][8], self.new_grid[5][6], self.new_grid[5][7], self.new_grid[5][8] ],
              [ self.new_grid[6][0], self.new_grid[6][1], self.new_grid[6][2], self.new_grid[7][0], self.new_grid[7][1], self.new_grid[7][2], self.new_grid[8][0], self.new_grid[8][1], self.new_grid[8][2] ],
              [ self.new_grid[6][3], self.new_grid[6][4], self.new_grid[6][5], self.new_grid[7][3], self.new_grid[7][4], self.new_grid[7][5], self.new_grid[8][3], self.new_grid[8][4], self.new_grid[8][5] ],
              [ self.new_grid[6][6], self.new_grid[6][7], self.new_grid[6][8], self.new_grid[7][6], self.new_grid[7][7], self.new_grid[7][8], self.new_grid[8][6], self.new_grid[8][7], self.new_grid[8][8] ]]
        return Box
    
    def box_to_col(self):
        self.new_grid = [[ self.new_Box[0][0], self.new_Box[0][1], self.new_Box[0][2], self.new_Box[1][0], self.new_Box[1][1], self.new_Box[1][2], self.new_Box[2][0], self.new_Box[2][1], self.new_Box[2][2] ],
                    [ self.new_Box[0][3], self.new_Box[0][4], self.new_Box[0][5], self.new_Box[1][3], self.new_Box[1][4], self.new_Box[1][5], self.new_Box[2][3], self.new_Box[2][4], self.new_Box[2][5] ],
                    [ self.new_Box[0][6], self.new_Box[0][7], self.new_Box[0][8], self.new_Box[1][6], self.new_Box[1][7], self.new_Box[1][8], self.new_Box[2][6], self.new_Box[2][7], self.new_Box[2][8] ],
                    [ self.new_Box[3][0], self.new_Box[3][1], self.new_Box[3][2], self.new_Box[4][0], self.new_Box[4][1], self.new_Box[4][2], self.new_Box[5][0], self.new_Box[5][1], self.new_Box[5][2] ],
                    [ self.new_Box[3][3], self.new_Box[3][4], self.new_Box[3][5], self.new_Box[4][3], self.new_Box[4][4], self.new_Box[4][5], self.new_Box[5][3], self.new_Box[5][4], self.new_Box[5][5] ],
                    [ self.new_Box[3][6], self.new_Box[3][7], self.new_Box[3][8], self.new_Box[4][6], self.new_Box[4][7], self.new_Box[4][8], self.new_Box[5][6], self.new_Box[5][7], self.new_Box[5][8] ],
                    [ self.new_Box[6][0], self.new_Box[6][1], self.new_Box[6][2], self.new_Box[7][0], self.new_Box[7][1], self.new_Box[7][2], self.new_Box[8][0], self.new_Box[8][1], self.new_Box[8][2] ],
                    [ self.new_Box[6][3], self.new_Box[6][4], self.new_Box[6][5], self.new_Box[7][3], self.new_Box[7][4], self.new_Box[7][5], self.new_Box[8][3], self.new_Box[8][4], self.new_Box[8][5] ],
                    [ self.new_Box[6][6], self.new_Box[6][7], self.new_Box[6][8], self.new_Box[7][6], self.new_Box[7][7], self.new_Box[7][8], self.new_Box[8][6], self.new_Box[8][7], self.new_Box[8][8] ]]
        
        self.new_column =[]
        for i in range(9):
            c = [self.new_grid[x][i] for x in range(9)]
            self.new_column.append(c)
        return self.new_column

    def find_singleton(self):
        for i in range(9):
            for j in range(9):
                if type(self.new_grid[i][j]) == set and len(self.new_grid[i][j]) == 1:
                    self.new_grid[i][j] = list(self.new_grid[i][j])[0]
                    self.arrange(i, j, self.new_grid[i][j], self.new_grid)
                    self.find_singleton()

    def get_box_number(self, a, b):
        box_cord ={1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], 2: [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)], 3: [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)], 4: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)], 5: [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)], 6: [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)], 7: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)], 8: [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)], 9: [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]}
        for i in range(1,10):
            for j in range(9):
                if box_cord[i][j][0] == a and box_cord[i][j][1] == b:
                    n = i
                    return n
                
    def arrange(self, a, b, value, new_grid):
        for e in range(9):
            if type(self.new_grid[a][e]) == set and len(self.new_grid[a][e]) > 1 and value in self.new_grid[a][e]:
                self.new_grid[a][e].remove(value)
                
        self.new_column = self.grid_to_col()
        self.new_Box = self.grid_to_box()
        
        for e in range(len(self.new_column[b])):
            if type(self.new_column[b][e]) == set and len(self.new_column[b][e]) > 1 and value in self.new_column[b][e]:
                self.new_column[b][e].remove(value)
        
        self.new_grid = self.col_to_grid()
        self.new_Box = self.col_to_Box()
        
        #function to take a,b and return box number

        n = self.get_box_number(a, b)
        for e in range(len(self.new_Box[n-1])):
            if type(self.new_Box[n-1][e]) == set and len(self.new_Box[n-1][e]) > 1 and value in self.new_Box[n-1][e]:
                self.new_Box[n-1][e].remove(value)

        self.new_grid = self.box_to_grid()
        self.new_column = self.box_to_col()
        
    def preassess(self):
    # To check if there are repeats in a row
        
        for row in self.given_grid:
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
            for row in self.given_grid:            
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
            for j in self.P_Box[i]:
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

    
    def run_bare(self):

        # finding the index to add grid elements to self.latex
        for row in range(9):
            for string in range(len(self.latex)):
                if self.latex[string] == '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n' and\
                   (self.latex[string+2]== '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n' or\
                    self.latex[string+2]== '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n'):
                    
                    
                    if self.grid[row][0] != 0:
                        self.latex[string] = self.latex[string][:11] + str(self.grid[row][0]) + self.latex[string][11:]
                    else:
                        self.latex[string] = self.latex[string][:11] + ' ' + self.latex[string][11:]
                    if self.grid[row][3] != 0:
                        self.latex[string+1] = self.latex[string+1][:11] + str(self.grid[row][3]) + self.latex[string+1][11:]
                    else:
                        self.latex[string+1] = self.latex[string+1][:11] + ' ' + self.latex[string+1][11:]
                    if self.grid[row][6] != 0:
                        self.latex[string+2] = self.latex[string+2][:11] + str(self.grid[row][6]) + self.latex[string+2][11:]
                    else:
                        self.latex[string+2] = self.latex[string+2][:11] + ' ' + self.latex[string+2][11:]
                        
                    if self.grid[row][1] != 0:
                        self.latex[string] = self.latex[string][:27] + str(self.grid[row][1]) + self.latex[string][27:]
                    else:
                        self.latex[string] = self.latex[string][:27] + ' ' + self.latex[string][27:]
                        
                    if self.grid[row][4] != 0:
                        self.latex[string+1] = self.latex[string+1][:27] + str(self.grid[row][4]) + self.latex[string+1][27:]
                    else:
                        self.latex[string+1] = self.latex[string+1][:27] + ' ' + self.latex[string+1][27:]
                        
                    if self.grid[row][7] != 0:
                        self.latex[string+2] = self.latex[string+2][:27] + str(self.grid[row][7]) + self.latex[string+2][27:]
                    else:
                        self.latex[string+2] = self.latex[string+2][:27] + ' ' + self.latex[string+2][27:]

                    if self.grid[row][2] != 0:
                        self.latex[string] = self.latex[string][:43] + str(self.grid[row][2]) + self.latex[string][43:]
                    else:
                        self.latex[string] = self.latex[string][:43] + ' ' + self.latex[string][43:]
                        
                    if self.grid[row][5] != 0:
                        self.latex[string+1] = self.latex[string+1][:43] + str(self.grid[row][5]) + self.latex[string+1][43:]
                    else:
                        self.latex[string+1] = self.latex[string+1][:43] + ' ' + self.latex[string+1][43:]
                        
                    if self.grid[row][8] != 0:
                        self.latex[string+2] = self.latex[string+2][:43] + str(self.grid[row][8]) + self.latex[string+2][43:]
                    else:
                        self.latex[string+2] = self.latex[string+2][:43] + ' ' + self.latex[string+2][43:]

                    #print(row)
                    break

        for i in range(len(self.latex)):
            for j in range(len(self.latex[i])):
                try:
                    if self.latex[i][j] == '{' and self.latex[i][j+1] == ' ' and self.latex[i][j+2] == '}':
                        self.latex[i] = self.latex[i][:j+1] + self.latex[i][j+2:]
                except IndexError:
                    pass
                
    def bare_tex_output(self):    
        with open(self.fname[:-4] + '_bare.tex','w+') as bare:      
            for line in self.latex:
                bare.write(line)
        
    def run_forced(self):

        # Finding the high frequency numbers        
        temp_grid = []
        
        for row in self.grid:
            for e in row:
                if e != 0:          
                    temp_grid.append(e)    

        high_freq_dict = Counter(temp_grid)
        high_freq_dict = sorted(high_freq_dict, key=lambda x: high_freq_dict[x], reverse= True)

        #print(high_freq_dict)
        #Checking if the high frequency numbers exist in the box

    
        list_of_boxes = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        
        box_cord ={1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], 2: [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)], 3: [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)], 4: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)], 5: [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)], 6: [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)], 7: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)], 8: [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)], 9: [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]}
        row_cord ={1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)], 2: [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)], 3: [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], 4: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)], 5: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)], 6: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)], 7: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)], 8: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)], 9: [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]}
        col_cord ={1: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)], 2: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)], 3: [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)], 4: [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)], 5: [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)], 6: [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)], 7: [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)], 8: [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)], 9: [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]}

        high_freq_num_list = []
        for high_freq_num in high_freq_dict:

            high_freq_num_list.append(high_freq_num)
            found_boxes = []
            not_found_boxes = set()
            for key in box_cord:
                for i in range(9):
                    m,n = box_cord[key][i][0], box_cord[key][i][1]
                    if self.grid[m][n] == high_freq_num:
                        found_boxes.append(key)
                        break

            not_found_boxes = list_of_boxes - set(found_boxes)
            not_found_boxes = list(not_found_boxes)
            not_found_boxes.sort()
            
            #print(f'{high_freq_num} Not found in {not_found_boxes}')

        #print(high_freq_num_list)

        for _ in range(15):
            self.Box =  [[ self.grid[0][0], self.grid[0][1], self.grid[0][2], self.grid[1][0], self.grid[1][1], self.grid[1][2], self.grid[2][0], self.grid[2][1], self.grid[2][2] ],
                        [ self.grid[0][3], self.grid[0][4], self.grid[0][5], self.grid[1][3], self.grid[1][4], self.grid[1][5], self.grid[2][3], self.grid[2][4], self.grid[2][5] ],
                        [ self.grid[0][6], self.grid[0][7], self.grid[0][8], self.grid[1][6], self.grid[1][7], self.grid[1][8], self.grid[2][6], self.grid[2][7], self.grid[2][8] ],
                        [ self.grid[3][0], self.grid[3][1], self.grid[3][2], self.grid[4][0], self.grid[4][1], self.grid[4][2], self.grid[5][0], self.grid[5][1], self.grid[5][2] ],
                        [ self.grid[3][3], self.grid[3][4], self.grid[3][5], self.grid[4][3], self.grid[4][4], self.grid[4][5], self.grid[5][3], self.grid[5][4], self.grid[5][5] ],
                        [ self.grid[3][6], self.grid[3][7], self.grid[3][8], self.grid[4][6], self.grid[4][7], self.grid[4][8], self.grid[5][6], self.grid[5][7], self.grid[5][8] ],
                        [ self.grid[6][0], self.grid[6][1], self.grid[6][2], self.grid[7][0], self.grid[7][1], self.grid[7][2], self.grid[8][0], self.grid[8][1], self.grid[8][2] ],
                        [ self.grid[6][3], self.grid[6][4], self.grid[6][5], self.grid[7][3], self.grid[7][4], self.grid[7][5], self.grid[8][3], self.grid[8][4], self.grid[8][5] ],
                        [ self.grid[6][6], self.grid[6][7], self.grid[6][8], self.grid[7][6], self.grid[7][7], self.grid[7][8], self.grid[8][6], self.grid[8][7], self.grid[8][8] ]]

            
            column =[]
            for i in range(9):
                for j in range(9):
                    c = [self.grid[x][i] for x in range(9)]
                column.append(c)

            for i in high_freq_num_list:
                for box_num in range(1,10):
                    if i in self.Box[box_num - 1]:
                        continue
                    possibilities= []
                    for e in range(9):
                        if self.Box[box_num - 1][e] == 0:
                            possibilities.append(box_cord[box_num][e])


                    for e in possibilities:
                        r,c = e

                        if i in self.grid[r]:
                            possibilities = [e for e in possibilities if e[0] != r]

                        if i in column[c]:
                            possibilities = [e for e in possibilities if e[1] != c]

                        if len(possibilities) == 1:
                            self.grid[possibilities[0][0]][possibilities[0][1]] = i
                            #print(f'{i} has been forced in {(possibilities[0][0] +1 ,possibilities[0][1] +1)} in Box[{box_num}]')
                            break
                
            
            # finding the index to add grid elements to latex
        for row in range(9):
            for string in range(len(self.forced_latex)):
                if self.forced_latex[string] == '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n' and\
                   (self.forced_latex[string+2]== '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n' or\
                    self.forced_latex[string+2]== '\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n'):
                    
                    
                    if self.grid[row][0] != 0:
                        self.forced_latex[string] = self.forced_latex[string][:11] + str(self.grid[row][0]) + self.forced_latex[string][11:]
                    else:
                        self.forced_latex[string] = self.forced_latex[string][:11] + ' ' + self.forced_latex[string][11:]
                    if self.grid[row][3] != 0:
                        self.forced_latex[string+1] = self.forced_latex[string+1][:11] + str(self.grid[row][3]) + self.forced_latex[string+1][11:]
                    else:
                        self.forced_latex[string+1] = self.forced_latex[string+1][:11] + ' ' + self.forced_latex[string+1][11:]
                    if self.grid[row][6] != 0:
                        self.forced_latex[string+2] = self.forced_latex[string+2][:11] + str(self.grid[row][6]) + self.forced_latex[string+2][11:]
                    else:
                        self.forced_latex[string+2] = self.forced_latex[string+2][:11] + ' ' + self.forced_latex[string+2][11:]
                        
                    if self.grid[row][1] != 0:
                        self.forced_latex[string] = self.forced_latex[string][:27] + str(self.grid[row][1]) + self.forced_latex[string][27:]
                    else:
                        self.forced_latex[string] = self.forced_latex[string][:27] + ' ' + self.forced_latex[string][27:]
                        
                    if self.grid[row][4] != 0:
                        self.forced_latex[string+1] = self.forced_latex[string+1][:27] + str(self.grid[row][4]) + self.forced_latex[string+1][27:]
                    else:
                        self.forced_latex[string+1] = self.forced_latex[string+1][:27] + ' ' + self.forced_latex[string+1][27:]
                        
                    if self.grid[row][7] != 0:
                        self.forced_latex[string+2] = self.forced_latex[string+2][:27] + str(self.grid[row][7]) + self.forced_latex[string+2][27:]
                    else:
                        self.forced_latex[string+2] = self.forced_latex[string+2][:27] + ' ' + self.forced_latex[string+2][27:]

                    if self.grid[row][2] != 0:
                        self.forced_latex[string] = self.forced_latex[string][:43] + str(self.grid[row][2]) + self.forced_latex[string][43:]
                    else:
                        self.forced_latex[string] = self.forced_latex[string][:43] + ' ' + self.forced_latex[string][43:]
                        
                    if self.grid[row][5] != 0:
                        self.forced_latex[string+1] = self.forced_latex[string+1][:43] + str(self.grid[row][5]) + self.forced_latex[string+1][43:]
                    else:
                        self.forced_latex[string+1] = self.forced_latex[string+1][:43] + ' ' + self.forced_latex[string+1][43:]
                        
                    if self.grid[row][8] != 0:
                        self.forced_latex[string+2] = self.forced_latex[string+2][:43] + str(self.grid[row][8]) + self.forced_latex[string+2][43:]
                    else:
                        self.forced_latex[string+2] = self.forced_latex[string+2][:43] + ' ' + self.forced_latex[string+2][43:]

                    #print(row)
                    break

        for i in range(len(self.forced_latex)):
            for j in range(len(self.forced_latex[i])):
                try:
                    if self.forced_latex[i][j] == '{' and self.forced_latex[i][j+1] == ' ' and self.forced_latex[i][j+2] == '}':
                        self.forced_latex[i] = self.forced_latex[i][:j+1] + self.forced_latex[i][j+2:]
                except IndexError:
                    pass
                
    def forced_tex_output(self):
        with open(self.fname[:-4] + '_forced.tex','w+') as forced:
            for line in self.forced_latex:
                forced.write(line)
                #print(line)

    def run_marked(self):
        
        #Removing the elements existing in row
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = set([x for x in range(1,10) if x not in self.grid[i]])

        # Removing the elements exiting in column 
        column =[]
        for i in range(9):
            for j in range(9):
                c = [self.grid[x][i] for x in range(9)]
            column.append(c)

         
        for i in range(9):
            for j in range(9): 
                if type(column[i][j]) == set:
                    self.grid[j][i] = column[i][j] - set([x for x in column[i] if type(x) == int])
       
        # Removing the elements exiting in Box    
        Box =   [[ self.grid[0][0], self.grid[0][1], self.grid[0][2], self.grid[1][0], self.grid[1][1], self.grid[1][2], self.grid[2][0], self.grid[2][1], self.grid[2][2] ],
                [ self.grid[0][3], self.grid[0][4], self.grid[0][5], self.grid[1][3], self.grid[1][4], self.grid[1][5], self.grid[2][3], self.grid[2][4], self.grid[2][5] ],
                [ self.grid[0][6], self.grid[0][7], self.grid[0][8], self.grid[1][6], self.grid[1][7], self.grid[1][8], self.grid[2][6], self.grid[2][7], self.grid[2][8] ],
                [ self.grid[3][0], self.grid[3][1], self.grid[3][2], self.grid[4][0], self.grid[4][1], self.grid[4][2], self.grid[5][0], self.grid[5][1], self.grid[5][2] ],
                [ self.grid[3][3], self.grid[3][4], self.grid[3][5], self.grid[4][3], self.grid[4][4], self.grid[4][5], self.grid[5][3], self.grid[5][4], self.grid[5][5] ],
                [ self.grid[3][6], self.grid[3][7], self.grid[3][8], self.grid[4][6], self.grid[4][7], self.grid[4][8], self.grid[5][6], self.grid[5][7], self.grid[5][8] ],
                [ self.grid[6][0], self.grid[6][1], self.grid[6][2], self.grid[7][0], self.grid[7][1], self.grid[7][2], self.grid[8][0], self.grid[8][1], self.grid[8][2] ],
                [ self.grid[6][3], self.grid[6][4], self.grid[6][5], self.grid[7][3], self.grid[7][4], self.grid[7][5], self.grid[8][3], self.grid[8][4], self.grid[8][5] ],
                [ self.grid[6][6], self.grid[6][7], self.grid[6][8], self.grid[7][6], self.grid[7][7], self.grid[7][8], self.grid[8][6], self.grid[8][7], self.grid[8][8] ]]
       
        for i in range(9):
            for j in range(9): 
                if type(Box[i][j]) == set:
                    Box[i][j] = Box[i][j] - set([x for x in Box[i] if type(x) == int])
        
        
        self.grid =  [[ Box[0][0], Box[0][1], Box[0][2], Box[1][0], Box[1][1], Box[1][2], Box[2][0], Box[2][1], Box[2][2] ],
                [ Box[0][3], Box[0][4], Box[0][5], Box[1][3], Box[1][4], Box[1][5], Box[2][3], Box[2][4], Box[2][5] ],
                [ Box[0][6], Box[0][7], Box[0][8], Box[1][6], Box[1][7], Box[1][8], Box[2][6], Box[2][7], Box[2][8] ],
                [ Box[3][0], Box[3][1], Box[3][2], Box[4][0], Box[4][1], Box[4][2], Box[5][0], Box[5][1], Box[5][2] ],
                [ Box[3][3], Box[3][4], Box[3][5], Box[4][3], Box[4][4], Box[4][5], Box[5][3], Box[5][4], Box[5][5] ],
                [ Box[3][6], Box[3][7], Box[3][8], Box[4][6], Box[4][7], Box[4][8], Box[5][6], Box[5][7], Box[5][8] ],
                [ Box[6][0], Box[6][1], Box[6][2], Box[7][0], Box[7][1], Box[7][2], Box[8][0], Box[8][1], Box[8][2] ],
                [ Box[6][3], Box[6][4], Box[6][5], Box[7][3], Box[7][4], Box[7][5], Box[8][3], Box[8][4], Box[8][5] ],
                [ Box[6][6], Box[6][7], Box[6][8], Box[7][6], Box[7][7], Box[7][8], Box[8][6], Box[8][7], Box[8][8] ]]

        #for e in self.grid:
            #print(e)
    def get_marked_latex(self):
        R = [x for x in range(10)]
        G = [[None] * 9] * 9

        for a in range(9):
            for b in range(9):
                if isinstance(self.grid[a][b],set):
                    G[a][b] = list()
                    Q = list()
                    for N in R:
                    
                        if N in self.grid[a][b]:
                            Q.append(str(N))
                        else:
                            Q.append('')

                        if N == 2 or N == 4 or N == 6 or N == 9:
                            M = '{' + ' '.join(x for x in Q if x != '') + '}'
                            G[a][b].append(M)                  
                            Q = list()
                            
                    G[a][b].append('{}')
                    self.grid[a][b] = ''.join(x for x in G[a][b])
                elif isinstance(self.grid[a][b],int):
                    self.grid[a][b] = '{}{}{}{}{' + str(self.grid[a][b])+ '}'
        

        #print(self.grid[a][b])
        marked_latex = ['\\documentclass[10pt]{article}\n',
              '\\usepackage[left=0pt,right=0pt]{geometry}\n',
              '\\usepackage{tikz}\n', '\\usetikzlibrary{positioning}\n',
              '\\usepackage{cancel}\n', '\\pagestyle{empty}\n', '\n',
              '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n', '                               label=above right:{\\tiny #2},\n',
              '                               label=below left:{\\tiny #3},\n', '                               label=below right:{\\tiny #4}]{#5};}}\n',
              '\n', '\\begin{document}\n', '\n', '\\tikzset{every node/.style={minimum size=.5cm}}\n', '\n', '\\begin{center}\n',
              '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n',
              
              '% Line 1\n',
              '\\N' + self.grid[0][0] + ' & \\N' + self.grid[0][1] + ' & \\N' + self.grid[0][2] + ' &\n',
              '\\N' + self.grid[0][3] + ' & \\N' + self.grid[0][4] + ' & \\N' + self.grid[0][5] + ' &\n',
              '\\N' + self.grid[0][6] + ' & \\N' + self.grid[0][7] + ' & \\N' + self.grid[0][8] + ' \\\\ \\hline\n', '\n',

              '% Line 2\n',
              '\\N' + self.grid[1][0] + ' & \\N' + self.grid[1][1] + ' & \\N' + self.grid[1][2] + ' &\n',
              '\\N' + self.grid[1][3] + ' & \\N' + self.grid[1][4] + ' & \\N' + self.grid[1][5] + ' &\n',
              '\\N' + self.grid[1][6] + ' & \\N' + self.grid[1][7] + ' & \\N' + self.grid[1][8] + ' \\\\ \\hline\n', '\n',

              '% Line 3\n',
              '\\N' + self.grid[2][0] + ' & \\N' + self.grid[2][1] + ' & \\N' + self.grid[2][2] + ' &\n',
              '\\N' + self.grid[2][3] + ' & \\N' + self.grid[2][4] + ' & \\N' + self.grid[2][5] + ' &\n',
              '\\N' + self.grid[2][6] + ' & \\N' + self.grid[2][7] + ' & \\N' + self.grid[2][8] + ' \\\\ \\hline\\hline\n', '\n',

              '% Line 4\n',
              '\\N' + self.grid[3][0] + ' & \\N' + self.grid[3][1] + ' & \\N' + self.grid[3][2] + ' &\n',
              '\\N' + self.grid[3][3] + ' & \\N' + self.grid[3][4] + ' & \\N' + self.grid[3][5] + ' &\n',
              '\\N' + self.grid[3][6] + ' & \\N' + self.grid[3][7] + ' & \\N' + self.grid[3][8] + ' \\\\ \\hline\n', '\n',

              '% Line 5\n',
              '\\N' + self.grid[4][0] + ' & \\N' + self.grid[4][1] + ' & \\N' + self.grid[4][2] + ' &\n',
              '\\N' + self.grid[4][3] + ' & \\N' + self.grid[4][4] + ' & \\N' + self.grid[4][5] + ' &\n',
              '\\N' + self.grid[4][6] + ' & \\N' + self.grid[4][7] + ' & \\N' + self.grid[4][8] + ' \\\\ \\hline\n', '\n',

              '% Line 6\n',
              '\\N' + self.grid[5][0] + ' & \\N' + self.grid[5][1] + ' & \\N' + self.grid[5][2] + ' &\n',
              '\\N' + self.grid[5][3] + ' & \\N' + self.grid[5][4] + ' & \\N' + self.grid[5][5] + ' &\n',
              '\\N' + self.grid[5][6] + ' & \\N' + self.grid[5][7] + ' & \\N' + self.grid[5][8] + ' \\\\ \\hline\\hline\n', '\n',

              '% Line 7\n',
              '\\N' + self.grid[6][0] + ' & \\N' + self.grid[6][1] + ' & \\N' + self.grid[6][2] + ' &\n',
              '\\N' + self.grid[6][3] + ' & \\N' + self.grid[6][4] + ' & \\N' + self.grid[6][5] + ' &\n',
              '\\N' + self.grid[6][6] + ' & \\N' + self.grid[6][7] + ' & \\N' + self.grid[6][8] + ' \\\\ \\hline\n', '\n',

              '% Line 8\n',
              '\\N' + self.grid[7][0] + ' & \\N' + self.grid[7][1] + ' & \\N' + self.grid[7][2] + ' &\n',
              '\\N' + self.grid[7][3] + ' & \\N' + self.grid[7][4] + ' & \\N' + self.grid[7][5] + ' &\n',
              '\\N' + self.grid[7][6] + ' & \\N' + self.grid[7][7] + ' & \\N' + self.grid[7][8] + ' \\\\ \\hline\n', '\n',

              '% Line 9\n',
              '\\N' + self.grid[8][0] + ' & \\N' + self.grid[8][1] + ' & \\N' + self.grid[8][2] + ' &\n',
              '\\N' + self.grid[8][3] + ' & \\N' + self.grid[8][4] + ' & \\N' + self.grid[8][5] + ' &\n',
              '\\N' + self.grid[8][6] + ' & \\N' + self.grid[8][7] + ' & \\N' + self.grid[8][8] + ' \\\\ \\hline\\hline\n',

              '\\end{tabular}\n', '\\end{center}\n', '\n', '\\end{document}\n']

        #print(self.grid)
        
        return marked_latex

    def marked_tex_output(self):
        with open(self.fname[:-4] + '_marked.tex','w+') as marked:
            for line in self.marked_latex:
                marked.write(line)


    def run_worked(self):
        
        count1 = 0
        for _ in range(100):
            # Checking for pre-emptive sets in row
            for i in range(9):
                for j in range(9):
                    count1 += 1
                    if type(self.new_grid[i][j]) == set:
                        L = list(self.new_grid[i][j])
                        if len(L) < 1:
                            count1 = 0
                        subset = [x for x in self.new_grid[i] if type(x) == set and x.issubset(self.new_grid[i][j])]    
                        if len(L) == len(subset) and 2 <= len(L) and len(L) <= 9:
                            #print(f'({L}, {subset}, ROW {i+1}, {(i+1, j+1)}')        
                            for number in L:
                                for s in range(9):
                                    if type(self.new_grid[i][s]) == set and number in self.new_grid[i][s] and self.new_grid[i][s] not in subset and len(self.new_grid[i][s]) > 1:
                                        self.new_grid[i][s].remove(number)
                                        self.find_singleton()
            # print(count1)
            # Checking for pre-emptive sets in column
            count2 = 0
            for i in range(9):        
                for j in range(9):
                    count2 += 1
                    if type(self.new_column[i][j]) == set:                
                        L = list(self.new_column[i][j])
                        if len(L) < 1:
                            count2 = 0
                        subset = [x for x in self.new_column[i] if type(x) == set and x.issubset(self.new_column[i][j])]
                        if len(L) == len(subset) and 2 <= len(L) and len(L) <= 9:
                            #print(f'({L}, {subset}, COL {i+1}, {(i+1, j+1)}')
                            for number in L:
                                for s in range(9):
                                    if type(self.new_column[i][s]) == set and number in self.new_column[i][s] and self.new_column[i][s] not in subset and len(self.new_column[i][s]) > 1:
                                        self.new_column[i][s].remove(number)
                                        self.new_grid = self.col_to_grid()
                                        self.find_singleton()                         
            #print(count2)      
            # Checking for pre-emptive sets in the box
            count3 = 0
            for i in range(9):        
                for j in range(9):
                    count3 +=1
                    if type(self.new_Box[i][j]) == set:                
                        L = list(self.new_Box[i][j])
                        if len(L) < 1:
                            count3 = 0
                        subset = [x for x in self.new_Box[i] if type(x) == set and x.issubset(self.new_Box[i][j])]      
                        if len(L) == len(subset) and 2 <= len(L) and len(L) <= 9:
                            #print(f'({L}, {subset}, Box {i+1}, {(i+1, j+1)}')
                            for number in L:
                                for s in range(9):
                                    if type(self.new_Box[i][s]) == set and number in self.new_Box[i][s] and self.new_Box[i][s] not in subset and len(self.new_Box[i][s]) > 1:
                                        self.new_Box[i][s].remove(number)
                                        self.new_grid = self.box_to_grid()
                                        self.find_singleton()
            #print(count3)


    def get_worked_latex(self):

        R = [x for x in range(10)]
        G = [[None] * 9] * 9

        cancel_header = '\cancel{'
        cancel_footer = '}'

        for a in range(9):
            for b in range(9):
                if type(self.marked_grid[a][b]) == int and type(self.new_grid[a][b]) == int:
                    self.new_grid[a][b] = '{}{}{}{}{' + str(self.new_grid[a][b])+ '}'

                elif type(self.marked_grid[a][b]) == set and type(self.new_grid[a][b]) == int:
                    G[a][b] = list()
                    Q = list()
                    for N in R:
                        if N in self.marked_grid[a][b]:
                            Q.append(cancel_header + str(N) + cancel_footer)
                        else:
                            Q.append('')

                        if N == 2 or N == 4 or N == 6 or N == 9:
                            M = '{' + ' '.join(x for x in Q if x != '') + '}'
                            G[a][b].append(M)                  
                            Q = list()
                        
                    G[a][b].append('{' + str(self.new_grid[a][b]) + '}')
                    self.new_grid[a][b] = ''.join(x for x in G[a][b])
                    
                elif type(self.marked_grid[a][b]) == set and type(self.new_grid[a][b]) == set:
                    G[a][b] = list()
                    Q = list()
                    for N in R:
                        if N not in self.marked_grid[a][b]:
                            Q.append('')
                        elif N in self.marked_grid[a][b] and N in self.new_grid[a][b]:
                            Q.append(str(N))
                        elif N in self.marked_grid[a][b] and N not in self.new_grid[a][b]:
                            Q.append(cancel_header + str(N) + cancel_footer)

                        if N == 2 or N == 4 or N == 6 or N == 9:
                            M = '{' + ' '.join(x for x in Q if x != '') + '}'
                            G[a][b].append(M)                  
                            Q = list()


                    G[a][b].append('{}')
                    self.new_grid[a][b] = ''.join(x for x in G[a][b])
                                    
                #print(W_grid[a][b])

        worked_latex = ['\\documentclass[10pt]{article}\n',
              '\\usepackage[left=0pt,right=0pt]{geometry}\n',
              '\\usepackage{tikz}\n', '\\usetikzlibrary{positioning}\n',
              '\\usepackage{cancel}\n', '\\pagestyle{empty}\n', '\n',
              '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n', '                               label=above right:{\\tiny #2},\n',
              '                               label=below left:{\\tiny #3},\n', '                               label=below right:{\\tiny #4}]{#5};}}\n',
              '\n', '\\begin{document}\n', '\n', '\\tikzset{every node/.style={minimum size=.5cm}}\n', '\n', '\\begin{center}\n',
              '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n',
              
              '% Line 1\n',
              '\\N' + self.new_grid[0][0] + ' & \\N' + self.new_grid[0][1] + ' & \\N' + self.new_grid[0][2] + ' &\n',
              '\\N' + self.new_grid[0][3] + ' & \\N' + self.new_grid[0][4] + ' & \\N' + self.new_grid[0][5] + ' &\n',
              '\\N' + self.new_grid[0][6] + ' & \\N' + self.new_grid[0][7] + ' & \\N' + self.new_grid[0][8] + ' \\\\ \\hline\n', '\n',

              '% Line 2\n',
              '\\N' + self.new_grid[1][0] + ' & \\N' + self.new_grid[1][1] + ' & \\N' + self.new_grid[1][2] + ' &\n',
              '\\N' + self.new_grid[1][3] + ' & \\N' + self.new_grid[1][4] + ' & \\N' + self.new_grid[1][5] + ' &\n',
              '\\N' + self.new_grid[1][6] + ' & \\N' + self.new_grid[1][7] + ' & \\N' + self.new_grid[1][8] + ' \\\\ \\hline\n', '\n',

              '% Line 3\n',
              '\\N' + self.new_grid[2][0] + ' & \\N' + self.new_grid[2][1] + ' & \\N' + self.new_grid[2][2] + ' &\n',
              '\\N' + self.new_grid[2][3] + ' & \\N' + self.new_grid[2][4] + ' & \\N' + self.new_grid[2][5] + ' &\n',
              '\\N' + self.new_grid[2][6] + ' & \\N' + self.new_grid[2][7] + ' & \\N' + self.new_grid[2][8] + ' \\\\ \\hline\\hline\n', '\n',

              '% Line 4\n',
              '\\N' + self.new_grid[3][0] + ' & \\N' + self.new_grid[3][1] + ' & \\N' + self.new_grid[3][2] + ' &\n',
              '\\N' + self.new_grid[3][3] + ' & \\N' + self.new_grid[3][4] + ' & \\N' + self.new_grid[3][5] + ' &\n',
              '\\N' + self.new_grid[3][6] + ' & \\N' + self.new_grid[3][7] + ' & \\N' + self.new_grid[3][8] + ' \\\\ \\hline\n', '\n',

              '% Line 5\n',
              '\\N' + self.new_grid[4][0] + ' & \\N' + self.new_grid[4][1] + ' & \\N' + self.new_grid[4][2] + ' &\n',
              '\\N' + self.new_grid[4][3] + ' & \\N' + self.new_grid[4][4] + ' & \\N' + self.new_grid[4][5] + ' &\n',
              '\\N' + self.new_grid[4][6] + ' & \\N' + self.new_grid[4][7] + ' & \\N' + self.new_grid[4][8] + ' \\\\ \\hline\n', '\n',

              '% Line 6\n',
              '\\N' + self.new_grid[5][0] + ' & \\N' + self.new_grid[5][1] + ' & \\N' + self.new_grid[5][2] + ' &\n',
              '\\N' + self.new_grid[5][3] + ' & \\N' + self.new_grid[5][4] + ' & \\N' + self.new_grid[5][5] + ' &\n',
              '\\N' + self.new_grid[5][6] + ' & \\N' + self.new_grid[5][7] + ' & \\N' + self.new_grid[5][8] + ' \\\\ \\hline\\hline\n', '\n',

              '% Line 7\n',
              '\\N' + self.new_grid[6][0] + ' & \\N' + self.new_grid[6][1] + ' & \\N' + self.new_grid[6][2] + ' &\n',
              '\\N' + self.new_grid[6][3] + ' & \\N' + self.new_grid[6][4] + ' & \\N' + self.new_grid[6][5] + ' &\n',
              '\\N' + self.new_grid[6][6] + ' & \\N' + self.new_grid[6][7] + ' & \\N' + self.new_grid[6][8] + ' \\\\ \\hline\n', '\n',

              '% Line 8\n',
              '\\N' + self.new_grid[7][0] + ' & \\N' + self.new_grid[7][1] + ' & \\N' + self.new_grid[7][2] + ' &\n',
              '\\N' + self.new_grid[7][3] + ' & \\N' + self.new_grid[7][4] + ' & \\N' + self.new_grid[7][5] + ' &\n',
              '\\N' + self.new_grid[7][6] + ' & \\N' + self.new_grid[7][7] + ' & \\N' + self.new_grid[7][8] + ' \\\\ \\hline\n', '\n',

              '% Line 9\n',
              '\\N' + self.new_grid[8][0] + ' & \\N' + self.new_grid[8][1] + ' & \\N' + self.new_grid[8][2] + ' &\n',
              '\\N' + self.new_grid[8][3] + ' & \\N' + self.new_grid[8][4] + ' & \\N' + self.new_grid[8][5] + ' &\n',
              '\\N' + self.new_grid[8][6] + ' & \\N' + self.new_grid[8][7] + ' & \\N' + self.new_grid[8][8] + ' \\\\ \\hline\\hline\n',

              '\\end{tabular}\n', '\\end{center}\n', '\n', '\\end{document}\n']        
        
        
        return worked_latex
        
        
    def worked_tex_output(self):
        with open(self.fname[:-4] + '_worked.tex','w+') as worked:
            for line in self.worked_latex:
                worked.write(line)

