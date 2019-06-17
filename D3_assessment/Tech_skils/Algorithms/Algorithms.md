# Search Algorithm

### Depth first search (DFS)
DFS is a searching technique for tree or graph data structures. It involes choosing an arbitrary node at the root, and explores as far as possible along each branch before backtracking. Backtracking here means that on a forward movement, when there is no more node to visit, the search goes back along the same path. DFS is also known as traversing.

DFS is usually implemented using a stack or an adjacency list/matrix.

### Breadth first seaarch
BFS is a searching technique for tree or graph data structures. It involes choosing an arbitrary node at the root, and explores all the neighbours at the present level, before moving to the next level. if it does not find possible along each branch before backtracking.

### A* search
A* is an algorithm used in pathfinding and graph traversal. It is an extension of Dijkstra algorithm with some characteristics of BFS.

Like Dijkstra, A* works by making a low-cost path tree from the start node to the target node. It makes this decision by the heuristic values. What makes A* different is that for each node, A* uses a function f(n) that gives an estimate of the total cost of a path using that node. We can say thus, A* is a heuristic function f(n).
 ```       
        f(n) = g(n) + h(n)
    
where:
    f(n) = Total estimate cost
    g(n) = cost so far to reach node n
    h(n) = heuristic value. The estimated cost to reach node n
```

A* makes better decision by choosing a lowest cost among neighboring nodes.

# Sorting Algorithm

### Quick sort
Quick sort is an algorithm from the Divide-and-conquer category. It operates by breaking down large problems into smaller, more easily solvable problems. In Quick sort, a large list is broken down into two smaller lists. One of which holds valus that are smaller than a specified value, called a pivot, and the other holds values that are larger than the pivot. The process of partitioning the list is recurssive on the sublists until a sorted sequence is achieved.

The pivot can be chosing by any means. First, last, median or randomly.

Time complexity: Best: O(nlog n), Worst:O(n**2), Average: O(nlog n)
Space complexity: Best: O(log n), Average: O(n)

[Quick sort implementation](quick_sort.py)


### Heap sort
Heap sort is a comparison-based sorting algorithm that uses an ordered binary heap (a tree which has the root node greater than or equal to children nodes in the tree, or lesser than or equal to all nodes in the tree) data structure. Like Merge sort, Heap sort has a time complexity of O(nlog n), and like Insertion sort, Heap sorts in-place, so no extra space is required.
To implement Heap sort, we first make sure the heap is sorted (call it heapify or max-heap). That is, parent node must be greater than children node. That means, the root node will be the highest value, Assuming we use max-heap. Then we interchange root node (max value) with the last node on the tree(or list) and run heapify(max-heap) on the new tree.

Time complexity: O(nlog n)
Space complexity: O(1)

[Heap sort implementation](heap_sort.py)

### Merge sort
Merge sort is an efficient sorting algorithm that uses Divide-and-conquer approach to order elements in a list. This algorithm operates by breaking down large problems into smaller, more easily solvable promblems. The idea of Merge sort is to divide the list in half, and over again until each piece is only one item long. Then those items are merged in sored order.

The implematation follows three basic step: divide, conquer, combine.

Time complexity: O(nlog n)
Space complexity: O(n)

[Merge sort implementation](merge_sort.py)

### Insertion sort
Insertion sort is a simple algorithm that builds a final sorted array one element at a time. It works the way we sort a pack of cards. We sort the first two cards and then place the third card in the appropriate position within the first two, and then the fourth is position within the first three and so on until the cards are sorted. 
During an iteration, an element of a list is inserted into the sorted portion of the list to its left, So basically, foreach iteration, we have an array of other elements yet to be soreted to the right.

Time complexity: O(n**2)
Space complexity: O(1)

[Insertion sort implementation](insertion_sort.py)

# Hashing Algorithm
A Hashing algorithm is a cryptographic hash function. It is a mathematical algorithm that maps data to a hash of fixed size. It is designed to be a one-way function, where the output cannot be easily reveresed to get the input.

Hashing can be used for:
- Cheksums. To determine the authenticity of a downloaded file.
- Message authentication codes
- Finger printing
- Detecting duplicates

### Qualities of a good hash funtion
- The hash function makes use of every data input
- The hash key is fully determined by the data input
- The hash function generates very different keys for similar data
- It should be simple to compute.
- There should be less collisions in the hash table

### Message Digest 5 (MD5)
An MD5 is created by taking a string of any length and encoding it into a string of 128 bit. Encoding the same string using MD5 will always return the same hash key. It was commonly used when storing password, credit card digits and other sensitive data. But not any longer. It has since been found that MD5 is vulnerable and can be cracked by PCs of this generation. Files with MD5 hash can now be tampered with and still produce thesame MD5 hash. It is no longer suitable for use,  except for non-cryptographic purposes. More sucure hash algorithms are SHA2 and SHA3.

### Collision
It is a situation in which a hash fucntion returns the same hash key for more than one record.

### linear probing
It is a simple method of resolving hash collisions. It involves placing the second record linearly down the hash table,  where ever a space is found.

