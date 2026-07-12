# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/gameskraft*
*Total questions: 14*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Get Max Occurrences

**Topic:** `Strings`, `Sliding Window`, `Hashing`  

Given a string `components`, find the maximum number of occurrences of any substring that satisfies the following conditions:
- Substring length is between `minLength` and `maxLength` (inclusive).
- The number of unique characters in the substring is at most `maxUnique`.

#### Constraints
- $1 \le \text{len}(components) \le 10^5$
- $1 \le minLength \le maxLength \le 26$
- $2 \le maxUnique \le 26$

#### Example
**components:** `"aababcaab"`  
**minLength:** `2`  
**maxLength:** `3`  
**maxUnique:** `2`  
**Output:** `2`  
**Explanation:**  
The valid substrings of length 2 and 3 with at most 2 unique characters are:
- `"aa"` occurs 2 times: `[aababcaab]`, `[aababcaab]`
- `"ab"` occurs 2 times: `[aababcaab]`, `[aababcaab]`
- `"ba"` occurs 2 times: `[aababcaab]`, `[aababcaab]`
- `"bc"` occurs 1 time: `[aababcaab]`
- `"ca"` occurs 1 time: `[aababcaab]`
- `"aab"` occurs 2 times: `[aababcaab]`, `[aababcaab]`
- `"aba"` occurs 1 time: `[aababcaab]`
- `"bab"` occurs 1 time: `[aababcaab]`
- `"abc"` occurs 1 time: `[aababcaab]` (3 unique characters, invalid)
- `"bca"` occurs 1 time: `[aababcaab]` (3 unique characters, invalid)
- `"caa"` occurs 1 time: `[aababcaab]`
The maximum frequency among all valid substrings is 2.

#### Solution Explanation
Since any longer valid substring containing a shorter valid substring will occur at most as many times as the shorter one, we only need to search for substrings of length exactly `minLength`. Substrings of length greater than `minLength` cannot have a higher frequency than their prefix of length `minLength`.
We can use a sliding window of size `minLength` to find and count the frequencies of all valid substrings in $O(N \cdot minLength)$ time.

```python
from collections import defaultdict

def getMaxOccurrences(components: str, minLength: int, maxLength: int, maxUnique: int) -> int:
    counts = defaultdict(int)
    n = len(components)
    max_freq = 0
    
    # Slide a window of size minLength across the string
    for i in range(n - minLength + 1):
        substring = components[i : i + minLength]
        unique_chars = len(set(substring))
        if unique_chars <= maxUnique:
            counts[substring] += 1
            if counts[substring] > max_freq:
                max_freq = counts[substring]
                
    return max_freq
```

- **Time Complexity:** $O(N \times minLength)$ where $N$ is the length of the string `components`.
- **Space Complexity:** $O(N \times minLength)$ to store the frequency of each substring.

---

### Q2. Total Palindrome Transformation Cost

**Topic:** `Strings`, `Palindromes`, `Frequency Count`  

Given a string `dna` of length $N$, find the sum of palindrome transformation costs over all substrings of `dna`.
The palindrome transformation cost of a string is defined as the minimum number of character modifications required so that its characters can be rearranged to form a palindrome.
For a string with character frequencies, if the number of characters with odd frequencies is $k$, we can change $\lfloor k/2 \rfloor$ characters to reduce the number of odd frequencies to at most 1, which allows the string to be rearranged into a palindrome.

#### Constraints
- $1 \le N \le 10^5$
- `dna` contains only lowercase English letters (`a-z`).

#### Example
**dna:** `"aabcd"`  
**Output:** `5`  
**Explanation:**  
- Length 1 substrings: `"a"`, `"a"`, `"b"`, `"c"`, `"d"` (all cost 0) -> Total = 0
- Length 2 substrings: `"aa"` (cost 0), `"ab"` (cost 0), `"bc"` (cost 0), `"cd"` (cost 0) -> Total = 0
- Length 3 substrings: `"aab"` (cost 0), `"abc"` (cost 1), `"bcd"` (cost 1) -> Total = 2
- Length 4 substrings: `"aabc"` (cost 1), `"abcd"` (cost 1) -> Total = 2
- Length 5 substrings: `"aabcd"` (cost 1) -> Total = 1
Sum of costs = 0 + 0 + 2 + 2 + 1 = 5.

