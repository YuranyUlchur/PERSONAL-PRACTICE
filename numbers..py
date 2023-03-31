#!/usr/bin/python3
"""
this function counts the number of repeating numbers in the list.
"""

def numbers():
    
    my_list = [2, 2, 2, 2, 1, 1, 4, 4, 12, 12, 12, 100, 100, 100, 100, 20, 20]
    new_list = []
    count = 0

    for x in range(0, len(my_list)- 1):
        count = 0

        if my_list[x] not in new_list:
            for i in range(len(my_list)):
                if my_list[x] == my_list[i]:
                    count += 1
                    new_list.append(my_list[x])

            print("este numero  {} se imprime {} veces\n".format(my_list[x], count), end="")
print(numbers())
