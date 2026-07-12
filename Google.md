# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Google*
*Total questions: 7*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. First Subsequence

**Topic:** `Strings`, `Two Pointers`, `Binary Search`, `Greedy`  

Given string $A$ and string $B$. Find the first 1-based index in $A$ where $B$ occurs as a subsequence, allowing at most 1 character change in $B$ (excluding the first character of $B$, which cannot be changed). If not found, return `-1`.

#### Example
- **Input:** $A = \text{"abcdef"}$, $B = \text{"bxf"}$
- **Output:** `2` (subsequence starts with `b` at index 2, with `x` matched to `d` as a mismatch).

#### Solution Explanation
To find the first starting index in $A$ where $B$ occurs as a subsequence with at most 1 mismatch (excluding the first character), we can precompute the occurrences of each character in $A$. For each character, we maintain a list of sorted indices where it appears.

We iterate through all possible starting indices $i$ in $A$ where $A[i] == B[0]$. For each such starting index, we check if we can match the rest of $B$ ($B[1:]$) as a subsequence of $A[i+1:]$ with at most 1 mismatch. We use dynamic programming:
- Let $pos[0]$ be the earliest index in $A$ that matches the prefix of $B[1:]$ with 0 mismatches.
- Let $pos[1]$ be the earliest index in $A$ that matches the prefix of $B[1:]$ with at most 1 mismatch.

For each character $B[j]$ of $B$ (from $1$ to $|B|-1$):
- The new $pos[0]$ is the next occurrence of $B[j]$ after the old $pos[0]$.
- The new $pos[1]$ is the minimum of:
  - The next occurrence of $B[j]$ after the old $pos[1]$ (mismatch already used).
  - The old $pos[0] + 1$ (mismatch used on $B[j]$).

If both $pos[0]$ and $pos[1]$ become invalid, then this starting index $i$ is invalid. As soon as we find a valid starting index $i$, we return $i + 1$ (1-based index). If no index is valid, we return $-1$.

```python
import bisect

def firstSubsequence(A: str, B: str) -> int:
    n, m = len(A), len(B)
    if m == 0:
        return 1
    
    # Store indices of each character in A
    char_indices = {}
    for idx, char in enumerate(A):
        if char not in char_indices:
            char_indices[char] = []
        char_indices[char].append(idx)
        
    def get_next_occurrence(char, start_idx):
        if char not in char_indices:
            return float('inf')
        lst = char_indices[char]
        pos = bisect.bisect_left(lst, start_idx)
        if pos < len(lst):
            return lst[pos]
        return float('inf')
        
    # We only need to check starting indices where A[i] == B[0]
    if B[0] not in char_indices:
        return -1
        
    for start_i in char_indices[B[0]]:
        # pos0: best index matching prefix of B[1:] with 0 mismatches
        # pos1: best index matching prefix of B[1:] with 1 mismatch
        pos0 = start_i
        pos1 = start_i
        
        possible = True
        for j in range(1, m):
            next_pos0 = get_next_occurrence(B[j], pos0 + 1)
            
            # For pos1, we can either:
            # 1. Use the next occurrence of B[j] after pos1 (mismatch already used)
            # 2. Use pos0 + 1 (using the mismatch on B[j])
            next_pos1 = min(get_next_occurrence(B[j], pos1 + 1), pos0 + 1)
            
            pos0 = next_pos0
            pos1 = next_pos1
            
            if pos0 == float('inf') and pos1 == float('inf'):
                possible = False
                break
                
        if possible and pos1 < n:
            return start_i + 1 # 1-based index
            
    return -1
```

- **Time Complexity:** $O(|A| + C \cdot |B| \log |A|)$, where $C$ is the number of occurrences of $B[0]$ in $A$. In the worst case, $O(|A| \cdot |B| \log |A|)$, but with fast $O(1)$ DP transitions and early termination, it runs extremely fast in practice.
- **Space Complexity:** $O(|A|)$ to store character occurrences.

---

### Q2. Maximum Length Subarray

**Topic:** `Arrays`, `Sliding Window`, `Two Pointers`, `Heaps`  