#### Solution Explanation
We can compute this in $O(N \cdot \Sigma)$ time (where $\Sigma = 26$ is the alphabet size):
1. Represent the parity of character frequencies in any prefix of `dna` using a 26-bit mask. The $b$-th bit is 1 if the $b$-th character occurs an odd number of times in the prefix, and 0 otherwise.
2. The frequency parity mask of substring `dna[L...R]` is the bitwise XOR of the prefix masks: `mask[R+1] ^ mask[L]`.
3. The number of odd frequency characters in the substring is the number of set bits (popcount) in the XORed mask. The transformation cost is $\lfloor \text{popcount} / 2 \rfloor$.
4. Mathematically, $\lfloor \text{popcount} / 2 \rfloor = (\text{popcount} - (\text{popcount} \pmod 2)) / 2$.
5. The parity of the popcount of `A ^ B` is the XOR of their individual popcount parities. Thus, we can compute the sum of popcounts bit-by-bit, and subtract the number of pairs with different popcount parities.

```python
def getTotalPalindromeTransformationCost(dna: str) -> int:
    n = len(dna)
    mask = 0
    prefix_masks = [0] * (n + 1)
    
    for i, char in enumerate(dna):
        bit = ord(char) - ord('a')
        mask ^= (1 << bit)
        prefix_masks[i + 1] = mask
        
    # Count prefix masks with 1-bits at each position
    cnt_ones = [0] * 26
    for m in prefix_masks:
        for b in range(26):
            if (m >> b) & 1:
                cnt_ones[b] += 1
                
    total_popcounts = 0
    total_prefixes = n + 1
    for b in range(26):
        ones = cnt_ones[b]
        zeros = total_prefixes - ones
        total_popcounts += ones * zeros
        
    # Count prefix masks with odd popcount parity
    cnt_odd_parity = 0
    for m in prefix_masks:
        pop = bin(m).count('1')
        if pop % 2 == 1:
            cnt_odd_parity += 1
            
    cnt_even_parity = total_prefixes - cnt_odd_parity
    total_parity_diff = cnt_odd_parity * cnt_even_parity
    
    # total_cost = sum(floor(popcount / 2))
    return (total_popcounts - total_parity_diff) // 2
```

- **Time Complexity:** $O(N \times \Sigma)$ where $\Sigma = 26$.
- **Space Complexity:** $O(N)$ to store prefix masks.

---

### Q3. Get Min Inversions

**Topic:** `Trees`, `DFS`, `Graph Inversion`  

An airport limousine can take multiple riders to the airport at the same time. On the way back to the starting point, the driver may pick up additional riders for the next trip. A map of locations represents a directed tree with `gNodes` nodes.
Root the tree at some node $r$ such that the number of edge inversions needed to make all edges point away from $r$ (towards all other nodes) is minimized. Return this minimum number of inversions.

#### Constraints
- $1 \le gNodes \le 2 \times 10^5$
- The graph is a connected tree.

#### Example
**gNodes:** `3`  
**gFrom:** `[0, 1]`  
**gTo:** `[1, 2]`  
**Output:** `0`  
**Explanation:**  
If we root the tree at node 0, the edges are 0 -> 1 and 1 -> 2. All nodes are reachable from the root without inverting any edges. Inversion cost = 0.

#### Solution Explanation
This is a tree rerooting problem that can be solved in $O(N)$ time with two DFS traversals:
1. Traverse the tree starting from an arbitrary root (node 0) using DFS. Calculate the inversion cost to make all edges point away from node 0.
2. In a second DFS, propagate the costs. If we transition from parent $u$ to child $v$:
   - If the edge is directed $u \to v$ (correct direction when rooted at $u$), rooting at $v$ means this edge must point $v \to u$. Thus, cost increases by 1: $dp[v] = dp[u] + 1$.
   - If the edge is directed $v \to u$ (wrong direction when rooted at $u$), rooting at $v$ means this edge points $v \to u$ naturally. Thus, cost decreases by 1: $dp[v] = dp[u] - 1$.
3. Return the minimum DP value found.

