# Interview Questions

*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Nearby Batch
**Topic:** `Greedy`, `Sorting` `[Latest]`

#### Description
Your team must send push notifications to $n$ users. User $i$ has priority score $p[i]$ (higher means more urgent).
Notifications are sent in batches under the following conditions:
- A batch can contain 1 or 2 users.
- A batch with 2 users is allowed only if the absolute difference between their priorities is at most $D$: $|p[i] - p[j]| \le D$.
- A batch with 1 user is always allowed.

Find the minimum number of batches needed to notify all users.

#### Input Format
- Line 1: integer $D$ — the maximum allowed priority difference for pairing.
- Line 2: integer $n$ — the number of users.
- Line 3: $n$ space-separated integers — the priorities $p[i]$.

#### Output Format
Print one integer: the minimum number of batches.

#### Constraints
- $1 \le n \le 2 \times 10^5$
- $0 \le D \le 10^9$
- $1 \le p[i] \le 10^9$

#### Sample Case
**Input:**
```text
2
5
1 2 3 4 5
```

**Output:**
```text
3
```

**Explanation:**
- Sorted priorities: $[1, 2, 3, 4, 5]$
- We can form pairs:
  - Batch 1: users with priorities $(1, 2)$ ($2-1 = 1 \le 2$)
  - Batch 2: users with priorities $(3, 4)$ ($4-3 = 1 \le 2$)
  - Batch 3: user with priority $5$ (single user)
- Total batches = 3.

---

#### Python Solution
```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    d = int(input_data[0])
    n = int(input_data[1])
    p = [int(x) for x in input_data[2:2+n]]
    
    # Sort priorities to enable greedy adjacent pairing
    p.sort()
    
    pairs = 0
    i = 0
    while i < n - 1:
        if p[i+1] - p[i] <= d:
            pairs += 1
            i += 2  # Skip both paired elements
        else:
            i += 1  # Skip only the left element (must remain single)
            
    # Each pair reduces the total required batches by 1
    print(n - pairs)

if __name__ == '__main__':
    solve()
```

---

### Q2. Array Stabilization (GCD version)
**Topic:** `Number Theory`, `Sparse Table`, `Two Pointers` `[Latest]`

#### Description
You are given an array $a$ of $n$ integers. In one operation, you replace every element $a_i$ with $\gcd(a_i, a_{(i+1) \pmod n})$ simultaneously.
Find the minimum number of operations required until all elements in the array become equal.

#### Input Format
- The first line contains $t$, the number of test cases.
- For each test case:
  - The first line contains $n$.
  - The second line contains $n$ space-separated integers representing the array $a$.

#### Output Format
For each test case, print the minimum number of operations.

#### Constraints
- $1 \le t \le 10^4$
- $2 \le n \le 2 \times 10^5$
- $1 \le a_i \le 10^6$
- The sum of $n$ over all test cases does not exceed $2 \times 10^5$.

#### Sample Case
**Input:**
```text
5
4
16 24 10 5
4
42 42 42 42
3
4 6 2
10
1 2 1 1 1 2 1 1 1 1
2
9 9
```

**Output:**
```text
3
0
2
1
0
```

---

#### Python Solution
```python
import sys
import math

def solve_case(n, a):
    # If all elements are already equal
    if len(set(a)) == 1:
        return 0
        
    # Find the target GCD of the entire array
    g = a[0]
    for x in a:
        g = math.gcd(g, x)
        
    # Concatenate the array to easily handle circular queries
    ap = a + a
    st = [ap]
    
    # Precompute Sparse Table for range GCD queries
    while (1 << (len(st) - 1)) <= n:
        L = 1 << (len(st) - 1)
        st.append([math.gcd(st[-1][i], st[-1][i + L]) for i in range(len(st[-1]) - L)])
        
    ans = 0
    j = 0
    for i in range(n):
        if j < i:
            j = i
        # Use two pointers: expand j until the range GCD equals the overall GCD
        while True:
            length = j - i + 1
            k = length.bit_length() - 1
            current_gcd = math.gcd(st[k][i], st[k][j - (1 << k) + 1])
            if current_gcd == g:
                break
            j += 1
        ans = max(ans, j - i)
        
    return ans

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        a = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        out.append(solve_case(n, a))
    print('\n'.join(map(str, out)))

if __name__ == '__main__':
    solve()
```

