## Quick Sort

### How it works
1. Pick a pivot in the data collection
2. Move the rest of the data in the collection in comparison with the pivot

  i.e Values < pivot are moved to LHS while values > pivot are moved to RHS
3. Continuously pick a pivot in the ordered sections until full collection is sorted.

Worst case **O(n^2)**- array can't be split in half.

All comparisons have to be done if the largest / smallest value at the end

Best case **O(nlogn)**- pivot can be moved to the middle

Array can be split in half.