```python
import sys
sys.setrecursionlimit(250000)

def getMinInversions(gNodes: int, gFrom: list[int], gTo: list[int]) -> int:
    adj = [[] for _ in range(gNodes)]
    # Edge format: (neighbor, direction)
    # direction = 1 if edge is u -> neighbor, 0 if edge is neighbor -> u
    for u, v in zip(gFrom, gTo):
        adj[u].append((v, 1))
        adj[v].append((u, 0))
        
    dp = [0] * gNodes
    
    # First DFS: compute cost for root = 0
    def dfs1(u, p):
        cost = 0
        for v, direct in adj[u]:
            if v != p:
                cost += (1 - direct) + dfs1(v, u)
        return cost
        
    dp[0] = dfs1(0, -1)
    
    # Second DFS: compute DP values using parent transitions
    def dfs2(u, p):
        for v, direct in adj[u]:
            if v != p:
                if direct == 1:
                    dp[v] = dp[u] + 1
                else:
                    dp[v] = dp[u] - 1
                dfs2(v, u)
                
    dfs2(0, -1)
    return min(dp)
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

---

### Q4. Minimum Energy

**Topic:** `Grid Search`, `BFS`, `Dijkstra`  

A grid represents a river where `'.'` is a path cell and `'#'` is an obstacle. Moving right or down consumes 0 energy. Moving left or up consumes 1 energy.
Find the minimum energy to travel from `(initial_x, initial_y)` to `(final_x, final_y)`. If it is impossible to reach the final coordinates, return `-1`.

#### Constraints
- $1 \le n, m \le 1000$
- Start and end cells are guaranteed to be `'.'`

#### Example
**river:**
```
.#.
.##
...
```
**initial_x, initial_y:** `2, 0`  
**final_x, final_y:** `0, 2`  
**Output:** `-1`  
**Explanation:**  
Due to the obstacles, it is impossible to reach `(0, 2)` from `(2, 0)`. Thus, return -1.

#### Solution Explanation
Since the edge weights are 0 and 1, we can use 0-1 BFS with a deque to find the shortest path in $O(N \times M)$ time:
- Maintain a deque. When we move to a cell with cost 0 (right/down), push it to the front of the deque.
- When we move with cost 1 (left/up), push it to the back.
- This ensures we always process nodes in increasing order of distance.

```python
from collections import deque

def minimumEnergy(river: list[str], initial_x: int, initial_y: int, final_x: int, final_y: int) -> int:
    n = len(river)
    m = len(river[0])
    
    dist = [[float('inf')] * m for _ in range(n)]
    dist[initial_x][initial_y] = 0
    
    q = deque([(initial_x, initial_y)])
    
    # Directions: (dr, dc, energy_cost)
    directions = [
        (0, 1, 0),   # Right (cost 0)
        (1, 0, 0),   # Down (cost 0)
        (0, -1, 1),  # Left (cost 1)
        (-1, 0, 1)   # Up (cost 1)
    ]
    
    while q:
        r, c = q.popleft()
        
        if r == final_x and c == final_y:
            return dist[r][c]
            
        for dr, dc, w in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and river[nr][nc] == '.':
                if dist[r][c] + w < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + w
                    if w == 0:
                        q.appendleft((nr, nc))
                    else:
                        q.append((nr, nc))
                        
    return -1
```

- **Time Complexity:** $O(N \times M)$
- **Space Complexity:** $O(N \times M)$

---

### Q5. Count Tree Paths

**Topic:** `Trees`, `Combinatorics`, `DFS`  

Given a tree of product dependencies represented as $N$ vertices. Determine the number of triplets of vertices $(i, j, k)$ such that $0 \le i < j < k < N$ and there is no simple path connecting them.
Due to the potentially large number of triplets, return the answer modulo $10^9 + 7$.

#### Constraints
- $1 \le N \le 10^5$
- Tree is represented by `treeFrom` and `treeTo` lists of size $N-1$.

#### Example
**treeNodes:** `5`  
**treeFrom:** `[0, 2, 2, 2]`  
**treeTo:** `[2, 1, 3, 4]`  
**Output:** `4`  
**Explanation:**  
The following 4 triplets lack a simple path connecting them:
- `(0, 1, 4)`
- `(0, 3, 4)`
- `(0, 1, 3)`
- `(1, 3, 4)`

#### Solution Explanation
A triplet of vertices $(i, j, k)$ lacks a simple path if and only if they branch out from a single junction vertex $x$.
For each vertex $x$, when $x$ is removed, the tree splits into several components of sizes $S_1, S_2, \dots, S_d$.
Any triplet chosen from three distinct components will have $x$ as their junction.
We can compute the number of such triplets for each vertex $x$ using Newton's sums for symmetric polynomials in $O(\text{degree}(x))$ time:
$$e_3 = \frac{p_1^3 - 3p_1p_2 + 2p_3}{6}$$
where $p_1 = \sum S_i$, $p_2 = \sum S_i^2$, and $p_3 = \sum S_i^3$.
We can perform a DFS to find the subtree sizes and parent component sizes, yielding an $O(N)$ solution.

```python
import sys
sys.setrecursionlimit(250000)

