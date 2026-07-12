# Interview Questions

*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Black and White Tree

**Topic:** `trees`, `dfs`, `graphs`

Given a tree with $N$ vertices labeled from $1$ to $N$, rooted at vertex $1$. The tree is an undirected graph with $N - 1$ edges. Each edge connects two vertices, $a_i$ and $b_i$. Each vertex $i$ is colored either white (represented by `'0'`) or black (represented by `'1'`).

The beauty of a vertex $i$ is the number of paths in its subtree that have end vertices of the opposite color.

Find the beauty of all $N$ vertices.

#### Note
- A subtree of a vertex $i$ is a connected sub-graph consisting of all the descendants of $i$ including $i$.
- A simple path has distinct start and end vertices of opposite colors.

#### Input Format
- The first line contains a single integer $N$ denoting the number of vertices in the tree.
- The second line contains the string `Color` of size $N$ consisting of characters `'0'` and `'1'`.
- The next $N - 1$ lines describe the elements of `Edges`. Each line contains two integers $a_i$ and $b_i$ denoting an undirected edge between the vertices numbered $a_i$ and $b_i$.

#### Output Format
- Print $N$ space-separated integers denoting the beauty of the vertices from $1$ to $N$.

#### Constraints
- $1 \le N \le 10^5$
- $\text{Color}_i \in \{0, 1\} \ \forall i \in [1, N]$
- $1 \le a_i, b_i \le N \ \forall i \in [1, N-1]$

#### Sample Input
```
5
11110
3 1
4 3
5 3
2 4
```

#### Sample Output
```
4 0 3 0 0
```

#### Explanation
The given tree hierarchy rooted at 1 is:
```
    1 (Black)
    |
    3 (Black)
   / \
  4   5 (White)
  |
  2 (Black)
```
- For vertex 1: Subtree contains all vertices $\{1, 2, 3, 4, 5\}$. The white node is 5, and black nodes are $\{1, 2, 3, 4\}$. The paths with opposite colored endpoints are: `(5-3-1)`, `(5-3-4-2)`, `(5-3-4)`, `(5-3)`. Beauty = 4.
- For vertex 3: Subtree contains $\{2, 3, 4, 5\}$. The white node is 5, and black nodes are $\{2, 3, 4\}$. The paths with opposite colored endpoints are: `(5-3-4-2)`, `(5-3-4)`, `(5-3)`. Beauty = 3.
- For other vertices, there are no opposite colored endpoints in their subtrees. Beauty = 0.

```python
import sys

def solve(N, Color, Edges):
    # Construct adjacency list
    adj = [[] for _ in range(N + 1)]
    for u, v in Edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # Perform iterative DFS to find post-order traversal and parent relationship
    # This avoids Python recursion depth limit issues.
    parent = [0] * (N + 1)
    order = []
    visited = [False] * (N + 1)
    visited[1] = True
    
    queue = [1]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                
    # Initialize DP counters
    white_cnt = [0] * (N + 1)
    black_cnt = [0] * (N + 1)
    beauty = [0] * (N + 1)
    
    # Process bottom-up (reverse BFS/DFS order)
    for u in reversed(order):
        w = 1 if Color[u - 1] == '0' else 0
        b = 1 if Color[u - 1] == '1' else 0
        white_cnt[u] += w
        black_cnt[u] += b
        beauty[u] = white_cnt[u] * black_cnt[u]
        
        p = parent[u]
        if p != 0:
            white_cnt[p] += white_cnt[u]
            black_cnt[p] += black_cnt[u]
            
    return beauty[1:]

# Main execution block
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if data:
        N = int(data[0])
        Color = data[1]
        Edges = []
        idx = 2
        for _ in range(N - 1):
            u = int(data[idx])
            v = int(data[idx+1])
            Edges.append([u, v])
            idx += 2
        res = solve(N, Color, Edges)
        print(*(res))
```

---

### Q2. Value of an Expression

**Topic:** `sliding-window`, `monotonic-queue`, `number-theory`

Given a sequence of $N$ integers $(a_1, a_2, \dots, a_n)$. You are asked to perform the following operation and return the obtained result.
- For a given integer $x$, calculate the value of expression:
  $$\min_{i=1}^{n - x + 1} (\text{fun}(a_i, a_{i+1}, \dots, a_{i+x-1}))$$

Here, $\text{fun}(a_i, a_{i+1}, \dots, a_{i+x-1})$ returns the value of the rightmost number in the window with the highest number of distinct prime factors.

In other words, if $m_i = \text{fun}(a_i, a_{i+1}, \dots, a_{i+x-1})$, then you are required to find the value of $\min(m_i)$ over all valid sliding windows of size $x$.

#### Input Format
- The first line contains two integers $x$ and $n$.
- The second line contains $n$ integers $(a_1, a_2, \dots, a_n)$.

#### Output Format
- Print an integer denoting the minimum value of the expression over all sliding windows.

#### Constraints
- $1 \le n \le 10^6$
- $1 \le x \le n$
- $0 \le a_i \le 10^6$

#### Sample Input
```
3 5
2 4 6 10 5
```

#### Sample Output
```
6
```

#### Explanation
- Prime factor counts for elements:
  - 2: $\{2\}$ (1 distinct prime factor)
  - 4: $\{2\}$ (1 distinct prime factor)
  - 6: $\{2, 3\}$ (2 distinct prime factors)
  - 10: $\{2, 5\}$ (2 distinct prime factors)
  - 5: $\{5\}$ (1 distinct prime factor)
