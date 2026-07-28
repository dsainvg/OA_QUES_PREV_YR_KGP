# Interview Questions

*Total questions: 5*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Request Redirection

`[Latest]`

**Topic:** `Greedy`, `Binary Search`, `Two Pointers`

#### Description
There are $n$ servers for deploying applications. Server $i$ can handle a maximum of `max_req[i]` requests, but currently has `requests[i]` requests to serve.

To balance the load, some requests must be redirected between servers. The latency when redirecting from server $i$ to server $j$ is $|i - j|$. The goal is to find the minimum possible maximum latency (min-max latency) when redirecting requests optimally, ensuring no server exceeds its capacity.

If it is impossible to serve all requests, return `-1`.

#### Function Description
Complete the function `getMinLatency` in the editor.
- `requests`: A list of requests currently assigned to each server.
- `max_req`: A list of the maximum capacity of each server.

#### Returns
- `int`: The minimal max_latency possible, or `-1` if it is impossible to satisfy all requests.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le requests[i] \le 10^9$
- $1 \le max\_req[i] \le 10^9$

#### Sample Cases

**Sample Case 0**
- **Input:**
  - `requests = [1, 2, 3, 4]`
  - `max_req = [2, 3, 4, 5]`
- **Output:** `0`
- **Explanation:**
  Since $requests[i] \le max\_req[i]$ for all $i$, each request can be served by the server it came to. No redirection is needed, so latency is `0`.

**Sample Case 1**
- **Input:**
  - `requests = [4, 3]`
  - `max_req = [2, 3]`
- **Output:** `-1`
- **Explanation:**
  The total number of requests is 7, while the total capacity of the servers is only 5. Thus, it's impossible to satisfy all requests.

**Sample Case 2**
- **Input:**
  - `requests = [1, 3, 2, 4]`
  - `max_req = [2, 1, 5, 3]`
- **Output:** `1`
- **Explanation:**
  Optimal redirections:
  - Redirect 2 requests from server 2 to server 3.
  - Redirect 1 request from server 4 to server 3.
  The maximum latency is $\max(|2 - 3|, |4 - 3|) = 1$.

#### Python Solution
```python
def getMinLatency(requests, max_req):
    if sum(requests) > sum(max_req):
        return -1
    n = len(requests)
    
    def check(d):
        c = list(max_req)
        ptr = 0
        for i, r in enumerate(requests):
            if r == 0:
                continue
            ptr = max(ptr, i - d)
            limit = min(n - 1, i + d)
            while r > 0 and ptr <= limit:
                val = c[ptr]
                if r >= val:
                    r -= val
                    c[ptr] = 0
                    ptr += 1
                else:
                    c[ptr] = val - r
                    r = 0
            if r > 0:
                return False
        return True

    low, high = 0, n - 1
    ans = n - 1
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
```

---

### Q2. Word Matching

`[Latest]`

**Topic:** `Greedy`, `String`, `Math / Divisibility`

#### Description
Two strings $a$ and $b$ are considered matching if $a$ can be converted to $b$ using the following operations any number of times:
1. Choose an integer $k > 1$.
2. **Operation Type 1:** Select any index $i$ ($1 \le i < \text{length}(a)$) and swap $a[i]$ with $a[i+1]$.
3. **Operation Type 2:** Select a substring of length $k$ where all characters are the same and increase each character to its alphabetically next character (e.g., `"aa"` $\to$ `"bb"`). Note: A substring containing `'z'` cannot be incremented.

Given two arrays of strings `words1` and `words2` with $n$ words each, determine if each pair of strings `words1[i]` and `words2[i]` are matching. Return an array where the $i$-th element is `1` if the pair is matching, and `0` otherwise.

#### Constraints
- $1 \le n \le 100$
- $1 \le \text{length}(words1[i]) \le 1000$
- $1 \le \text{length}(words2[i]) \le 1000$
- `words1[i]` and `words2[i]` consist of lowercase English letters only.

#### Sample Cases

**Sample Case 0**
- **Input:**
  - `words1 = ["acbcdd", "abc", "abcde"]`
  - `words2 = ["abeded", "aab", "ab"]`
- **Output:** `[1, 0, 0]`
- **Explanation:**
  - For pair 0: `"acbcdd"` can be converted to `"abeded"` using $k = 2$:
    - Swap characters to get: `"acbcdd"` $\to$ `"abccdd"`.
    - Apply Type 2 operation twice on `"cc"` to get `"ee"`: `"abccdd"` $\to$ `"abeedd"`.
    - Swap characters to get: `"abeedd"` $\to$ `"abeded"`.
  - For pair 1: `"abc"` cannot be converted to `"aab"`.
  - For pair 2: `"abcde"` cannot be converted to `"ab"` (lengths are different).

#### Python Solution
```python
def checkMatchingStrings(words1, words2):
    res = []
    for a, b in zip(words1, words2):
        if len(a) != len(b):
            res.append(0)
            continue
        if a == b:
            res.append(1)
            continue
        count_a = [0] * 26
        count_b = [0] * 26
        for char in a:
            count_a[ord(char) - 97] += 1
        for char in b:
            count_b[ord(char) - 97] += 1
        
        matched = False
        # Try all possible block sizes k
        for k in range(2, len(a) + 1):
            excess = 0
            possible = True
            for i in range(25):
                have = count_a[i] + excess
                need = count_b[i]
                if have < need or (have - need) % k != 0:
                    possible = False
                    break
                excess = have - need
            if possible and count_a[25] + excess == count_b[25]:
                matched = True
                break
        res.append(1 if matched else 0)
    return res
```

