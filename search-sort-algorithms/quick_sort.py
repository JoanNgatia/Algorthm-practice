"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    bigger_than = []
    less_than = []
    equal = []
    if len(array) > 1:
        for val in array:
            if val < array[0]:
                less_than.append(val)
            if val == array[0]:
                equal.append(val)
            if val > array[0]:
                bigger_than.append(val)
        return quicksort(less_than) + equal + quicksort(bigger_than)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
