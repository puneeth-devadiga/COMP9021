grid =     [[2, 9, 5, 7, {3, 4}, {1, 3, 4}, 8, 6, {1, 3, 4}], [{4, 7}, 3, 1, 8, 6, 5, {9, 4}, 2, {4, 7}], [8, {4, 7}, 6, {1, 2, 4, 9}, {9, 2, 3, 4}, {1, 2, 3, 4, 9}, {9, 4, 5}, {1, 3, 4, 9}, {1, 3, 4, 5, 7}], [{1, 3, 4, 9}, {8, 1, 4}, 7, {9, 2, 4}, 5, {9, 2, 4}, {9, 2, 4}, {1, 3, 4, 8, 9}, 6], [{1, 4, 6, 9}, {1, 4, 6}, {9, 2}, 3, 8, 7, {9, 2, 4, 5}, {1, 4, 9}, {1, 4, 5}], [5, {8, 4}, {8, 9, 2, 3}, {9, 2, 4}, 1, 6, 7, {8, 9, 3, 4}, {8, 3, 4}], [{3, 6, 7}, {8, 6, 7}, {8, 3}, 5, {2, 3, 4, 7}, {2, 3, 4}, 1, {8, 4}, 9], [{1, 9, 7}, 2, {8, 9}, 6, {9, 4, 7}, {1, 4, 9}, 3, 5, {8, 4}], [{1, 3, 9}, 5, 4, {1, 9}, {9, 3}, 8, 6, 7, 2]]
      

W_grid =   [[2, 9, 5, 7, {3, 4}, {1, 3, 4}, 8, 6, {1, 3, 4}], [{4, 7}, 3, 1, 8, 6, 5, 9, 2, {4, 7}], [8, {4, 7}, 6, {1, 2, 4, 9}, {9, 2, 3, 4}, {1, 2, 3, 4, 9}, {4, 5}, {1, 3, 4}, {1, 3, 4, 5, 7}], [{1, 3}, {8, 1}, 7, {9, 2, 4}, 5, {9, 2, 4}, {2, 4}, {1, 3, 8}, 6], [{1, 4, 6, 9}, {1, 4, 6}, {9, 2}, 3, 8, 7, {2, 4, 5}, {1, 4, 9}, {1, 4, 5}], [5, {8, 4}, {8, 9, 2, 3}, {9, 2, 4}, 1, 6, 7, {8, 9, 3, 4}, {8, 3, 4}], [{3, 6, 7}, {8, 6, 7}, {8, 3}, 5, {2, 3, 4, 7}, {2, 3, 4}, 1, {8, 4}, 9], [{1, 9, 7}, 2, {8, 9}, 6, {9, 4, 7}, {1, 4, 9}, 3, 5, {8, 4}], [{1, 3, 9}, 5, 4, {1, 9}, {9, 3}, 8, 6, 7, 2]]

R = [x for x in range(10)]
G = [[None] * 9] * 9

cancel_header = '\cancel{'
cancel_footer = '}'

for a in range(9):
    for b in range(9):
        if type(grid[a][b]) == int and type(W_grid[a][b]) == int:
            W_grid[a][b] = '{}{}{}{}{' + str(W_grid[a][b])+ '}'

        elif type(grid[a][b]) == set and type(W_grid[a][b]) == int:
            G[a][b] = list()
            Q = list()
            for N in R:
                if N in grid[a][b]:
                    Q.append(cancel_header + str(N) + cancel_footer)
                else:
                    Q.append('')

                if N == 2 or N == 4 or N == 6 or N == 9:
                    M = '{' + ' '.join(x for x in Q if x != '') + '}'
                    G[a][b].append(M)                  
                    Q = list()
                
            G[a][b].append('{' + str(W_grid[a][b]) + '}')
            W_grid[a][b] = ''.join(x for x in G[a][b])
            
        elif type(grid[a][b]) == set and type(W_grid[a][b]) == set:
            G[a][b] = list()
            Q = list()
            for N in R:
                if N not in grid[a][b]:
                    Q.append('')
                elif N in grid[a][b] and N in W_grid[a][b]:
                    Q.append(str(N))
                elif N in grid[a][b] and N not in W_grid[a][b]:
                    Q.append(cancel_header + str(N) + cancel_footer)

                if N == 2 or N == 4 or N == 6 or N == 9:
                    M = '{' + ' '.join(x for x in Q if x != '') + '}'
                    G[a][b].append(M)                  
                    Q = list()


            G[a][b].append('{}')
            W_grid[a][b] = ''.join(x for x in G[a][b])
                            
        print(W_grid[a][b])
