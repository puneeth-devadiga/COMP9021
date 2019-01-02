grid =     [[{2, 4, 6, 7, 8}, 3, 9, 5, {2, 4, 6, 7}, {2, 4, 6, 7}, {1, 6}, {8, 1, 2}, {1, 2, 6}],
             [{2, 4, 5, 6}, {2, 4, 5, 6}, 1, 8, {2, 3, 4, 6}, 9, {3, 5, 6}, 7, {2, 6}],
             [{2, 5, 6, 7, 8}, {2, 5, 6, 7, 8}, {8, 2, 5}, {2, 3, 6}, 1, {2, 3, 6, 7}, 9, {8, 2, 3, 5}, 4],
             [1, {2, 5, 6, 8, 9}, {8, 2, 5}, 4, {2, 5, 6, 7, 8}, {2, 5, 6, 7}, {5, 7}, {9, 2, 5}, 3],
             [{2, 3, 4, 5, 6, 8, 9}, {2, 4, 5, 6, 8, 9}, {2, 3, 4, 5, 8}, {1, 2, 3, 6, 9}, {2, 3, 5, 6, 7, 8}, {2, 3, 5, 6, 7}, {1, 4, 5, 7}, {1, 2, 4, 5, 9}, {1, 2, 9, 7}],
             [{2, 3, 4, 5, 9}, {9, 2, 4, 5}, 7, {1, 2, 3, 9}, {2, 3, 5}, {2, 3, 5}, 8, 6, {1, 2, 9}],
             [{9, 3, 4, 5}, {9, 4, 5}, 6, 7, {3, 4, 5}, 8, 2, {1, 3, 4, 9}, {1, 9}],
             [{2, 3, 4, 7, 8}, 1, {8, 2, 3, 4}, {2, 3, 6}, 9, {2, 3, 4, 6}, {3, 4, 6, 7}, {3, 4}, 5],
             [{2, 3, 4, 5, 7, 9}, {2, 4, 5, 7, 9}, {2, 3, 4, 5}, {2, 3, 6}, {2, 3, 4, 5, 6}, 1, {3, 4, 6, 7}, {9, 3, 4}, 8]]


R = [x for x in range(10)]
G = [[None] * 9] * 9

for a in range(9):
    for b in range(9):
        if isinstance(grid[a][b],set):
            G[a][b] = list()
            Q = list()
            for N in R:
                
                if N in grid[a][b]:
                    Q.append(str(N))
                else:
                    Q.append('')

                if N == 2 or N == 4 or N == 6 or N == 9:
                    M = '{' + ' '.join(x for x in Q if x != '') + '}'
                    G[a][b].append(M)                  
                    Q = list()
                    
            G[a][b].append('{}')
            grid[a][b] = ''.join(x for x in G[a][b])
        elif isinstance(grid[a][b],int):
            grid[a][b] = '{}{}{}{}{' + str(grid[a][b])+ '}'


        print(grid[a][b])
