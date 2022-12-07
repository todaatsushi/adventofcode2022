import os
def check_for_distinct_letters(letters, number):
    marker_set = set(letters)
    return len(marker_set) == number

def make_string_length_specified(input_string, length):
    string_of_specified_length = input_string[0:length]
    return string_of_specified_length

def remove_first_character_from_string(input_string):
    new_string = input_string[1:]
    return new_string

path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    data = f.read()

# # Part 1
# counter = 1
# while counter in range(1,len(data)):
#     if counter == 1:
#         four_letter_string = make_string_length_specified(data, 4)
#     else:
#         data = remove_first_character_from_string(data)
#         four_letter_string = make_string_length_specified(data, 4)

#     answer = check_for_distinct_letters(four_letter_string, 4)
#     if answer == True:
#         break
#     counter += 1
# marker_location = counter + 3

# print(four_letter_string, marker_location)

# Part 2
# data = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
# print(len(make_string_length_specified(data,14)))
counter = 1
# print(len(data))
while counter in range(1,len(data)):
    if counter == 1:
        fourteen_letter_string = make_string_length_specified(data, 14)
    else:
        data = remove_first_character_from_string(data)
        fourteen_letter_string = make_string_length_specified(data, 14)

    answer = check_for_distinct_letters(fourteen_letter_string, 14)
    answer_set = set(fourteen_letter_string)
    poo = len(answer_set)
    print(fourteen_letter_string, answer_set, poo, counter)
    if poo == 14:
        print("JISOJDOSIJOSIJ")
        break
    counter += 1

marker_location = counter + 13

print(counter, marker_location)

# print(fourteen_letter_string, marker_location)