"""pick one value in the array(a pivot), recursively.
move all values
around it accordingly."""

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
            elif val == array[0]:
                equal.append(val)
            else:
                bigger_than.append(val)
        final_list = bigger_than + equal + less_than
        return quicksort(final_list)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
