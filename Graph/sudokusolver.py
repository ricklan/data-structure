def solve_sudoku(array):
    '''
    This function uses backtracking to solve a sudoku puzzle.
    '''
    row = 0
    col = 0
    completed = True

    for i in range(9):
        for j in range(9):
            if array[i][j] == 0:
                completed = False
                row = i
                col = j
                break
        else:
            continue
        break
    
    if(completed):
        return array
    else:
        results = find_valid_inputs(array, row, col)
        for item in results:
            array[row][col] = item
            
            if (solve_sudoku(array) is not None): # Recursively calling solve_sudoku()
                return array
        
        # backtracking
        array[row][col] = 0
    
    return None

def find_valid_inputs(array, row, column):
    '''
    This function is used to find all the possible valid inputs.
    '''

    # This is used to store the possible values.
    possible_values = [1,2,3,4,5,6,7,8,9]

    # Removes all the numbers that are already in the given row.
    for number in array[row]:
        if number in possible_values:
            possible_values.remove(number)

    # Removes all the numbers that are already in the given column.
    for row_value in range(9):
        if array[row_value][column] in possible_values:
            possible_values.remove(array[row_value][column])

    # Removes all the numbers that are already in that block.
    # This finds the row section the element is in.
    if (row >= 0 and row <= 2):
        row_index = 0
    elif (row >= 3 and row <= 5):
        row_index = 3
    else:
        row_index = 6
        
    # This finds the columnumn section the element is in.
    if (column >= 0 and column <= 2):
        column_index = 0
    elif (column >= 3 and column <= 5):
        column_index = 3
    else:
        column_index = 6
    
    # This for loop goes through each 3 by 3 section to check if there's a
    # number there already.
    for i in range(row_index, row_index + 3):
        for j in range(column_index, column_index + 3):
            if array[i][j] in possible_values:
                possible_values.remove(array[i][j])    

    return possible_values

def print_array(array):
    '''
    This function prints the completed sudoku array, if possible.
    '''
    print("-"*25)
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            print(array[i][j], end=" ")
            if (j % 3 == 2):
                print("|", end=" ")
        print()
        if (i % 3 == 2):
            print("-"*25)

if (__name__ == "__main__"):
    # 0's represent an empty space.
    array = [
             [0, 0, 0, 0, 0, 0, 9, 4, 0],
             [6, 0, 0, 0, 0, 0, 2, 7, 0],
             [8, 2, 0, 0, 4, 9, 6, 0, 0],
             [0, 7, 4, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 7, 6, 0, 0, 0, 0],
             [0, 6, 2, 0, 0, 5, 0, 8, 0],
             [0, 0, 0, 0, 5, 7, 0, 2, 3],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [7, 5, 3, 2, 0, 4, 0, 0, 0]
            ]

    completed_array = solve_sudoku(array)
    print_array(completed_array)