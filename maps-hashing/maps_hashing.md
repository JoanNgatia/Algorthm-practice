## Maps
- Similar to Python dictionaries.
- Data can be looked up according to a key, similar to a cartographic map legend
- Are set based data structures.
- Keys have to be unique(only exist once in a map).

### Use cases
- Dictionaries

## Hashing
- It is the process of generating a unique value from a text or a list of numbers using a hash function.
- Hash functions allow for linear time search, constant lookups **O(1)**.
- They transform values into easier storable values. They do this by converting input values into other compressed numerical values.

### How it works
1. Element is converted into an integer using a hash function.

  This integer now acts as an index to store original element
2. The element is stored in a hash table where it can be retrieved using a hashed key.

- Hash algorithms work by using a load factor to generate the hashed values.
- load factor = Number of entries / number of buckets
- the closer the load factor is to 1 the more the need to rehash the values in the bucket.
e.g for a hash function that divides a group of values by 100 and uses the remainder a key. the values are 100 numbers all of which are multiples of 5.
The load factor in this case is 1 since
```number of entries = 100 and number of buckets = 100```
To speed up the function, we can use a bucket size that's not divisible by 5 e.g 107. in this case, the load factor will be ```(100 / 107)```

A **hash table** is a data structure that maps keys to values.
It uses a hash function to calculate the index for the data key and the key is stored in the index.

**Collisions** occur when a function maps two distinct inputs to the same output.
To resolve this, linear probing can be employed. This involves looking into the hash table and trying to find another open slot to hold the item causing the collision.

## Use cases
- Encrypt digital signatures
- index data in hash tables
- detect duplicates in files
- Generating codes for scratch cards, eg. airtime, gift cards

### Hash Maps
e.g python dictionaries
- key, values pairs. Hash functions applied on the keys

## Known Hash algorithms

- SHA 1 (e.g SHA 128) - Produce a 20 byte hash value
- MD5 - generate a 16 bit, 32 digit hexadecimal hashed value
- SHA 2 (e.g SHA 256) - Produce a 32 byte hash value
Both of the above have been used to hash out passwords for storage in databases.
