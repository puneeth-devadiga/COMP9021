header = ["\\documentclass[10pt]{article}\n"
        "\\usepackage[left=0pt,right=0pt]{geometry}\n"
        "\\usepackage{tikz}\n"
        "\\usetikzlibrary{positioning}\n"
        "\\usepackage{cancel}\n"
        "\\pagestyle{empty}\n\n"
        "\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n"
        "                               label=above right:{\\tiny #2},\n" 
        "                               label=below left:{\\tiny #3},\n"
        "                               label=below right:{\\tiny #4}]{#5};}}\n\n"
        "\\begin{document}\n\n"
        "\\tikzset{every node/.style={minimum size=.5cm}}\n\n"
        "\\begin{center}\n"
        "\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline"]

footer = ["\\end{tabular}\n"
        "\\end{center}\n\n"
        "\\end{document}"]


 # Print the grid as a LaTeX table
 # view = 0 - bare, 1 - marked, 2 - worked
 
create_latex(view):
    for i in range(9):
        print("\n%% Line %d\n", i + 1)
        for j in range(9):
            print("\\N")
    
            if(view):
                print("{");
                domain = grid[i][j][1];
                crossed = grid[i][j][2];
                for k in range(9):
                    if (domain & 1):
                        printf(i)
                    if (crossed & 1):
                        print("\\cancel{i} ");
    
                    domain >>= 1;
                    crossed >>= 1;
    
                    if(i % 2 == 0 && i != 8)
                        printf("}{");
                printf("}")
            else
                printf("{}{}{}{}");
            #Print actual value if one exists
            if (grid[i][j][0] > 0):
                print("f{grid[r][c][0]}")
            else
                print("{}");
            #Ending(s)
            if((j + 1) % 9 != 0)
                print(" & ");
            else
                print(" \\\\ \\hline");
            #Double line
            if((j + 1) % 9 == 0 && (i + 1) % 3 == 0)
                print("\\hline");
          
            if((j + 1) % 3 == 0)
                print("\n");
        
    

