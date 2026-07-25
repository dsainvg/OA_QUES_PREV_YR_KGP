# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Binary Tree Maximum Path Sum

**Topic:** `Trees`, `DFS`, `Dynamic Programming`

Find the maximum path sum of any non-empty path in a binary tree.

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(H)$

##### Python Implementation
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')
    def gain(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(0, gain(node.left))
        right = max(0, gain(node.right))
        max_sum = max(max_sum, node.val + left + right)
        return node.val + max(left, right)
    gain(root)
    return max_sum
```

##### C++ Implementation
```cpp
#include <algorithm>
#include <climits>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int max_sum = INT_MIN;
    int gain(TreeNode* node) {
        if (!node) return 0;
        int left = max(0, gain(node->left));
        int right = max(0, gain(node->right));
        max_sum = max(max_sum, node->val + left + right);
        return node->val + max(left, right);
    }
public:
    int maxPathSum(TreeNode* root) {
        gain(root);
        return max_sum;
    }
};
```

---

### Q2. Course Schedule II

**Topic:** `Graphs`, `Topological Sort`

Return the ordering of courses you should take to finish all courses given prerequisites.

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(V + E)$
- **Space Complexity:** $\mathcal{O}(V + E)$

##### Python Implementation
```python
from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    adj = defaultdict(list)
    indegree = [0] * numCourses
    for u, v in prerequisites:
        adj[v].append(u)
        indegree[u] += 1
    
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
                
    return order if len(order) == numCourses else []
```

##### C++ Implementation
```cpp
#include <vector>
#include <queue>
using namespace std;

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(numCourses);
    vector<int> indegree(numCourses, 0);
    for (auto& p : prerequisites) {
        adj[p[1]].push_back(p[0]);
        indegree[p[0]]++;
    }
    queue<int> q;
    for (int i = 0; i < numCourses; ++i) if (indegree[i] == 0) q.push(i);
    vector<int> order;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        order.push_back(node);
        for (int neighbor : adj[node]) {
            if (--indegree[neighbor] == 0) q.push(neighbor);
        }
    }
    return order.size() == numCourses ? order : vector<int>();
}
```