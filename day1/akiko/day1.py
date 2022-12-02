# make sure data file is in same dir as this python file
import os

# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    raw_data = f.read().splitlines()

all_calories_per_elf = [[]]

for i in raw_data:
    if i == '':
        all_calories_per_elf.append([])
    else:
        all_calories_per_elf[-1].append(int(i))

total_calories_per_elf = []
for calories_one_elf in all_calories_per_elf:
    total_calories_per_elf.append(sum(calories_one_elf))

total_calories_per_elf.sort(reverse=True)

# Part 1: total calories carried by most calorific elf
most_calorific_elf = total_calories_per_elf[0]
print(most_calorific_elf)

# Part 2: top 3 calorific elves
top_three_calorie_elves = total_calories_per_elf[0:3]
print(sum(top_three_calorie_elves))