Given array $A$ of size $N$, maximum decrement operations $X$ (Type 1: $A[i] = A[i] - 1$), and maximum zero-replacement operations $Y$ (Type 2: $A[i] = 0$). Find the maximum length of a contiguous subarray consisting entirely of zeros.

#### Example
- **Input:** $N = 6, X = 4, Y = 2$, $A = [4, 2, 1, 3, 2, 5]$
- **Output:** `4` (Subarray $A[1 \dots 4] = [4, 2, 1, 3]$ can be turned to $[0, 0, 0, 0]$ by using 2 replacement operations on $4$ and $3$, and 3 decrement operations on $2$ and $1$).

#### Solution Explanation
For a subarray $A[L \dots R]$, to make all elements zero, we can:
1. Replace up to $Y$ elements with 0 (using Type 2 operations). We should choose the $Y$ largest elements in the subarray to replace with 0.
2. For the remaining elements in the subarray, we must decrement them to 0 using Type 1 operations. The cost is the sum of these remaining elements.

We want this remaining sum to be $\le X$. Since all elements are non-negative, the validity of a window is monotonic. We can use a sliding window (two pointers) approach. We maintain a window $A[L \dots R]$. As we expand $R$, we add $A[R]$ to our window. If the window becomes invalid, we increment $L$ until the window becomes valid again.
To check validity, we maintain the $Y$ largest elements in a min-heap `large` and the remaining elements in a max-heap `small` using lazy deletion for elements that fall out of the window.

```python
import heapq

def longestSubarray(N: int, X: int, Y: int, A: list[int]) -> int:
    L = 0
    max_len = 0
    
    large = []  # min-heap of (val, idx)
    small = []  # max-heap of (-val, idx)
    
    sum_small = 0
    large_size = 0  # number of active elements in large
    in_large = [False] * N
    
    def clean_large():
        nonlocal large_size
        while large and large[0][1] < L:
            heapq.heappop(large)
    
    def clean_small():
        while small and small[0][1] < L:
            heapq.heappop(small)
            
    def balance():
        nonlocal sum_small, large_size
        # Move elements from small to large if large is not full
        while large_size < Y:
            clean_small()
            if not small:
                break
            val, idx = heapq.heappop(small)
            val = -val
            heapq.heappush(large, (val, idx))
            in_large[idx] = True
            sum_small -= val
            large_size += 1
            
        # Check if the largest in small is larger than the smallest in large
        while True:
            clean_large()
            clean_small()
            if not small or not large:
                break
            if -small[0][0] > large[0][0]:
                s_val, s_idx = heapq.heappop(small)
                s_val = -s_val
                l_val, l_idx = heapq.heappop(large)
                
                heapq.heappush(large, (s_val, s_idx))
                in_large[s_idx] = True
                
                heapq.heappush(small, (-l_val, l_idx))
                in_large[l_idx] = False
                
                sum_small += s_val - l_val
            else:
                break

    for R in range(N):
        heapq.heappush(small, (-A[R], R))
        in_large[R] = False
        sum_small += A[R]
        
        balance()
        
        while sum_small > X:
            if in_large[L]:
                large_size -= 1
            else:
                sum_small -= A[L]
            L += 1
            balance()
            
        max_len = max(max_len, R - L + 1)
        
    return max_len
```

- **Time Complexity:** $O(N \log N)$ as each element is pushed and popped from the heaps at most a constant number of times.
- **Space Complexity:** $O(N)$ to store heap states and window memberships.

---

### Q3. Subtree XOR

**Topic:** `Trees`, `DFS`, `Bitwise Operations`, `Dynamic Programming`  

Given a tree with $N$ nodes, node values $A$, and an integer $K$. You can perform the following operation on the tree at most once:
- Pick a node $r$ and make it the root of the tree.
- In the new tree, pick a node $x$, and for each node in the subtree of $x$, update $A_{\text{node}} = A_{\text{node}} \oplus K$.

Determine the maximum sum of values of all nodes in the tree that can be obtained.