def countTreePaths(treeNodes: int, treeFrom: list[int], treeTo: list[int]) -> int:
    MOD = 10**9 + 7
    if treeNodes < 3:
        return 0
        
    adj = [[] for _ in range(treeNodes)]
    for u, v in zip(treeFrom, treeTo):
        adj[u].append(v)
        adj[v].append(u)
        
    subtree_size = [0] * treeNodes
    
    def get_sizes(u, p):
        sz = 1
        for v in adj[u]:
            if v != p:
                sz += get_sizes(v, u)
        subtree_size[u] = sz
        return sz
        
    get_sizes(0, -1)
    
    invalid_triplets = 0
    
    def dfs(u, p):
        nonlocal invalid_triplets
        comp_sizes = []
        for v in adj[u]:
            if v != p:
                comp_sizes.append(subtree_size[v])
        if u != 0:
            comp_sizes.append(treeNodes - subtree_size[u])
            
        p1 = sum(comp_sizes)
        p2 = sum(x**2 for x in comp_sizes)
        p3 = sum(x**3 for x in comp_sizes)
        
        e3 = (p1**3 - 3 * p1 * p2 + 2 * p3) // 6
        invalid_triplets = (invalid_triplets + e3) % MOD
        
        for v in adj[u]:
            if v != p:
                dfs(v, u)
                
    dfs(0, -1)
    return invalid_triplets % MOD
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

---

### Q6. Get Cluster Sizes

**Topic:** `DSU`, `GCD`, `Factorization`  

Given an array `serverProp` of size $N$, representing properties of servers. Two servers $i$ and $j$ are connected if $\gcd(serverProp[i], serverProp[j]) > 1$.
Find the size of the cluster (connected component) for each server.

#### Constraints
- $1 \le N \le 10^5$
- $1 \le serverProp[i] \le 10^6$

#### Example
**serverProp:** `[12, 15, 35]`  
**Output:** `[3, 3, 3]`  
**Explanation:**  
- $\gcd(12, 15) = 3 > 1$, so servers 0 and 1 are connected.
- $\gcd(15, 35) = 5 > 1$, so servers 1 and 2 are connected.
- Thus, all three servers are in the same cluster. Size of the cluster is 3.

#### Solution Explanation
We can use a Disjoint Set Union (DSU) to connect prime factors and servers:
1. For each server, factorize its property value into prime factors.
2. Maintain a map/array `prime_to_server` which records the first server index containing that prime factor.
3. For each prime factor $p$ of `serverProp[i]`, union $i$ with `prime_to_server[p]`.
4. Find component sizes in the DSU and map each server to its component size.

```python
def getClusterSizes(serverProp: list[int]) -> list[int]:
    n = len(serverProp)
    max_val = max(serverProp) if n > 0 else 0
    
    # Precompute smallest prime factor (SPF) sieve
    spf = list(range(max_val + 1))
    for i in range(2, int(max_val**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_val + 1, i):
                if spf[j] == j:
                      spf[j] = i
                      
    parent = list(range(n))
    size = [1] * n
    
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            
    prime_to_server = {}
    for i in range(n):
        val = serverProp[i]
        factors = set()
        while val > 1:
            p = spf[val]
            factors.add(p)
            val //= p
            
        for p in factors:
            if p in prime_to_server:
                union(i, prime_to_server[p])
            else:
                prime_to_server[p] = i
                
    return [size[find(i)] for i in range(n)]
```

- **Time Complexity:** $O(N \log(\max A) + \max A \log \log \max A)$ where $\max A \le 10^6$.
- **Space Complexity:** $O(N + \max A)$

---

### Q7. Get Greatest Elements

**Topic:** `Prefix Order Statistics`, `Binary Indexed Tree`, `Segment Tree`  

Given a permutation array `arr` of $N$ integers from 1 to $N$. Find the $k$-th greatest element for each prefix of length $i$, where $i$ ranges from $k$ to $N$.

#### Constraints
- $1 \le N \le 2 \times 10^5$
- $1 \le k \le N$
- `arr` is a permutation of $1$ to $N$.

#### Example
**arr:** `[4, 2, 1, 3]`  
**k:** `2`  
**Output:** `[2, 2, 3]`  
**Explanation:**  
- Prefix of length 2: `[4, 2]` -> sorted descending: `[4, 2]` -> 2nd greatest is 2.
- Prefix of length 3: `[4, 2, 1]` -> sorted descending: `[4, 2, 1]` -> 2nd greatest is 2.
- Prefix of length 4: `[4, 2, 1, 3]` -> sorted descending: `[4, 3, 2, 1]` -> 2nd greatest is 3.

