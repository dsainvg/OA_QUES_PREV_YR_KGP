# Interview Questions

*Total questions: 5*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Minimum Stress Path

`[Latest]`

**Topic:** `Graph`, `Dijkstra`, `Minimax Path`, `Bottleneck Path`

### Problem Description
You are given a weighted undirected graph with `graph_nodes` nodes and `m` edges. The stress level of a path between two nodes is defined as the weight of the heaviest edge in that path.

Given a source node `source` and a destination node `destination`, find the minimum possible stress level of a path. If no such path exists, return $-1$.

### Sample Case
Consider a graph where `source = 1` and `destination = 3`:
- Node $1$ is connected to $2$ (weight $100$) and $4$ (weight $10$).
- Node $2$ is connected to $3$ (weight $200$).
- Node $4$ is connected to $3$ (weight $20$).

There are two paths from node $1$ to node $3$:
1. $1 \to 2 \to 3$: The maximum edge weight is $200$.
2. $1 \to 4 \to 3$: The maximum edge weight is $20$.

The minimum possible stress level is $20$.

---

### Python Solution

```python
import heapq

def getMinimumStress(graph_nodes, graph_from, graph_to, graph_weight, source, destination):
    if source == destination:
        return 0
        
    adj = [[] for _ in range(graph_nodes + 1)]
    for u, v, w in zip(graph_from, graph_to, graph_weight):
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    dist = [float('inf')] * (graph_nodes + 1)
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == destination:
            return d
            
        for v, w in adj[u]:
            nxt = max(d, w)
            if nxt < dist[v]:
                dist[v] = nxt
                heapq.heappush(pq, (nxt, v))
                
    return -1
```

---

### Q2. Service Scaling Max Throughput

`[Latest]`

**Topic:** `Binary Search`, `Greedy`

### Problem Description
We have a composite service consisting of $N$ underlying services. The $i$-th service has an initial throughput `throughput[i]`.
We can increase the throughput of the $i$-th service in integer scaling increments. Each scaling step adds another `throughput[i]` to its capacity (e.g., scaling it $k-1$ times gives a throughput of $k \times \text{throughput}[i]$).
Each scaling increment for the $i$-th service costs `scalingCost[i]`. We have a total budget `budget`.

The overall throughput of the composite service is the minimum throughput among all $N$ services. Maximize this overall throughput.

---

### Python Solution

```python
def getMaximumThroughput(throughput, scalingCost, budget):
    def check(T):
        cost = 0
        for t, c in zip(throughput, scalingCost):
            # To get at least T throughput, we need scaling factor k >= ceil(T/t)
            # number of scaling steps = k - 1 = ceil(T/t) - 1
            x = (T + t - 1) // t - 1
            if x > 0:
                cost += x * c
                if cost > budget:
                    return False
        return True

    low = min(throughput)
    high = min(t * (1 + budget // c) for t, c in zip(throughput, scalingCost))
    ans = low
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
```

---

### Q3. Knight's Minimum Moves

`[Latest]`

**Topic:** `Graph`, `BFS`, `Shortest Path`

### Problem Description
Given an $n \times n$ chessboard, determine the minimum number of valid knight moves required to travel from a starting position $A$ to an ending position $B$. If it is impossible to reach the destination, return $-1$.
All moves must be within the boundaries of the board.

Assume positions $A$ and $B$ are given as $(row, column)$ coordinates using 0-based indexing.

---

### Python Solution

```python
from collections import deque

def minMoves(n, startRow, startCol, endRow, endCol):
    if startRow == endRow and startCol == endCol:
        return 0
        
    q = deque([(startRow, startCol, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[startRow][startCol] = True
    
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    while q:
        r, c, d = q.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if nr == endRow and nc == endCol:
                    return d + 1
                visited[nr][nc] = True
                q.append((nr, nc, d + 1))
                
    return -1
```

---

### Q4. Confluence Text Editor Parity Check

**Topic:** `Strings`, `Bit Manipulation`, `Parity`  

Atlassian has a collaborative text editor called Confluence. Let's assume the text editor receives an array of strings `s`. Each string is considered as a zero-indexed array of characters. All characters in the strings fall within the ASCII range of lowercase letters (`a-z`), with decimal ordinal values ranging from 97 to 122 (e.g., `ord('a') = 97`).

Given an array of strings `s` of size `k`, and an integer `m`, we calculate the value of each string `s[i]` of length `len(s[i])` as:
$$\text{value}[i] = (\text{ord}[s[i][0]])^m \times (\text{ord}[s[i][1]])^m \times \dots \times (\text{ord}[s[i][\text{len}(s[i]) - 1]])^m$$

Perform this calculation on each string, sum them up, and determine whether their sum is `EVEN` or `ODD`.

#### Constraints
- $1 \le t \le 50$ (number of test cases)
- $2 \le k \le 20$ (number of strings per test case)
- $1 \le |s[i]| \le 10^5$ (length of each string)
- $0 \le m \le 10^9$ (exponent)