#### Example
- **Input:** $N = 3$, $K = 3$, $A = [1, 1, 3]$, $\text{edges} = [[1, 2], [1, 3]]$
- **Output:** `7` (Root the tree at $r = 3$, and select subtree of $x = 1$. The subtree of $1$ contains nodes $1$ and $2$. Their values become $1 \oplus 3 = 2$, and the tree values become $[2, 2, 3]$. Sum = 7).

#### Solution Explanation
Choosing a root $r$ and selecting a node $x$ divides the tree into two connected components by removing the edge between $x$ and its parent (if $x \neq r$), and we XOR the component containing $x$. If $x = r$, we XOR the entire tree.
Thus, the set of nodes we can XOR is exactly:
1. The empty set (no operation).
2. The entire tree.
3. For each edge $(u, v)$, either of the two connected components obtained by removing $(u, v)$.

We can solve this in $O(N)$ time by rooting the tree arbitrarily (say, at node 1).
For each node $u \neq 1$, let $T_u$ be its subtree in this rooted tree. The two components formed by removing the edge between $u$ and its parent are $T_u$ and $T \setminus T_u$.
Let $diff[i] = (A[i] \oplus K) - A[i]$ be the change in value of node $i$ if it is XORed.
We can compute the sum of $diff[i]$ for all $i \in T_u$ using a post-order DFS. Let this be $subtree\_diff[u]$.
The sum of $diff[i]$ for the entire tree is $total\_diff$.

Then the possible changes in the total sum of the tree are:
- $0$ (no operation)
- $total\_diff$ (XOR the entire tree)
- $subtree\_diff[u]$ (XOR $T_u$)
- $total\_diff - subtree\_diff[u]$ (XOR $T \setminus T_u$)

We take the maximum of these changes and add it to the original sum of $A$.

```python
def maximumSum(N: int, edges: list[list[int]], A: list[int], K: int) -> int:
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    parent = [0] * (N + 1)
    visited = [False] * (N + 1)
    
    # BFS to orient the tree and get post-order traversal order
    queue = [1]
    visited[1] = True
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                
    post_order = queue[::-1]
    
    # diff[i] is the change in value for node i
    diff = [0] + [(val ^ K) - val for val in A]
    subtree_diff = list(diff)
    
    # Accumulate subtree differences
    for u in post_order:
        p = parent[u]
        if p != 0:
            subtree_diff[p] += subtree_diff[u]
            
    total_diff = subtree_diff[1]
    max_change = 0
    max_change = max(max_change, total_diff)
    
    for u in range(2, N + 1):
        # Option 1: XOR subtree of u
        max_change = max(max_change, subtree_diff[u])
        # Option 2: XOR tree excluding subtree of u
        max_change = max(max_change, total_diff - subtree_diff[u])
        
    return sum(A) + max_change
```

- **Time Complexity:** $O(N)$ to orient the tree and compute subtree sums.
- **Space Complexity:** $O(N)$ for adjacency list and traversal structures.

---

### Q4. Find Palindromes

**Topic:** `Trees`, `DFS`, `String Hashing`, `Palindromes`  

Given a tree with $N$ nodes, rooted at node 1. Every node has a character $C[i]$ assigned to it.
Post-order traversal (where children of a node are traversed in increasing order of their node numbers) generates a string $S_u$ for node $u$.
Answer $Q$ queries: is $S_u$ palindromic?

#### Example
- **Input:** $N = 5$, $C = [a, b, a, b, c]$, $\text{edges} = [[1, 2], [1, 3], [2, 4], [2, 5]]$, $Q = 2$, $\text{queries} = [1, 2]$
- **Output:** `0 1` (For node 1, $S_1 = \text{"bcbaa"}$ (not palindromic); for node 2, $S_2 = \text{"bcb"}$ (palindromic)).

#### Solution Explanation
The post-order traversal of the subtree of any node $u$ is always a contiguous substring of the post-order traversal of the entire tree.
Specifically:
- We perform a post-order traversal of the entire tree, visiting children in increasing order of node numbers.
- Let `P_str` be the string generated by this traversal.
- The substring corresponding to the subtree of $u$ ends at the position of $u$ in `P_str`, and its length is equal to the size of the subtree of $u$.
- We can check if a substring of `P_str` is a palindrome in $O(1)$ time using rolling hashes of `P_str` and its reverse `P_str[::-1]`.
We use double hashing to prevent collisions.

