def extract_row(grid, location):
    return grid[location]

def extract_col(grid, location):
    max_len = len(grid)
    col_list = []
    for i in range(0, max_len):
        col_list.append(grid[i][location])
    return col_list

def max_in_range(list_of_values, starting_index, max_index):
    comparison_values = []
    for i in range(starting_index, max_index+1):
        comparison_values.append(list_of_values[i])
    return max(comparison_values)

def is_tree_visible_horizontally(grid, row_index, column_index):
    row = extract_row(grid, row_index)
    tree = row[column_index]
    max_row_index = len(row)-1
    # trees at edge are always visible
    if column_index == max_row_index or column_index == 0:
        return True
    # check to right of grid column location within my row
    max_tree_to_right = max_in_range(row,column_index+1, max_row_index)
    if tree > max_tree_to_right:
        return True
    # check to left of grid column location within my row
    max_tree_to_left = max_in_range(row, 0, column_index-1)
    if tree > max_tree_to_left:
        return True
    return False

def is_tree_visible_vertically(grid, row_index, column_index):
    column = extract_col(grid, column_index)
    tree = column[row_index]
    max_column_index = len(column)-1
    # trees at edge are always visible
    if row_index == max_column_index or row_index == 0:
        return True
    # check to right of grid row location within my column
    max_tree_to_right = max_in_range(column,row_index+1, max_column_index)
    if tree > max_tree_to_right:
        return True
    # check to left of grid row location within my column
    max_tree_to_left = max_in_range(column, 0, row_index-1)
    if tree > max_tree_to_left:
        return True
    return False

def is_tree_visible(grid, row_index, column_index):
    return is_tree_visible_horizontally(grid, row_index, column_index) or is_tree_visible_vertically(grid, row_index, column_index)


grid = [
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
]

counter = 0
for row_index in range(0, len(grid)): 
    for col_index in range(0, len(grid[row_index])):
        # print(row_index, col_index)
        if is_tree_visible(grid, row_index, col_index) == True:
            counter += 1
print(counter)