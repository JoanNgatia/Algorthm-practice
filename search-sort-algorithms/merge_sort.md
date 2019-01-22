### Merge Sort

Break down sequence in question and build it back again while sorting it.
e.g big array broken down into smaller blocks with one element each.
Referred to as `divide and conquer` method.

Efficiency = **O(nlog(n))** since log(n) iterations are done over n comparisons.

e.g to run [21, 4, 1, 3, 9, 20, 25] over merge sort
``` python
first breakdown - [21], [4,1], [3, 9] , [20, 25]
first iteration - [4, 21, 1], [3, 9, 20, 25]
second iteration - [1, 4, 21,] [3, 9, 20 , 25]
third iteration - [1, 3, 4, 9, 21, 20, 25]
```