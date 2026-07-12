# Interview Questions

*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Longest String Chain

**Topic:** `dynamic-programming`, `strings`

Given an array of words representing a dictionary, test each word to see if it can be made into another word in the dictionary when characters are removed one at a time. Each word represents its own first element of its string chain, so start with a string chain length of 1. Each time a character is removed, increment the string chain by 1. In order to remove a character, the resulting word must be in the original dictionary. Determine the longest string chain achievable for a given dictionary.

#### Example
`n = 4`  
`words = ['a', 'and', 'an', 'bear']`

- The word `'and'` could be reduced to `'an'` and then to `'a'`. The single character `'a'` cannot be reduced any further because there is not a null string in the dictionary.
- The word `'bear'` cannot be reduced at all.
- The longest string chain has a length of 3.

#### Function Description
Complete the function `longestChain` in the editor.

`longestChain` has the following parameter:
- `words`: a list of strings representing the dictionary of words to test.

**Returns:**
- `int`: the length of the longest string chain.

#### Constraints
- $1 \le n \le 50000$
- $1 \le |words[i]| \le 60$, where $0 \le i < n$
- Each `words[i]` is composed of lowercase letters in the range `ascii[a-z]`.

```python
def longestChain(words: list[str]) -> int:
    """
    Finds the length of the longest string chain in the given list of words.
    
    Time Complexity: O(N * L^2) where N is the number of words and L is the max word length.
    Space Complexity: O(N) to store the word set and DP map.
    """
    words_set = set(words)
    # Sort words by length to process shorter words (predecessors) first
    words.sort(key=len)
    
    dp = {}
    max_chain_len = 0
    
    for word in words:
        best = 1
        for i in range(len(word)):
            # Form predecessor by removing the i-th character
            pred = word[:i] + word[i+1:]
            if pred in words_set:
                best = max(best, dp.get(pred, 1) + 1)
        dp[word] = best
        max_chain_len = max(max_chain_len, best)
        
    return max_chain_len
```

---

### Q2. Rooted Tree Prime Query

**Topic:** `trees`, `dfs`, `graphs`, `sieve`

In this challenge, construct a rooted undirected graph and then answer some queries on the graph. There are `n` nodes numbered from `1` to `n`. All the nodes are disconnected initially. Construct the graph by drawing an undirected edge between `m` pairs of nodes, picking one pair at a time and connecting the first and second nodes. After connecting each of the pairs, the graph construction is complete, and node `1` is the root node of this graph.

A node's parent is the next node on the shortest path from that node to node `1`, and a descendant is on the shortest path to a leaf moving away from node `1`. At this point, the graph can be considered a tree rooted at node `1`, and subtrees can be formed rooted at any node and consisting of its descendants.

Each node has a positive integer value associated with it. Find the total number of nodes with values as prime numbers in a given subtree rooted at a given node. There are multiple queries.

#### Function Description
Complete the function `primeQuery` in the editor.

`primeQuery` has the following parameters:
- `n`: an integer that denotes the number of nodes in the graph
- `first`: an array of integers that denotes the first node of each edge pair
- `second`: an array of integers that denotes the second node of each edge pair
- `values`: an array of integers that denotes the data value for each node `i` (1-indexed, i.e., `values[i-1]` is the value of node `i`)
- `queries`: an array of integers, representing the node numbers to query

**Returns:**
- `list[int]`: an array of integers representing the result of each query aligned by index.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le m \le n-1$
- $1 \le first[i], second[i], values[i] \le 10^5$
- $first[i] \neq second[i]$
- $1 \le q \le 10^5$
- $1 \le queries[i] \le 10^5$
- Note that `1` is not a prime number.