---

### Q3. Signal Propagation
**Topic:** `Dynamic Programming on Trees`, `Combinatorics` `[Latest]`

#### Description
A research lab models a signal network as a directed tree of $n$ sensors, rooted at sensor 1. A directed edge from sensor $u$ to sensor $v$ means sensor $u$ must transmit its reading before sensor $v$ can begin processing.

The lab has discovered a phenomenon called echo propagation: once a signal reaches any boundary sensor (a sensor with no outgoing connections), it echoes back through the network. The echo follows the same connections but in reverse direction — however, the boundary sensors themselves do not echo (they absorb the signal).

Formally, the full propagation network is constructed as follows:
- Start with the original sensor tree (nodes $1$ to $n$, edges as given).
- For every non-boundary sensor $v$, create a shadow node $v'$.
- For every edge $u \to v$ in the original tree where both $u$ and $v$ are non-boundary, add a shadow edge $v' \to u'$.
- For every edge $u \to v$ in the original tree where $v$ is a boundary sensor, add an edge $v \to u'$ (the boundary sensor triggers the shadow of its parent).
- Node 1 has no incoming edges in the original tree; its shadow $1'$ has no outgoing edges.

The lab wants to schedule all sensor activations (both original and shadow nodes) in a valid order — meaning every sensor activates only after all sensors that must precede it have done so.

Count the number of valid activation schedules, modulo $10^9 + 7$.

#### Input Format
- Line 1: integer $n$ — the number of sensors.
- Next $n-1$ lines: two space-separated integers $u$ and $v$, representing a directed edge from $u$ to $v$.

#### Output Format
Print the number of valid activation schedules modulo $10^9 + 7$.

#### Constraints
- $1 \le n \le 2 \times 10^5$
- Time Limit: 1.0 sec
- Modulo: $10^9 + 7$

#### Sample Case
**Input:**
```text
4
1 2
2 3
2 4
```

**Output:**
```text
2
```

**Explanation:**
- Nodes: $1, 2$ are non-boundary; $3, 4$ are boundary (leaves).
- Shadows: $1', 2'$.
- DAG has 6 nodes: $\{1, 2, 3, 4, 1', 2'\}$.
- The dependencies dictate that:
  - Node $2$ and its children's subtrees must execute between $1$ and $1'$.
  - Nodes $3$ and $4$ must execute between $2$ and $2'$.
- At node 2: leaves 3 and 4 are independent, leading to $2! = 2$ ways.
- At root 1: only child subtree is 2 (which already contains its structure).
- Total valid schedules = 2.

---

#### Python Solution
```python
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if n == 1:
        print(1)
        return
        
    adj = [[] for _ in range(n + 1)]
    idx = 1
    # Build tree representation
    for _ in range(n - 1):
        if idx >= len(input_data):
            break
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        
    # Get BFS traversal order
    order = []
    queue = [1]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        for v in adj[u]:
            queue.append(v)
            
    MOD = 10**9 + 7
    
    # Precompute factorials and inverse factorials for combinations
    fact = [1] * (2 * n + 5)
    inv = [1] * (2 * n + 5)
    for i in range(1, len(fact)):
        fact[i] = (fact[i - 1] * i) % MOD
        
    inv[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(len(fact) - 2, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD
        
    dp = [1] * (n + 1)
    size = [1] * (n + 1)
    
    # Dynamic programming bottom-up traversal
    for u in reversed(order):
        if not adj[u]:
            # Leaf nodes have size 1 and 1 way to order
            size[u] = 1
            dp[u] = 1
        else:
            total_child_size = 0
            prod_dp = 1
            prod_inv_sizes = 1
            for c in adj[u]:
                total_child_size += size[c]
                prod_dp = (prod_dp * dp[c]) % MOD
                prod_inv_sizes = (prod_inv_sizes * inv[size[c]]) % MOD
                
            # Interleave child subtrees using multinomial coefficients
            multinomial = (fact[total_child_size] * prod_inv_sizes) % MOD
            dp[u] = (prod_dp * multinomial) % MOD
            
            # Subtree size = original node u + shadow node u' + size of all children
            size[u] = 2 + total_child_size
            
    print(dp[1])

if __name__ == '__main__':
    solve()
```

