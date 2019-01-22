## Graphs
- Network
- Show relationship between objects.
- Nodes used to represent objects with edges showing the connections.
- Cycles are possible i.e can come back to one node after traversing all the other nodes.
- Edges can contain data e.g what the connection is , strength of connection between nodes.
- **directed graphs** - Edges have directions(relationship between two nodes applies one way).
- **undirected graphs** - have edges with no sense of direction/
- **disconnected graph** - vertex that cant be reached by other vertices, no edge/ connection between them.
- **connected graph** - no diconnected vertices(nodes) connectivity can be used to display strength of relationship.
- **Strongly connected graphs** - have edges coming to and from each node.

### Traversal and Search
- **Depth First search** - follow one path as far as it will go. Can store in a stacknodes as you traverse .
  Alternatively, pick an edge, mark node as seen until all nodes are explored.
- **Breadth First search** - look at all nodes adjacent to one, before moving to the next level.
  search every edge of one node before moving to the next. Store nodes in a queue as you traverse.