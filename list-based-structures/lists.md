## Collections

This section covers list-based-collections.

These include:
- lists
- arrays
- Linked lists
- Stacks
- Queues

## Arrays

- Have a fixed number of items of the same type.
- Each element in the array has an index.
- Each element stores the value that it holds as well as what index it is.

### Operations on arrays
- Insertion occurs in linear time having the worst case of **O(n)**.
    This is because a copy of existing elements has to be made first and a blank space is left
    where the new element is inserted.

- Searching for an element if it's in  a particulat spot **O(1)**.
  This is because the data in the collection has an index attached to it.

- Finding length of the array is **O(1)** if  you use the python inbuilt `len()` function.
  This runs only once on the input.(in constant time)



## Linked Lists
- Sequence of links with each link having a connection to the next link.
- Each element has an idea of the next element.
- Each element stores the value it holds and a reference to the next item in the linked list.
  (e.g memory address of the next or null if it doesn't point to anything)
- No indices.
- Adding and removing elements is easier.
- Types of Linked Lists:
* singly linked lists = Data records Have references to the **next** item in the list
* doubly linked lists = Data records have references to the **next** and the **previous** items. in list.

### Operations
- Insertion takes constant time since we're just shifting pointers i.e
  it will take place in **O(n)** for worst case if inserting at the
  end of the list and, will take **O(1)** if insertion is to take place at the beginning of the list.


### Possible uses

#### Difference between arrays and linked lists
|Arrays | Linked Lists|
| -------- | ------------ |
| composed of fixed size data records stored in adjoining memory blocks | made of data records linked together by pointers |
| The size of each data record is known. | The records can be stored any where in memory and only need to "point" to the next record.|