---

### Q3. Neural Network Neuron Vigor

`[Latest]`

**Topic:** `Tree DP`, `Rerooting DP`, `DFS/BFS`

#### Description
A neural network has $n$ neurons numbered from $1$ to $n$. If the $i$-th neuron has strong connectivity, `strongConnectivity[i] = 1`. If it has weak connectivity, `strongConnectivity[i] = 0`.

The neurons form a tree-like network with $n-1$ connections, where the $i$-th connection connects neurons `neuronFrom[i]` and `neuronTo[i]`. A neuron's strength is defined as the maximum difference between strongly connected and weakly connected neurons in any subnetwork (connected subgraph) including that neuron.

Return an array of $n$ integers, where the $i$-th integer represents the strength of neuron $i$ (1-indexed).

#### Constraints
- $1 \le n \le 2 \cdot 10^5$
- $1 \le neuronFrom[i], neuronTo[i] \le n$
- `strongConnectivity[i]` is either `0` or `1`

#### Sample Cases

**Sample Case 0**
- **Input:**
  - `n = 4`
  - `neuronFrom = [1, 1, 1]`
  - `neuronTo = [2, 3, 4]`
  - `strongConnectivity = [0, 0, 1, 0]`
- **Output:** `[0, -1, 1, -1]`
- **Explanation:**
  - Neuron 3 has strong connectivity.
  - For neuron 1, the best subnetwork is $\{1, 3\}$, having 1 strong and 1 weak neuron $\to$ strength = $1 - 1 = 0$.
  - For neuron 2, the best subnetwork is $\{1, 2, 3\}$, having 1 strong and 2 weak neurons $\to$ strength = $1 - 2 = -1$.
  - For neuron 3, the best subnetwork is $\{3\}$ containing only itself $\to$ strength = $1 - 0 = 1$.
  - For neuron 4, the best subnetwork is $\{4\}$ containing only itself $\to$ strength = $0 - 1 = -1$.

**Sample Case 1**
- **Input:**
  - `n = 5`
  - `neuronFrom = [1, 1, 3, 3]`
  - `neuronTo = [2, 3, 4, 5]`
  - `strongConnectivity = [1, 1, 1, 1, 1]`
- **Output:** `[5, 5, 5, 5, 5]`
- **Explanation:**
  Since all neurons have strong connectivity, the best subnetwork for any neuron is the entire tree of size 5 $\to$ strength = 5.

#### Python Solution
```python
from collections import deque

def getNeuronStrengths(neuron_nodes, neuron_from, neuron_to, strong_connectivity):
    n = neuron_nodes
    adj = [[] for _ in range(n)]
    for u, v in zip(neuron_from, neuron_to):
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    # BFS to find parent relationships and topological ordering from root 0
    parent = [-1] * n
    order = []
    queue = deque([0])
    parent[0] = -2
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                queue.append(v)
                
    # Assign weights: +1 for strong, -1 for weak connectivity
    w = [1 if x == 1 else -1 for x in strong_connectivity]
    
    # Bottom-up DP: dp[u] stores the max connected weight in subtree of u containing u
    dp = list(w)
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                if dp[v] > 0:
                    dp[u] += dp[v]
                    
    # Top-down rerooting pass: up[u] is the max connected weight outside u's subtree containing parent
    up = [0] * n
    ans = [0] * n
    ans[0] = dp[0]
    for u in order:
        if u == 0:
            continue
        p = parent[u]
        up[u] = ans[p] - max(0, dp[u])
        ans[u] = dp[u] + max(0, up[u])
        
    return ans
```

---

### Q4. Minimum Operations to Balance Array

**Topic:** `Arrays`, `Greedy`, `Two Pointers`

Given an array of positive integers, calculate the minimum number of operations required to make all adjacent element differences equal to a given target $K$.

#### Input
- `arr`: list of integers
- `k`: integer

#### Constraints
- $1 \le \text{len}(arr) \le 10^5$
- $1 \le k \le 10^9$

#### Example 1
**Input:** `arr = [2, 4, 6, 8], k = 2`  
**Output:** `0`  

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

##### Python Implementation
```python
def minOperations(arr, k):
    ops = 0
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        if diff != k:
            ops += abs(diff - k)
    return ops
```

##### C++ Implementation
```cpp
#include <vector>
#include <cmath>
using namespace std;

int minOperations(vector<int>& arr, int k) {
    int ops = 0;
    for (size_t i = 1; i < arr.size(); ++i) {
        int diff = abs(arr[i] - arr[i-1]);
        if (diff != k) ops += abs(diff - k);
    }
    return ops;
}
```

---

## MCQs

---

### Q5. Time Complexity of Search in Balanced BST

**Topic:** `Data Structures`, `Trees`

What is the worst-case time complexity for searching an element in a balanced Binary Search Tree (BST) of $N$ nodes?

**Options:**
- A) $\mathcal{O}(1)$
- B) $\mathcal{O}(\log N)$
- C) $\mathcal{O}(N)$
- D) $\mathcal{O}(N \log N)$

**Correct Answer:** **B) $\mathcal{O}(\log N)$**  
**Explanation:** In a balanced BST, height is bounded by $\log_2 N$. Thus searching takes logarithmic time.

