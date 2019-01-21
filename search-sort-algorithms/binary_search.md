## Binary Search

#### How it works
1. Find the midpoint in the data colllection
2. Compare our search value with the midpoint value.
3. If search_val = midpoint value:
    we've found it :-)
4. if search_value < midpoint value:
    find the midpoint in the left hand side of the collection and repeat step 2
5. if search_value > midpoint value:
    find the midpoint in the right hand side of the collection and repeat step 2


Worst case: **O(log(n))**

``` python
def binary_search(alist, item):
        if len(alist) == 0:
            return False
        else:
            midpoint = len(alist) // 2
            if alist[midpoint] == item:
                return True
            else:
                if item < alist[midpoint]:
                    return binary_search(alist[:midpoint], item)
                else:
                    return binary_search(alist[midpoint + 1:], item)
```

## Recursion
- Functions that call themselves
Characteristics:
- Has to call itself at some point.
- Has a base case covered.
- Has to alter the input parameter at some point

e.g to achieve the Fibonnacci sequence:
``` python
def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)

```
this generates the value in the sequence at the `position` stated.

to achieve the factorial of a number:
``` python
def get_factorial(number):
  if number == 1:
    return 1
  else:
    return number * get_factorial(number - 1)
```