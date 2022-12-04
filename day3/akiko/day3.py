# make sure data file is in same dir as this python file
import os

def priority_score(bag):
    priority = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,
        'j' : 10,
        'k' : 11,
        'l' : 12,
        'm' : 13,
        'n' : 14,
        'o' : 15,
        'p' : 16,
        'q' : 17,
        'r' : 18,
        's' : 19,
        't' : 20,
        'u' : 21,
        'v' : 22,
        'w' : 23,
        'x' : 24,
        'y' : 25,
        'z' : 26,
        'A' : 27,
        'B' : 28,
        'C' : 29,
        'D' : 30,
        'E' : 31,
        'F' : 32,
        'G' : 33,
        'H' : 34,
        'I' : 35,
        'J' : 36,
        'K' : 37,
        'L' : 38,
        'M' : 39,
        'N' : 40,
        'O' : 41,
        'P' : 42,
        'Q' : 43,
        'R' : 44,
        'S' : 45,
        'T' : 46,
        'U' : 47,
        'V' : 48,
        'W' : 49,
        'X' : 50,
        'Y' : 51,
        'Z' : 52
    }
    priority_list = []
    for i in bag:
        priority_list.append(priority[i])
    return sum(priority_list)

# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    data = f.read().splitlines()

# # Part 1: find the common character between the two halves of string
bag = []
for content in data:
    if (len(content) % 2) == 0:
        split_location = int(len(content)/2)
        first_compartment = set(content[:split_location])
        second_compartment = set(content[split_location:])
        common_character = first_compartment.intersection(second_compartment)
        bag.append(''.join(common_character)) #return a string of the common character
    else:
        print('error')

print(priority_score(bag))

# Part 2: find the common character between every three strings
input = [[]]
counter = 1
while counter < 6:
    for i in data:
        if counter % 3 == 0:
            input[-1].append(i)
            counter += 1
            # input.append([])
            if counter == len(data)+1:
                break
            else:
                input.append([])
        else:
            input[-1].append(i)
            counter += 1
            if counter == len(data)+1:
                break

part2_bag =[]
for elf_group in input:
    first_elf = set(elf_group[0])
    second_elf = set(elf_group[1])
    third_elf = set(elf_group[2])
    common_character_first_and_second_elf = first_elf.intersection(second_elf)
    common_character_all_elves = common_character_first_and_second_elf.intersection(third_elf)
    part2_bag.append(''.join(common_character_all_elves))

print(priority_score(part2_bag))