```python
class StringHasher:
    def __init__(self, s, base=313, mod=1000000007):
        self.base = base
        self.mod = mod
        n = len(s)
        self.pref = [0] * (n + 1)
        self.power = [1] * (n + 1)
        for i in range(n):
            self.pref[i+1] = (self.pref[i] * base + ord(s[i])) % mod
            self.power[i+1] = (self.power[i] * base) % mod
            
    def get_hash(self, l, r):
        val = (self.pref[r+1] - self.pref[l] * self.power[r-l+1]) % self.mod
        return val if val >= 0 else val + self.mod

def solvePalindromes(N: int, edges: list[list[int]], C: str, Q: int, queries: list[int]) -> list[int]:
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    children = [[] for _ in range(N + 1)]
    parent = [0] * (N + 1)
    visited = [False] * (N + 1)
    
    queue = [1]
    visited[1] = True
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
                
    for u in range(1, N + 1):
        children[u].sort()
        
    post_order = []
    stack = [[1, 0]]
    while stack:
        u, idx = stack[-1]
        if idx < len(children[u]):
            stack[-1][1] += 1
            v = children[u][idx]
            stack.append([v, 0])
        else:
            post_order.append(u)
            stack.pop()
            
    size = [1] * (N + 1)
    for u in post_order:
        p = parent[u]
        if p != 0:
            size[p] += size[u]
            
    P_str = "".join(C[u-1] for u in post_order)
    P_str_rev = P_str[::-1]
    
    hasher1 = StringHasher(P_str, 313, 1000000007)
    hasher2 = StringHasher(P_str, 317, 1000000009)
    rev_hasher1 = StringHasher(P_str_rev, 313, 1000000007)
    rev_hasher2 = StringHasher(P_str_rev, 317, 1000000009)
    
    pos_in_post = [0] * (N + 1)
    for idx, u in enumerate(post_order):
        pos_in_post[u] = idx
        
    ans = []
    for u in queries:
        r = pos_in_post[u]
        l = r - size[u] + 1
        
        h1 = hasher1.get_hash(l, r)
        h2 = hasher2.get_hash(l, r)
        
        rev_l = N - 1 - r
        rev_r = N - 1 - l
        
        rh1 = rev_hasher1.get_hash(rev_l, rev_r)
        rh2 = rev_hasher2.get_hash(rev_l, rev_r)
        
        if h1 == rh1 and h2 == rh2:
            ans.append(1)
        else:
            ans.append(0)
            
    return ans
```

- **Time Complexity:** $O(N \log N + Q)$ for sorting children and building the hashes, followed by $O(1)$ query evaluation.
- **Space Complexity:** $O(N)$ to store post-order structures and hash tables.

---

### Q5. Complex Subsequences

**Topic:** `Arrays`, `Sweep-line`, `Dynamic Programming`, `Coordinate Compression`  

You have an array of infinite length with all elements 0. You are given $N$ updates of the form $(L, R, X)$, which adds $X$ to every element from index $L$ to $R$ (inclusive).
We want to find a maximum length subsequence of positive elements of the form $Z, Z+K, Z+2K, \dots$ for some positive $Z$. If there are multiple such subsequences of maximum length, we want the one that is lexicographically smallest.

Output the length $L$ and the values of the subsequence.

#### Example
- **Input:** $N = 4, K = 2$, $\text{updates} = [[1, 3, 1], [2, 4, 2], [5, 6, 3], [5, 5, 1]]$
- **Output:** `2 1 3` (The positive subarray is $[1, 3, 3, 2, 4, 3]$. The possible subsequences of difference 2 are $[1, 3]$ and $[2, 4]$. $[1, 3]$ is lexicographically smaller).

