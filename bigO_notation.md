## Intro
**O(n)** where n represents length of input to the function. An algebraic expr is added in the parentheses defining the functions applied to the input
- Used to define time / space efficiency.

e.g
for
``` python
def example1(manatees):
    for manatee in manatees:
        print manatee['name']
```
the time efficiency is `O(n)` since the code will only run through `n` elements.

for
```python
def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']
```
the time efficiency is `O(n + 1)` that results in `O(1)` since the print function only runs once. There is no iteration involved.


for
```python
def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

```
the time efficiency is `O(nm)` since the there is nested iteration. The code will run through `n` number of manatees , looking through `m` number of properties.

for
```python
def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee
```
the time efficiency is `O(n^2)`, since we're iterating over `n` number of manatees twice.


#### Worst case and approximation

Some no. of computations must be performed for each value in input.
Worst case defines where the max possible input can be applied on a function.
E.g while iterating through the alphabet.
```
worst case = iterating through all 26 letters
average case = Iteratign through 13 letter
best case = Finding that the first alphabet is what you need.
```