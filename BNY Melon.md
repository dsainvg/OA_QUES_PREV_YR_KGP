# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [SQL Questions](#sql-questions)
3. [Theoretical Questions](#theoretical-questions)
4. [System Design Questions](#system-design-questions)
5. [Behavioral Questions](#behavioral-questions)
6. [MCQs](#mcqs)
7. [Puzzles](#puzzles)

---

## Coding Questions

### Q1. Maximum Cluster Quality

**Topic:** `greedy`, `heap`, `sorting`, `priority-queue`  

When building a computing cluster consisting of several machines, two parameters are most important: **speed** and **reliability**. The quality of a computing cluster is the sum of its machines' speeds multiplied by the minimum reliability of its machines.

Given information about several available machines, select machines to create a cluster of less than or equal to a particular size. Determine the maximum quality of cluster that can be created.

#### Function Description
Complete the function `maxClusterQuality` in the editor below.

`maxClusterQuality` has the following parameter(s):
* `int speed[n]`: an integer array of size $n$, such that `speed[i]` is the speed of the $i$-th machine
* `int reliability[n]`: an integer array of size $n$, such that `reliability[i]` is the reliability of the $i$-th machine
* `int maxMachines`: an integer denoting the maximum number of machines you want in a cluster

#### Returns
* `long long` (or `int` depending on arbitrary precision in Python): the maximum quality of a computing cluster that can be built.

#### Constraints
* $1 \le n \le 10^5$
* $1 \le speed[i] \le 10^5$
* $1 \le reliability[i] \le 10^5$
* $1 \le maxMachines \le n$

#### Example
```text
n = 5
speed = [4, 3, 15, 5, 6]
reliability = [7, 6, 1, 2, 8]
maxMachines = 3
```
The maximum number of machines to use is `maxMachines = 3` chosen from `n = 5` available machines.
Select the first, second, and fifth machines. The quality of the cluster is:
`(speed[0] + speed[1] + speed[4]) * min(reliability[0], reliability[1], reliability[4]) = (4 + 3 + 6) * min(7, 6, 8) = 13 * 6 = 78`.
This is the highest quality that can be achieved, so the answer is `78`.

#### Sample Case 0
**Sample Input**
```text
5 -> speed[] size n = 5
12 -> speed[] = [12, 112, 100, 13, 55]
112
100
13
55
5 -> reliability[] size n = 5
31 -> reliability[] = [31, 4, 100, 55, 50]
4
100
55
50
3 -> maxMachines = 3
```
**Sample Output**
```text
10000
```
**Explanation**
There are 5 machines available. Their speeds are 12, 112, 100, 13, and 55 respectively, while their reliabilities are 31, 4, 100, 55, and 50 respectively. The maximum number of machines allowed in a cluster is 3.
The best quality of a cluster can be achieved by selecting only the third machine. The quality of a cluster will be `100 * 100 = 10000`.

#### Python 3 Solution

```python
import heapq

def maxClusterQuality(speed, reliability, maxMachines):
    # Pair each machine's speed and reliability and sort by reliability in descending order
    machines = sorted(zip(reliability, speed), key=lambda x: x[0], reverse=True)
    
    max_quality = 0
    speed_sum = 0
    min_heap = []
    
    for rel, spd in machines:
        heapq.heappush(min_heap, spd)
        speed_sum += spd
        
        # If the size of the cluster exceeds maxMachines, remove the machine with the smallest speed
        if len(min_heap) > maxMachines:
            speed_sum -= heapq.heappop(min_heap)
            
        # The current reliability is the minimum reliability of all machines currently in the cluster
        max_quality = max(max_quality, speed_sum * rel)
        
    return max_quality
```

#### C++ Solution

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

long long maxClusterQuality(vector<int>& speed, vector<int>& reliability, int maxMachines) {
    int n = speed.size();
    vector<pair<int, int>> machines(n);
    for (int i = 0; i < n; ++i) {
        machines[i] = {reliability[i], speed[i]};
    }
    
    // Sort machines by reliability in descending order
    sort(machines.rbegin(), machines.rend());
    
    priority_queue<int, vector<int>, greater<int>> min_heap;
    long long speed_sum = 0;
    long long max_quality = 0;
    
    for (int i = 0; i < n; ++i) {
        int rel = machines[i].first;
        int spd = machines[i].second;
        
        min_heap.push(spd);
        speed_sum += spd;
        
        if (min_heap.size() > maxMachines) {
            speed_sum -= min_heap.top();
            min_heap.pop();
        }
        
        max_quality = max(max_quality, speed_sum * rel);
    }
    
    return max_quality;
}
```

---

### Q2. Minimum Leaves to Remove

**Topic:** `trees`, `dfs`, `graphs`, `depth-first-search`  

The country of Hackerland can be represented as a tree of `tree_nodes` nodes numbered from 1 to `tree_nodes`. The $i$-th edge is a bidirectional connection between the nodes numbered `tree_from[i]` and `tree_to[i]` and has a weight `tree_weight[i]`. Each node $i$ is associated with an integer `arr[i]`. The tree is rooted at node index 1.

A tree is *special* if for every node $u$ and every ancestor $a$ of $u$ in the tree, we have:
$$arr[u] \ge distance(a, u)$$
where $distance(a, u)$ is the sum of weights of the edges on the unique path between nodes $a$ and $u$.

A leaf of the tree is a node connected to a single node by a single edge. In one operation, any one leaf is removed from the tree. The root of the tree cannot be removed. Find the minimum number of leaves that must be removed in order to make the tree special. (Note: Removing a node also removes its connection, potentially making its parent a leaf, which can then be removed in subsequent operations).

#### Function Description
Complete the function `getMinLeavesToRemove` in the editor below.

`getMinLeavesToRemove` has the following parameters:
* `int tree_nodes`: the number of nodes
* `int tree_from[tree_edges]`: one end of each edge
* `int tree_to[tree_edges]`: the other end of each edge
* `int tree_weight[tree_edges]`: edge weights
* `arr[tree_nodes]`: an array of integers (1-indexed node values)

#### Returns
* `int`: the minimum number of leaves that need to be removed from the tree to make it special.

#### Constraints
* $1 \le tree\_nodes \le 10^5$
* `tree_edges` = `tree_nodes` - 1
* The graph is connected
* $1 \le tree\_from[i], tree\_to[i] \le tree\_nodes$
* $-10^9 \le tree\_weight[i] \le 10^9$
* $1 \le arr[i] \le 10^9$

#### Example
```text
tree_nodes = 5
arr = [12, 2, 27, 11, 1]
tree_from = [1, 1, 3, 3]
tree_to = [2, 3, 4, 5]
tree_weight = [8, 5, 2, 7]
```
* Node labels are `<node number>:<arr[node number]>`.
* Node 1: The root is not removed.
* Node 2: Test `arr[2] > dist(node 2, node 1)`, i.e. $2 > 8$ is false, so remove the node.
* Node 3: Test `arr[3] > dist(node 3, node 1)`, i.e. $27 > 5$ is true, so the node remains.
* Node 4: Test `11 > 2` and `11 > 2 + 5`. Both are true, so node remains.
* Node 5: Test `1 > 7`. This is false, so remove node 5.

The minimum number of leaves that must be removed is `2` (nodes 2 and 5).

#### Python 3 Solution

```python
import sys
# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def getMinLeavesToRemove(tree_nodes, tree_from, tree_to, tree_weight, arr):
    # Build adjacency list
    adj = [[] for _ in range(tree_nodes + 1)]
    for i in range(len(tree_from)):
        u = tree_from[i]
        v = tree_to[i]
        w = tree_weight[i]
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    # Calculate subtree sizes
    subtree_size = [0] * (tree_nodes + 1)
    
    def calc_subtree_size(u, p):
        size = 1
        for v, w in adj[u]:
            if v != p:
                size += calc_subtree_size(v, u)
        subtree_size[u] = size
        return size
        
    calc_subtree_size(1, 0)
    
    # DFS to count the removed nodes
    def dfs(u, p, current_depth, min_ancestor_depth):
        # Root node (1) cannot be removed and has no ancestors
        if u != 1:
            # Check if there is some ancestor that makes this node bad
            if current_depth - min_ancestor_depth > arr[u - 1]:
                # If u is bad, we must remove it and its entire subtree
                return subtree_size[u]
                
        removed_count = 0
        new_min_ancestor = min(min_ancestor_depth, current_depth)
        for v, w in adj[u]:
            if v != p:
                removed_count += dfs(v, u, current_depth + w, new_min_ancestor)
        return removed_count

    return dfs(1, 0, 0, float('inf'))
```

#### C++ Solution

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

struct Edge {
    int to;
    long long weight;
};

void calcSubtreeSize(int u, int p, const vector<vector<Edge>>& adj, vector<int>& subtree_size) {
    subtree_size[u] = 1;
    for (auto& edge : adj[u]) {
        if (edge.to != p) {
            calcSubtreeSize(edge.to, u, adj, subtree_size);
            subtree_size[u] += subtree_size[edge.to];
        }
    }
}

int dfs(int u, int p, long long current_depth, long long min_ancestor_depth,
        const vector<vector<Edge>>& adj, const vector<int>& subtree_size, const vector<int>& arr) {
    if (u != 1) {
        if (current_depth - min_ancestor_depth > arr[u - 1]) {
            return subtree_size[u];
        }
    }
    
    int removed_count = 0;
    long long new_min_ancestor = min(min_ancestor_depth, current_depth);
    for (auto& edge : adj[u]) {
        if (edge.to != p) {
            removed_count += dfs(edge.to, u, current_depth + edge.weight, new_min_ancestor, adj, subtree_size, arr);
        }
    }
    return removed_count;
}

int getMinLeavesToRemove(int tree_nodes, vector<int>& tree_from, vector<int>& tree_to, vector<int>& tree_weight, vector<int>& arr) {
    vector<vector<Edge>> adj(tree_nodes + 1);
    for (size_t i = 0; i < tree_from.size(); ++i) {
        int u = tree_from[i];
        int v = tree_to[i];
        long long w = tree_weight[i];
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    
    vector<int> subtree_size(tree_nodes + 1, 0);
    calcSubtreeSize(1, 0, adj, subtree_size);
    
    return dfs(1, 0, 0LL, LLONG_MAX, adj, subtree_size, arr);
}
```

---

## SQL Questions

*No SQL questions were found in the source files.*

---

## Theoretical Questions

*No theoretical questions were found in the source files.*

---

## System Design Questions

*No system design questions were found in the source files.*

---

## Behavioral Questions

*No behavioral questions were found in the source files.*

---

## MCQs

*No MCQs were found in the source files.*

---

## Puzzles

*No puzzles were found in the source files.*
