#!/usr/bin/python3
"""
function that finds the second max in an array
"""
def find_second_max(my_list):
    max1 = max2 = float('-inf')
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max2

print(find_second_max([1000, 2, 20, 10, 100, 40]))
