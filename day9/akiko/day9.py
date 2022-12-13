import os
# | | | |^
# | |H| |y
# | | | | x - >
# head = [x, y]
# x = head[0]
# y = head[1]

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


instruction = ['R', '4']
head = [0,0]
tail = [0,0]
loop_count = int(instruction[1])+1
for i in range(1, loop_count):
    if instruction[0] == 'R':
        move_head_one_right(head, tail)
    if instruction[0] == 'L':
        move_head_one_left(head, tail)
    if instruction[0] == 'U':
        move_head_one_up(head, tail)
    if instruction[0] == 'D':
        move_head_one_down(head, tail)

print(head, tail)