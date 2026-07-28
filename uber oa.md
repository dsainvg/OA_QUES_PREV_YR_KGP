# Interview Questions

*Total questions: 5*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Uber Drivers Network Coordination

`[Latest]`

**Topic:** `Tree`, `Graph`, `DFS/BFS`, `Connected Components`, `Diameter`

#### Description
You are given a network of Uber drivers represented as a tree structure. Each driver operates on a specific service compatibility level, represented by an integer value of `1`, `2`, or `3`.

Two drivers can directly coordinate with each other if the absolute difference between their compatibility levels is at most `1`.
The driver network consists of `network_nodes` drivers connected by `network_nodes - 1` roads, ensuring the structure forms a tree. The roads are defined by two arrays: `network_from` and `network_to`, where an undirected road connects `network_from[i]` and `network_to[i]` for $1 \le i < network\_nodes$.

An additional array, `compatibility`, represents the service compatibility level of each driver.

The distance between two drivers is defined as the number of roads in the simple path connecting them. A simple path is a sequence of drivers where each consecutive pair is connected by a road, and no driver appears more than once.

Your task is to determine the maximum distance between any two drivers who can coordinate successfully. Two drivers can coordinate if there exists a simple path between them such that the compatibility difference between every pair of consecutive drivers along the path is at most `1`.

If no such pair of drivers exists, return `0`.

#### Input Format
- `network_nodes`: Number of drivers.
- `network_from`: List of starting nodes for the roads (1-based index).
- `network_to`: List of ending nodes for the roads (1-based index).
- `compatibility`: List of service compatibility levels.

#### Constraints
- $2 \le network\_nodes \le 2 \cdot 10^5$
- $1 \le network\_from[i], network\_to[i] \le network\_nodes$
- $1 \le compatibility[i] \le 3$

#### Sample Cases

**Sample Case 0**
- **Input:**
  - `network_nodes = 4`
  - `network_from = [1, 1, 1]`
  - `network_to = [2, 3, 4]`
  - `compatibility = [1, 1, 1, 1]`
- **Output:** `2`
- **Explanation:**
  The tree is a star graph where node 1 is connected to 2, 3, and 4. All compatibilities are 1. The maximum path between any two nodes is 2 (e.g., path $2 \to 1 \to 3$).

**Sample Case 1**
- **Input:**
  - `network_nodes = 3`
  - `network_from = [2, 1]`
  - `network_to = [1, 3]`
  - `compatibility = [3, 1, 1]`
- **Output:** `0`
- **Explanation:**
  The edges are $(2, 1)$ and $(1, 3)$. The compatibility levels are $comp[1]=3, comp[2]=1, comp[3]=1$.
  The compatibility difference for adjacent drivers is $|3 - 1| = 2 > 1$. No two adjacent drivers can coordinate. Hence, the output is `0`.

**Sample Case 2**
- **Input:**
  - `network_nodes = 4`
  - `network_from = [1, 2, 3]`
  - `network_to = [2, 3, 4]`
  - `compatibility = [1, 3, 2, 1]`
- **Output:** `2`
- **Explanation:**
  The path is $1 \to 2 \to 3 \to 4$.
  - Edge $(1, 2)$: $|1 - 3| = 2 > 1$ (Disconnected)
  - Edge $(2, 3)$: $|3 - 2| = 1 \le 1$ (Connected)
  - Edge $(3, 4)$: $|2 - 1| = 1 \le 1$ (Connected)
  The connected components with compatibility difference $\le 1$ are $\{1\}$ and $\{2, 3, 4\}$.
  The path in the second component is $2 \to 3 \to 4$ which has a maximum distance of `2` (between nodes 2 and 4).

#### Python Solution
```python
from collections import deque

def calculateMax(network_nodes, network_from, network_to, compatibility):
    adj = [[] for _ in range(network_nodes + 1)]
    for u, v in zip(network_from, network_to):
        if abs(compatibility[u - 1] - compatibility[v - 1]) <= 1:
            adj[u].append(v)
            adj[v].append(u)
    
    vis = [0] * (network_nodes + 1)
    ans = 0
    for i in range(1, network_nodes + 1):
        if not vis[i]:
            # First BFS to find the farthest node in the component
            q = deque([i])
            vis[i] = 1
            far1 = i
            while q:
                u = q.popleft()
                far1 = u
                for v in adj[u]:
                    if not vis[v]:
                        vis[v] = 1
                        q.append(v)
            
            # Second BFS from the farthest node to find the diameter of the component
            q2 = deque([(far1, 0)])
            vis[far1] = 2
            max_d = 0
            while q2:
                u, d = q2.popleft()
                max_d = max(max_d, d)
                for v in adj[u]:
                    if vis[v] != 2:
                        vis[v] = 2
                        q2.append((v, d + 1))
            ans = max(ans, max_d)
    return ans
```

---

### Q2. Uber City Grid Route Optimization

`[Latest]`

**Topic:** `Grid`, `BFS`, `Binary Search`, `Shortest Path`

