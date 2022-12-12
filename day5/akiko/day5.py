import os

def move_top_crate_from_origin_stack_to_destination_stack(all_stacks, origin_stack_location, destination_stack_location):
    all_stacks[destination_stack_location].append(all_stacks[origin_stack_location].pop())

def split_on_whitespace(input):
    x = []
    for i in input:
        delimitted = i.split(' ')
        x.append(delimitted)
    return x

# Import the instructions file
path = os.path.join(os.path.dirname(__file__), './instructions.csv')
# path = os.path.join(os.path.dirname(__file__), './sample_instructions.csv')
with open(path,"r") as f:
    instructions_input = f.read().splitlines()
instructions_white_space_split = split_on_whitespace(instructions_input)
instructions =[]
for i in instructions_white_space_split:
    instructions.append([i[1], i[3], i[5]])

# Import the start state - not programming this, because screw that
# hardcoded inputs
stacks = {
    '1' : ['B', 'Z', 'T'],
    '2' : ['V', 'H', 'T', 'D', 'N'],
    '3' : ['B', 'F', 'M', 'D'],
    '4' : ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
    '5' : ['W', 'D', 'G', 'P', 'V', 'F', 'Q' ,'M'],
    '6' : ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
    '7' : ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
    '8' : ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
    '9' : ['M', 'Q', 'L', 'F', 'D', 'S'],
}

for every_step in instructions:
    loop_count = every_step[0]
    original_stack = every_step[1]
    destination_stack = every_step[2]
    for i in range(1, int(loop_count)+1):
        move_top_crate_from_origin_stack_to_destination_stack(stacks, original_stack, destination_stack)

# stack_height = []
# # for columns 1 - 9
# for i in range(1, 10):
#     str_i = str(i)
#     stack_height.append(len(stacks[str_i])-1)
# print(stack_height)
# # stack_height = [10, 4, 1, 1, 2, 17, 10, 0, 2]

# Part 1: Find the top crates
top_crates = ''
for every_column in stacks:
    max_index = len(stacks[every_column])-1
    top_crate = stacks[every_column][max_index]
    top_crates+=top_crate
print(top_crates)
