# Interview Questions

*Total questions: 4*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Find Duplicate Account IDs

`[Latest]`

**Topic:** `Array`, `Hashing In-Place`

#### Description
You are given an array of account IDs containing integers from $1$ to $N$, where $N$ is the size of the array. Some account IDs may repeat multiple times. 

Find all account IDs that appear exactly twice **without using extra space for frequency counting** (in $O(1)$ auxiliary space and $O(N)$ time). Return the duplicate IDs in ascending order.

*Note: You may modify the input array.*

#### Constraints
- $1 \le N \le 100,000$
- $1 \le \text{accountIds}[i] \le N$

#### Input Format
- The first line of input contains an integer $N$, representing the number of account IDs.
- The second line of input contains $N$ space-separated integers.

#### Output Format
- Print all account IDs repeated exactly twice in ascending order, separated by spaces.
- If no duplicate IDs exist, print `-1`.

#### Sample Input 1
```text
6
2 5 3 2 3 6
```

#### Sample Output 1
```text
2 3
```

---

#### Python Solution
```python
import sys

def solve(accountIds):
    n = len(accountIds)
    b = n + 1
    # Use array indices to record frequency in-place
    for x in accountIds:
        v = (x % b) - 1
        if 0 <= v < n:
            accountIds[v] += b
            
    ans = [i + 1 for i in range(n) if accountIds[i] // b == 2]
    return ans if ans else [-1]

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        arr = [int(x) for x in input_data[1:n+1]]
        res = solve(arr)
        print(' '.join(map(str, res)))
```

---

### Q2. Minimum Audit Tour (TSP)

`[Latest]`

**Topic:** `Bitmask DP`, `Graphs`

#### Description
An auditor must visit every branch office exactly once and then return to the headquarters.
The travel costs between locations are provided as an $N \times N$ cost matrix, where `cost[i][j]` represents the cost of traveling from office `i` to office `j`.

The auditor starts from Headquarters (office 0), visits every other office exactly once, and finally returns to Headquarters. Find the minimum possible total travel cost.

#### Constraints
- $1 \le N \le 18$
- $0 \le \text{cost}[i][j] \le 10^6$

#### Input Format
- The first line contains an integer $N$, representing the number of offices.
- The second line contains an integer $M$, representing the number of columns (always equal to $N$).
- The next $N$ lines each contain $N$ space-separated integers representing the travel cost matrix.

#### Output Format
- Print a single integer representing the minimum tour cost.

#### Sample Input 1
```text
4
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```

#### Sample Output 1
```text
80
```

#### Explanation 1
The optimal tour is $0 \to 1 \to 3 \to 2 \to 0$ with cost $10 + 25 + 30 + 15 = 80$.

#### Sample Input 2
```text
3
3
0 5 9
5 0 10
9 10 0
```

#### Sample Output 2
```text
24
```

---

#### Python Solution
```python
import sys

def solve(cost):
    n = len(cost)
    if n <= 1:
        return 0
        
    cost_T = [list(col) for col in zip(*cost)]
    
    # Precompute set bits for all mask transitions
    set_bits = [[] for _ in range(1 << n)]
    for mask in range(1, 1 << n):
        low = mask & -mask
        idx = low.bit_length() - 1
        set_bits[mask] = set_bits[mask ^ low] + [idx]
        
    set_bits_no_zero = [
        [u for u in set_bits[mask] if u != 0]
        for mask in range(1 << n)
    ]
    
    # dp[mask][u] stores the min cost to visit subset `mask` ending at node `u`
    dp = [[10**9] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting at 0
    
    for mask in range(3, 1 << n, 2):
        dp_mask = dp[mask]
        for u in set_bits_no_zero[mask]:
            prev_mask = mask ^ (1 << u)
            dp_prev = dp[prev_mask]
            cost_u = cost_T[u]
            val = 10**9
            for v in set_bits[prev_mask]:
                c = dp_prev[v] + cost_u[v]
                if c < val:
                    val = c
            dp_mask[u] = val
            
    return min(dp[(1 << n) - 1][u] + cost[u][0] for u in range(1, n))

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        m = int(input_data[1])
        cost = []
        idx = 2
        for i in range(n):
            cost.append([int(x) for x in input_data[idx : idx + n]])
            idx += n
        print(solve(cost))
```

---

### Q3. LRU Cache Operations

`[Latest]`

**Topic:** `Design`, `LRU Cache`

#### Description
Design a Least Recently Used (LRU) Cache data structure supporting:
- `LRUCache(int capacity)`: Initialize the cache.
- `int get(int key)`: Return the value of the key if it exists, otherwise return `-1`.
- `void put(int key, int value)`: Insert or update the value. Evict the least recently used key if cache exceeds capacity.

#### Constraints
- $1 \le N \le 20$ (cache capacity)
- $1 \le M \le 1000$ (number of operations)

#### Input Format
- The first line contains the capacity $N$.
- The second line contains the number of operations $M$.
- The third line contains $M$ space-separated operation strings (e.g. `GET,x` or `PUT,x,y`).

#### Output Format
- Print space-separated results returned by the `GET` operations.

#### Sample Input 1
```text
2
6
GET,2 PUT,1,100 PUT,2,125 PUT,3,150 GET,1 GET,3
```

#### Sample Output 1
```text
-1 -1 150
```

---

#### Python Solution
```python
import sys
from collections import OrderedDict

def solve(N, operations):
    cache = OrderedDict()
    res = []
    
    for cmd in operations:
        if not cmd:
            continue
        parts = cmd.split(',')
        op = parts[0].strip().upper()
        
        if op == 'GET':
            k = int(parts[1].strip())
            if k in cache:
                res.append(cache[k])
                cache.move_to_end(k)
            else:
                res.append(-1)
        elif op == 'PUT':
            k = int(parts[1].strip())
            v = int(parts[2].strip())
            if k in cache:
                cache.move_to_end(k)
            cache[k] = v
            if len(cache) > N:
                cache.popitem(last=False)
                
    return res

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        N = int(input_data[0])
        M = int(input_data[1])
        # Join any split elements by spaces to parse correctly
        ops = input_data[2:]
        res = solve(N, ops)
        print(' '.join(map(str, res)))
```

---

### Q4. Top K Frequent Transaction Types

`[Latest]`

**Topic:** `Hashing`, `Heap`, `Sorting`

#### Description
Identify the $K$ most frequent transaction types. Ties in frequency must be broken alphabetically in ascending order.

#### Constraints
- $1 \le N \le 100,000$
- $1 \le K \le \text{Number of unique transaction types}$
- Transaction type names contain only English letters and digits.

#### Input Format
- The first line contains an integer $N$.
- The second line contains $N$ space-separated transaction types.
- The third line contains an integer $K$.

#### Output Format
- Print the top $K$ transaction types separated by spaces.

#### Sample Input 1
```text
8
Deposit Withdrawal Deposit Transfer Deposit Withdrawal Payment Transfer
2
```

#### Sample Output 1
```text
Deposit Transfer
```

---

#### Python Solution
```python
import sys
from collections import Counter
import heapq

def solve(transactions, K):
    count = Counter(transactions)
    # Min-heap elements: (-frequency, word)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    
    res = []
    for _ in range(min(K, len(heap))):
        res.append(heapq.heappop(heap)[1])
    return " ".join(res)

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        transactions = input_data[1 : n + 1]
        k = int(input_data[n + 1])
        print(solve(transactions, k))
```

