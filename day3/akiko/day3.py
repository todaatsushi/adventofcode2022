# make sure data file is in same dir as this python file
import os

# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    raw_data = f.read().splitlines()

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
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

# raw_data = ['bjgGqQGbQnjGQgnQgbGgjJnDLHLdfPVtdDmLZdBFVVZttdTf']
# raw_data = ['jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'bjgGqQGbQnjGQgnQgbGgjJnDLHLdfPVtdDmLZdBFVVZttdTf']
# print(raw_data)
bag = []
for content in raw_data:
    if (len(content) % 2) == 0:
        split_location = int(len(content)/2)
        first_compartment = set(content[:split_location])
        second_compartment = set(content[split_location:])
        common_character = first_compartment.intersection(second_compartment)
        bag.append(''.join(common_character)) #return a string of the common character
    else:
        print('error')

print(bag)
priority_list = []
for i in bag:
    priority_list.append(priority[i])

print(sum(priority_list))
