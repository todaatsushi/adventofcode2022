import os

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
    max_index = len(row)-1
    # trees at edge are always visible
    if column_index == max_index or column_index == 0:
        return True
    # check to right of grid column location within my row
    max_tree_to_right = max_in_range(row,column_index+1, max_index)
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
    max_index = len(column)-1
    # trees at edge are always visible
    if row_index == max_index or row_index == 0:
        return True
    # check to right of grid row location within my column
    max_tree_to_right = max_in_range(column,row_index+1, max_index)
    if tree > max_tree_to_right:
        return True
    # check to left of grid row location within my column
    max_tree_to_left = max_in_range(column, 0, row_index-1)
    if tree > max_tree_to_left:
        return True
    return False

def is_tree_visible(grid, row_index, column_index):
    return is_tree_visible_horizontally(grid, row_index, column_index) or is_tree_visible_vertically(grid, row_index, column_index)

def number_of_trees_visible_to_right(grid, row_index, column_index):
    # row: check right
    row = extract_row(grid, row_index)
    current_tree = row[column_index]
    max_index = len(row)
    trees_visible_to_right = 0 
    index_of_tree_to_right = column_index + 1
    # If a tree is right on the edge, its viewing distances will be zero.
    if column_index == max_index:
        return trees_visible_to_right
    # check to right of grid column location within my row
    for i in range(index_of_tree_to_right, max_index):
        # print(i, trees_visible_to_right)
        trees_visible_to_right += 1
        if row[i] >= current_tree:
            break
    return trees_visible_to_right

def number_of_trees_visible_down(grid, row_index, column_index):
    # column: checking right
    column = extract_col(grid, column_index)
    current_tree = column[row_index]
    max_index = len(column)
    trees_visible_down = 0 
    index_of_tree_below = row_index + 1
    # If a tree is right on the edge, its viewing distances will be zero.
    if row_index == max_index:
        return trees_visible_down
    # check to right of grid column location within my row
    for i in range(index_of_tree_below, max_index):
        trees_visible_down += 1
        if column[i] >= current_tree:
            break
    return trees_visible_down

def number_of_trees_visible_to_left(grid, row_index, column_index):
    # row: check left
    row = extract_row(grid, row_index)
    current_tree = row[column_index]
    trees_visible_to_left = 0 
    index_of_tree_to_left = column_index - 1
    end_index = -1
    # If a tree is right on the edge, its viewing distances will be zero.
    if column_index == 0:
        return trees_visible_to_left
    for i in range(index_of_tree_to_left, end_index, -1):
        trees_visible_to_left += 1
        if row[i] >= current_tree:
            break
    return trees_visible_to_left

def number_of_trees_visible_up(grid, row_index, column_index):
    # column: checking left
    column = extract_col(grid, column_index)
    current_tree = column[row_index]
    trees_visible_up = 0 
    index_of_tree_up = row_index - 1
    end_index = -1
    # If a tree is right on the edge, its viewing distances will be zero.
    if row_index == 0:
        return trees_visible_up
    # check to right of grid column location within my row
    for i in range(index_of_tree_up, end_index, -1):
        trees_visible_up += 1
        if column[i] >= current_tree:
            break
    return trees_visible_up

def scenic_score(grid, row, column):
    up = number_of_trees_visible_up(grid, row, column)
    left = number_of_trees_visible_to_left(grid, row, column)
    right = number_of_trees_visible_to_right(grid, row, column)
    down = number_of_trees_visible_down(grid, row, column)
    return up * left * right * down

# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    input = f.read().splitlines()

grid = []
for row in input:
    # row = '30373'
    grid.append([])
    for tree in row:
        # tree = '3'
        grid[-1].append(int(tree))

# grid = [
#     [3,0,3,7,3],
#     [2,5,5,1,2],
#     [6,5,3,3,2],
#     [3,3,5,4,9],
#     [3,5,3,9,0]
# ]


# Part 1
# counter = 0
# for row_index in range(0, len(grid)): 
#     for col_index in range(0, len(grid[row_index])):
#         # print(row_index, col_index)
#         if is_tree_visible(grid, row_index, col_index) == True:
#             counter += 1
# print(counter)

# Part 2
scenic_score_log = []
for row_index in range(0, len(grid)):
    for col_index in range(0, len(grid[row_index])):
        scenic_score_log.append(scenic_score(grid, row_index, col_index))

print(max(scenic_score_log))
