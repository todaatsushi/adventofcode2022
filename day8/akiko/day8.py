def max_in_range(list_of_values, min_index, max_index):
    comparison_values = []
    for i in range(min_index, max_index):
        comparison_values.append(list_of_values[i])
    return max(comparison_values)

def extract_row(grid, location):
    return grid[location]

def extract_col(grid, location):
    max_len = len(grid)
    col_list = []
    for i in range(0, max_len):
        col_list.append(grid[i][location])
    return col_list

grid = [
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
]

row = 2
col = 3

print(extract_row(grid, row))
print(extract_col(grid, col))
# row = extract_row(grid, 1)
# print(max_in_range(row, 3, len(row)))

# col = extract_col(grid, 1)
# print(col)
# print(max_in_range(col, 3, len(col)))

# row = [3,5,3,9,0]
# print(horizontal_max(row, 0, 2))
# print(horizontal_max(row, 2, len(row)))

# len(grid) -> max_row

# extract row 

# extract column