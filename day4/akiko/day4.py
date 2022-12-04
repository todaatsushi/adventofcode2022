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
        x.append(elf_pair_assigment)
    return x

path = os.path.join(os.path.dirname(__file__), './sample.csv')
# path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    input = f.read().splitlines()

input_split_on_comma = split_on_comma(input)

z = []
for i in input_split_on_comma:
    input_split_on_hyphen = split_on_hyphen(i)
    z.append(input_split_on_hyphen)

data = []
for elf_pair in z:
    bar=[]
    for elf in elf_pair:
        start = int(elf[0])
        end = int(elf[1])+1
        starter_string = ''
        for i in range(start, end):
            starter_string += str(i)
        bar.append(starter_string)
    data.append(bar)

data = [['234', '678'], ['23', '45'], ['567', '789'], ['2345678', '34567'], ['6', '456'], ['23456', '45678']]

overlapping_pairs_count = 0
for each_pair in data:
    first_elf = set(each_pair[0])
    second_elf = set(each_pair[1])
    overlap_first_and_second_elf = first_elf.intersection(second_elf)
    print(overlap_first_and_second_elf, len(overlap_first_and_second_elf))

    if len(overlap_first_and_second_elf) > 0: #eliminate no matches
        sorted_first_elf = list(first_elf).sort()
        sorted_second_elf = list(second_elf).sort()
        sorted_overlap = list(overlap_first_and_second_elf).sort()
        print(sorted_first_elf, sorted_second_elf, sorted_overlap)

        if sorted_overlap == sorted_first_elf:
            print('hello')
            if sorted_overlap == sorted_second_elf:
                print('hello world')
                overlapping_pairs_count += 1
                print(overlapping_pairs_count)
        # elif
        #     overlapping_pairs_count += 1

print(overlapping_pairs_count)
