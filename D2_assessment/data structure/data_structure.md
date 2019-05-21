## Binary tree
A binary tree is a tree data structure in which every node has at most two children, each child node is labeled as beign either a left child or a right child. Nodes without children are called leaves, and with exception to the parent node, every node has a parent.

Binary tree are usually used in sorting and searching algorithms.
### Binary search tree
Binary search tree is an ordered binary tree where a left child precedes a right child in the order of children of a node.

### B-tree
B-tree is a self-balanced search tree with multiple keys in every node and more than two children for every node. A B-tree of order m is a tree which satisfies the following properties:
1. All the leaf nodes must be at same level
2. Every node has at most m children.
3. Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.
4. The root has at least two children if it is not a leaf node.
5. A non-leaf node with k children contains k − 1 keys.
6. When a key is to be inserted into a full node, the node is splitted into two nodes, and the key with the median value is inserted in the parent node. In case the parent node is the root, then a new root is created.

## Heap tree
A heap is a special case of balanced binary tree data structure where the root node key iscompared with itschildren and arranged accordinlgy. 

### Types of heap
Max-heap - Where the value of the root node is greater than or equal to either of its children
Min-heap - Where the valueof theroot node is less than or equal to either of its children

## Graph datastructure
We can represent a graph using an array of vertices and a two-dimentional array of edges.
Vertes- Each node of the graph is represented as a vertex
Edge -Edge represents the path between two veritces

#### Types of graph
Directed graph - Have a pair of ordered vertices
Un-directed graph - Have a pair of unordered vertices

#### Graph implementation
- Adjacency list - Represents the vertices and edges as a list
- Adjacency matrix - Reperesents the graph as a matrix
#### Basic primary operation of a graph:
- Add vertex
- Add edge
- Display vertex

#### Graph applications
Social networks -Facebook, Linkedin, Instagram...
City-Road network 
