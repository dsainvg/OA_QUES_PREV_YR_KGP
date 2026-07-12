# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
   - [Q1. Reach Teammates](#q1-reach-teammates)
   - [Q2. Towers](#q2-towers)

---

## Coding Questions

### Q1. Reach Teammates

**Topic:** `minimum-spanning-tree`, `graphs`, `disjoint-set-union`, `manhattan-distance`  

#### Question Text
Logan is playing a two-dimensional game in which he has $N$ teammates, and the position of his teammates is represented by a 2D array $V$ (containing $X$ and $Y$ coordinates).
He can jump from the $i$-th to the $j$-th teammate if:
$P$ is greater than or equal to the manhattan distance between two points, i.e., $P \ge |X_i - X_j| + |Y_i - Y_j|$.

Find the minimum points $P$ Logan should initially have to reach his teammates from any of the chosen teammates with some jumps.

**Note:**
Logan's objective is to be able to choose a starting teammate such that he can reach any of his teammates from the chosen one with some jumps.
The Manhattan Distance between two points $(X_1, Y_1)$ and $(X_2, Y_2)$ is given by $|X_1 - X_2| + |Y_1 - Y_2|$.

#### Function Description
In the provided code snippet, implement the provided `ReachTeammates(...)` method to find the minimum points $P$ Logan should initially have to reach his teammates from any of the chosen teammates with some jumps.

#### Input Format
- The first line contains an integer $N$ denoting the number of teammates.
- Next $N$ lines contain 2 space-separated integers of 2D array $V$, denoting the $X$ and $Y$ coordinates.

#### Constraints
- $2 \le N \le 200$
- $-10^9 \le X_i, Y_i \le 10^9$

#### Output Format
- The output contains an integer denoting the minimum points $P$ Logan should initially have to reach his teammates from any of the chosen teammates with some jumps.

#### Sample Input
```
4
-10 0
0 0
10 0
11 0
```

#### Sample Output
```
10
```

#### Explanation
Logan chooses the starting teammate as $(0, 0)$, and having 10 points initially, he can reach all his teammates:
- A teammate at $(-10, 0)$ can reach in one jump (manhattan distance between $(0,0)$ and $(-10, 0)$ is 10).
- A teammate at $(10, 0)$ can reach in one jump (manhattan distance between $(0,0)$ and $(10, 0)$ is 10).
- A teammate at $(11, 0)$ can reach in two jumps making the first jump to reach $(10, 0)$ and then another jump to reach $(11, 0)$ (manhattan distance between $(10,0)$ and $(11, 0)$ is 1).
Hence, the output is 10.

#### Python Solution
```python
def ReachTeammates(N, V):
    """
    Finds the minimum points P Logan should initially have to reach all teammates.
    
    Parameters:
    N (int): Number of teammates
    V (list of list of int): 2D array containing [X, Y] coordinates
    
    Returns:
    int: Minimum points P
    """
    edges = []
    # Generate all pairs of teammates and calculate Manhattan distance
    for i in range(N):
        for j in range(i + 1, N):
            dist = abs(V[i][0] - V[j][0]) + abs(V[i][1] - V[j][1])
            edges.append((dist, i, j))
            
    # Sort edges in ascending order of distance
    edges.sort()
    
    # Disjoint Set Union (DSU) implementation
    parent = list(range(N))
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False
        
    components = N
    max_edge = 0
    for dist, u, v in edges:
        if union(u, v):
            components -= 1
            max_edge = max(max_edge, dist)
            if components == 1:
                return max_edge
                
    return 0
```

#### C++ Solution
```cpp
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>

using namespace std;

struct Edge {
    int u, v;
    long long dist;
    bool operator<(const Edge& other) const {
        return dist < other.dist;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int ReachTeammates(int N, int *vptr) {
    // V[N][2] is passed as a flat array.
    // If we want to construct/retrieve points:
    vector<pair<long long, long long>> pts(N);
    for (int i = 0; i < N; i++) {
        // vptr represents 2D array V[N][2]
        pts[i] = { vptr[i * 2], vptr[i * 2 + 1] };
    }
    
    vector<Edge> edges;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            long long dist = abs(pts[i].first - pts[j].first) + abs(pts[i].second - pts[j].second);
            edges.push_back({i, j, dist});
        }
    }
    
    sort(edges.begin(), edges.end());
    DSU dsu(N);
    int components = N;
    long long ans = 0;
    
    for (const auto& edge : edges) {
        if (dsu.unite(edge.u, edge.v)) {
            components--;
            ans = max(ans, edge.dist);
            if (components == 1) {
                return ans;
            }
        }
    }
    return 0;
}
```

---

### Q2. Towers

**Topic:** `dynamic-programming`, `arrays`  

#### Question Text
Alex has a signal of a certain frequency with him and wants to transmit it to the towers.
There are $N$ towers in a row, and each tower has a receiver vibrating at a certain frequency $f_i$.
A tower can receive the signal only if the signal's frequency matches that tower's receiver's frequency.

After receiving the signal, the tower may change the frequency of the signal and then transmit it to the next tower.
If a tower cannot receive the signal, the signal will not be affected and will move to the next tower.
The frequency of the signal can be changed at most $K$ times.

Find the maximum number of towers that will receive the signal.

**Note:**
Initially, Alex can choose any signal frequency and transmit it.

#### Function Description
In the provided code snippet, implement the provided `maximumTower(...)` method to find the maximum number of towers that will receive the signal.

#### Input Format
- The first line contains two integers, $N$, denoting the number of towers, and $K$, denoting the maximum number of changes.
- The second line contains $N$ space-separated integers, denoting the frequency of the receiver of each tower.

#### Constraints
- $1 \le N \le 100$
- $1 \le K \le 50$
- $1 \le f_i \le 100,000$

#### Sample Input
```
5 1
10 10 30 40 30
```

#### Sample Output
```
4
```

#### Explanation
If Alex chooses the initial signal frequency as 10, the first tower will receive the signal and transmit it to the next tower.
After receiving the signal at the second tower, change the frequency to 30 and transmit it to the next tower.
The third tower will receive the signal and transmit it to the next tower.
The fourth tower will not be able to receive the signal, and the signal moves to the next tower.
The fifth tower will receive the signal.
The total number of towers to receive the signal is 4.

#### Python Solution
```python
def maximumTower(N, K, f):
    """
    Finds the maximum number of towers that will receive the signal.
    
    Parameters:
    N (int): Number of towers
    K (int): Maximum number of frequency changes allowed
    f (list of int): Frequencies of the towers
    
    Returns:
    int: Maximum number of towers receiving the signal
    """
    # Cap K at N since we cannot change the frequency more times than the number of towers
    K = min(K, N)
    
    # dp[i][j] stores the max towers that received the signal ending at index i with exactly j changes
    dp = [[0] * (K + 1) for _ in range(N)]
    
    # Base cases for j = 0 (0 changes)
    # The signal must have frequency f[i] from the beginning, so any tower in 0..i
    # with frequency f[i] will receive the signal.
    freq_count = {}
    for i in range(N):
        freq_count[f[i]] = freq_count.get(f[i], 0) + 1
        dp[i][0] = freq_count[f[i]]
        # Initialize dp[i][j] for j >= 1 with the base case of j = 0
        for j in range(1, K + 1):
            dp[i][j] = dp[i][0]
            
    # DP transitions
    for i in range(N):
        for j in range(1, K + 1):
            best_same = 0
            best_diff = 0
            for p in range(i):
                if f[p] == f[i]:
                    best_same = max(best_same, dp[p][j])
                else:
                    best_diff = max(best_diff, dp[p][j - 1])
            
            if best_same > 0:
                dp[i][j] = max(dp[i][j], best_same + 1)
            if best_diff > 0:
                dp[i][j] = max(dp[i][j], best_diff + 1)
                
    # The result is the maximum value in the entire dp table
    ans = 0
    for i in range(N):
        for j in range(K + 1):
            ans = max(ans, dp[i][j])
            
    return ans
```

#### C++ Solution
```cpp
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int maximumTower(int N, int K, int f[]) {
    // Cap K at N since we cannot change the frequency more times than the number of towers
    K = min(K, N);
    
    // dp[i][j] stores the max towers that received the signal ending at index i with exactly j changes
    vector<vector<int>> dp(N, vector<int>(K + 1, 0));
    
    unordered_map<int, int> freq_count;
    for (int i = 0; i < N; i++) {
        freq_count[f[i]]++;
        dp[i][0] = freq_count[f[i]];
        for (int j = 1; j <= K; j++) {
            dp[i][j] = dp[i][0];
        }
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 1; j <= K; j++) {
            int best_same = 0;
            int best_diff = 0;
            for (int p = 0; p < i; p++) {
                if (f[p] == f[i]) {
                    best_same = max(best_same, dp[p][j]);
                } else {
                    best_diff = max(best_diff, dp[p][j - 1]);
                }
            }
            if (best_same > 0) {
                dp[i][j] = max(dp[i][j], best_same + 1);
            }
            if (best_diff > 0) {
                dp[i][j] = max(dp[i][j], best_diff + 1);
            }
        }
    }
    
    int ans = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= K; j++) {
            ans = max(ans, dp[i][j]);
        }
    }
    return ans;
}
```
