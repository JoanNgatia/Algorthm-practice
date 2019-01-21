## Quick intro
- Hash functions allow for linear time search, constant lookups
- They transform values into easier storable values. They do this by converting input values into another compresed numerical values.
- Hash algorithms work by using a load factor to generate the hashed values.
- load factor = Number of entries / number of buckets
- the closer the load factor is to 1 the more the need to rehash the values in the bucket.
e.g for a hash function that divides a group of values by 100 and uses the remainder a key. the values are 100 numbers all of which are multiples of 5.
The load factor in this case is 1 since
```number of entries = 100 and number of buckets = 100```
To speed up the function, we can use a bucket size that's not divisible by 5 e.g 107. in this case, the load factor will be ```(100 / 107)```

## Use cases
- Encrypt digital signatures
- index data in hash tables
- detect duplicates in files

### Hash Maps
e.g python dictionaries
- key, values pairs. Hash functions applied on the keys

**Collisions** occur when a function maps two distinct inputs to the same output.
To resolve this, linear probing can be employed. This involves looking into the hash table and trying to find another open slot to hold the item causing the collision.

## Hash algorithms
- SHA 128 and SHA 256
- MD5