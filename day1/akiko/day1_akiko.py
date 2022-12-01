# work laptop path
# path = '/Users/akikotoda/Projects/adventofcode2022/day1/akiko_sample.csv'
path = '/Users/akikotoda/Projects/adventofcode2022/day1/data.csv'
raw_data = open(path, "r").read().splitlines()

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
