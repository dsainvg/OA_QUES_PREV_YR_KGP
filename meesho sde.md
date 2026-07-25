# Interview Questions
*Total questions: 4*

---

## Table of Contents
1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Maximum Removals for Subsequence

**Topic:** `Binary Search`, `String`, `Two Pointers`  

**Problem Description:**
Given two strings `source` and `target`, and an array `order` containing a permutation of 1-based indices of `source`. We remove characters from `source` one by one in the order specified by `order` (while keeping the remaining characters at their original indices). 

Find the maximum number of characters we can remove from `source` following the sequence of indices defined by the permutation `order[]`, such that the string `target` remains a subsequence of `source`.

**Constraints:**
* $1 \le |source| \le 10^5$
* $1 \le |target| \le |source|$
* `order` forms a permutation of $1$ to $|source|$.
* It is guaranteed that `target` exists as a subsequence of `source` initially.

**Example:**
* **Source:** `"abbabaa"`
* **Target:** `"bb"`
* **Order:** `[7, 1, 2, 5, 4, 3, 6]`
* **Output:** `3`

*Explanation:*
The removals occur as follows (the characters in bold show the desired subsequence, whereas `-` represents removed characters):
1. Character at index 7 is removed: source = `"abbaba-"`. Thus, target `"bb"` exists as a subsequence.
2. Character at index 1 is removed: source = `"-bbaba-"`. Thus, target `"bb"` exists as a subsequence.
3. Character at index 2 is removed: source = `"--baba-"`. Thus, target `"bb"` exists as a subsequence.
4. Character at index 5 is removed: source = `"--ba-a-"`. Here, target `"bb"` does not exist as a subsequence.
Therefore, a maximum of 3 removals can be done.

```python
def getMaximumRemovals(order, source, target):
    n = len(source)
    
    def check(k):
        # Mark characters to be removed
        removed = [False] * n
        for i in range(k):
            # order is 1-based
            removed[order[i] - 1] = True
        
        # Check if target is a subsequence of the remaining source
        t_idx = 0
        t_len = len(target)
        for s_idx in range(n):
            if not removed[s_idx]:
                if source[s_idx] == target[t_idx]:
                    t_idx += 1
                    if t_idx == t_len:
                        return True
        return False

    low, high = 0, n
    ans = 0
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

### Q2. Round-Robin Load Balancer

**Topic:** `Heap (Priority Queue)`, `Sorting`, `Simulation`  

**Problem Description:**
Implement a prototype of a round-robin load-balancing algorithm.
There are $n$ servers indexed from 1 to $n$, and $m$ requests to be processed. The $i$-th request arrives at time `arrival[i]` and takes `burstTime[i]` time to execute.

The load balancer assigns the request to the available server with the minimum index. A server that is assigned the $i$-th request is unavailable from time `arrival[i]` to `arrival[i] + burstTime[i]`. At `arrival[i] + burstTime[i]`, the server is available to serve a new request.

Given $n$, `arrival`, and `burstTime` for each request, find the index of the server that executes it. If no server is available at the time, the request is dropped, and -1 is reported. If multiple requests arrive at the same time, the one with the smaller index in the input array is assigned first.

**Constraints:**
* $1 \le n \le 10^5$
* $1 \le m \le 10^5$
* $1 \le arrival[i], burstTime[i] \le 10^9$

**Example:**
* **n:** `3`
* **Arrival:** `[2, 4, 1, 8, 9]`
* **Burst Time:** `[7, 9, 2, 4, 5]`
* **Output:** `[2, 1, 1, 3, 2]`

*Explanation:*
* At time 1: Request 3 (index 2) arrives. Available servers: `[1, 2, 3]`. Assigned to server 1. Server 1 busy until 3.
* At time 2: Request 1 (index 0) arrives. Available servers: `[2, 3]`. Assigned to server 2. Server 2 busy until 9.
* At time 4: Request 2 (index 1) arrives. Available servers: `[1, 3]` (server 1 became free at 3). Assigned to server 1. Server 1 busy until 13.
* At time 8: Request 4 (index 3) arrives. Available servers: `[3]`. Assigned to server 3. Server 3 busy until 12.
* At time 9: Request 5 (index 4) arrives. Available servers: `[2]` (server 2 became free at 9). Assigned to server 2. Server 2 busy until 14.

```python
import heapq

def getServerIndex(n, arrival, burstTime):
    m = len(arrival)
    ans = [-1] * m
    
    # Store requests as (arrival_time, original_index, burst_time)
    requests = []
    for i in range(m):
        requests.append((arrival[i], i, burstTime[i]))
    
    # Sort requests by arrival time. If arrival times are equal,
    # the request with the smaller original index will come first.
    requests.sort()
    
    # Min-heap of available servers
    available_servers = list(range(1, n + 1))
    heapq.heapify(available_servers)
    
    # Min-heap of busy servers: stores (completion_time, server_id)
    busy_servers = []
    
    for arr_time, orig_idx, burst in requests:
        # Free up servers that finished their tasks before or at arr_time
        while busy_servers and busy_servers[0][0] <= arr_time:
            comp_time, server_id = heapq.heappop(busy_servers)
            heapq.heappush(available_servers, server_id)
            
        # Assign the request to the available server with the minimum index
        if available_servers:
            assigned_server = heapq.heappop(available_servers)
            ans[orig_idx] = assigned_server
            heapq.heappush(busy_servers, (arr_time + burst, assigned_server))
            
    return ans
