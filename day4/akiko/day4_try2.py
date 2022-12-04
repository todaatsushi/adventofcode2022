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

print(data)

counter = 0
for i in data:
    a = i[0]
    b = i[1]
    if contains(a,b) or contains(b,a):
        counter += 1
print(counter)
