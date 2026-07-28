# Interview Questions

*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [SQL Questions](#sql-questions)

---

## Coding Questions

### Q1. Minimum Height of Rooted Tree

`[Latest]`

**Topic:** `Binary Search on Answer`, `Tree DP`, `Graphs`

#### Description
A database is represented as a rooted tree with `tree_nodes` tables, where Table 1 is the root. 

Up to `max_operations` operations are allowed. In one operation:
- Select a child table $u$ of a parent table $v$ and remove the edge $(u, v)$.
- Move $u$ (and its subtree) to become a direct child of the root (Table 1), reducing its depth.

Determine the minimum possible height of the tree.

**Note:**
- The height of the tree is defined as the maximum depth of any table.
- The depth of a table is the number of edges from the root to that table.
- A subtree in a rooted tree is a subgraph of the tree consisting of a vertex (the root) and its descendants, along with all edges incident to these descendants.

#### Constraints
- $2 \le \text{tree\_nodes} \le 2 \times 10^5$
- $1 \le \text{tree\_from}[i], \text{tree\_to}[i] \le \text{tree\_nodes}$
- $0 \le \text{max\_operations} \le \text{tree\_nodes} - 1$

#### Input Format
- The first line contains two space-separated integers: `tree_nodes` and `tree_edges` (which is equal to `tree_nodes - 1`).
- The next `tree_edges` lines each contain two integers, representing an edge in the tree.
- The last line contains the integer `max_operations`.

#### Output Format
- Print a single integer: the minimum possible height of the tree.

#### Sample Input 0
```text
5 4
2 3
4 2
3 1
1 5
2
```

#### Sample Output 0
```text
1
```

#### Explanation 0
Initially, the tree is:
```text
    1
   / \
  3   5
  |
  2
  |
  4
```
One optimal way of doing operations is:
1. Remove edge $(2, 4)$ and add edge $(1, 4)$.
2. Remove edge $(3, 2)$ and add edge $(1, 2)$.

This makes nodes 2 and 4 direct children of root 1.
All nodes 2, 3, 4, and 5 have depth 1, so the tree height is 1.

---

#### Python Solution
```python
import sys
from collections import deque

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def getMinimumHeight(tree_nodes, tree_from, tree_to, max_operations):
    adj = [[] for _ in range(tree_nodes + 1)]
    for u, v in zip(tree_from, tree_to):
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to determine parent-child relationships and BFS order
    parent = [0] * (tree_nodes + 1)
    depth = [0] * (tree_nodes + 1)
    order = []
    q = deque([1])
    vis = [False] * (tree_nodes + 1)
    vis[1] = True
    
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
                
    orig_h = max(depth)
    if max_operations == 0:
        return orig_h
        
    children = [[] for _ in range(tree_nodes + 1)]
    for i in range(2, tree_nodes + 1):
        children[parent[i]].append(i)
        
    # Process only non-leaf nodes bottom-up (excluding the root 1)
    non_leaves = [u for u in reversed(order) if u != 1 and children[u]]
    
    low, high, ans = 1, orig_h, orig_h
    ops = [0] * (tree_nodes + 1)
    h = [0] * (tree_nodes + 1)
    
    # Binary search for the minimum possible height
    while low <= high:
        mid = (low + high) // 2
        lim = mid - 1
        
        for u in non_leaves:
            c_ops = 0
            max_h = -1
            for v in children[u]:
                c_ops += ops[v]
                if h[v] == lim:
                    c_ops += 1  # Must detach and move v to the root
                elif h[v] > max_h:
                    max_h = h[v]
            ops[u] = c_ops
            h[u] = max_h + 1
            
        # Root (1) children check
        root_ops = sum(ops[v] for v in children[1])
        if root_ops <= max_operations:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        tree_nodes = int(input_data[0])
        tree_edges = int(input_data[1])
        tree_from = []
        tree_to = []
        idx = 2
        for _ in range(tree_edges):
            tree_from.append(int(input_data[idx]))
            tree_to.append(int(input_data[idx+1]))
            idx += 2
        max_operations = int(input_data[idx])
        print(getMinimumHeight(tree_nodes, tree_from, tree_to, max_operations))
```

---

### Q2. Minimum Processing Time

`[Latest]`

**Topic:** `Dynamic Programming`, `Bitset DP`, `Subset Sum`

#### Description
There are $n$ data files where each contains a specific amount of data represented as `data[i]`. Each file must be processed using either Processor A or Processor B. Processor A takes `processTimeA` seconds to process a single unit of data, and Processor B requires `processTimeB` seconds.

Determine the minimum time needed to process all the data files by efficiently allocating them to the processors.

#### Constraints
- $1 \le n \le 100$
- $1 \le \text{data}[i] \le 10^3$
- $1 \le \text{processTimeA}, \text{processTimeB} \le 10^3$

#### Input Format
- Line 1: `n`
- Line 2: `data` (space-separated integers)
- Line 3: `processTimeA`
- Line 4: `processTimeB`

#### Output Format
- Print a single integer representing the minimum total processing time.

#### Sample Input 1
```text
5
4 4 6 2 5
3
2
```

#### Sample Output 1
```text
26
```

#### Explanation 1
- Assign files 1 and 2 to Processor A: $(4 + 4) \times 3 = 24$ seconds.
- Assign files 3, 4, and 5 to Processor B: $(6 + 2 + 5) \times 2 = 26$ seconds.
The minimum total processing time is $\max(24, 26) = 26$ seconds.

---

#### Python Solution
```python
import sys

def getMinProcessingTime(data, processTimeA, processTimeB):
    total_sum = sum(data)
    
    # Subset sum using bitset DP
    # dp represents all possible subset sums of data
    dp = 1
    for x in data:
        dp |= (dp << x)
        
    ans = float('inf')
    for x in range(total_sum + 1):
        if (dp >> x) & 1:
            ans = min(ans, max(x * processTimeA, (total_sum - x) * processTimeB))
    return ans

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        data = [int(x) for x in input_data[1:n+1]]
        processTimeA = int(input_data[n+1])
        processTimeB = int(input_data[n+2])
        print(getMinProcessingTime(data, processTimeA, processTimeB))
```

---

## SQL Questions

### Q1. SQL: Visitor Viewing Report

`[Latest]`

**Topic:** `PostgreSQL`

#### Description
An online streaming company wants to generate a report that provides insights into the viewing habits of visitors to its platform. The task is to create a report with two fixed rows: one for anonymous visitors and another for subscribed visitors.

The result should have the following columns: `visitor_type` | `total_visitors` | `avg_view_length_seconds`.
- `visitor_type`: the type of visitor ("anonymous" or "subscribed")
- `total_visitors`: the total number of visitors for each type
- `avg_view_length_seconds`: the average stream view length in seconds for each type, rounded up to the nearest integer.

The result should be sorted in ascending order by `visitor_type`.

*Note: Calculate the view length by finding the difference between the start and end times for each viewer.*

#### Database Schema
Table: `anonymous_viewers`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | INT | NOT NULL | The identifier of the anonymous viewer |
| start_dt | VARCHAR(19) | NOT NULL | The date and time when the anonymous viewer started watching |
| end_dt | VARCHAR(19) | NOT NULL | The date and time when the anonymous viewer stopped watching |

Table: `subscribed_viewers`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | INT | NOT NULL | The identifier of the subscribed viewer |
| start_dt | VARCHAR(19) | NOT NULL | The date and time when the subscribed viewer started watching |
| end_dt | VARCHAR(19) | NOT NULL | The date and time when the subscribed viewer stopped watching |

#### Sample Output
```text
visitor_type | total_visitors | avg_view_length_seconds
anonymous    | 10             | 1764
subscribed   | 10             | 1703
```

---

#### SQL Query Solution (PostgreSQL)
```sql
SELECT
    'anonymous' AS visitor_type,
    COUNT(*) AS total_visitors,
    CEIL(AVG(EXTRACT(EPOCH FROM (CAST(end_dt AS TIMESTAMP) - CAST(start_dt AS TIMESTAMP))))) AS avg_view_length_seconds
FROM
    anonymous_viewers

UNION ALL

SELECT
    'subscribed' AS visitor_type,
    COUNT(*) AS total_visitors,
    CEIL(AVG(EXTRACT(EPOCH FROM (CAST(end_dt AS TIMESTAMP) - CAST(start_dt AS TIMESTAMP))))) AS avg_view_length_seconds
FROM
    subscribed_viewers

ORDER BY
    visitor_type ASC;
```

