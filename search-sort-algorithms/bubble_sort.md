### Bubble Sort
Items in a sequence are  gone over one by one comparing them with the immediate next item and sorting accordingly.

At the end of every sort sequence, the largest value is at the furthest point

since we need to make (n-1) comparisons for (n-1) iterations, results in an efficiency where the 
worst And average case is O(n^2) and the 
best case = O(n) which happens if the sequence is already sorted.

eg. to run [21, 4, 1, 3, 9, 20, 25, 6, 21, 14] over bubble sort
first iteration = [4, 1, 3, 9, 20, 21, 6, 21, 14, 25]
second iteration = [1,3,4,9, 20,6,21,14, 21, 25]
third iteration = [1,3, 4,9,6, 20,14, 21,21,25]
fourth iteration = [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
the sequence is sorted in the fourth iteration.