latex = ['\\documentclass[10pt]{article}\n',
      '\\usepackage[left=0pt,right=0pt]{geometry}\n',
      '\\usepackage{tikz}\n', '\\usetikzlibrary{positioning}\n',
      '\\usepackage{cancel}\n', '\\pagestyle{empty}\n', '\n',
      '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n', '                               label=above right:{\\tiny #2},\n',
      '                               label=below left:{\\tiny #3},\n', '                               label=below right:{\\tiny #4}]{#5};}}\n',
      '\n', '\\begin{document}\n', '\n', '\\tikzset{every node/.style={minimum size=.5cm}}\n', '\n', '\\begin{center}\n',
      '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n',
      
      '% Line 1\n',
      '\\N' + grid[0][0] + ' & \\N' + grid[0][1] + ' & \\N' + grid[0][2] + ' &\n',
      '\\N' + grid[0][3] + ' & \\N' + grid[0][4] + ' & \\N' + grid[0][5] + ' &\n',
      '\\N' + grid[0][6] + ' & \\N' + grid[0][7] + ' & \\N' + grid[0][8] + ' \\\\ \\hline\n', '\n',

      '% Line 2\n',
      '\\N' + grid[1][0] + ' & \\N' + grid[1][1] + ' & \\N' + grid[1][2] + ' &\n',
      '\\N' + grid[1][3] + ' & \\N' + grid[1][4] + ' & \\N' + grid[1][5] + ' &\n',
      '\\N' + grid[1][6] + ' & \\N' + grid[1][7] + ' & \\N' + grid[1][8] + ' \\\\ \\hline\n', '\n',

      '% Line 3\n',
      '\\N' + grid[2][0] + ' & \\N' + grid[2][1] + ' & \\N' + grid[2][2] + ' &\n',
      '\\N' + grid[2][3] + ' & \\N' + grid[2][4] + ' & \\N' + grid[2][5] + ' &\n',
      '\\N' + grid[2][6] + ' & \\N' + grid[2][7] + ' & \\N' + grid[2][8] + ' \\\\ \\hline\\hline\n', '\n',

      '% Line 4\n',
      '\\N' + grid[3][0] + ' & \\N' + grid[3][1] + ' & \\N' + grid[3][2] + ' &\n',
      '\\N' + grid[3][3] + ' & \\N' + grid[3][4] + ' & \\N' + grid[3][5] + ' &\n',
      '\\N' + grid[3][6] + ' & \\N' + grid[3][7] + ' & \\N' + grid[3][8] + ' \\\\ \\hline\n', '\n',

      '% Line 5\n',
      '\\N' + grid[4][0] + ' & \\N' + grid[4][1] + ' & \\N' + grid[4][2] + ' &\n',
      '\\N' + grid[4][3] + ' & \\N' + grid[4][4] + ' & \\N' + grid[4][5] + ' &\n',
      '\\N' + grid[4][6] + ' & \\N' + grid[4][7] + ' & \\N' + grid[4][8] + ' \\\\ \\hline\n', '\n',

      '% Line 6\n',
      '\\N' + grid[5][0] + ' & \\N' + grid[5][1] + ' & \\N' + grid[5][2] + ' &\n',
      '\\N' + grid[5][3] + ' & \\N' + grid[5][4] + ' & \\N' + grid[5][5] + ' &\n',
      '\\N' + grid[5][6] + ' & \\N' + grid[5][7] + ' & \\N' + grid[5][8] + ' \\\\ \\hline\\hline\n', '\n',

      '% Line 7\n',
      '\\N' + grid[6][0] + ' & \\N' + grid[6][1] + ' & \\N' + grid[6][2] + ' &\n',
      '\\N' + grid[6][3] + ' & \\N' + grid[6][4] + ' & \\N' + grid[6][5] + ' &\n',
      '\\N' + grid[6][6] + ' & \\N' + grid[6][7] + ' & \\N' + grid[6][8] + ' \\\\ \\hline\n', '\n',

      '% Line 8\n',
      '\\N' + grid[7][0] + ' & \\N' + grid[7][1] + ' & \\N' + grid[7][2] + ' &\n',
      '\\N' + grid[7][3] + ' & \\N' + grid[7][4] + ' & \\N' + grid[7][5] + ' &\n',
      '\\N' + grid[7][6] + ' & \\N' + grid[7][7] + ' & \\N' + grid[7][8] + ' \\\\ \\hline\n', '\n',

      '% Line 9\n',
      '\\N' + grid[8][0] + ' & \\N' + grid[8][1] + ' & \\N' + grid[8][2] + ' &\n',
      '\\N' + grid[8][3] + ' & \\N' + grid[8][4] + ' & \\N' + grid[8][5] + ' &\n',
      '\\N' + grid[8][6] + ' & \\N' + grid[8][7] + ' & \\N' + grid[8][8] + ' \\\\ \\hline\\hline\n',

      '\\end{tabular}\n', '\\end{center}\n', '\n', '\\end{document}\n'] 

with open('Kachra.tex','w+') as f:
    for line in latex:
        f.write(line)
