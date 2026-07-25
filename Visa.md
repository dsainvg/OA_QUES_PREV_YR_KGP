# Interview Questions

*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Maximum Subarray Sum with One Deletion

**Topic:** `Arrays`, `Dynamic Programming`, `Kadane's Algorithm`

Given an array of integers `arr`, return the maximum sum of a non-empty subarray with at most one element deleted.

#### Input
- `arr`: list of integers

#### Constraints
- $1 \le \text{len}(arr) \le 10^5$
- $-10^4 \le arr[i] \le 10^4$

#### Example 1
**Input:** `arr = [1, -2, 0, 3]`  
**Output:** `4`  
**Explanation:** Deleting `-2` yields `[1, 0, 3]` with sum `4`.

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

##### Python Implementation
```python
def maxSubarraySumOneDeletion(arr):
    n = len(arr)
    no_del = arr[0]
    one_del = 0
    max_sum = arr[0]
    
    for i in range(1, n):
        one_del = max(no_del, one_del + arr[i])
        no_del = max(arr[i], no_del + arr[i])
        max_sum = max(max_sum, no_del, one_del)
        
    return max_sum
```

##### C++ Implementation
```cpp
#include <vector>
#include <algorithm>
using namespace std;

int maxSubarraySumOneDeletion(vector<int>& arr) {
    int n = arr.size();
    int no_del = arr[0], one_del = 0, max_sum = arr[0];
    for (int i = 1; i < n; ++i) {
        one_del = max(no_del, one_del + arr[i]);
        no_del = max(arr[i], no_del + arr[i]);
        max_sum = max({max_sum, no_del, one_del});
    }
    return max_sum;
}
```

---

### Q2. Network Delay Time

**Topic:** `Graphs`, `Dijkstra`, `Shortest Path`

Given a network of `n` nodes labeled `1` to `n` and `times[i] = (ui, vi, wi)`, return the minimum time for all nodes to receive a signal sent from node `k`.

#### Input
- `n`: integer
- `times`: list of `[u, v, w]`
- `k`: integer

#### Constraints
- $1 \le k \le n \le 100$
- $1 \le \text{len}(times) \le 6000$

#### Example 1
**Input:** `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`  
**Output:** `2`  

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(E \log V)$
- **Space Complexity:** $\mathcal{O}(V + E)$

##### Python Implementation
```python
import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
        
    pq = [(0, k)]
    dist = {}
    
    while pq:
        d, u = heapq.heappop(pq)
        if u in dist:
            continue
        dist[u] = d
        for v, w in graph[u]:
            if v not in dist:
                heapq.heappush(pq, (d + w, v))
                
    return max(dist.values()) if len(dist) == n else -1
```

##### C++ Implementation
```cpp
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    unordered_map<int, vector<pair<int, int>>> graph;
    for (auto& t : times) graph[t[0]].push_back({t[1], t[2]});
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    vector<int> dist(n + 1, 1e9);
    dist[k] = 0;
    pq.push({0, k});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto& [v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    int ans = *max_element(dist.begin() + 1, dist.end());
    return ans == 1e9 ? -1 : ans;
}
```

---

### Q3. Valid Parentheses String

**Topic:** `Strings`, `Greedy`, `Dynamic Programming`

Given a string containing `(`, `)`, and `*`, return `True` if the string is valid where `*` can represent `(`, `)`, or empty string.

#### Example 1
**Input:** `s = "(*)"`  
**Output:** `True`  

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

##### Python Implementation
```python
def checkValidString(s):
    cmin = cmax = 0
    for char in s:
        if char == '(':
            cmin += 1
            cmax += 1
        elif char == ')':
            cmin = max(0, cmin - 1)
            cmax -= 1
        else:
            cmin = max(0, cmin - 1)
            cmax += 1
        if cmax < 0:
            return False
    return cmin == 0
```

##### C++ Implementation
```cpp
#include <string>
#include <algorithm>
using namespace std;

bool checkValidString(string s) {
    int cmin = 0, cmax = 0;
    for (char c : s) {
        if (c == '(') { cmin++; cmax++; }
        else if (c == ')') { cmin = max(0, cmin - 1); cmax--; }
        else { cmin = max(0, cmin - 1); cmax++; }
        if (cmax < 0) return false;
    }
    return cmin == 0;
}
```