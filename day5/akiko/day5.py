import os
def split_on_whitespace(input):
    x = []
    for i in input:
        delimitted = i.split(' ')
        x.append(delimitted)
    return x

# Part 1
def move_top_crate_from_origin_stack_to_destination_stack(all_stacks, origin_stack_location, destination_stack_location):
    all_stacks[destination_stack_location].append(all_stacks[origin_stack_location].pop())

# Part 2
def cratemover9001(stacks, instruction):
    origin = instruction[1]
    destination = instruction[2]
    num_crates = int(instruction[0])

    slice_location = len(stacks[origin])-num_crates
    sliced_off_crates = stacks[origin][slice_location:]

    # set new crate states for origin column in stacks dictionary
    new_origin_crates = stacks[origin][:slice_location]
    stacks[origin] = new_origin_crates

    # set new crate states for destination column in stacks dictionary
    new_destination_crates = stacks[destination]+sliced_off_crates
    stacks[destination] = new_destination_crates

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

# Part 1: Find the top crates
for every_step in instructions:
    loop_count = every_step[0]
    original_stack = every_step[1]
    destination_stack = every_step[2]
    for i in range(1, int(loop_count)+1):
        move_top_crate_from_origin_stack_to_destination_stack(stacks, original_stack, destination_stack)

top_crates = ''
for every_column in stacks:
    max_index = len(stacks[every_column])-1
    top_crate = stacks[every_column][max_index]
    top_crates+=top_crate
print(top_crates)

# Part 2: CrateMover 9001
# Retain the order, can't use pop
for every_step in instructions:
    # every_step = ['1', '2', '1']
    cratemover9001(stacks, every_step)

print(stacks)

top_crates = ''
for every_column in stacks:
    max_index = len(stacks[every_column])-1
    top_crate = stacks[every_column][max_index]
    top_crates+=top_crate
print(top_crates)