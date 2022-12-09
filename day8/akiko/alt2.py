import os

def extract_row(grid, location):
    return grid[location]

def extract_col(grid, location):
    max_len = len(grid)
    col_list = []
    for i in range(0, max_len):
        col_list.append(grid[i][location])
    return col_list

def num_trees_taller_to_right(row, index, starting_tree_height):

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