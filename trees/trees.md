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
1. Binary Search trees - every node has 2 children, levels have number of nodes increasing to the power of 2