#### Description
Given an $n \times m$ city grid representing Uber city blocks, rows are numbered from $1$ to $n$ and columns from $1$ to $m$. Some city blocks are restricted/blocked due to construction, traffic, or safety issues. These restricted blocks are provided in the array `blockedPositions`, where `blockedPositions[i]` represents the 1-based coordinates of a restricted block.

An Uber driver starts from the top-left block $(1, 1)$ and must reach the bottom-right block $(n, m)$ without passing through any restricted blocks. The driver can move up, down, left, or right at each step.

The safety strength of a route is defined as the minimum Manhattan distance from any block visited in the route to the nearest restricted block.

Among all possible routes from $(1, 1)$ to $(n, m)$, determine the route that maximizes safety strength. If multiple routes have the same maximum strength, choose the route that visits the fewest city blocks.

Return two integers in an integer array:
1. The maximum safety strength achievable.
2. The minimum number of blocks visited (path length) for that maximum strength.

If it is impossible to travel from $(1, 1)$ to $(n, m)$, return `[-1, -1]`.

The Manhattan distance between two blocks $(a, b)$ and $(c, d)$ is defined as $|a - c| + |b - d|$.

#### Constraints
- $1 \le n, m, x \le 5 \cdot 10^4$
- $3 \le n \cdot m \le 10^5$
- $1 \le blockedPositions[i][0] \le n$
- $1 \le blockedPositions[i][1] \le m$
- Neither $(1, 1)$ nor $(n, m)$ is blocked.

#### Sample Cases

**Sample Case 0**
- **Input:**
  - `n = 4`, `m = 4`
  - `blockedPositions = [[1, 2], [4, 3]]`
- **Output:** `[1, 7]`
- **Explanation:**
  The blocked positions are $(1, 2)$ and $(4, 3)$.
  The start $(1, 1)$ has a distance of 1 to $(1, 2)$, so any path has safety strength at most 1.
  The shortest path with strength $\ge 1$ has length 7 (e.g., $(1, 1) \to (2, 1) \to (3, 1) \to (3, 2) \to (3, 3) \to (3, 4) \to (4, 4)$).

**Sample Case 1**
- **Input:**
  - `n = 4`, `m = 3`
  - `blockedPositions = [[1, 3], [2, 3]]`
- **Output:** `[2, 6]`
- **Explanation:**
  The optimal path is $(1, 1) \to (2, 1) \to (3, 1) \to (4, 1) \to (4, 2) \to (4, 3)$.
  Every cell on this path has a Manhattan distance of at least 2 to the blocked positions $(1, 3)$ and $(2, 3)$. The path length is 6.

#### Python Solution
```python
from collections import deque

def findOptimalPair(n, m, blockedPositions):
    n = int(n)
    m = int(m)
    
    pairs = []
    if blockedPositions:
        if not isinstance(blockedPositions[0], (list, tuple)):
            for i in range(0, len(blockedPositions), 2):
                if i + 1 < len(blockedPositions):
                    pairs.append((blockedPositions[i], blockedPositions[i+1]))
        else:
            for pos in blockedPositions:
                if len(pos) >= 2:
                    pairs.append((pos[0], pos[1]))

    q = deque()
    dist = [-1] * (n * m)
    for row_val, col_val in pairs:
        r, c = int(row_val) - 1, int(col_val) - 1
        if 0 <= r < n and 0 <= c < m:
            idx = r * m + c
            if dist[idx] == -1:
                dist[idx] = 0
                q.append(idx)
            
    if not q:
        dist = [n + m] * (n * m)
    else:
        while q:
            u = q.popleft()
            d = dist[u]
            r, c = u // m, u % m
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < m:
                    v = nr * m + nc
                    if dist[v] == -1:
                        dist[v] = d + 1
                        q.append(v)
                    
    visited = [0] * (n * m)
    vis_id = 0
    target = n * m - 1
    
    def check(S):
        nonlocal vis_id
        if dist[0] < S or dist[target] < S:
            return -1
        vis_id += 1
        visited[0] = vis_id
        q_check = deque([(0, 1)])
        while q_check:
            u, length = q_check.popleft()
            if u == target:
                return length
            r, c = u // m, u % m
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < m:
                    v = nr * m + nc
                    if visited[v] != vis_id and dist[v] >= S:
                        visited[v] = vis_id
                        q_check.append((v, length + 1))
        return -1
        
    init_len = check(1)
    if init_len == -1:
        return [-1, -1]
        
    low, high = 1, min(dist[0], dist[target])
    best_S, best_len = 1, init_len
    
    while low <= high:
        mid = (low + high) // 2
        length = check(mid)
        if length != -1:
            best_S, best_len, low = mid, length, mid + 1
        else:
            high = mid - 1
            
    return [best_S, best_len]
```

---

### Q3. Route Latency Stabilization Steps

`[Latest]`

**Topic:** `Inversions`, `Fenwick Tree / Binary Indexed Tree`, `Merge Sort`

