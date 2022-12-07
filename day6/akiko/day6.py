data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

marker_list = ''
for i in data:
    # i = 'm'
    print(i)
    if len(marker_list) == 4:
        marker_set = set(marker_list)
        if len(marker_set) == 4:
            print('hello')
            break
    
    else:
        marker_list = marker_list + i
    # print(marker_list)break 

print(marker_set)

# start with empty string
# append letters from input
# when length of string is 4, check to see that 