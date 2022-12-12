import os
import pprint as pp
def move_top_crate_from_origin_stack_to_destination_stack(all_stacks, origin_stack_location, destination_stack_location):
    all_stacks[destination_stack_location].append(all_stacks[origin_stack_location].pop())

def split_on_whitespace(input):
    x = []
    for i in input:
        delimitted = i.split(' ')
        x.append(delimitted)
    return x

# path = os.path.join(os.path.dirname(__file__), './data.csv')

# Import the instructions file
# path = os.path.join(os.path.dirname(__file__), './instructions.csv')
# path = os.path.join(os.path.dirname(__file__), './sample_instructions.csv')
# with open(path,"r") as f:
#     instructions_input = f.read().splitlines()
# instructions_white_space_split = split_on_whitespace(instructions_input)
# instructions =[]
# for i in instructions_white_space_split:
#     instructions.append([i[1], i[3], i[5]])


# Import the start state
# path = os.path.join(os.path.dirname(__file__), './start_crate_state.csv')
path = os.path.join(os.path.dirname(__file__), './sample_start_crate_state.csv')
with open(path,"r") as f:
    start_state_input = f.read()
start_state_white_space_split = split_on_whitespace(start_state_input)
pp.pprint(start_state_white_space_split)
# print(instructions_white_space_split)
[['', '', '', '', '[D]', '', '', '', ''],
 ['[N]', '[C]', '', '', '', ''],
 ['[Z]', '[M]', '[P]'],
 ['', '1', '', '', '2', '', '', '3', '']]

# hardcoded inputs
# stacks = {
#     '1' : ['Z', 'N'],
#     '2' : ['M', 'C', 'D'],
#     '3' : ['P']
# }
# instructions = [['1', '2', '1'], ['3', '1', '3'], ['2', '2', '1'], ['1', '1', '2']]


# for every_step in instructions:
#     print(every_step)
#     loop_count = every_step[0]
#     original_stack = every_step[1]
#     destination_stack = every_step[2]

#     for i in range(1, int(loop_count)+1):
#         move_top_crate_from_origin_stack_to_destination_stack(stacks, original_stack, destination_stack)
#     print(stacks)
# print('end state: ', stacks)