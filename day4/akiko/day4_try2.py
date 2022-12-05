import os

def split_on_comma(input):
    x = []
    for i in input:
        elf_pair_assigment = i.split(',')
        x.append(elf_pair_assigment)
    return x

def split_on_hyphen(input):
    x = []
    for i in input:
        elf_pair_assigment = i.split('-')
        y = []
        for foo in elf_pair_assigment:
            y.append(int(foo))
        x.append(y)
    return x

def contains(a, b):
    return b[0] >= a[0] and b[1] <= a[1]

def overlaps(a, b):
    return (a[1] >= b[0] and a[0] < b[1]) or (b[1] >= a[0] and b[0] < a[1])


# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    input = f.read().splitlines()

input_split_on_comma = split_on_comma(input)
print(input_split_on_comma)

data = []
for i in input_split_on_comma:
    input_split_on_hyphen = split_on_hyphen(i)
    data.append(input_split_on_hyphen)

# print(data)

# Part 1: fully contained
counter = 0
# for i in data:
#     a = i[0]
#     b = i[1]
#     if contains(a,b) or contains(b,a):
#         counter += 1
# print(counter)

# Part 2: overlap
for i in data:
    a = i[0]
    b = i[1]
    if overlaps(a,b) or overlaps(b,a):
        counter += 1
print(counter)

# a = [2,4]
# b = [6,8]
# print(overlaps(a,b))

# 1 2 3 4 5 6 7 8
# x 2 3 4 x x x x x 10 11 12
# x x x x x 6 7 8 x xx xx xx
#
# a[1] < b[0] or a[0] < b[1]