#### Solution Explanation
1. Since the updates can have coordinates up to $10^9$, we use a coordinate sweep-line to partition the active part of the array into disjoint intervals of constant value.
2. Each constant-value interval can contribute at most one element to the subsequence (since the subsequence values are strictly increasing).
3. This gives us a sequence of interval values $A = [v_1, v_2, \dots, v_m]$.
4. We want to find the longest subsequence of $A$ of the form $Z, Z+K, \dots$. We can solve this with dynamic programming.
   Let `dp[v] = (length, -start_val)` be the best state ending at value $v$.
   For each element $v$ in $A$:
   - If $v - K > 0$ and $v - K$ in $dp$, we can transition to `(dp[v-K][0] + 1, dp[v-K][1])`.
   - Otherwise, we start a new subsequence: `(1, -v)`.
   We update `dp[v] = max(dp[v], new_state)` to maximize the length, and minimize the starting value $Z$.

```python
def longestSubsequence(N: int, K: int, queries: list[list[int]]) -> list[int]:
    events = []
    for L, R, X in queries:
        events.append((L, X))
        events.append((R + 1, -X))
        
    events.sort()
    
    A = []
    curr_val = 0
    prev_x = -1
    
    i = 0
    while i < len(events):
        x = events[i][0]
        if prev_x != -1 and curr_val > 0 and x > prev_x:
            A.append(curr_val)
            
        while i < len(events) and events[i][0] == x:
            curr_val += events[i][1]
            i += 1
        prev_x = x
        
    dp = {}
    max_len = 0
    best_neg_start = 0
    
    for v in A:
        prev_v = v - K
        if prev_v > 0 and prev_v in dp:
            length, neg_start = dp[prev_v]
            new_state = (length + 1, neg_start)
        else:
            new_state = (1, -v)
            
        if v not in dp or new_state > dp[v]:
            dp[v] = new_state
            
        if new_state > (max_len, best_neg_start):
            max_len, best_neg_start = new_state
            
    if max_len == 0:
        return [0]
        
    start_val = -best_neg_start
    subseq = [start_val + j * K for j in range(max_len)]
    return [max_len] + subseq
```

- **Time Complexity:** $O(N \log N)$ to sort coordinates, plus $O(N)$ for the DP.
- **Space Complexity:** $O(N)$ to store events and interval configurations.

---

### Q6. Median Path

**Topic:** `Trees`, `DFS`, `Fenwick Tree`, `Binary Lifting`  

Given a tree with $N$ nodes, and node values $C$.
Calculate the sum of medians of every simple path of odd length (i.e. odd number of nodes) starting from node 1.

#### Example
- **Input:** $N = 6, C = [1, 2, 4, 3, 1, 5]$, $\text{edges} = [[1, 4], [4, 5], [4, 3], [4, 2], [1, 6]]$
- **Output:** `7` (Paths of odd length from 1 are: to 1 ({1}, median 1), to 2 ({1, 4, 2}, median 2), to 3 ({1, 4, 3}, median 3), to 5 ({1, 4, 5}, median 1). Sum = 1 + 2 + 3 + 1 = 7).

#### Solution Explanation
A simple path starting from node 1 to node $u$ has an odd number of nodes if and only if the depth of $u$ is even (with $depth(1) = 0$).
We can perform a DFS from root 1. During DFS, we maintain the values of the nodes on the current path in a Fenwick tree (Binary Indexed Tree) after coordinate compressing the node values $C$.
- When we enter a node $u$, we insert its compressed value into the Fenwick tree.
- If $depth(u)$ is even, the path has $L = depth(u) + 1$ elements. The median is the element at rank $(L + 1) / 2$. We find the rank in the Fenwick tree in $O(\log N)$ time using binary lifting and add the actual value to the sum.
- When we backtrack from $u$, we remove its compressed value from the Fenwick tree.

```python
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
        
    def add(self, idx, val):
        idx += 1
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)
            
    def find_kth(self, k):
        idx = 0
        h = 1
        while h * 2 <= self.size:
            h *= 2
        while h > 0:
            if idx + h <= self.size and self.tree[idx + h] < k:
                idx += h
                k -= self.tree[idx]
            h //= 2
        return idx

def sumOfMedians(n: int, C: list[int], edges: list[list[int]]) -> int:
    sorted_unique = sorted(list(set(C)))
    val_to_rank = {val: idx for idx, val in enumerate(sorted_unique)}
    U = len(sorted_unique)
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    fenwick = FenwickTree(U)
    total_median_sum = 0
    
    import sys
    sys.setrecursionlimit(200000)
    
    def dfs(u, p, depth):
        nonlocal total_median_sum
        rank = val_to_rank[C[u - 1]]
        fenwick.add(rank, 1)
        
        if depth % 2 == 0:
            L = depth + 1
            k = (L + 1) // 2
            med_rank = fenwick.find_kth(k)
            total_median_sum += sorted_unique[med_rank]
            
        for v in adj[u]:
            if v != p:
                dfs(v, u, depth + 1)
                
        fenwick.add(rank, -1)
        
    dfs(1, 0, 0)
    return total_median_sum
```