#### Example 1 (Sample Case 0, Test 1)
**Exponent ($m$):** `50`  
**Strings:** `['aceace', 'ceceaa', 'abdbdbdbakjkljhkjh']`  
**Output:** `EVEN`

#### Example 2 (Sample Case 0, Test 2)
**Exponent ($m$):** `47`  
**Strings:** `['azbde', 'abcher', 'acegk']`  
**Output:** `ODD`

#### Solution Explanation
Computing the exact values would require massive power calculations and big-number multiplication, which is highly inefficient. We can solve this in $O(k \times L)$ time (where $L$ is the string length) using parity arithmetic (modulo 2):
1. For any character $c$, if $\text{ord}(c)$ is even, then $(\text{ord}(c))^m \pmod 2 \equiv 0$ (for $m \ge 1$). If $\text{ord}(c)$ is odd, then $(\text{ord}(c))^m \pmod 2 \equiv 1$.
2. The product of ordinals $(\text{ord}[s[i][j]])^m$ for a string $s[i]$ is odd if and only if **all characters in the string have odd ordinal values** (e.g., `a, c, e, g, i, k, m, o, q, s, u, w, y`). If there is even one character with an even ordinal (e.g., `b, d, f, h, j, l, n, p, r, t, v, x, z`), the product becomes even.
3. The sum of the values is odd if and only if the number of strings with odd values is odd.

*(Note: If $m = 0$, every string value is 1, so all strings are odd).*

```python
def checkParity(m: int, s: list[str]) -> str:
    if m == 0:
        return "ODD" if len(s) % 2 != 0 else "EVEN"
        
    even_chars = set("bdfhjlnprtvxz")
    odd_string_count = 0
    
    for string in s:
        # If no even character exists in the string, it is odd
        if not any(char in even_chars for char in string):
            odd_string_count += 1
            
    return "ODD" if odd_string_count % 2 != 0 else "EVEN"
```

- **Time Complexity:** $O(k \times L)$ where $L$ is the maximum string length.
- **Space Complexity:** $O(1)$ auxiliary space.

---

### Q5. Rearrange Students (Height Balance)

**Topic:** `Arrays`, `Greedy`, `Sorting`, `Math`  

In a school, two lines of students, `A` and `B`, are arranged with `N` students in each line, facing each other. The Physical Education teacher aims to make the heights of students standing across from each other equal. This can be achieved by swapping students between the two lines. Any student in one line can be swapped with any student in the other line.

Each swap, regardless of the students involved, incurs a cost equal to the height of the shorter student in the swap. Rearranging students within the same line does not incur any cost.

Find the minimal cost to rearrange the students so that the lines can be sorted to be identical, or return `-1` if it is impossible.

#### Constraints
- $1 \le n \le 2 \times 10^5$
- $1 \le \text{arrA}[i], \text{arrB}[i] \le 10^9$

#### Example
**arrA:** `[4, 2, 2, 2]`  
**arrB:** `[1, 4, 1, 2]`  
**Output:** `1`  
**Explanation:** 
- If we sort the combined set, we get: `[1, 1, 2, 2, 2, 2, 4, 4]`.
- The target multiset for each array is `[1, 2, 2, 4]`.
- `arrA` has one excess `2`, and `arrB` has one excess `1`.
- Swapping a `2` in `arrA` with a `1` in `arrB` costs $\min(2, 1) = 1$. This swap is sufficient.

#### Solution Explanation
1. Count the frequencies of all heights across both arrays. If any height has an odd total count, it's impossible to balance them equally, so return `-1`.
2. Determine the target count for each height, which is half of its total count.
3. Identify the excess heights in `arrA` and `arrB` (heights that exceed their target count). Let the sorted excess lists be `excess_A` (ascending) and `excess_B` (descending).
4. Pair up the excess elements: $u \in \text{excess\_A}$ and $v \in \text{excess\_B}$.
5. For each pair, we can either swap them directly at cost $\min(u, v)$, or swap them using the global minimum element in the entire school as a helper at cost $2 \times \text{min\_val}$. We take the minimum of these two options.

```python
from collections import Counter

def rearrangeStudents(arrA: list[int], arrB: list[int]) -> int:
    countA = Counter(arrA)
    countB = Counter(arrB)
    all_elements = set(arrA) | set(arrB)
    
    excess_A = []
    excess_B = []
    
    for val in all_elements:
        total_count = countA[val] + countB[val]
        if total_count % 2 != 0:
            return -1
        target = total_count // 2
        if countA[val] > target:
            excess_A.extend([val] * (countA[val] - target))
        elif countB[val] > target:
            excess_B.extend([val] * (countB[val] - target))
            
    if len(excess_A) != len(excess_B):
        return -1
        
    excess_A.sort()
    excess_B.sort(reverse=True)
    
    min_val = min(min(arrA), min(arrB))
    
    total_cost = 0
    for u, v in zip(excess_A, excess_B):
        total_cost += min(min(u, v), 2 * min_val)
        
    return total_cost
```

- **Time Complexity:** $O(N \log N)$ due to sorting the excess arrays.
- **Space Complexity:** $O(N)$ to store counts and excess arrays.

