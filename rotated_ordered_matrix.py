#!/usr/bin/python3
"""
matriz ordenada rotada  and cuántas veces ha sido rotada
"""
arr = [4, 5, 6, 1, 2, 3]

def count_rotations(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        """
        Calculate the index of the element in the medium
        """
        mid = (left + right) // 2
        """
        If the element in the middle
        is smaller than the previous one,
        the rotation has been found.
        """
        if arr[mid] < arr[mid - 1]:
            return mid
        elif arr[mid] > arr[mid + 1]:
            return mid + 1
        elif arr[mid] > arr[left]:
            left = mid + 1
        else:
            right = mid - 1
rotations = count_rotations(arr)
print("La matriz ha sido rotada {} veces.".format(rotations))
