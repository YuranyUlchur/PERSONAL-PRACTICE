#!/usr/bin/python3
"""
this function organizes the numbers from largest to smallest
"""


def majo_to_minor():
    my_list = [1000, 2, 20, 10, 100, 40]

    for x in range(0, len(my_list)- 1):

        if my_list[x] > my_list[x + 1]:
            aux = my_list[x]
            my_list[x] = my_list[x + 1]
            my_list[x + 1] = aux 

    return(aux)
print(majo_to_minor())
