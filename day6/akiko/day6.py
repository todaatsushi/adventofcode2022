data = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']

marker_list = ''
for i in data:
    # i = 'm'
    if len(marker_list) == 4:
        print(marker_list)
    
    else:
            marker_list = marker_list + i
    # print(marker_list)break 