#### Solution Explanation
We can insert elements one-by-one into a Fenwick tree (Binary Indexed Tree) representing the frequencies of the seen values.
Finding the $k$-th greatest element in a prefix of size $S$ is equivalent to finding the value $x$ such that there are exactly $k$ elements $\ge x$.
Since the elements are values up to $N$, we can perform binary lifting directly on the BIT in $O(\log N)$ time per prefix, yielding an $O(N \log N)$ total time solution.

```python
def getGreatestElements(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    bit = [0] * (n + 1)
    
    def update(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)
            
    def find_kth_greatest(total_elements):
        target = total_elements - k
        idx = 0
        current_sum = 0
        h = 1 << (n.bit_length() - 1)
        while h > 0:
            if idx + h <= n and current_sum + bit[idx + h] <= target:
                idx += h
                current_sum += bit[idx]
            h >>= 1
        return idx + 1
        
    result = []
    for i in range(n):
        update(arr[i], 1)
        if i + 1 >= k:
            result.append(find_kth_greatest(i + 1))
            
    return result
```

- **Time Complexity:** $O(N \log N)$
- **Space Complexity:** $O(N)$

---

### Q8. Choose Flask

**Topic:** `Binary Search`, `Greedy`  

A lab needs to choose a flask type that minimizes total waste.
Given `requirements` (a list of $N$ requirement values) and `markings` (a list of lists containing markings for different flask types).
Each flask type has a set of markings. If we choose a flask type, for each requirement $r$, we must use the smallest marking $m$ of that flask type such that $m \ge r$. The waste is $m - r$. If a flask type cannot satisfy all requirements (i.e., some requirement is strictly larger than the maximum marking of that flask type), it is invalid.
Find the flask type index (0-based) that minimizes the total waste. If there is a tie, return the smallest index. If no flask type can satisfy all requirements, return -1.

#### Constraints
- $1 \le N \le 10^5$
- $1 \le flaskTypes \le 10^4$
- Total number of markings $\le 10^5$

#### Solution Explanation
1. Sort the `requirements` array and calculate its prefix sums.
2. For each flask type, check if its maximum marking is $\ge$ the maximum requirement. If not, mark it invalid.
3. For each marking $m$ of this flask, find the range of requirements it satisfies using binary search (`bisect_right`).
4. Using the prefix sums of the requirements, compute the total waste for the flask type in $O(M \log N)$ total time.

```python
import bisect

def chooseFlask(requirements: list[int], flaskTypes: int, markings: list[list[int]]) -> int:
    requirements.sort()
    n = len(requirements)
    
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + requirements[i]
        
    flask_markings = [[] for _ in range(flaskTypes)]
    for type_idx, mark in markings:
        flask_markings[type_idx].append(mark)
        
    best_flask = -1
    min_waste = float('inf')
    
    for i in range(flaskTypes):
        marks = flask_markings[i]
        if not marks or marks[-1] < requirements[-1]:
            continue
            
        current_waste = 0
        prev_req_idx = 0
        possible = True
        
        for mark in marks:
            req_idx = bisect.bisect_right(requirements, mark)
            if req_idx > prev_req_idx:
                count = req_idx - prev_req_idx
                sum_reqs = pref[req_idx] - pref[prev_req_idx]
                current_waste += mark * count - sum_reqs
                prev_req_idx = req_idx
                
        if prev_req_idx < n:
            possible = False
            
        if possible and current_waste < min_waste:
            min_waste = current_waste
            best_flask = i
            
    return best_flask
```

- **Time Complexity:** $O(M \log N + N \log N)$ where $M$ is the total number of markings.
- **Space Complexity:** $O(N)$

---

### Q9. Collect Max

**Topic:** `Dynamic Programming`, `Grid Path`  

A driver starts at `(0, 0)` in an $n \times n$ matrix, travels to `(n-1, n-1)` moving only right or down, and then travels back to `(0, 0)` moving only left or up.
Each cell has:
- `0`: empty path
- `1`: contains a rider (can be collected once, cell becomes 0)
- `-1`: blocked/obstacle
Find the maximum number of riders that can be collected. If there is no valid path, return 0.

#### Constraints
- $1 \le n \le 100$
- $-1 \le mat[i][j] \le 1$

#### Example
**mat:**
```
0 1 -1
1 0 -1
1 1 1
```
**Output:** `5`  
**Explanation:**  
The optimal path is: `(0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2)` (collects 3 riders) and then back `(2,2) -> (2,1) -> (2,0) -> (1,0) -> (0,0)` (collects 2 more riders). Total = 5.

