# Intro
- Data starts from a root with data added being branches.
- Are extensions of linkedlists in that every node has its data and points to the next data.(parent-child rltps between nodes)
- completely connected- some way to reach every node
- no cycles, nodes can't be encountered twice.
- nodes grouped by levels(parent-child)
- nodes with no children = leaves
- height of node = number of edges between it and furthest leaf on tree

## Tree Traversal
### Depth FIrst search - DFS
- explore children nodes first
- (pre-order-traversal) Start at root, pick one child, traverse down left most child of this checking them off.
- (post-order traversal) Check off node only if you;ve gone through all its' children


### Breadth first search - BFS
- view all nodes on current level first
- start at root, view all its children on same level from the left to right,next move to children of children

## Tree Types
1. Binary Search trees - every parent node has 2 or fewer children, levels have number of nodes increasing to the power of 2. the trees are sorted. Every value on the left side is smaller than the values on the right within a level.
2. Heaps - Elements arranged incr /decr order such that the root is the min / max element. Parents can have any number of children.