- **Time Complexity:** $O(N \log N)$ to sort and coordinate compress values, followed by $O(\log N)$ median lookup per node.
- **Space Complexity:** $O(N)$ for recursive stack and Fenwick tree.

---

### Q7. Reckon Strings

**Topic:** `Dynamic Programming`, `Graphs`, `Matrix Exponentiation`, `Combinatorics`  

Given an integer $N$, and $M$ pairs of distinct characters (lowercase English letters only) that cannot occur together in a formed string. The relation is transitive (if $u$ and $v$ are in relation, and $v$ and $w$ are in relation, then $u$ and $w$ are in relation).

Determine the total number of strings of length $N$ such that no two adjacent characters in the string hold any relation.
Since this number can be large, output it modulo $10^9 + 7$.

#### Example
- **Input:** $N = 2, M = 3$, $\text{pairs} = [[a, b], [b, c], [c, d]]$
- **Output:** `664` (All adjacent combinations of distinct elements in $\{a, b, c, d\}$ are prohibited. The total valid combinations of length 2 are $26^2 - 12 = 664$).

#### Solution Explanation
The relation partitions the 26 lowercase English letters into disjoint connected components (equivalence classes). Within any component $C_j$, no two *distinct* characters can be adjacent. A character can be adjacent to itself (since the relation is only defined between distinct characters).

Let $dp[i][C_j]$ be the number of valid strings of length $i$ ending with a character of component $C_j$.
For any character in $C_j$, the transition to length $i+1$ is:
- We can transition from the same character (1 choice).
- We can transition from any character in a different component $C_k$ ($k \neq j$) (size of $C_k$ choices).

Thus:
$$dp[i+1][C_j] = dp[i][C_j] + \sum_{k \neq j} |C_k| \cdot dp[i][C_k]$$

This is a system of linear recurrences which can be solved in $O(K^3 \log N)$ time using matrix exponentiation, where $K \le 26$ is the number of connected components.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

def multiply_matrices(A, B, mod):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == 0:
                continue
            for j in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def power_matrix(A, p, mod):
    n = len(A)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    base = A
    while p > 0:
        if p & 1:
            res = multiply_matrices(res, base, mod)
        base = multiply_matrices(base, base, mod)
        p >>= 1
    return res

def reckonStrings(N: int, M: int, pairs: list[list[str]]) -> int:
    mod = 1000000007
    if N == 0:
        return 0
    
    dsu = DSU(26)
    for u, v in pairs:
        dsu.union(ord(u) - ord('a'), ord(v) - ord('a'))
        
    components = {}
    for i in range(26):
        root = dsu.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)
        
    comp_list = list(components.values())
    K = len(comp_list)
    comp_sizes = [len(c) for c in comp_list]
    
    M_matrix = [[0] * K for _ in range(K)]
    for j in range(K):
        for k in range(K):
            if j == k:
                M_matrix[j][k] = 1
            else:
                M_matrix[j][k] = comp_sizes[k]
                
    M_pow = power_matrix(M_matrix, N - 1, mod)
    
    dp_N = [0] * K
    for j in range(K):
        dp_N[j] = sum(M_pow[j]) % mod
        
    total = 0
    for j in range(K):
        total = (total + comp_sizes[j] * dp_N[j]) % mod
        
    return total
```

- **Time Complexity:** $O(K^3 \log N)$, where $K \le 26$ is the number of equivalence classes of characters. This is extremely efficient and fast.
- **Space Complexity:** $O(K^2)$ to store matrices.
