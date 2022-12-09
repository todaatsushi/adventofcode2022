import os

def num_trees_taller_to_right(grid, row, col, starting_tree_height):
    row_length = len(grid[0])
    if row == row_length - 1:
        return 0
    right_tree_height = grid[col][row+1]
    if right_tree_height >= starting_tree_height:
        return 1
    return 1 + num_trees_taller_to_right(grid, row+1, col, starting_tree_height)

def num_trees_taller_down(grid, row, col, starting_tree_height):
    col_length = len(grid)
    if col == col_length - 1:
        return 0
    tree_height_below = grid[col+1][row]
    if tree_height_below >= starting_tree_height:
        return 1
    return 1 + num_trees_taller_down(grid, row, col+1, starting_tree_height)

def num_trees_taller_to_left(grid, row, col, starting_tree_height):
    row_length = len(grid[0])
    if row == 0:
        return 0
    left_tree_height = grid[col][row-1]
    if left_tree_height >= starting_tree_height:
        return 1
    return 1 + num_trees_taller_to_left(grid, row-1, col, starting_tree_height)

def num_trees_taller_up(grid, row, col, starting_tree_height):
    col_length = len(grid)
    if col == 0:
        return 0
    tree_height_above = grid[col-1][row]
    if tree_height_above >= starting_tree_height:
        return 1
    return 1 + num_trees_taller_up(grid, row, col-1, starting_tree_height)

def scenic_score(grid, row, col):
    right = num_trees_taller_to_right(grid, row, col, grid[col][row])
    left = num_trees_taller_to_left(grid, row, col, grid[col][row])
    down = num_trees_taller_down(grid, row, col, grid[col][row])
    up = num_trees_taller_up(grid, row, col, grid[col][row])
    return right * left * down * up

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
#     [3,0,3],
#     [2,5,5],
#     [6,5,3],
# ]
# row = 2
# col = 2




scenic_score_log = []
for row_index in range(0, len(grid)):
    for col_index in range(0, len(grid[row_index])):
        scenic_score_log.append(scenic_score(grid, row_index, col_index))
print(max(scenic_score_log))

# 252000