#### Description
You are developing a backend tool for Uber's route optimization engine. The list of predicted route segment latencies sometimes ends up out of order, leading to inconsistent navigation recommendations.

To stabilize the route plan, a background correction process runs that performs the following:
1. Find the smallest pair $(i, j)$ such that $0 \le i < j < n$ and $latencies[i] > latencies[j]$, using lexicographical order on $(i, j)$.
2. Swap the latencies at positions $i$ and $j$.
3. Repeat the process until all latencies are in non-decreasing order.

Each swap is considered one stabilization step. Calculate the total number of stabilization swaps required to fix the route.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le latencies[i] \le 10^9$
- All elements of `latencies` are distinct.

#### Sample Cases

**Sample Case 0**
- **Input:**
  - `latencies = [7, 1, 2]`
- **Output:** `2`
- **Explanation:**
  - $[7, 1, 2] \to [1, 7, 2]$ (swap 0 and 1)
  - $[1, 7, 2] \to [1, 2, 7]$ (swap 1 and 2)
  Two swaps are required.

**Sample Case 1**
- **Input:**
  - `latencies = [7, 12]`
- **Output:** `0`
- **Explanation:**
  The array is already sorted.

**Sample Case 2**
- **Input:**
  - `latencies = [5, 1, 4, 2]`
- **Output:** `4`
- **Explanation:**
  - $[5, 1, 4, 2] \to [1, 5, 4, 2]$ (swap 0 and 1)
  - $[1, 5, 4, 2] \to [1, 4, 5, 2]$ (swap 1 and 2)
  - $[1, 4, 5, 2] \to [1, 4, 2, 5]$ (swap 2 and 3)
  - $[1, 4, 2, 5] \to [1, 2, 4, 5]$ (swap 1 and 2)
  Total swaps = 4.

#### Python Solution
```python
def countStabilizationSteps(latencies):
    n = len(latencies)
    ranks = {v: i + 1 for i, v in enumerate(sorted(latencies))}
    tree = [0] * (n + 1)
    ans = 0
    for x in reversed(latencies):
        i = ranks[x] - 1
        while i > 0:
            ans += tree[i]
            i -= i & -i
        i = ranks[x]
        while i <= n:
            tree[i] += 1
            i += i & -i
    return ans
```

---

### Q4. Reconstruct Itinerary

**Topic:** `Graphs`, `Eulerian Path`, `DFS`

Reconstruct the travel itinerary from a list of flight tickets beginning from `"JFK"`.

#### Example 1
**Input:** `tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]`  
**Output:** `["JFK", "MUC", "LHR", "SFO", "SJC"]`  

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(E \log E)$
- **Space Complexity:** $\mathcal{O}(E)$

##### Python Implementation
```python
from collections import defaultdict

def findItinerary(tickets):
    targets = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        targets[a].append(b)
        
    route = []
    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)
        
    visit('JFK')
    return route[::-1]
```

##### C++ Implementation
```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>
using namespace std;

vector<string> findItinerary(vector<vector<string>>& tickets) {
    unordered_map<string, multiset<string>> targets;
    for (auto& ticket : tickets) targets[ticket[0]].insert(ticket[1]);
    vector<string> route;
    auto visit = [&](auto& self, string airport) -> void {
        while (!targets[airport].empty()) {
            auto next = *targets[airport].begin();
            targets[airport].erase(targets[airport].begin());
            self(self, next);
        }
        route.push_back(airport);
    };
    visit(visit, "JFK");
    reverse(route.begin(), route.end());
    return route;
}
```

---

### Q5. Minimum Cost to Cut a Stick

**Topic:** `Dynamic Programming`, `Arrays`

Given a wooden stick of length `n` and cuts array `cuts`, return minimum cost to cut the stick into pieces.

#### Example 1
**Input:** `n = 7, cuts = [1, 3, 4, 5]`  
**Output:** `16`  

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(M^3)$ where $M = \text{len}(cuts)$
- **Space Complexity:** $\mathcal{O}(M^2)$

##### Python Implementation
```python
def minCost(n, cuts):
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)
    dp = [[0] * m for _ in range(m)]
    
    for l in range(2, m):
        for i in range(m - l):
            j = i + l
            dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + (cuts[j] - cuts[i])
            
    return dp[0][m - 1]
```

##### C++ Implementation
```cpp
#include <vector>
#include <algorithm>
using namespace std;

int minCost(int n, vector<int>& cuts) {
    cuts.push_back(0);
    cuts.push_back(n);
    sort(cuts.begin(), cuts.end());
    int m = cuts.size();
    vector<vector<int>> dp(m, vector<int>(m, 0));
    for (int l = 2; l < m; ++l) {
        for (int i = 0; i < m - l; ++i) {
            int j = i + l;
            int mini = 1e9;
            for (int k = i + 1; k < j; ++k) mini = min(mini, dp[i][k] + dp[k][j]);
            dp[i][j] = mini + (cuts[j] - cuts[i]);
        }
    }
    return dp[0][m - 1];
}
```