#### Solution Explanation
This is equivalent to finding two paths starting at `(0, 0)` and moving to `(n-1, n-1)` simultaneously.
Let $t$ be the step count. $t = x_1 + y_1 = x_2 + y_2$.
We define $dp[t][x_1][x_2]$ as the maximum riders collected.
- Transition: both paths can move right or down.
- If $x_1 == x_2$, both paths are at the same cell, so the rider is collected once.
- Else, we collect from both cells.
We can optimize the space to $O(N^2)$ by only keeping the DP values of the previous step.

```python
def collectMax(mat: list[list[int]]) -> int:
    n = len(mat)
    if not mat or mat[0][0] == -1 or mat[n - 1][n - 1] == -1:
        return 0
        
    dp = [[-1] * n for _ in range(n)]
    dp[0][0] = mat[0][0]
    
    for t in range(1, 2 * n - 1):
        next_dp = [[-1] * n for _ in range(n)]
        
        for x1 in range(max(0, t - n + 1), min(n, t + 1)):
            for x2 in range(max(0, t - n + 1), min(n, t + 1)):
                y1 = t - x1
                y2 = t - x2
                
                if mat[x1][y1] == -1 or mat[x2][y2] == -1:
                    continue
                    
                prev_max = -1
                for px1 in (x1 - 1, x1):
                    for px2 in (x2 - 1, x2):
                        if px1 >= 0 and px2 >= 0:
                            prev_max = max(prev_max, dp[px1][px2])
                            
                if prev_max == -1:
                    continue
                    
                riders = mat[x1][y1]
                if x1 != x2:
                    riders += mat[x2][y2]
                    
                next_dp[x1][x2] = prev_max + riders
                
        dp = next_dp
        
    return max(0, dp[n - 1][n - 1])
```

- **Time Complexity:** $O(N^3)$
- **Space Complexity:** $O(N^2)$

---

### Q10. Find Min Changes

**Topic:** `Functional Graph`, `Union-Find`  

A scheduling app has $N$ tasks. Each task $i$ has exactly one dependency `taskDependency[i]`.
Minimize the number of changes to the dependency structure to ensure that all tasks have a clear and valid execution order.
A valid dependency structure consists of a single connected component that is a tree directed towards a single self-loop.

#### Constraints
- $1 \le N \le 2 \times 10^5$
- $1 \le taskDependency[i] \le N$

#### Example
**taskDependency:** `[2, 3, 3, 4]`  
**Output:** `1`  
**Explanation:**  
We have self-loops at task 3 and task 4. Changing task 4's dependency to 1 (`taskDependency = [2, 3, 3, 1]`) creates a single component rooted at the self-loop 3. Total changes = 1.

#### Solution Explanation
The dependency graph is a functional graph where each vertex has out-degree 1.
Let $C$ be the total number of connected components in the undirected representation.
Let $S$ be the number of self-loops.
- If $S > 0$: we keep one self-loop as the root. For the remaining $C-1$ components, we change their cycles to point to the root. Total changes = $C - 1$.
- If $S = 0$: we must create one self-loop (1 change), and point the remaining $C-1$ components to it ($C-1$ changes). Total changes = $C$.
We can count components using DSU and count self-loops in $O(N)$ time.

```python
def findMinChanges(taskDependency: list[int]) -> int:
    n = len(taskDependency)
    parent = list(range(n + 1))
    
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i
            
    for i in range(1, n + 1):
        union(i, taskDependency[i - 1])
        
    roots = set(find(i) for i in range(1, n + 1))
    c = len(roots)
    
    s = sum(1 for i in range(1, n + 1) if taskDependency[i - 1] == i)
    
    return c - 1 if s > 0 else c
```

- **Time Complexity:** $O(N \alpha(N))$
- **Space Complexity:** $O(N)$

---

### Q11. Get Maximum Efficiency

**Topic:** `Trees`, `Dynamic Programming`, `DFS`  

Given a tree of $N$ nodes rooted at node 1. Each node $u$ has a value `computer_val[u]`.
In one operation, we can delete the subtree of any node $u$ (removing $u$ and all its descendants) with a cost of $k$.
The efficiency of the tree after $num\_ops$ operations is:
$$(\text{sum of values of remaining nodes}) - k \times num\_ops$$
Find the maximum possible efficiency.

#### Constraints
- $2 \le N \le 10^5$
- $|computer\_val[i]| \le 10^9$
- $1 \le k \le 10^9$

