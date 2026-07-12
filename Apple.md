# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Apple*
*Total questions: 5*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [Theoretical Questions](#theoretical-questions)
3. [MCQs](#mcqs)

---

## Coding Questions

### Q1. Perfect Pairs

**Topic:** `Arrays`, `Binary Search`, `Two Pointers`  

A pair of integers $(x, y)$ is perfect if both of the following conditions are met:
- $\min(|x - y|, |x + y|) \le \min(|x|, |y|)$
- $\max(|x - y|, |x + y|) \ge \max(|x|, |y|)$

Given an array `arr` of length `n`, find the number of perfect pairs `(arr[i], arr[j])` where $0 \le i < j < n$.

Here $\min(a, b)$ is the minimum of $a$ and $b$, $\max(a, b)$ is the maximum of $a$ and $b$, and $|x|$ is the absolute value of $x$.

#### Example
`arr = [2, 5, -3]`  
In this example, $n = 3$. The possible pairs are `(2, 5)`, `(2, -3)` and `(5, -3)`.

- `(2, 5)` is not perfect:
  - $\min(|2-5|, |2+5|) = 3$, $\min(|2|, |5|) = 2$.
  - It fails the first test: $3 > 2$.
- `(2, -3)` is perfect:
  - $\min(|2 - (-3)|, |2 + (-3)|) = \min(5, 1) = 1 \le \min(2, 3) = 2$.
  - $\max(|2 - (-3)|, |2 + (-3)|) = \max(5, 1) = 5 \ge \max(2, 3) = 3$.
- `(5, -3)` is perfect:
  - $\min(|5 - (-3)|, |5 + (-3)|) = \min(8, 2) = 2 \le \min(5, 3) = 3$.
  - $\max(|5 - (-3)|, |5 + (-3)|) = \max(8, 2) = 8 \ge \max(5, 3) = 5$.

Total perfect pairs: 2.

#### Solution Explanation
The conditions can be simplified mathematically. Let $|x| \le |y|$.
1. $\min(|x - y|, |x + y|) \le |x|$
2. $\max(|x - y|, |x + y|) \ge |y|$

Whether $x$ and $y$ have the same sign or opposite signs, the two values $\{|x-y|, |x+y|\}$ are always $\{|y| - |x|, |y| + |x|\}$.
- The minimum is always $|y| - |x|$.
- The maximum is always $|y| + |x|$.

Plugging these in:
- Condition 1: $|y| - |x| \le |x| \implies |y| \le 2|x|$.
- Condition 2: $|y| + |x| \ge |y| \implies |x| \ge 0$, which is always true.

Thus, a pair $(x, y)$ is perfect if and only if:
$$\max(|x|, |y|) \le 2 \times \min(|x|, |y|)$$

We can solve this efficiently by mapping all elements to their absolute values and sorting them. For each element $A[i]$, we binary search for the largest index $j$ such that $A[j] \le 2 \times A[i]$. All elements in the index range $[i + 1, j]$ form a perfect pair with $A[i]$.

```python
import bisect

def solve(arr):
    # Transform elements to absolute values and sort
    a = sorted([abs(x) for x in arr])
    n = len(a)
    ans = 0
    
    for i in range(n):
        limit = 2 * a[i]
        # Find index of first element > 2 * a[i]
        idx = bisect.bisect_right(a, limit)
        # All elements in range [i + 1, idx - 1] are valid
        ans += max(0, idx - 1 - i)
        
    return ans
```

- **Time Complexity:** $O(N \log N)$ due to sorting and binary search.
- **Space Complexity:** $O(N)$ to store the absolute values.

---

### Q2. Eraser Tool (Red Pixel Connected Components)

**Topic:** `Graphs`, `Depth First Search (DFS)`, `Breadth First Search (BFS)`  

Given an array of strings representing a pixel graph where `"R"` represents a Red pixel and `"E"` represents an Empty pixel. You are provided with an eraser tool, which can be used on any Red pixel in the graph. It will erase all Red pixels connected horizontally and vertically and convert them into Empty pixels.

Calculate how many times you need to use the eraser tool to erase all of the Red pixels in the graph. Input pixel graph only contains `"E"` and/or `"R"` pixels.

#### Example 1
**Input:** `graph = ["RREEE", "RREEE", "EEREE", "EEERR"]`  
**Output:** `3`

#### Example 2
**Input:** `graph = ["RRRRE", "RRERE", "RREEE", "EEEEE"]`  
**Output:** `1`

```python
def eraserTool(pixelGraph: list[str]) -> int:
    if not pixelGraph or not pixelGraph[0]:
        return 0
    
    rows = len(pixelGraph)
    cols = len(pixelGraph[0])
    # Convert strings to character arrays to allow modifications (or use a visited set)
    grid = [list(row) for row in pixelGraph]
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 'R':
            return
        # Erase the red pixel
        grid[r][c] = 'E'
        # Traverse all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'R':
                count += 1
                dfs(r, c)
                
    return count
```

- **Time Complexity:** $O(\text{rows} \times \text{cols})$ as each pixel is visited at most a constant number of times.
- **Space Complexity:** $O(\text{rows} \times \text{cols})$ for the grid representation and recursive call stack.

---

### Q3. Longest Profit

**Topic:** `Dynamic Programming`, `Binary Search`, `Longest Increasing Subsequence`  

You are given an array of integers, which represent the monthly net profits of a company. The company wants you to look for the longest sequence of chronologically ordered months that have increasing profit, and return the length. The sequence can include non-adjacent months.

Implement the method `longestProfit(data)` which takes as input an array of integers `data`, representing a given set of consecutive monthly profit values. 

#### Example
**Input:** `[-1, 9, 0, 8, -5, 6, -24]`  
**Output:** `3` (the sequence could be `[-1, 0, 6]` or `[-1, 0, 8]`).

```python
import bisect

def longestProfit(data: list[int]) -> int:
    if not data:
        return 0
    
    sub = []
    for x in data:
        idx = bisect.bisect_left(sub, x)
        if idx == len(sub):
            sub.append(x)
        else:
            sub[idx] = x
            
    return len(sub)
```

- **Time Complexity:** $O(N \log N)$ using binary search (`bisect_left`) to perform the tail-replacement.
- **Space Complexity:** $O(N)$ to store the active increasing subsequence.

---

## MCQs

### Q4. DBMS MCQ: Removing a Relation from SQL

Which command is used to remove a relation from an SQL?

**Options:**
- A) Drop table
- B) Remove
- C) Purge
- D) Delete

**Correct Answer:** **A) Drop table**

**Explanation:** In SQL, a relation refers to a table. The `DROP TABLE` command is used to delete the table definition as well as all its rows, indexes, triggers, constraints, and permission specifications. `DELETE` is used to remove rows from a table, not the table itself.

---

### Q5. DSA MCQ: Binary Tree Function Identification

For a given binary tree, what does the following function do?

```c
int fun(struct node *root) {
    if (root == NULL)
        return 0;
    if (root->left == NULL && root->right == NULL)
        return 0;
    return 1 + fun(root->left) + fun(root->right);
}
```

**Options:**
- A) Returns height where height is defined as the number of edges on the path from the root to the deepest node
- B) Counts leaf nodes
- C) Counts total number of nodes
- D) Counts internal nodes

**Correct Answer:** **D) Counts internal nodes**

**Explanation:** 
- If the tree is empty (`root == NULL`), the function returns `0`.
- If the node is a leaf node (`root->left == NULL && root->right == NULL`), the function returns `0`.
- Otherwise, the node is an internal node, so it returns `1` (for itself) plus the recursive counts of internal nodes in its left and right subtrees.
- Therefore, the function counts the total number of internal nodes in the binary tree.
