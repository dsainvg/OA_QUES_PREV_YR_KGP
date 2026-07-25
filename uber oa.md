# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Reconstruct Itinerary

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

### Q2. Minimum Cost to Cut a Stick

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