- Windows of size 3:
  - Window 1: `[2, 4, 6]`. Prime factor counts are `[1, 1, 2]`. Max is 2 (at index 2, value 6). So $m_1 = 6$.
  - Window 2: `[4, 6, 10]`. Prime factor counts are `[1, 2, 2]`. Max is 2. The rightmost index with max counts is index 3 (value 10). So $m_2 = 10$.
  - Window 3: `[6, 10, 5]`. Prime factor counts are `[2, 2, 1]`. Max is 2. The rightmost index with max counts is index 3 (value 10). So $m_3 = 10$.
- The minimum value among $m_i$ is $\min(6, 10, 10) = 6$.

```python
import sys
from collections import deque

def solve(x, n, a):
    if not a or n == 0:
        return 0
        
    max_val = max(a)
    limit = max(2, max_val)
    
    # Precompute distinct prime factor counts using sieve
    num_factors = [0] * (limit + 1)
    for i in range(2, limit + 1):
        if num_factors[i] == 0:
            for j in range(i, limit + 1, i):
                num_factors[j] += 1
                
    # Monotonic queue to store indices.
    # Sorted by (num_factors[a[index]], index) in descending order.
    dq = deque()
    min_m = float('inf')
    
    for j in range(n):
        # Remove elements outside the current window
        if dq and dq[0] < j - x + 1:
            dq.popleft()
            
        # Maintain decreasing order:
        # Since new index j > dq[-1], if num_factors[a[j]] >= num_factors[a[dq[-1]]],
        # then j is strictly better because it either has more prime factors or
        # has the same count but is further to the right.
        while dq and num_factors[a[j]] >= num_factors[a[dq[-1]]]:
            dq.pop()
        dq.append(j)
        
        # When the window is fully formed
        if j >= x - 1:
            m_i = a[dq[0]]
            if m_i < min_m:
                min_m = m_i
                
    return min_m

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        x = int(input_data[0])
        n = int(input_data[1])
        a = [int(val) for val in input_data[2:]]
        print(solve(x, n, a))
```

---

### Q3. Minimum Required Value

**Topic:** `dynamic-programming`, `bit-manipulation`, `optimization`

You are given two arrays, $A$ and $B$, of size $N$ consisting of non-negative integers.

You have to select $K$ numbers from $B$ and take the bitwise OR of all the array elements in $A$ with the chosen $K$ numbers and add their sum. In other words, take each element from array $A$ and add its bitwise OR with each chosen element from array $B$ to the sum.
*(Note: You cannot choose two adjacent elements in $B$).*

Find the minimum value of $K$ such that the sum is greater than or equal to $M$. Print `-1` if it is impossible to reach $M$.

#### Input Format
- The first line contains a single integer $T$ which denotes the number of test cases.
- For each test case:
  - The first line contains $N$, denoting the size of the arrays.
  - The second line contains $M$, denoting the target sum.
  - The third line contains $N$ space-separated integers representing array $A$.
  - The fourth line contains $N$ space-separated integers representing array $B$.

#### Output Format
- Print an integer denoting the minimum value of $K$ for each test case, line-separated.

#### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^3$
- $0 \le A_i, B_i \le 10^9$
- $0 \le M \le 10^{18}$

#### Sample Input
```
2
5
40
1 2 3 4 5
2 2 2 2 2
5
0
1 2 3 4 5
2 2 2 2 2
```

#### Sample Output
```
2
0
```

#### Explanation
- **Case 1**:
  For any chosen element $y$ from $B$, its contribution to the sum is $V(y) = \sum_{i=1}^N (A[i] \text{ OR } y)$.
  Since $B = [2, 2, 2, 2, 2]$ and $A = [1, 2, 3, 4, 5]$:
  $V(2) = (1|2) + (2|2) + (3|2) + (4|2) + (5|2) = 3 + 2 + 3 + 6 + 7 = 21$.
  - If we choose $K = 1$, the max sum is $21 < 40$.
  - If we choose $K = 2$ non-adjacent elements (e.g., $B[0]$ and $B[2]$), the total sum is $21 + 21 = 42 \ge 40$.
  Hence, minimum $K = 2$.
- **Case 2**:
  Since $M = 0$, choosing $K = 0$ elements gives sum $0 \ge 0$. Hence, minimum $K = 0$.

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    T = int(input_data[ptr])
    ptr += 1
    
    out = []
    for _ in range(T):
        N = int(input_data[ptr])
        M = int(input_data[ptr+1])
        ptr += 2
        
        A = []
        for _ in range(N):
            A.append(int(input_data[ptr]))
            ptr += 1
            
        B = []
        for _ in range(N):
            B.append(int(input_data[ptr]))
            ptr += 1
            
        # Calculate contribution V[j] for each B[j]
        # V[j] = sum(A[i] | B[j] for all i)
        V = []
        for bj in B:
            s = 0
            for ai in A:
                s += (ai | bj)
            V.append(s)
            
        # DP to find the maximum sum of k non-adjacent elements
        K_max = (N + 1) // 2
        dp = [[-float('inf')] * 2 for _ in range(K_max + 1)]
        dp[0][0] = 0
        
        for x in V:
            new_dp = [[-float('inf')] * 2 for _ in range(K_max + 1)]
            new_dp[0][0] = 0
            for k in range(1, K_max + 1):
                # Don't choose x
                new_dp[k][0] = max(dp[k][0], dp[k][1])
                # Choose x
                new_dp[k][1] = dp[k-1][0] + x
            dp = new_dp
            
        ans = -1
        for k in range(K_max + 1):
            if max(dp[k][0], dp[k][1]) >= M:
                ans = k
                break
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
```

---
