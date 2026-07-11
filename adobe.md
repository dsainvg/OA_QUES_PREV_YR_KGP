# Interview Questions

*Generated from: `R:\DSA\Company wise prep resource\Adobe`*  
*Total questions: 3*  

---

## Table of Contents

1. [Coding Questions](#coding-questions)
   - [Q1. Count Good Edge](#q1-count-good-edge)
   - [Q2. Minimum Sum](#q2-minimum-sum)
   - [Q3. Good Subarrays](#q3-good-subarrays)

---

## Coding Questions

### Q1. Count Good Edge

**Topic:** `trees`, `dfs`, `depth-first-search`, `frequency-map`, `hash-map`

**Question:**  
You are given a tree of `n` nodes and `n-1` edges rooted on node 1. There is a `values` array of length `n`, where `values[i]` represents the number written on node `i` (1-base indexing). You have to count good edges in the tree.

An edge is considered good if you remove that edge from the tree and the tree splits into two subtrees such that there will be no subtree in which the frequency of any node value is more than `k`.

#### Input
- `n`: integer
- `k`: integer
- `values`: list of integers
- `edges`: list of pairs of integers

#### Constraints
- $1 \le n \le 10^5$
- $1 \le k, values[i] \le n$
- $1 \le edges[i][0], edges[i][1] \le n$

#### Example 1
**Input:**
```text
n = 5
k = 3
values = {1, 1, 1, 2, 1}
edges = {{1, 2}, {1, 3}, {2, 4}, {3, 5}}
```
**Output:**
```text
3
```
**Explanation:**  
The values of the nodes are:

- Node 1: 1
- Node 2: 1
- Node 3: 1
- Node 4: 2
- Node 5: 1

If we remove:

- Edge `{2, 4}`: One subtree has node `{4}` (value 2, freq 1), and the other has `{1, 2, 3, 5}` (values `{1, 1, 1, 1}`, freq of 1 is 4 > k=3). Hence, `{2, 4}` is bad.
- Edge `{1, 2}`: One subtree has `{2, 4}` (values `{1, 2}`, max freq 1 <= 3), and the other has `{1, 3, 5}` (values `{1, 1, 1}`, max freq of 1 is 3 <= 3). Good!
- Edge `{1, 3}`: One subtree has `{3, 5}` (values `{1, 1}`, max freq 2 <= 3), and the other has `{1, 2, 4}` (values `{1, 1, 2}`, max freq 2 <= 3). Good!
- Edge `{3, 5}`: One subtree has `{5}` (value 1, freq 1 <= 3), and the other has `{1, 2, 3, 4}` (values `{1, 1, 1, 2}`, max freq of 1 is 3 <= 3). Good!

Total good edges = 3.

#### Example 2
**Input:**
```text
n = 4
k = 2
values = {1, 1, 1, 1}
edges = {{1, 2}, {1, 3}, {1, 4}}
```
**Output:**
```text
0
```
**Explanation:**  
In the tree there is no good edge. If we remove any edge, one subtree will contain 3 nodes, all with the value `1`, meaning the frequency of value `1` in that subtree is `3`, which is greater than `k` (2).

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N \log N)$ using DSU on Tree / small-to-large merging.
- **Space Complexity:** $O(N)$ for adjacency list and frequency maps.

##### Python Implementation
```python
import sys
from collections import Counter

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def countGoodEdge(n, k, values, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    total_freq = Counter(values)
    
    # Store required frequencies for heavy values
    H = {}
    for val, freq in total_freq.items():
        if freq > k:
            H[val] = freq - k
            
    heavy_needed = len(H)
    good_edges_count = 0
    
    def dfs(u, p):
        nonlocal good_edges_count
        
        u_val = values[u - 1]
        u_map = {u_val: 1}
        u_max_freq = 1
        u_heavy_satisfied = 0
        if u_val in H and H[u_val] <= 1:
            u_heavy_satisfied = 1
            
        for v in adj[u]:
            if v == p:
                continue
            v_map, v_max_freq, v_heavy_satisfied = dfs(v, u)
            
            # Small-to-large merge
            if len(u_map) < len(v_map):
                u_map, v_map = v_map, u_map
                u_max_freq = max(u_max_freq, v_max_freq)
                u_heavy_satisfied = v_heavy_satisfied
                
            for val, count in v_map.items():
                old_count = u_map.get(val, 0)
                new_count = old_count + count
                u_map[val] = new_count
                if new_count > u_max_freq:
                    u_max_freq = new_count
                if val in H:
                    req = H[val]
                    if old_count < req and new_count >= req:
                        u_heavy_satisfied += 1
                        
        if u != 1:
            if u_max_freq <= k and u_heavy_satisfied == heavy_needed:
                good_edges_count += 1
                
        return u_map, u_max_freq, u_heavy_satisfied

    dfs(1, 0)
    return good_edges_count
```

##### C++ Implementation
```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
    int good_edges_count = 0;
    int heavy_needed = 0;
    
    struct DFSResult {
        unordered_map<int, int> freq_map;
        int max_freq;
        int heavy_satisfied;
    };
    
    DFSResult dfs(int u, int p, const vector<vector<int>>& adj, const vector<int>& values, 
                  const unordered_map<int, int>& H, int k) {
        
        DFSResult res;
        int u_val = values[u - 1];
        res.freq_map[u_val] = 1;
        res.max_freq = 1;
        res.heavy_satisfied = 0;
        
        if (H.count(u_val) && 1 >= H.at(u_val)) {
            res.heavy_satisfied = 1;
        }
        
        for (int v : adj[u]) {
            if (v == p) continue;
            DFSResult child_res = dfs(v, u, adj, values, H, k);
            
            // Merge child_res.freq_map into res.freq_map (small-to-large)
            if (res.freq_map.size() < child_res.freq_map.size()) {
                swap(res.freq_map, child_res.freq_map);
                res.max_freq = max(res.max_freq, child_res.max_freq);
                res.heavy_satisfied = child_res.heavy_satisfied;
            }
            
            for (auto const& [val, count] : child_res.freq_map) {
                int old_count = res.freq_map[val];
                int new_count = old_count + count;
                res.freq_map[val] = new_count;
                if (new_count > res.max_freq) {
                    res.max_freq = new_count;
                }
                if (H.count(val)) {
                    int req = H.at(val);
                    if (old_count < req && new_count >= req) {
                        res.heavy_satisfied++;
                    }
                }
            }
        }
        
        if (u != 1) {
            if (res.max_freq <= k && res.heavy_satisfied == heavy_needed) {
                good_edges_count++;
            }
        }
        
        return res;
    }
    
public:
    int countGoodEdge(int n, int k, vector<int>& values, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n + 1);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        unordered_map<int, int> total_freq;
        for (int val : values) {
            total_freq[val]++;
        }
        
        unordered_map<int, int> H;
        for (auto const& [val, freq] : total_freq) {
            if (freq > k) {
                H[val] = freq - k;
            }
        }
        
        heavy_needed = H.size();
        good_edges_count = 0;
        
        dfs(1, 0, adj, values, H, k);
        return good_edges_count;
    }
};
```

---

### Q2. Minimum Sum

**Topic:** `trees`, `dfs`, `disjoint-set-union`, `dsu`, `sorting`, `greedy`

**Question:**  
You are given a tree consisting of `n` nodes numbered from `0` to `n-1` and also an array `weight` of length `n` such that `weight[i]` represents the weight of the `i`-th node. You are given a 2D integer array `edges` where `edges[i] = [x, y]` means there exists an undirected edge between `x` and `y`.

For each pair `(i, j)` of nodes (with $i \ne j$), find the weight of the node with the minimum weight that occurs in the simple path between `i` and `j`. Sum these minimum weights over all pairs `(i, j)` with $i < j$, and return that value.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le weight[i] \le 10^5$
- $0 \le edges[i][0], edges[i][1] \le n-1$
- The sum of `n` over all test cases won't exceed $10^6$.

#### Example 1
**Input:**
```text
n = 4
weight = {6, 3, 7, 5}
edges = {{0, 1}, {1, 3}, {0, 2}}
```
**Output:**
```text
21
```
**Explanation:**  
The simple paths and their minimum node weights are:
- `(0, 1)`: path `0 -> 1`, min weight = `min(6, 3) = 3`
- `(0, 2)`: path `0 -> 2`, min weight = `min(6, 7) = 6`
- `(0, 3)`: path `0 -> 1 -> 3`, min weight = `min(6, 3, 5) = 3`
- `(1, 2)`: path `1 -> 0 -> 2`, min weight = `min(3, 6, 7) = 3`
- `(1, 3)`: path `1 -> 3`, min weight = `min(3, 5) = 3`
- `(2, 3)`: path `2 -> 0 -> 1 -> 3`, min weight = `min(7, 6, 3, 5) = 3`

Total sum = `3 + 6 + 3 + 3 + 3 + 3 = 21`.

#### Example 2
**Input:**
```text
n = 5
weight = {6, 1, 2, 5, 3}
edges = {{0, 1}, {1, 2}, {0, 4}, {2, 3}}
```
**Output:**
```text
13
```
**Explanation:**  
The simple paths and their minimum node weights are:
- `(0, 1)`: min weight = `min(6, 1) = 1`
- `(0, 2)`: min weight = `min(6, 1, 2) = 1`
- `(0, 3)`: min weight = `min(6, 1, 2, 5) = 1`
- `(0, 4)`: min weight = `min(6, 3) = 3`
- `(1, 2)`: min weight = `min(1, 2) = 1`
- `(1, 3)`: min weight = `min(1, 2, 5) = 1`
- `(1, 4)`: min weight = `min(1, 6, 3) = 1`
- `(2, 3)`: min weight = `min(2, 5) = 2`
- `(2, 4)`: min weight = `min(2, 1, 6, 3) = 1`
- `(3, 4)`: min weight = `min(5, 2, 1, 6, 3) = 1`

Total sum = `1 + 1 + 1 + 3 + 1 + 1 + 1 + 2 + 1 + 1 = 13`.

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N \log N)$ to sort nodes by weight, plus DSU operations which run in $O(N \alpha(N))$ time.
- **Space Complexity:** $O(N)$ for adjacency lists and DSU structure.

##### Python Implementation
```python
def minimumSum(n, weight, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    parent = list(range(n))
    size = [1] * n
    active = [False] * n
    
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
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            
    # Process nodes by weight in descending order
    nodes = [(weight[i], i) for i in range(n)]
    nodes.sort(key=lambda x: x[0], reverse=True)
    
    total_sum = 0
    for w, u in nodes:
        active[u] = True
        for v in adj[u]:
            if active[v]:
                root_u = find(u)
                root_v = find(v)
                if root_u != root_v:
                    total_sum += size[root_u] * size[root_v] * w
                    union(root_u, root_v)
                    
    return total_sum
```

##### C++ Implementation
```cpp
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
    struct DSU {
        vector<int> parent;
        vector<long long> size;
        
        DSU(int n) {
            parent.resize(n);
            iota(parent.begin(), parent.end(), 0);
            size.assign(n, 1);
        }
        
        int find(int i) {
            if (parent[i] == i)
                return i;
            return parent[i] = find(parent[i]);
        }
        
        void unite(int i, int j) {
            int root_i = find(i);
            int root_j = find(j);
            if (root_i != root_j) {
                parent[root_j] = root_i;
                size[root_i] += size[root_j];
            }
        }
    };
    
public:
    long long minimumSum(int n, vector<int>& weight, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        vector<pair<int, int>> nodes(n);
        for (int i = 0; i < n; ++i) {
            nodes[i] = {weight[i], i};
        }
        
        // Sort in descending order of weights
        sort(nodes.begin(), nodes.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first;
        });
        
        DSU dsu(n);
        vector<bool> active(n, false);
        long long total_sum = 0;
        
        for (const auto& [w, u] : nodes) {
            active[u] = true;
            for (int v : adj[u]) {
                if (active[v]) {
                    int root_u = dsu.find(u);
                    int root_v = dsu.find(v);
                    if (root_u != root_v) {
                        total_sum += dsu.size[root_u] * dsu.size[root_v] * w;
                        dsu.unite(root_u, root_v);
                    }
                }
            }
        }
        
        return total_sum;
    }
};
```

---

### Q3. Good Subarrays

**Topic:** `arrays`, `sliding-window`, `two-pointers`, `frequency-map`, `hash-map`

**Question:**  
Given an integer array `arr[]` of size `n` and an integer `X`. Your task is to count the number of good subarrays of the given array `arr`.  
A subarray `arr[l...r]` is considered to be good if it satisfies the golden condition: the subarray has exactly `X` elements that have occurred at least 3 times in the subarray.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le arr[i] \le 10^5$
- $1 \le X \le n$
- The sum of `n` over all test cases won't exceed $10^5$.

#### Example 1
**Input:**
```text
n = 6
arr = {1, 2, 2, 2, 1, 1}
X = 2
```
**Output:**
```text
1
```
**Explanation:**  
Only the subarray `{1, 2, 2, 2, 1, 1}` satisfies the golden condition because both element `1` (3 times) and element `2` (3 times) occurred at least 3 times.

#### Example 2
**Input:**
```text
n = 7
arr = {1, 2, 2, 3, 3, 2, 3}
X = 1
```
**Output:**
```text
4
```
**Explanation:**  
The 4 subarrays that satisfy the golden condition are:
1. `{1, 2, 2, 3, 3, 2}` (only `2` occurs at least 3 times)
2. `{2, 2, 3, 3, 2}` (only `2` occurs at least 3 times)
3. `{2, 3, 3, 2, 3}` (only `3` occurs at least 3 times)
4. `{3, 3, 2, 3}` (only `3` occurs at least 3 times)

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$ since the two-pointer sliding window traverses the array at most once for each call.
- **Space Complexity:** $O(N)$ for the frequency map.

##### Python Implementation
```python
def goodSubarrays(n, arr, X):
    def solve(k):
        if k <= 0:
            return n * (n + 1) // 2
        
        freq = {}
        count_ge_3 = 0
        l = 0
        ans = 0
        
        for r in range(n):
            val = arr[r]
            freq[val] = freq.get(val, 0) + 1
            if freq[val] == 3:
                count_ge_3 += 1
                
            while count_ge_3 >= k:
                left_val = arr[l]
                if freq[left_val] == 3:
                    count_ge_3 -= 1
                freq[left_val] -= 1
                l += 1
                
            ans += l
            
        return ans

    return solve(X) - solve(X + 1)
```

##### C++ Implementation
```cpp
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    long long solve(int n, const vector<int>& arr, int k) {
        if (k <= 0) {
            return 1LL * n * (n + 1) / 2;
        }
        
        unordered_map<int, int> freq;
        int count_ge_3 = 0;
        int l = 0;
        long long ans = 0;
        
        for (int r = 0; r < n; ++r) {
            int val = arr[r];
            freq[val]++;
            if (freq[val] == 3) {
                count_ge_3++;
            }
            
            while (count_ge_3 >= k) {
                int left_val = arr[l];
                if (freq[left_val] == 3) {
                    count_ge_3--;
                }
                freq[left_val]--;
                l++;
            }
            
            ans += l;
        }
        
        return ans;
    }
    
public:
    long long goodSubarrays(int n, vector<int>& arr, int X) {
        return solve(n, arr, X) - solve(n, arr, X + 1);
    }
};
```