```python
def primeQuery(n: int, first: list[int], second: list[int], values: list[int], queries: list[int]) -> list[int]:
    """
    Computes the number of prime-valued nodes in the subtree of each queried node.
    
    Time Complexity: O(M log log M + N + Q) where M is max(values), N is number of nodes, Q is queries.
    Space Complexity: O(N) for tree adjacency and BFS/DFS arrays.
    """
    # Build adjacency list (1-indexed nodes)
    adj = [[] for _ in range(n + 1)]
    for u, v in zip(first, second):
        adj[u].append(v)
        adj[v].append(u)
        
    # Sieve of Eratosthenes up to the maximum node value
    max_val = max(values) if values else 0
    is_prime = [True] * (max_val + 1)
    if max_val >= 0:
        is_prime[0] = False
    if max_val >= 1:
        is_prime[1] = False
    for i in range(2, int(max_val**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_val + 1, i):
                is_prime[j] = False
                
    # Level-order BFS to find parent relationships and bottom-up traversal order
    from collections import deque
    parent = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                
    # Initialize DP array: prime_count[u] is 1 if values[u-1] is prime, else 0
    prime_count = [0] * (n + 1)
    for u in range(1, n + 1):
        val = values[u - 1]
        if val <= max_val and is_prime[val]:
            prime_count[u] = 1
            
    # Accumulate prime counts bottom-up
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            prime_count[p] += prime_count[u]
            
    # Resolve queries
    return [prime_count[q] for q in queries]
```

---

### Q3. Compromised Subarray Count

**Topic:** `arrays`, `bitwise-operations`, `monotonic-stack`

A cyber security expert has just intercepted a transmission containing an array `arr` of binary codes. An array is considered to be compromised if the bitwise OR of all elements in the subarray is present in the subarray itself.
The goal is to find the number of compromised subarrays in the intercepted transmission.
Note: A subarray is defined as any contiguous segment of the array.

#### Example
`n = 3`  
`arr = [2, 4, 7]`

| Subarray | Bitwise OR | Is compromised? |
| :--- | :--- | :--- |
| `[2]` | `2` | Yes |
| `[2, 4]` | `6` | No |
| `[2, 4, 7]` | `7` | Yes |
| `[4]` | `4` | Yes |
| `[4, 7]` | `7` | Yes |
| `[7]` | `7` | Yes |

Total number of compromised subarrays = 5.

#### Function Description
Complete the function `getCompromisedSubarrayCount` in the editor.

`getCompromisedSubarrayCount` has the following parameter:
- `arr`: an array of integers representing the transmission codes.

**Returns:**
- `int`: the total number of compromised subarrays.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le arr[i] \le 10^6$

```python
def getCompromisedSubarrayCount(arr: list[int]) -> int:
    """
    Finds the number of subarrays where the bitwise OR is equal to the maximum element.
    
    Time Complexity: O(N * log(max_val)) where log(max_val) <= 20.
    Space Complexity: O(N) for monotonic stack and bit tracking arrays.
    """
    n = len(arr)
    if n == 0:
        return 0
        
    # Determine the number of bits needed based on the maximum element
    max_val = max(arr)
    num_bits = max_val.bit_length()
    
    # 1. Compute L[i]: largest index < i such that arr[L[i]] >= arr[i]
    L = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if stack:
            L[i] = stack[-1]
        stack.append(i)
        
    # 2. Compute R[i]: smallest index > i such that arr[R[i]] > arr[i]
    R = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            R[i] = stack[-1]
        stack.append(i)
        
    # 3. Compute L_ok[i]: largest index p <= i such that arr[p] has a bit set that is NOT set in arr[i]
    L_ok = [-1] * n
    last_seen = [-1] * num_bits
    for i in range(n):
        val = arr[i]
        max_idx = -1
        for b in range(num_bits):
            if not ((val >> b) & 1):
                if last_seen[b] > max_idx:
                    max_idx = last_seen[b]
        L_ok[i] = max_idx
        # Update last_seen positions for bits that are set in arr[i]
        for b in range(num_bits):
            if (val >> b) & 1:
                last_seen[b] = i
                
    # 4. Compute R_ok[i]: smallest index p >= i such that arr[p] has a bit set that is NOT set in arr[i]
    R_ok = [n] * n
    next_seen = [n] * num_bits
    for i in range(n - 1, -1, -1):
        val = arr[i]
        min_idx = n
        for b in range(num_bits):
            if not ((val >> b) & 1):
                if next_seen[b] < min_idx:
                    min_idx = next_seen[b]
        R_ok[i] = min_idx
        # Update next_seen positions for bits that are set in arr[i]
        for b in range(num_bits):
            if (val >> b) & 1:
                next_seen[b] = i
                
    # Calculate the total number of compromised subarrays
    total_count = 0
    for i in range(n):
        left_limit = max(L[i], L_ok[i])
        right_limit = min(R[i], R_ok[i])
        if left_limit < i and right_limit > i:
            total_count += (i - left_limit) * (right_limit - i)
            
    return total_count
```
