#!/usr/bin/python3
"""
in the range -10 to 0 will tell us the number squared in a dictionary
"""
def main():

    new_dict = {}
    for i in range(-10, 0):
        if i % 2 == 0:
            new_dict[i] = i **2
    print("without compressed dictionary {}".format(new_dict))

    """
    dictionary comprehension
    """

    dict1 = {'milk' : 0.75, 'meat' : 10.69, 'eggs' : 2.14, 'bread': 1.07}
    dict2 = {k : v*3 for (k, v) in dict1.items()}
    print("compressed dictionary {}".format(dict2))

if __name__ == '__main__':
    main()