```

---

### Q3. Bounded Number Line Subsequences

**Topic:** `Dynamic Programming`, `String`, `Combinatorics`  

**Problem Description:**
Given a number line from $0$ to $n$, a starting point $x$, and an ending point $y$. We are given a string `moves` representing a sequence of movements, where `'l'` denotes moving left (position decreases by 1) and `'r'` denotes moving right (position increases by 1).

Find the number of distinct subsequence strings of `moves` that, when applied starting from $x$, will end exactly at $y$ while ensuring that the current position on the number line never goes below $0$ or above $n$ at any intermediate step.
Return the answer modulo $10^9 + 7$.

**Constraints:**
* $1 \le n \le 1000$
* $0 \le x, y \le n$
* $1 \le |moves| \le 1000$

**Example:**
* **n:** `6`
* **x:** `1`
* **y:** `4`
* **moves:** `"rrlrlr"`
* **Output:** `3`

*Explanation:*
The 3 distinct subsequence strings that lead from 1 to 4 and stay in bounds are:
1. `rrrlr` (path: 1 -> 2 -> 3 -> 4 -> 3 -> 4)
2. `rrlrr` (path: 1 -> 2 -> 3 -> 2 -> 3 -> 4)
3. `rrr` (path: 1 -> 2 -> 3 -> 4)

```python
def countSubsequences(n, x, y, moves):
    MOD = 10**9 + 7
    
    # dp[pos] stores the number of distinct subsequence strings of moves
    # that lead from x to pos while staying within [0, n]
    dp = [0] * (n + 1)
    dp[x] = 1
    
    # last_r[pos] stores the number of subsequences ending in 'r' at pos
    last_r = [0] * (n + 1)
    # last_l[pos] stores the number of subsequences ending in 'l' at pos
    last_l = [0] * (n + 1)
    
    for c in moves:
        if c == 'r':
            # 'r' moves from pos-1 to pos.
            # We iterate backwards from n to 1 to use values from the previous step.
            for pos in range(n, 0, -1):
                new_val = dp[pos - 1]
                diff = (new_val - last_r[pos]) % MOD
                dp[pos] = (dp[pos] + diff) % MOD
                last_r[pos] = new_val
        elif c == 'l':
            # 'l' moves from pos+1 to pos.
            # We iterate forwards from 0 to n-1 to use values from the previous step.
            for pos in range(0, n):
                new_val = dp[pos + 1]
                diff = (new_val - last_l[pos]) % MOD
                dp[pos] = (dp[pos] + diff) % MOD
                last_l[pos] = new_val
                
    return dp[y]
```

---

### Q4. Maximum Device Transmission Distance

**Topic:** `Trees`, `Depth-First Search (DFS)`, `Tree Diameter`  

**Problem Description:**
We are given a tree with `network_nodes` nodes numbered from 1 to `network_nodes`. The tree is defined by edges between `network_from[i]` and `network_to[i]`. Each node $u$ has a compatibility value `frequency[u]`.

A device $u$ can transmit a message to device $v$ if there is a simple path between them such that the compatibility/frequency values of any two consecutive devices on the path differ by at most 1.

Find the maximum distance (measured in number of edges) between any pair of devices that can transmit messages to each other. If no pair of devices can transmit messages, return 0.

**Constraints:**
* $1 \le network\_nodes \le 10^5$
* $1 \le frequency[i] \le 10^9$

**Example:**
* **network_nodes:** `4`
* **network_from:** `[1, 2, 3]`
* **network_to:** `[2, 3, 4]`
* **frequency:** `[1, 3, 2, 1]`
* **Output:** `2`

*Explanation:*
* Edge (1, 2): frequencies are 1 and 3 (difference = 2 > 1). Message cannot be transmitted.
* Edge (2, 3): frequencies are 3 and 2 (difference = 1 <= 1). Message can be transmitted.
* Edge (3, 4): frequencies are 2 and 1 (difference = 1 <= 1). Message can be transmitted.
The communicating components are `{1}` (size 1) and `{2, 3, 4}`. Within `{2, 3, 4}`, the maximum distance is between 2 and 4 (path 2 -> 3 -> 4, distance is 2).
So the maximum transmission distance is 2.

```python
import sys
# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def calculateMax(network_nodes, network_from, network_to, frequency):
    # Adjust for 0-based indexing
    adj = [[] for _ in range(network_nodes)]
    for u, v in zip(network_from, network_to):
        u -= 1
        v -= 1
        # Only keep edges where |frequency[u] - frequency[v]| <= 1
        if abs(frequency[u] - frequency[v]) <= 1:
            adj[u].append(v)
            adj[v].append(u)
            
    visited = [False] * network_nodes
    
    def get_component(start):
        nodes = []
        stack = [start]
        visited[start] = True
        while stack:
            u = stack.pop()
            nodes.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return nodes

    def find_farthest(start, component_set):
        dist = {node: -1 for node in component_set}
        dist[start] = 0
        queue = [start]
        farthest_node = start
        max_d = 0
        
        # Simple BFS
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if dist[v] > max_d:
                        max_d = dist[v]
                        farthest_node = v
                    queue.append(v)
        return farthest_node, max_d

    max_diameter = 0
    for i in range(network_nodes):
        if not visited[i]:
            comp_nodes = get_component(i)
            if len(comp_nodes) <= 1:
                continue
            # Step 1: Find farthest node from any node in the component
            farthest_1, _ = find_farthest(comp_nodes[0], comp_nodes)
            # Step 2: Find farthest node from farthest_1 to get the diameter
            _, diameter = find_farthest(farthest_1, comp_nodes)
            max_diameter = max(max_diameter, diameter)
            
    return max_diameter
```
