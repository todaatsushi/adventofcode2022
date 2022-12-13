import os
# | | | |^
# | |H| |y
# | | | | x - >
# head = [x, y]
# x = head[0]
# y = head[1]

def split_on_whitespace(input):
    x = []
    for i in input:
        delimitted = i.split(' ')
        x.append(delimitted)
    return x

# Import the instructions file
# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    input = f.read().splitlines()
instructions = split_on_whitespace(input)
# instructions = [['R', '4'], ['U', '4'], ['L', '3'], ['D', '1'], ['R', '4'], ['D', '1'], ['L', '5'], ['R', '2']]

def head_is_same_as_tail(head, tail):
    return head[0] == tail[0] and head[1] == tail[1]

def head_is_one_right_of_tail(head, tail):
    return head[0] == tail[0] + 1 and head[1] == tail[1]

def head_is_one_left_of_tail(head, tail):
    return head[0] == tail[0] - 1 and head[1] == tail[1]

def head_is_one_above_tail(head, tail):
    return head[0] == tail[0] and head[1] == tail[1] + 1

def head_is_one_below_tail(head, tail):
    return head[0] == tail[0] and head[1] == tail[1] - 1

def head_is_top_right_of_tail(head, tail):
    return head[0] == tail[0] + 1 and head[1] == tail[1] + 1

def head_is_bottom_right_of_tail(head, tail):
    return head[0] == tail[0] + 1 and head[1] == tail[1] - 1

def head_is_top_left_of_tail(head, tail):
    return head[0] == tail[0] - 1 and head[1] == tail[1] + 1

def head_is_bottom_left_of_tail(head, tail):
    return head[0] == tail[0] - 1 and head[1] == tail[1] - 1

# move right -> [x+1, y]
def move_head_one_right(head, tail):
    if head_is_one_right_of_tail(head, tail):
        tail[0] += 1
    if head_is_top_right_of_tail(head, tail):
        tail[0] += 1
        tail[1] += 1   
    if head_is_bottom_right_of_tail(head, tail):
        tail[0] += 1
        tail[1] -= 1
    head[0] += 1

def move_head_one_left(head, tail):
    if head_is_one_left_of_tail(head, tail):
        tail[0] -= 1
    if head_is_top_left_of_tail(head, tail):
        tail[0] -= 1
        tail[1] += 1   
    if head_is_bottom_left_of_tail(head, tail):
        tail[0] -= 1
        tail[1] -= 1
    head[0] -= 1

def move_head_one_up(head, tail):
    if head_is_one_above_tail(head, tail):
        tail[1] += 1
    if head_is_top_right_of_tail(head, tail):
        tail[0] += 1
        tail[1] += 1
    if head_is_top_left_of_tail(head, tail):
        tail[0] -= 1
        tail[1] += 1        
    head[1] += 1

def move_head_one_down(head, tail):
    if head_is_one_below_tail(head, tail):
        tail[1] -= 1
    if head_is_bottom_right_of_tail(head, tail):
        tail[0] += 1
        tail[1] -= 1
    if head_is_bottom_left_of_tail(head, tail):
        tail[0] -= 1
        tail[1] -= 1        
    head[1] -= 1

head = [0,0]
tail = [0,0]
tail_set = set()

for instruction in instructions:
    # instruction = ['R', '4']
    loop_count = int(instruction[1])+1
    for i in range(1, loop_count):
        if instruction[0] == 'R':
            move_head_one_right(head, tail)
            tail_set.add(str(tail))
        if instruction[0] == 'L':
            move_head_one_left(head, tail)
            tail_set.add(str(tail))
        if instruction[0] == 'U':
            move_head_one_up(head, tail)
            tail_set.add(str(tail))
        if instruction[0] == 'D':
            move_head_one_down(head, tail)
            tail_set.add(str(tail))

print(len(tail_set))