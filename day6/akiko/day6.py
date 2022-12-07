import os
def check_for_four_distinct_letters(four_letters):
    marker_set = set(four_letters)
    return len(marker_set) == 4

def check_for_distinct_letters(four_letters, number):
    marker_set = set(four_letters)
    return len(marker_set) == number

def make_four_letter_string(input_string):
    four_letter_string = input_string[0:4]
    return four_letter_string

def remove_first_character_from_string(input_string):
    new_string = input_string[1:]
    return new_string

path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    data = f.read()

counter = 1
while counter in range(1,len(data)):
    if counter == 1:
        four_letter_string = make_four_letter_string(data)
    else:
        data = remove_first_character_from_string(data)
        four_letter_string = make_four_letter_string(data)

    answer = check_for_four_distinct_letters(four_letter_string)
    if answer == True:
        break
    counter += 1

# Part 1
marker_location = counter + 3

print(four_letter_string, marker_location)