#### Example
**connect_nodes:** `3`  
**connect_from:** `[1, 3]`  
**connect_to:** `[2, 2]`  
**computer_val:** `[9, -1, 3]`  
**k:** `3`  
**Output:** `11`  
**Explanation:**  
If we perform no operations, the total value is $9 - 1 + 3 = 11$. If we delete the subtree of node 2, we remove nodes {2, 3} at cost 3, leaving only node 1 (efficiency = $9 - 3 = 6$). The maximum efficiency is 11.

#### Solution Explanation
Let $dp[u]$ be the maximum efficiency obtained from the subtree of $u$.
- If we delete the subtree of $u$, the net contribution is $-k$.
- If we keep $u$, the contribution is `computer_val[u]` plus the optimal contributions from all of its children.
Thus, $dp[u] = \max\left(-k, \text{computer\_val}[u] + \sum_{v \in \text{children}(u)} dp[v]\right)$.
We can solve this in a single post-order traversal (DFS).

```python
import sys
sys.setrecursionlimit(250000)

def getMaximumEfficiency(connect_nodes: int, connect_from: list[int], connect_to: list[int], computer_val: list[int], k: int) -> int:
    adj = [[] for _ in range(connect_nodes + 1)]
    for u, v in zip(connect_from, connect_to):
        adj[u].append(v)
        adj[v].append(u)
        
    dp = [0] * (connect_nodes + 1)
    
    def dfs(u, p):
        val = computer_val[u - 1]
        child_sum = 0
        for v in adj[u]:
            if v != p:
                dfs(v, u)
                child_sum += dp[v]
        dp[u] = max(-k, val + child_sum)
        
    dfs(1, -1)
    return dp[1]
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

---

### Q12. Get Maximum XOR Sum

**Topic:** `Bit Manipulation`, `Math`  

Given two arrays `arr1` and `arr2` of size $N$, a matrix `mat` of size $N \times N$ is derived where $mat[i][j] = arr1[i] \oplus arr2[j]$.
Find the sum of all elements in `mat` modulo $10^9 + 7$.

#### Constraints
- $1 \le N \le 10^5$
- $1 \le arr1[i], arr2[i] \le 10^9$

#### Example
**arr1:** `[1, 2, 3, 4]`  
**arr2:** `[1, 2, 3, 4]`  
**Output:** `48`  

#### Solution Explanation
We can compute the sum bit-by-bit.
For the $b$-th bit position:
- Let $cnt1$ be the number of elements in `arr1` with the $b$-th bit set.
- Let $cnt2$ be the number of elements in `arr2` with the $b$-th bit set.
- The number of pairs $(i, j)$ where the $b$-th bit is 1 in $arr1[i] \oplus arr2[j]$ is:
  $$\text{pairs} = cnt1 \times (N - cnt2) + (N - cnt1) \times cnt2$$
- Add $\text{pairs} \times 2^b \pmod{10^9 + 7}$ to the total sum.

```python
def getMaximumXorSum(arr1: list[int], arr2: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(arr1)
    total_sum = 0
    
    for b in range(30):
        cnt1 = sum((x >> b) & 1 for x in arr1)
        cnt2 = sum((x >> b) & 1 for x in arr2)
        
        pairs = (cnt1 * (n - cnt2) + (n - cnt1) * cnt2) % MOD
        contrib = (pairs * (1 << b)) % MOD
        total_sum = (total_sum + contrib) % MOD
        
    return total_sum
```

- **Time Complexity:** $O(N \log(\max A))$
- **Space Complexity:** $O(1)$

---

### Q13. Min Operations (Circular Locks)

**Topic:** `Circular Distance`, `Median`, `Prefix Sums`  

Given a circular ring of size $k$ with positions labeled 1 to $k$. We have $N$ locks with initial positions given by the array `locks`.
We can increment or decrement any lock's position with cost 1 (with wrap-around between 1 and $k$).
Find the minimum operations to make all locks have the same position.

#### Constraints
- $2 \le k \le 10^9$
- $1 \le N \le 10^5$
- $1 \le locks[i] \le k$

#### Example
**k:** `100`  
**locks:** `[1, 2, 98]`  
**Output:** `4`  
**Explanation:**  
The optimal target position is 1:
- Lock at 1 needs 0 ops.
- Lock at 2 needs 1 op: `2 -> 1`
- Lock at 98 needs 3 ops: `98 -> 99 -> 100 -> 1`
Total operations = 0 + 1 + 3 = 4.

#### Solution Explanation
This is the 1-median problem on a circle. The optimal target position $Y$ will always be one of the initial lock positions.
We sort the unique lock positions $a_1, a_2, \dots, a_n$.
We duplicate and extend the array to size $2n$ by setting $a_{i+n} = a_i + k$.
For a target position $a_j$:
- The locks that are within distance $k/2$ going clockwise from $a_j$ are those $a_i$ with $a_i - a_j \le k/2$. Let the number of such locks be $m$ (so they are at indices $j, \dots, j+m-1$).
- The remaining $n - m$ locks are closer to $a_j$ going counter-clockwise (distance is $a_j + k - a_i$).
Using prefix sums of the extended array and a two-pointer approach to maintain the boundary $j+m$, we can compute the sum of distances for all candidate targets $a_j$ in $O(N)$ time.

```python
def minOperations(k: int, locks: list[int]) -> int:
    locks.sort()
    n = len(locks)
    
    A = [0] * (2 * n)
    for i in range(n):
        A[i] = locks[i]
        A[i + n] = locks[i] + k
        
    pref = [0] * (2 * n + 1)
    for i in range(2 * n):
        pref[i + 1] = pref[i] + A[i]
        
    min_total_ops = float('inf')
    half_k = k // 2
    boundary = 0
    
    for j in range(n):
        while boundary < j + n and A[boundary] - A[j] <= half_k:
            boundary += 1
            
        m = boundary - j
        sum_first = (pref[j + m] - pref[j]) - m * A[j]
        sum_second = (n - m) * (A[j] + k) - (pref[j + n] - pref[j + m])
        
        total_ops = sum_first + sum_second
        if total_ops < min_total_ops:
            min_total_ops = total_ops
            
    return min_total_ops
```

- **Time Complexity:** $O(N \log N)$
- **Space Complexity:** $O(N)$

---

### Q14. Shift Stones in Boxes

**Topic:** `Dynamic Programming`, `Knapsack`, `Greedy`  

There are $N$ boxes. The $i$-th box contains $A[i]$ stones and has a capacity of $B[i]$ stones ($A[i] \le B[i]$).
We want to shift the stones to a minimum number of boxes. Moving one stone from one box to another takes 1 unit of time.
Find the minimum number of boxes required, and the minimum time to shift the stones to those boxes.

#### Constraints
- $1 \le N \le 100$
- $A[i] \le B[i] \le 100$

#### Example
**A:** `[1, 2]`  
**B:** `[2, 3]`  
**Output:** `[1, 1]`  
**Explanation:**  
Total stones = 3. Sorting by capacity descending, the box with capacity 3 can hold all 3 stones. Thus, minimum boxes required = 1.
We keep 2 stones in box 1 (since $A[1]=2 \le 3$), and move 1 stone from box 0 to box 1 (takes 1 unit of time). Total time = 1.

#### Solution Explanation
1. Sort the capacities $B$ in descending order. The minimum number of boxes $k$ is the smallest index such that the sum of the top $k$ capacities is $\ge S$ (where $S = \sum A[i]$ is the total number of stones).
2. To minimize the number of stones shifted, we want to maximize the number of stones already in the chosen $k$ boxes. If we choose a subset $P$ of $k$ boxes, the number of stones we can keep without moving is $\sum_{i \in P} A[i]$.
3. So we want to find a subset $P$ of $k$ boxes such that $\sum_{i \in P} B[i] \ge S$, maximizing $\sum_{i \in P} A[i]$.
This is a standard 0/1 Knapsack DP:
Let $dp[i][j]$ be the maximum sum of $A$ we can get choosing exactly $i$ boxes with a total capacity of $j$.
- $dp[i][j] = \max(dp[i][j], dp[i-1][j - B[m]] + A[m])$
After filling the DP table, the minimum time is $S - \max_{j \ge S} dp[k][j]$.

```python
def shiftStones(A: list[int], B: list[int]) -> list[int]:
    n = len(A)
    total_stones = sum(A)
    
    boxes = sorted(zip(B, A), key=lambda x: x[0], reverse=True)
    
    k = 0
    capacity_sum = 0
    for cap, stones in boxes:
        capacity_sum += cap
        k += 1
        if capacity_sum >= total_stones:
            break
            
    max_capacity = sum(B)
    dp = [[-1] * (max_capacity + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    
    for cap, stones in boxes:
        for i in range(k, 0, -1):
            for j in range(max_capacity, cap - 1, -1):
                if dp[i - 1][j - cap] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - cap] + stones)
                    
    max_stones_kept = 0
    for j in range(total_stones, max_capacity + 1):
        max_stones_kept = max(max_stones_kept, dp[k][j])
        
    min_time = total_stones - max_stones_kept
    return [k, min_time]
```

- **Time Complexity:** $O(N \cdot k \cdot \sum B[i])$
- **Space Complexity:** $O(k \cdot \sum B[i])$
