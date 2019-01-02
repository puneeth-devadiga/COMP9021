

        x = y = 0
        
            for box_keys in not_found_boxes:
            for tuples in box[box_keys]:
                for i in range(9):
                    a, b = box[box_keys][i][0], box[box_keys][i][1]
                    
                    for row_key in row:
                        if row_key == 'row' + str(a):
                            for tuples in row[row_key]:
                                for i in range(9):
                                   x, y == row[row_key][i][0], row[row_key][i][1]
                                   if grid[a][b] == grid[x][y]:
                                       break                                    
                                   else:
                                       for col_key in col:
                                           if col_key == 'col' + str(b):
                                               for tuples in col[col_key]:
                                                   for y in range(9):
                                                       p, q = col[col_key][y][0], col[col_key][y][1]
                                                       if grid[a][b] == grid[p][q]:
                                                           break
            grid[a][b] = high_freq_num

    
    
    for high_freq_num in (high_freq_dict):
        box_numbers(high_freq_num, box)
