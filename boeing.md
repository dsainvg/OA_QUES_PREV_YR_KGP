# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/boeing*
*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Number with Maximum Occurrence of Digit K

**Topic:** `Arrays`, `String Manipulation`, `Digit Counting`  

Implement the following function:
```python
def NumWithMaxK(k, arr):
    pass
```

The function accepts a digit `k` (where $0 \le k \le 9$) and a positive integer array `arr` of size `n`. Implement the function to find the number in `arr` that has the maximum occurrence of the digit `k`.

#### Note:
- Return `-1` if the array is null (or `None` in Python).
- Return `0` if no number with digit `k` is present in the array.
- Assumption: Only one number has the maximum occurrence of digit `k`.

#### Example 1
**Input:**  
- `k: 2`  
- `arr: [37, 823, 122, 2322, 6017]`  
**Output:** `2322`  
**Explanation:** 
- Occurrence of digit 2 in 37 = 0
- Occurrence of digit 2 in 823 = 1
- Occurrence of digit 2 in 122 = 2
- Occurrence of digit 2 in 2322 = 3
- Occurrence of digit 2 in 6017 = 0
- Maximum occurrence of digit 2 is in 2322.

#### Example 2
**Input:**  
- `k: 1`  
- `arr: [2153, 65, 1, 12, 11, 1111]`  
**Output:** `1111`  

```python
def NumWithMaxK(k: int, arr: list[int]) -> int:
    if arr is None:
        return -1
    
    max_count = 0
    best_num = 0
    k_str = str(k)
    
    for num in arr:
        count = str(num).count(k_str)
        if count > max_count:
            max_count = count
            best_num = num
            
    if max_count == 0:
        return 0
    return best_num
```

- **Time Complexity:** $O(N \times D)$ where $N$ is the number of elements in the array and $D$ is the maximum number of digits of an element.
- **Space Complexity:** $O(D)$ to perform string conversions.

---

### Q2. Distance of Closest Leaf from Given Node in Binary Tree

**Topic:** `Trees`, `Depth First Search (DFS)`, `Binary Trees`  

A binary tree is represented by the following structure:
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Implement the following function:
```python
def ClosestLeaf(tree, k):
    pass
```

The function accepts the root node of a binary tree `tree` and an integer `k` as its arguments. Find the distance of the closest leaf from the node with value `k` and return the same.

#### Note:
- Return `-1` if the input tree is empty.
- Return `0` if the node given is itself a leaf node.
- Assumption: Only one node is present in the tree with data `k`.

#### Example 1
**Input Tree:**
```
       7
      / \
     5   6
    / \
   2   3
  / \ / \
 9  11 8 14
/ \ /  /  /
101215 16 18
```
- `k: 5`  
**Output:** `2`  
**Explanation:** Leaf node `6` is at distance 2 from node `5` (by going up to 7 and then down to 6), while all other leaf nodes are at distance 3. Thus, the output is 2.

#### Example 2
**Input Tree:**
```
    2
   / \
  3   4
 / \ / \
7  9 5  8
```
- `k: 4`  
**Output:** `1`  

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ClosestLeaf(tree: TreeNode, k: int) -> int:
    if tree is None:
        return -1
        
    # Helper to find closest leaf down from a given node
    def find_closest_down(node):
        if node is None:
            return float('inf')
        if node.left is None and node.right is None:
            return 0
        return 1 + min(find_closest_down(node.left), find_closest_down(node.right))
        
    # Helper to find path to the target node 'k'
    # Returns a list of (node, distance_from_target)
    path = []
    def find_path(node):
        if node is None:
            return False
        if node.data == k:
            path.append((node, 0))
            return True
        if find_path(node.left) or find_path(node.right):
            # Target node is in one of the subtrees
            dist = path[-1][1] + 1
            path.append((node, dist))
            return True
        return False
        
    find_path(tree)
    if not path:
        return -1 # Node with value k not found
        
    min_dist = float('inf')
    for ancestor, dist in path:
        min_dist = min(min_dist, dist + find_closest_down(ancestor))
        
    return min_dist
```

- **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree. We traverse to find the path and compute subtree leaf distances.
- **Space Complexity:** $O(H)$ where $H$ is the height of the tree (recursion stack and path storage).
