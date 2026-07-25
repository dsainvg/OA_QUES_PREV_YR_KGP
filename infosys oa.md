# Interview Questions
*Total questions: 14*

---

## Table of Contents
- [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. String Occurrences Maximization

**Topic:** `Dynamic Programming`, `Strings`

**Problem Statement:**
Given a string $S$ of length $N$, a string $T$ of length $M$, and a budget $K$. You can change at most $K$ characters in $S$ to any character. Find the maximum number of non-overlapping subsegments in $S$ that have $T$ as a subsequence.

**Constraints:**
- $1 \le N \le 10^5$
- $1 \le M \le 100$
- $1 \le K \le 100$

**Python Solution:**
```python
def solve(N, M, K, S, T):
    # dp[c][j] = max completed matches with exactly c changes, and current partial match length j
    dp = [[-1] * M for _ in range(K + 1)]
    dp[0][0] = 0
    
    for i in range(N):
        next_dp = [row[:] for row in dp]
        for c in range(K + 1):
            for j in range(M):
                if dp[c][j] == -1:
                    continue
                # Match S[i] with T[j]
                cost_add = 0 if S[i] == T[j] else 1
                if c + cost_add <= K:
                    nj = j + 1
                    nc = c + cost_add
                    if nj == M:
                        next_dp[nc][0] = max(next_dp[nc][0], dp[c][j] + 1)
                    else:
                        next_dp[nc][nj] = max(next_dp[nc][nj], dp[c][j])
        dp = next_dp
        
    ans = 0
    for c in range(K + 1):
        for j in range(M):
            ans = max(ans, dp[c][j])
    return ans
```

---

### Q2. Ali and his Numbers

**Topic:** `Bitmask DP`, `Math`

**Problem Statement:**
Find the size of the largest possible subset of elements in array $A$ of size $N$ that are pairwise coprime (i.e., the greatest common divisor of any two chosen numbers is 1).

**Constraints:**
- $1 \le N \le 50$
- $1 \le A[i] \le 50$

**Python Solution:**
```python
import math

def solve(N, A):
    # Prime factors <= 50
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    num_primes = len(primes)
    
    # Map elements to their prime mask
    masks = []
    ones_count = 0
    for x in A:
        if x == 1:
            ones_count += 1
            continue
        mask = 0
        for i, p in enumerate(primes):
            if x % p == 0:
                mask |= (1 << i)
        masks.append(mask)
        
    # dp[mask] = max coprime subset size using primes in mask
    dp = [-1] * (1 << num_primes)
    dp[0] = 0
    
    for mask in masks:
        for state in range((1 << num_primes) - 1, -1, -1):
            if dp[state] == -1:
                continue
            if (state & mask) == 0:
                dp[state | mask] = max(dp[state | mask], dp[state] + 1)
                
    return max(dp) + ones_count
```

---

### Q3. Out Of Range Distinct

**Topic:** `Mo's Algorithm`, `Queries`

**Problem Statement:**
Given an array $A$ of $N$ integers and $Q$ queries of range $[l, r]$ (1-based). For each query, count the number of distinct elements in $A$ after removing elements in $[l, r]$. Sum the counts over all queries.

**Constraints:**
- $N \le 10^5$
- $Q \le 10^4$
- $A[i] \le 2 \times 10^5$

**Python Solution:**
```python
import math

def solve(N, Q, A, queries):
    block_size = int(math.ceil(N ** 0.5))
    
    # Store queries with their original index
    q_queries = []
    for idx, (l, r) in enumerate(queries):
        q_queries.append((l - 1, r - 1, idx))
        
    # Sort queries by block of L, and then by R
    q_queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))
    
    max_val = max(A) if A else 0
    freq = [0] * (max_val + 1)
    
    # Initially all elements are in the complement
    distinct_count = 0
    for x in A:
        if freq[x] == 0:
            distinct_count += 1
        freq[x] += 1
        
    ans = [0] * Q
    cur_L, cur_R = 0, -1
    
    def exclude(idx):
        nonlocal distinct_count
        x = A[idx]
        freq[x] -= 1
        if freq[x] == 0:
            distinct_count -= 1
            
    def include(idx):
        nonlocal distinct_count
        x = A[idx]
        if freq[x] == 0:
            distinct_count += 1
        freq[x] += 1
        
    for L, R, idx in q_queries:
        while cur_L > L:
            cur_L -= 1
            exclude(cur_L)
        while cur_R < R:
            cur_R += 1
            exclude(cur_R)
        while cur_L < L:
            include(cur_L)
            cur_L += 1
        while cur_R > R:
            include(cur_R)
            cur_R -= 1
            
        ans[idx] = distinct_count
        
    return sum(ans)
```

---

### Q4. Mr. Box and his Boxes

**Topic:** `Greedy`, `Heap`, `Huffman Coding`

**Problem Statement:**
You are given $N$ boxes. $a[i]$ denotes the number of toys of type $i$. All toys are initially in the first box. We can split any box's toys into $K$ groups ($2 \le K \le 3$) and move each group to empty boxes. Cost of operation is the size of the group being split. Find the minimum total cost to organize the toys such that each box contains only one type of toy.

**Constraints:**
- $N \le 2 \times 10^5$
- $a[i] \le 10^9$

**Python Solution:**
```python
import heapq

def solve(N, A):
    # This is bottom-up ternary Huffman tree merging.
    # To minimize cost, we maximize 3-way merges.
    # If N is even, we perform exactly one 2-way merge first on the smallest elements.
    heapq.heapify(A)
    total_cost = 0
    
    if N % 2 == 0:
        if len(A) >= 2:
            x = heapq.heappop(A)
            y = heapq.heappop(A)
            cost = x + y
            total_cost += cost
            heapq.heappush(A, cost)
            
    while len(A) > 1:
        x = heapq.heappop(A)
        y = heapq.heappop(A)
        z = heapq.heappop(A) if A else 0
        cost = x + y + z
        total_cost += cost
        heapq.heappush(A, cost)
        
    return total_cost
```

---

### Q5. Maximum MEX Cutting

**Topic:** `Tree DP`, `Offline Queries`, `Segment Tree`

**Problem Statement:**
Given a tree of $N$ nodes, each node $i$ having value $A[i]$. Cut exactly one edge to divide the tree into two subtrees $T_1$ and $T_2$ such that $\text{MEX}(T_1) + \text{MEX}(T_2)$ is maximized.

**Constraints:**
- $2 \le N \le 10^6$
- $0 \le A[i] \le N$

**Python Solution:**
```python
import sys
sys.setrecursionlimit(2000000)

def solve(N, A, edges):
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    tin = [0] * (N + 1)
    tout = [0] * (N + 1)
    timer = 0
    B = []
    
    LOG = 20
    up = [[0] * LOG for _ in range(N + 1)]
    depth = [0] * (N + 1)
    
    def dfs_init(u, p):
        nonlocal timer
        timer += 1
        tin[u] = timer
        B.append(A[u - 1])
        up[u][0] = p
        for i in range(1, LOG):
            up[u][i] = up[up[u][i-1]][i-1]
        for v in adj[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs_init(v, u)
        tout[u] = timer
        
    depth[1] = 0
    dfs_init(1, 1)
    
    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for i in range(LOG - 1, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[u][i]
        if u == v:
            return u
        for i in range(LOG - 1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]
        
    present = [False] * (N + 2)
    for x in A:
        if x <= N + 1:
            present[x] = True
    min_missing = 0
    while present[min_missing]:
        min_missing += 1
        
    val_nodes = [[] for _ in range(min_missing)]
    for i, x in enumerate(A):
        if x < min_missing:
            val_nodes[x].append(i + 1)
            
    val_lca = [0] * min_missing
    for x in range(min_missing):
        if not val_nodes[x]:
            continue
        curr_lca = val_nodes[x][0]
        for node in val_nodes[x][1:]:
            curr_lca = get_lca(curr_lca, node)
        val_lca[x] = curr_lca
        
    val = [10**9] * (N + 1)
    for x in range(min_missing):
        if val_nodes[x]:
            l = val_lca[x]
            val[l] = min(val[l], x)
            
    min_subtree_L = [10**9] * (N + 1)
    
    def dfs_dp(u, p):
        curr = val[u]
        for v in adj[u]:
            if v != p:
                curr = min(curr, dfs_dp(v, u))
        min_subtree_L[u] = curr
        return curr
        
    dfs_dp(1, 1)
    
    tree_size = min_missing + 2
    tree = [0] * (4 * tree_size)
    
    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])
        
    def query(node, start, end, L_val):
        if start == end:
            return start
        mid = (start + end) // 2
        if tree[2 * node] < L_val:
            return query(2 * node, start, mid, L_val)
        else:
            return query(2 * node + 1, mid + 1, end, L_val)
            
    queries_by_tout = [[] for _ in range(N + 1)]
    for u in range(1, N + 1):
        queries_by_tout[tout[u]].append(u)
        
    mex_Tu = [0] * (N + 1)
    for i in range(1, N + 1):
        val_at_i = B[i - 1]
        if val_at_i < tree_size:
            update(1, 0, tree_size - 1, val_at_i, i)
        for u in queries_by_tout[i]:
            mex_Tu[u] = query(1, 0, tree_size - 1, tin[u])
            
    ans = 0
    for u, v in edges:
        child = v if depth[v] > depth[u] else u
        m_Tu = mex_Tu[child]
        m_comp = min(min_missing, min_subtree_L[child])
        ans = max(ans, m_Tu + m_comp)
        
    return ans
```

---

### Q6. MaxBridges / Bridges of Hono-Lolo

**Topic:** `Dynamic Programming`, `LCS`

**Problem Statement:**
There are $N$ cities on the left side of the river and $N$ cities on the right side.
A bridge can be built between cities $A[i]$ on the left and $B[j]$ on the right if $|A[i] - B[j]| \le 4$.
Find the maximum number of bridges that can be built with no two bridges intersecting.

**Constraints:**
- $1 \le N \le 1000$

**Python Solution:**
```python
def solve(N, A, B):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if abs(A[i-1] - B[j-1]) <= 4:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    return dp[N][N]
```

---

### Q7. Grid of Digits

**Topic:** `Digit DP`

**Problem Statement:**
You are given a grid of size $N \times M$, where each cell has a digit value between 0 and 9. Missed cells have value -1.
You can replace any missed cell with any digit between 0 and 9. After replacing all missed cells, you take one digit from each row and concatenate them to form an $N$-digit integer.
Find the number of possible resulting integers that are less than or equal to $R$, and are divisible by 3. Return the count modulo 998244353.

**Constraints:**
- $1 \le N \le 1000$
- $1 \le M \le 100$
- $-1 \le Grid[i][j] \le 9$
- $\text{len}(R) = N$

**Python Solution:**
```python
def solve(N, M, Grid, S):
    MOD = 998244353
    D = []
    for row in Grid:
        if -1 in row:
            D.append(list(range(10)))
        else:
            D.append(list(set(row)))
            
    memo = {}
    
    def dp(idx, tight, rem):
        if idx == N:
            return 1 if rem == 0 else 0
        state = (idx, tight, rem)
        if state in memo:
            return memo[state]
            
        limit = int(S[idx]) if tight else 9
        ans = 0
        for d in D[idx]:
            if d <= limit:
                ans = (ans + dp(idx + 1, tight and (d == limit), (rem + d) % 3)) % MOD
                
        memo[state] = ans
        return ans
        
    return dp(0, True, 0)
```

---

### Q8. Tree Cutting

**Topic:** `Group Steiner Tree on Trees`, `Dynamic Programming`

**Problem Statement:**
You have a tree $T$ with $N$ nodes. Each node has a value $A[i]$.
The cost of the tree is the LCM of all its node values.
Find the minimum size of a connected subgraph of the tree such that its cost is equal to the cost of $T$.

**Constraints:**
- $3 \le N \le 1000$
- $1 \le A[i] \le 10^9$
- LCM of all node values does not exceed $10^9$

**Python Solution:**
```python
import math

def solve(N, A, edges):
    def gcd(x, y):
        return math.gcd(x, y)
    def lcm(x, y):
        return (x * y) // gcd(x, y)
        
    L = 1
    for x in A:
        L = lcm(L, x)
        
    temp = L
    primes = []
    prime_powers = []
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            p_pow = 1
            while temp % d == 0:
                p_pow *= d
                temp //= d
            primes.append(d)
            prime_powers.append(p_pow)
        d += 1
    if temp > 1:
        primes.append(temp)
        prime_powers.append(temp)
        
    k = len(primes)
    if k == 0:
        return 1
        
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    node_masks = [0] * (N + 1)
    for u in range(1, N + 1):
        mask = 0
        for i, q in enumerate(prime_powers):
            if A[u - 1] % q == 0:
                mask |= (1 << i)
        node_masks[u] = mask
        
    INF = 10**9
    dp = [[INF] * (1 << k) for _ in range(N + 1)]
    
    order = []
    parent = [0] * (N + 1)
    queue = [1]
    parent[1] = 1
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                queue.append(v)
                
    for u in reversed(order):
        mask_u = node_masks[u]
        sub = mask_u
        while True:
            dp[u][sub] = 1
            if sub == 0:
                break
            sub = (sub - 1) & mask_u
            
        for v in adj[u]:
            if v == parent[u]:
                continue
            next_dp = [INF] * (1 << k)
            for m1 in range(1 << k):
                if dp[u][m1] == INF:
                    continue
                for m2 in range(1 << k):
                    if dp[v][m2] == INF:
                        continue
                    next_dp[m1 | m2] = min(next_dp[m1 | m2], dp[u][m1] + dp[v][m2])
            dp[u] = next_dp
            
    ans = INF
    for u in range(1, N + 1):
        ans = min(ans, dp[u][(1 << k) - 1])
        
    return ans
```

---

### Q9. Permutation Swaps

**Topic:** `Permutations`, `Cycles`, `Combinatorics`

**Problem Statement:**
You are given a permutation $P$ of length $N$. This represents a graph of $N$ nodes where there is an edge from $i$ to $P[i]$.
Find the total number of possible pairs of indices $\{i, j\}$ such that if $P[i]$ and $P[j]$ are swapped, the resulting graph has the maximum possible longest path among all possible swaps. Return the answer modulo $10^9+7$.

**Constraints:**
- $1 \le N \le 10^5$

**Python Solution:**
```python
def solve(N, P):
    MOD = 10**9 + 7
    visited = [False] * (N + 1)
    cycle_sizes = []
    
    for i in range(1, N + 1):
        if not visited[i]:
            curr = i
            size = 0
            while not visited[curr]:
                visited[curr] = True
                curr = P[curr - 1]
                size += 1
            cycle_sizes.append(size)
            
    cycle_sizes.sort(reverse=True)
    m = len(cycle_sizes)
    
    if m == 1:
        if N == 1:
            return 0
        elif N == 2:
            return 1
        else:
            return N
            
    C1 = cycle_sizes[0]
    C2 = cycle_sizes[1]
    
    from collections import Counter
    counts = Counter(cycle_sizes)
    
    if C1 > C2:
        ways = (counts[C1] * C1 * counts[C2] * C2) % MOD
    else:
        cnt = counts[C1]
        ways = (cnt * (cnt - 1) // 2) * C1 * C1
        ways %= MOD
        
    return ways
```

---

### Q10. Yet another LIS

**Topic:** `Dynamic Programming`, `Bitwise`

**Problem Statement:**
Given an array $A$ of size $N$. A sequence of integers is valid if the difference between any two consecutive numbers in the sequence is 0 or a power of 2.
Find the length of the longest valid non-decreasing subsequence of $A$.

**Constraints:**
- $1 \le N \le 10^5$
- $1 \le A[i] \le 10^9$

**Python Solution:**
```python
def solve(N, A):
    dp = {}
    for x in A:
        val = dp.get(x, 0) + 1
        for k in range(30):
            prev = x - (1 << k)
            if prev in dp:
                val = max(val, dp[prev] + 1)
        dp[x] = max(dp.get(x, 0), val)
    return max(dp.values()) if dp else 0
```

---

### Q11. Divisible Strings

**Topic:** `Math`, `Segment Sieve`, `Inclusion-Exclusion`

**Problem Statement:**
Given three integers $K$, $L$, and $R$. Find the total number of integers in $[L, R]$ that are NOT divisible by any integer from 2 to $K$.

**Constraints:**
- $1 \le K \le 10^5$
- $1 \le \text{len}(L), \text{len}(R) \le 10^5$

**Python Solution:**
```python
def solve(K, L_str, R_str):
    L = int(L_str)
    R = int(R_str)
    
    is_prime = [True] * (K + 1)
    primes = []
    for p in range(2, K + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, K + 1, p):
                is_prime[i] = False
                
    if R - L <= 1000000:
        length = R - L + 1
        marked = [False] * length
        for p in primes:
            rem = L % p
            start = (p - rem) % p
            for i in range(start, length, p):
                marked[i] = True
        return marked.count(False)
        
    if len(primes) <= 15:
        ans = 0
        M = len(primes)
        
        def dfs(idx, curr_lcm, sign):
            nonlocal ans
            if curr_lcm > R:
                return
            if idx == M:
                count = R // curr_lcm - (L - 1) // curr_lcm
                ans += count * sign
                return
            dfs(idx + 1, curr_lcm, sign)
            import math
            next_lcm = (curr_lcm * primes[idx]) // math.gcd(curr_lcm, primes[idx])
            dfs(idx + 1, next_lcm, -sign)
            
        dfs(0, 1, 1)
        return ans
        
    return 0
```

---

### Q12. Tree Function

**Topic:** `DSU on Tree`, `Dynamic Programming`

**Problem Statement:**
You are given a tree with $N$ nodes rooted at node 1. Each node $U$ has a value $A[U]$.
Let $F(U, K)$ be the number of ways to choose a subset of nodes in the subtree of $U$ such that the sum of values of the nodes in the subset is equal to $K$.
Find the sum of $F(U, K)$ for all $U$ from 1 to $N$, modulo $10^9+7$.

**Constraints:**
- $1 \le N \le 1000$
- $1 \le K \le 1000$

**Python Solution:**
```python
import sys
sys.setrecursionlimit(2000000)

def solve(N, M, K, A, edges):
    MOD = 10**9 + 7
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    sz = [0] * (N + 1)
    heavy = [0] * (N + 1)
    
    def dfs_sz(u, p):
        sz[u] = 1
        max_c = 0
        for v in adj[u]:
            if v != p:
                dfs_sz(v, u)
                sz[u] += sz[v]
                if sz[v] > max_c:
                    max_c = sz[v]
                    heavy[u] = v
                    
    dfs_sz(1, 0)
    
    dp = [0] * (K + 1)
    dp[0] = 1
    ans = 0
    
    def add_val(x):
        for i in range(K, x - 1, -1):
            dp[i] = (dp[i] + dp[i - x]) % MOD
            
    def remove_val(x):
        for i in range(x, K + 1):
            dp[i] = (dp[i] - dp[i - x] + MOD) % MOD
            
    def update_subtree(u, p, val_add):
        x = A[u - 1]
        if val_add:
            add_val(x)
        else:
            remove_val(x)
        for v in adj[u]:
            if v != p:
                update_subtree(v, u, val_add)
                
    def dfs_dsu(u, p, keep):
        for v in adj[u]:
            if v != p and v != heavy[u]:
                dfs_dsu(v, u, False)
        if heavy[u]:
            dfs_dsu(heavy[u], u, True)
            
        add_val(A[u - 1])
        for v in adj[u]:
            if v != p and v != heavy[u]:
                update_subtree(v, u, True)
                
        nonlocal ans
        ans = (ans + dp[K]) % MOD
        
        if not keep:
            remove_val(A[u - 1])
            for v in adj[u]:
                if v != p and v != heavy[u]:
                    update_subtree(v, u, False)
            if heavy[u]:
                update_subtree(heavy[u], u, False)
                
    dfs_dsu(1, 0, True)
    return ans
```

---

### Q13. Count Subsequences

**Topic:** `Dynamic Programming`, `Bitwise`

**Problem Statement:**
Given an array $A$ of size $N$. Find the total number of possible increasing subsequences such that the bitwise AND of all elements in the subsequence is 0. Return the count modulo $10^9+7$.

**Constraints:**
- $1 \le N \le 50000$
- $1 \le A[i] \le 63$

**Python Solution:**
```python
def solve(N, A):
    MOD = 10**9 + 7
    dp = [[0] * 64 for _ in range(64)]
    pref = [[0] * 64 for _ in range(64)]
    
    for x in A:
        add_dp = [0] * 64
        add_dp[x] = 1
        for mask in range(64):
            add_dp[mask & x] = (add_dp[mask & x] + pref[x - 1][mask]) % MOD
            
        for mask in range(64):
            dp[x][mask] = (dp[x][mask] + add_dp[mask]) % MOD
            for z in range(x, 64):
                pref[z][mask] = (pref[z][mask] + add_dp[mask]) % MOD
                
    return pref[63][0]
```

---

### Q14. Equal GCDs

**Topic:** `Math`, `Number Theory`, `Mobius Inversion`

**Problem Statement:**
Given an array $A$ of length $N$. You can paint each element of $A$ either black, white, or leave it unpainted.
A painting is valid if at least one element is black and at least one element is white.
Find the number of valid ways to paint $A$ such that the greatest common divisor (GCD) of the black-painted elements equals the GCD of the white-painted elements. Return the count modulo $10^9+7$.

**Constraints:**
- $1 \le N \le 300$
- $1 \le A[i] \le 300$

**Python Solution:**
```python
def solve(N, A):
    MOD = 10**9 + 7
    max_val = max(A) if A else 0
    if max_val == 0:
        return 0
        
    counts = [0] * (max_val + 1)
    for x in A:
        counts[x] += 1
        
    S = [0] * (max_val + 1)
    for i in range(1, max_val + 1):
        for j in range(i, max_val + 1, i):
            S[i] += counts[j]
            
    mu = [0] * (max_val + 1)
    mu[1] = 1
    is_prime = [True] * (max_val + 1)
    primes = []
    for i in range(2, max_val + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > max_val:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]
                
    pow2 = [1] * (N + 1)
    pow3 = [1] * (N + 1)
    for i in range(1, N + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD
        pow3[i] = (pow3[i - 1] * 3) % MOD
        
    total_ans = 0
    
    for g in range(1, max_val + 1):
        ans_g = 0
        limit = max_val // g
        for d in range(1, limit + 1):
            if mu[d] == 0:
                continue
            gd = g * d
            for e in range(1, limit + 1):
                if mu[e] == 0:
                    continue
                ge = g * e
                
                import math
                lcm_val = (gd * ge) // math.gcd(gd, ge)
                
                c_both = S[lcm_val] if lcm_val <= max_val else 0
                c_gd = S[gd]
                c_ge = S[ge]
                
                c_B = c_gd - c_both
                c_W = c_ge - c_both
                
                term = (pow3[c_both] * pow2[c_B + c_W]) % MOD
                term = (term - pow2[c_gd] + MOD) % MOD
                term = (term - pow2[c_ge] + MOD) % MOD
                term = (term + 1) % MOD
                
                factor = mu[d] * mu[e]
                if factor == 1:
                    ans_g = (ans_g + term) % MOD
                elif factor == -1:
                    ans_g = (ans_g - term + MOD) % MOD
                    
        total_ans = (total_ans + ans_g) % MOD
        
    return total_ans
```
