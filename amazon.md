# Interview Questions

*Total questions: 11*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [SQL Questions](#sql-questions)

---

## Coding Questions

### Q1. Fulfillment Station Target Display (Min Cost to Make Array Equal)

`[Latest]`

**Topic:** `Array`, `Greedy`

### Problem Description
You are given an array `arr` of length $N$ representing the target display value at each Amazon fulfillment station. The stations are lined up from left to right.

You can perform the following operations any number of times (possibly zero):
- **Prefix Operation:** Choose an index $i$ ($1 \le i \le N - 1$) and set all positions $0, 1, \dots, i-1$ to $arr[i]$. This operation costs $i \times arr[i]$.
- **Suffix Operation:** Choose an index $i$ ($0 \le i \le N - 2$) and set all positions $i+1, i+2, \dots, N-1$ to $arr[i]$. This operation costs $(N - 1 - i) \times arr[i]$.

Compute the minimum total cost to make all array elements equal.

### Constraints
- $1 \le N \le 2 \times 10^5$
- $1 \le arr[i] \le N$

### Sample Cases

#### Sample Input 0
```
5
1
1
2
1
1
```

#### Sample Output 0
```
3
```

#### Explanation 0
To make all elements equal to `1`:
- Choose index $i = 1$ (value `1`) and set position $0$ to $arr[1] = 1$. Cost is $1 \times 1 = 1$. The array remains `[1, 1, 2, 1, 1]`.
- Choose index $i = 1$ (value `1`) and set positions $2, 3, 4$ to $arr[1] = 1$. Cost is $(5 - 1 - 1) \times 1 = 3$. The array becomes `[1, 1, 1, 1, 1]`.
- Total cost = $3$. No sequence yields a smaller total cost.

#### Sample Input 1
```
3
1
1
3
```

#### Sample Output 1
```
1
```

#### Explanation 1
- Choose index $i = 1$ (value `1`) and set position $2$ to $arr[1] = 1$. Cost is $(3 - 1 - 1) \times 1 = 1$. The array becomes `[1, 1, 1]`.
- Total cost = $1$.

---

### Python Solution

```python
import sys

def getMinCost(arr):
    n = len(arr)
    ans = float('inf')
    i = 0
    while i < n:
        j = i
        while j < n and arr[j] == arr[i]:
            j += 1
        # We keep the block arr[i...j-1] as is.
        # Cost to set prefix arr[0...i-1] to arr[i] is i * arr[i]
        # Cost to set suffix arr[j...n-1] to arr[i] is (n - j) * arr[i]
        # Total cost is (i + n - j) * arr[i]
        ans = min(ans, arr[i] * (n - (j - i)))
        i = j
    return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:1+n]]
    print(getMinCost(arr))

if __name__ == "__main__":
    main()
```

---

### Q2. Energy Path in Booster Graph (Minimum Booster Power)

`[Latest]`

**Topic:** `Graph`, `BFS`, `Dijkstra`, `DSU`, `Kruskal`

### Problem Description
Bob is exploring an undirected, unweighted graph with $N$ nodes and $M$ edges. Among these nodes, there are $K$ special nodes known as energy boosters. Each booster node provides a power value $P$ whenever Bob visits it.
When Bob's current power is $x$, he can move across an edge by spending $1$ unit of power. If he reaches another energy booster node, his power is restored to $P$.

Bob wants to determine the minimum possible value of $P$ that allows him to travel from node $1$ to node $N$ without his power ever becoming negative, and such that his power never exceeds $P$ during the journey.
If it is impossible for Bob to reach node $N$, return $-1$.

You may assume:
- Node $1$ is always an energy booster node.
- Bob can revisit nodes any number of times.

### Constraints
- $1 \le N \le 10^5$
- $0 \le M \le 2 \times 10^5$
- $1 \le K \le N$
- $1$-based indexing is followed.
- The graph does not contain self-loops or multiple edges.

---

### Python Solution

```python
import sys
from collections import deque
import heapq

def solve(N, M, K, energy, edges):
    # Boosters set always includes 1 and N as sources (start and destination act as boosters/fully charged)
    boosters = set(energy)
    boosters.add(1)
    boosters.add(N)
    
    # Step 1: Multi-source BFS from all boosters to find distance to nearest booster and its identity
    dist = [-1] * (N + 1)
    closest = [0] * (N + 1)
    queue = deque()
    
    for b in boosters:
        dist[b] = 0
        closest[b] = b
        queue.append(b)
        
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    while queue:
        u = queue.popleft()
        d = dist[u]
        c = closest[u]
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = d + 1
                closest[v] = c
                queue.append(v)
                
    # Step 2: Build a virtual graph on boosters
    adj_prime = {b: {} for b in boosters}
    for u, v in edges:
        if dist[u] == -1 or dist[v] == -1:
            continue
        bu = closest[u]
        bv = closest[v]
        if bu != bv:
            w = dist[u] + 1 + dist[v]
            if bv not in adj_prime[bu] or w < adj_prime[bu][bv]:
                adj_prime[bu][bv] = w
                adj_prime[bv][bu] = w
                
    # Step 3: Dijkstra to find minimax path from 1 to N
    minimax = {b: float('inf') for b in boosters}
    minimax[1] = 0
    pq = [(0, 1)]
    
    while pq:
        w, u = heapq.heappop(pq)
        if w > minimax[u]:
            continue
        if u == N:
            return w
        for v, weight in adj_prime[u].items():
            next_w = max(w, weight)
            if next_w < minimax[v]:
                minimax[v] = next_w
                heapq.heappush(pq, (next_w, v))
                
    return -1
```

### C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

int solve(int N, int M, int K, const vector<int>& energy, const vector<pair<int, int>>& edges) {
    unordered_set<int> boosters(energy.begin(), energy.end());
    boosters.insert(1);
    boosters.insert(N);

    vector<int> dist(N + 1, -1);
    vector<int> closest(N + 1, 0);
    queue<int> q;

    for (int b : boosters) {
        dist[b] = 0;
        closest[b] = b;
        q.push(b);
    }

    vector<vector<int>> adj(N + 1);
    for (const auto& edge : edges) {
        adj[edge.first].push_back(edge.second);
        adj[edge.second].push_back(edge.first);
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        int d = dist[u];
        int c = closest[u];
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = d + 1;
                closest[v] = c;
                q.push(v);
            }
        }
    }

    unordered_map<int, unordered_map<int, int>> adj_prime;
    for (int b : boosters) {
        adj_prime[b] = unordered_map<int, int>();
    }

    for (const auto& edge : edges) {
        int u = edge.first;
        int v = edge.second;
        if (dist[u] == -1 || dist[v] == -1) continue;
        int bu = closest[u];
        int bv = closest[v];
        if (bu != bv) {
            int w = dist[u] + 1 + dist[v];
            if (adj_prime[bu].find(bv) == adj_prime[bu].end() || w < adj_prime[bu][bv]) {
                adj_prime[bu][bv] = w;
                adj_prime[bv][bu] = w;
            }
        }
    }

    unordered_map<int, int> minimax;
    for (int b : boosters) {
        minimax[b] = 1e9;
    }
    minimax[1] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 1});

    while (!pq.empty()) {
        auto [w, u] = pq.top();
        pq.pop();

        if (w > minimax[u]) continue;
        if (u == N) return w;

        for (const auto& [v, weight] : adj_prime[u]) {
            int next_w = max(w, weight);
            if (next_w < minimax[v]) {
                minimax[v] = next_w;
                pq.push({next_w, v});
            }
        }
    }

    return -1;
}
```

---

### Q3. Returns Evaluation Engine (Software Design Project)

`[Latest]`

**Topic:** `Object-Oriented Design`, `DSU`, `JSON Parsing`

### Problem Description
You are tasked with building a return evaluation system. It takes input rules defined in JSON files, profiles of accounts from JSON lines, and link relationships between accounts (representing accounts owned by the same user), and computes the risk score and final decision (AUTO_APPROVE, MANUAL_REVIEW, REJECT) for incoming return requests.

The rules are defined as follows:
- **Category Rules:** Defines if a category is returnable and the return window (in days).
- **Scoring Rules:** Lists the risk points based on various conditions for total return history, account age, and order value.
- **Decision Bands:** Maps the final total risk score ranges to decisions.
- **Account Profiles:** Initial return history counts for accounts.
- **Account Links:** Relates accounts. Accounts linked together share the total sum of all their individual return histories.

### C++ Solution

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

struct J {
    enum T {N,B,NUM,S,A,O} t=N; bool b=0; double n=0; string s; vector<J> a; map<string,J> o;
    bool has(string k)const{ return t==O&&o.count(k); }
    J at(string k)const{ return has(k)?o.at(k):J(); }
};

struct P {
    string x; size_t i=0;
    void ws(){ while(i<x.size() && isspace((unsigned char)x[i])) i++; }
    string str(){
        string r; i++;
        while(i<x.size() && x[i]!='"') {
            if(x[i]=='\\') { i++; r+=(x[i]=='n'?'\n':x[i]=='t'?'\t':x[i]=='r'?'\r':x[i]); }
            else r+=x[i];
            i++;
        }
        i++; return r;
    }
    J val(){
        ws(); if(i>=x.size()) return {};
        J j;
        if(x[i]=='{'){
            j.t=J::O; i++; ws();
            while(i<x.size() && x[i]!='}') {
                string k=str(); ws(); i++; j.o[k]=val(); ws(); if(x[i]==',') i++;
            }
            i++; return j;
        }
        if(x[i]=='['){
            j.t=J::A; i++; ws();
            while(i<x.size() && x[i]!=']'){
                j.a.push_back(val()); ws(); if(x[i]==',') i++;
            }
            i++; return j;
        }
        if(x[i]=='"') { j.t=J::S; j.s=str(); return j; }
        if(x.compare(i,4,"true")==0) { i+=4; j.t=J::B; j.b=1; return j; }
        if(x.compare(i,5,"false")==0) { i+=5; j.t=J::B; return j; }
        if(x.compare(i,4,"null")==0) { i+=4; return j; }
        j.t=J::NUM; size_t p=i;
        while(i<x.size() && (isdigit((unsigned char)x[i])||x[i]=='-'||x[i]=='.'||x[i]=='e'||x[i]=='E'||x[i]=='+')) i++;
        j.n=stod(x.substr(p,i-p)); return j;
    }
};

string readf(string p){ ifstream f(p); return string((istreambuf_iterator<char>(f)),{}); }
J parsef(string p){ return P{readf(p)}.val(); }
string js(const J& j){ return j.t==J::S?j.s:""; }
int ji(const J& j){ return j.t==J::NUM?(int)llround(j.n):0; }
bool jb(const J& j){ return j.t==J::B?j.b:ji(j)!=0; }

vector<J> lines(string p){
    ifstream f(p); string s; vector<J> v;
    while(getline(f,s)) if(s.find_first_not_of(" \t\r\n")!=string::npos) v.push_back(P{s}.val());
    return v;
}

void collect(const J& j, string k, vector<J>& v){
    if(j.t==J::O){
        if(j.has(k)) v.push_back(j);
        for(auto& p:j.o) collect(p.second,k,v);
    } else if(j.t==J::A) for(auto& e:j.a) collect(e,k,v);
}

int getint(const J& j, initializer_list<string> ks){
    for(auto& k:ks) if(j.has(k)) return ji(j.at(k));
    return 0;
}

string getstr(const J& j, initializer_list<string> ks){
    for(auto& k:ks) if(j.has(k)) return js(j.at(k));
    return "";
}

struct Cat{bool ret=0; int win=0;};
struct Range{int mn=0,mx=0,pts=0;};
struct Rule{string attr; vector<Range> rs;};
struct Band{int mn=0,mx=0; string dec;};
struct Prof{int hist=0;};
struct Req{string id,acc,cat; int days=0,age=0,val=0;};

struct DSU {
    unordered_map<string,string> p;
    string find(string x){ return !p.count(x)?p[x]=x:(p[x]==x?x:p[x]=find(p[x])); }
    void unite(string a,string b){ string x=find(a),y=find(b); if(x!=y) p[y]=x; }
};

string esc(string s){
    string r; for(char c:s){ if(c=='"'||c=='\\') r+='\\'; r+=c; } return r;
}

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    unordered_map<string,Cat> cats; vector<J> cv; collect(parsef("data/category_rules.json"),"category",cv);
    for(auto& j:cv){
        string c=getstr(j,{"category","name"});
        if(!c.empty()) cats[c]={jb(j.at("returnable")),getint(j,{"allowed_return_window_days","return_window_days","max_return_window_days"})};
    }
    
    vector<Rule> rules; vector<J> rv; collect(parsef("data/scoring_rules.json"),"rule",rv);
    for(auto& j:rv){
        Rule r{js(j.at("rule"))};
        for(auto& e:j.at("ranges").a) r.rs.push_back({getint(e,{"min"}),getint(e,{"max"}),getint(e,{"points"})});
        rules.push_back(r);
    }
    
    vector<Band> bands; vector<J> bv; collect(parsef("data/decision_bands.json"),"decision",bv);
    for(auto& j:bv) bands.push_back({getint(j,{"min","min_score","score_min"}),getint(j,{"max","max_score","score_max"}),js(j.at("decision"))});
    
    unordered_map<string,Prof> prof; DSU dsu;
    for(auto& j:lines("data/account_profiles.jsonl")){
        string a=js(j.at("account_id")); prof[a]={getint(j,{"return_history_count"})}; dsu.find(a);
    }
    for(auto& j:lines("data/account_links.jsonl")){
        string a=js(j.at("primary_account_id")), b=js(j.at("related_account_id"));
        if(!a.empty()&&!b.empty()) dsu.unite(a,b);
    }
    
    unordered_map<string,vector<string>> grp;
    for(auto& p:dsu.p) grp[dsu.find(p.first)].push_back(p.first);
    
    vector<Req> reqs;
    for(auto& j:lines("data/returns.jsonl")){
        Req r{js(j.at("request_id")), js(j.at("account_id")), js(j.at("category")), getint(j,{"days_since_purchase"}), getint(j,{"account_age_days"}), getint(j,{"order_value_usd","order_amount","order_value"})};
        reqs.push_back(r); dsu.find(r.acc);
    }
    for(auto& r:reqs) grp[dsu.find(r.acc)].push_back(r.acc);
    
    ofstream out("data/results.jsonl");
    for(auto& q:reqs){
        auto ci=cats.find(q.cat);
        if(ci==cats.end() || !ci->second.ret){
            out<<"{\"request_id\":\""<<esc(q.id)<<"\",\"risk_score\":null,\"decision\":\"REJECT\",\"reason\":\"CATEGORY_NON_RETURNABLE\"}\n"; continue;
        }
        if(q.days>ci->second.win){
            out<<"{\"request_id\":\""<<esc(q.id)<<"\",\"risk_score\":null,\"decision\":\"REJECT\",\"reason\":\"RETURN_WINDOW_EXPIRED\"}\n"; continue;
        }
        
        int hist=0; unordered_set<string> seen;
        for(auto& a:grp[dsu.find(q.acc)]) if(seen.insert(a).second) hist+=prof[a].hist;
        
        int score=0;
        for(auto& r:rules){
            int x=(r.attr=="total_return_history"?hist:(r.attr=="account_age_days"?q.age:q.val));
            for(auto& g:r.rs) if(x>=g.mn && x<=g.mx){ score+=g.pts; break; }
        }
        score=max(0,min(100,score)); string dec="REJECT";
        for(auto& b:bands) if(score>=b.mn && score<=b.mx){ dec=b.dec; break; }
        
        out<<"{\"request_id\":\""<<esc(q.id)<<"\",\"risk_score\":"<<score<<",\"decision\":\""<<dec<<"\"";
        if(dec=="MANUAL_REVIEW") out<<",\"reason\":\"MEDIUM_RISK_SCORE\"";
        else if(dec=="REJECT") out<<",\"reason\":\"HIGH_RISK_SCORE\"";
        out<<"}\n";
    }
}
```

---

### Q4. Contain Virus (Health Incharge District Grid)

`[Latest]`

**Topic:** `Grid`, `BFS`, `DFS`, `Simulation`

### Problem Description
You are appointed as the Health Incharge of a district. Your task is to contain the spread of Covid cases in your district by building walls to separate the infected areas from the healthy areas.
The district is represented as a grid of size $N \times M$. A cell with value `1` represents an infected area, and `0` represents a healthy area.

A wall can be erected between any two adjacent areas on a shared boundary.
In one day, you can install walls around only **one** infected region (a connected component of infected cells).
If there is no wall around an infected area, by the next day, the virus spreads to its healthy neighbors in the four cardinal directions (North, South, East, West). Walls once erected cannot be removed.
Your goal is to erect walls such that as many areas as possible stay healthy. If there are multiple regions whose containment saves the same number of healthy cells, choose the one requiring the minimum number of walls.

Write a program to find the minimum number of walls required to contain the virus completely.

### Constraints
- $1 < N, M \le 100$

---

### C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <set>
#include <algorithm>

using namespace std;

struct Region {
    set<pair<int, int>> cells;
    set<pair<int, int>> threatened;
    int walls = 0;
};

void dfs(int r, int c, int m, int n, int** grid, vector<vector<bool>>& visited, Region& region) {
    region.cells.insert({r, c});
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};
    
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
            if (grid[nr][nc] == 1 && !visited[nr][nc]) {
                visited[nr][nc] = true;
                dfs(nr, nc, m, n, grid, visited, region);
            } else if (grid[nr][nc] == 0) {
                region.threatened.insert({nr, nc});
                region.walls++;
            }
        }
    }
}

int minNumOfwalls(int** grid, int m, int n) {
    int total_walls = 0;
    
    while (true) {
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        vector<Region> regions;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    visited[i][j] = true;
                    Region r;
                    dfs(i, j, m, n, grid, visited, r);
                    regions.push_back(r);
                }
            }
        }
        
        if (regions.empty()) break;
        
        // Find region to contain
        int idx_to_contain = -1;
        int max_threatened = 0;
        int min_walls = 1e9;
        
        for (size_t i = 0; i < regions.size(); ++i) {
            int current_threat = regions[i].threatened.size();
            if (current_threat > max_threatened) {
                max_threatened = current_threat;
                min_walls = regions[i].walls;
                idx_to_contain = i;
            } else if (current_threat == max_threatened && current_threat > 0) {
                if (regions[i].walls < min_walls) {
                    min_walls = regions[i].walls;
                    idx_to_contain = i;
                }
            }
        }
        
        if (idx_to_contain == -1 || max_threatened == 0) break;
        
        // Add walls
        total_walls += regions[idx_to_contain].walls;
        
        // Cordon off contained region
        for (auto p : regions[idx_to_contain].cells) {
            grid[p.first][p.second] = 2; // 2 represents contained
        }
        
        // Spread virus for other regions
        for (size_t i = 0; i < regions.size(); ++i) {
            if ((int)i != idx_to_contain) {
                for (auto p : regions[i].threatened) {
                    grid[p.first][p.second] = 1;
                }
            }
        }
    }
    
    return total_walls;
}
```

---

### Q5. Drone Services Schedule (Complete Day)

`[Latest]`

**Topic:** `Graph`, `Clique`, `Complement Graph`

### Problem Description
There are $N$ locations in a city that need to be connected with drone pathways. Each location needs to be connected with all the other $N-1$ locations. Some of these pathways are already built, while the rest need to be constructed.

Due to the peculiarity of the technology, whenever new pathways from a location are constructed, all pre-existing pathways from that location are destroyed (vertex neighborhood toggle).
Every day, the citizens choose one of the $N$ locations and build all the missing pathways from that location, in the process toggling the status of all edges incident to it.

Determine if "Complete Day" (a state where all locations are connected to all other locations) is achievable from the initial configuration.

---

### C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void droneServicesSchedule(int arr[][2], int M, int N) {
    int start_idx = 1;
    for (int i = 0; i < M; i++) {
        if (arr[i][0] == 0 || arr[i][1] == 0) {
            start_idx = 0;
            break;
        }
    }

    vector<bool> s(N + 5, false);
    s[start_idx] = true;

    for (int i = 0; i < M; i++) {
        s[arr[i][0]] = s[arr[i][0]] | (arr[i][1] == start_idx);
        s[arr[i][1]] = s[arr[i][1]] | (arr[i][0] == start_idx);
    }

    long long c = 0;
    for (int i = start_idx; i < start_idx + N; i++) {
        c += s[i];
    }

    // A complete graph can be formed using toggles if and only if
    // the graph is a disjoint union of two cliques.
    bool ok = (long long)M == c * (c - 1) / 2 + (N - c) * (N - c - 1) / 2;
    for (int i = 0; i < M; i++) {
        ok &= (s[arr[i][0]] == s[arr[i][1]]);
    }

    cout << (ok ? "Complete Day\n" : "Not a Complete Day\n");
}
```

---

### Q6. Divisible Cost Pairs

**Topic:** `arrays`, `hash-map`, `math`, `two-pointers`

**Question:**  
Amazon is offering a discount on every purchase of a pair of products whose cost sum is divisible by `x`. Given the cost of `n` products in the store, find the number of pairs `(i, j)` where `i < j` and `cost[i] + cost[j]` is divisible by `x`.

#### Input
- `x`: integer ($1 \le x \le 2 \cdot 10^9$)
- `cost`: list of integers ($1 \le cost[i] \le 10^9$)

#### Constraints
- $1 \le n \le 10^5$
- $1 \le x \le 2 \cdot 10^9$
- $1 \le cost[i] \le 10^9$

#### Example 1
**Input:**
```text
x = 6
cost = [12, 2, 4]
```
**Output:**
```text
1
```
**Explanation:**  
The only pair whose sum is divisible by 6 is `(2, 4)` since `2 + 4 = 6`, which is divisible by 6.

#### Example 2
**Input:**
```text
x = 10
cost = [3, 7, 27, 23]
```
**Output:**
```text
4
```
**Explanation:**  
The pairs that get the discount are:
- `(3, 7)` since `3 + 7 = 10`
- `(3, 27)` since `3 + 27 = 30`
- `(23, 7)` since `23 + 7 = 30`
- `(23, 27)` since `23 + 27 = 50`

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ to store remainders in a hash map.

##### Python Implementation
```python
def findPairs(x, cost):
    remainder_counts = {}
    total_pairs = 0
    
    for c in cost:
        rem = c % x
        target = (x - rem) % x
        if target in remainder_counts:
            total_pairs += remainder_counts[target]
            
        remainder_counts[rem] = remainder_counts.get(rem, 0) + 1
        
    return total_pairs
```

##### C++ Implementation
```cpp
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    long long findPairs(int x, const vector<int>& cost) {
        unordered_map<int, int> remainder_counts;
        long long total_pairs = 0;
        
        for (int c : cost) {
            int rem = c % x;
            int target = (x - rem) % x;
            if (remainder_counts.count(target)) {
                total_pairs += remainder_counts[target];
            }
            remainder_counts[rem]++;
        }
        
        return total_pairs;
    }
};
```

---

### Q7. Duel Tournament Power Boosters

**Topic:** `arrays`, `sorting`, `greedy`

**Question:**  
Amazon games have recently launched a new multi-player tournament. Each game of the tournament has 3 rounds. The players are provided with exactly three power boosters at the start of the game. In each round, the player can choose to compete with any of the power boosters, and each power booster can be used at most once in a game. In any particular round, the player with the higher power booster wins.

A player `X` is considered to be capable of defeating player `Y` if there exists a pairing of X's boosters and Y's boosters such that X wins in at least 2 out of the 3 rounds.

Given the power boosters of `n` players defined by `power_type_a[i]`, `power_type_b[i]`, and `power_type_c[i]`, find the number of players who are capable of defeating all other players. All booster values of each player are distinct.

#### Input
- `power_type_a`: list of integers
- `power_type_b`: list of integers
- `power_type_c`: list of integers

#### Constraints
- $2 \le n \le 10^5$
- $1 \le power\_type\_a[i], power\_type\_b[i], power\_type\_c[i] \le 10^9$
- All power boosters of each player are pairwise distinct.

#### Example 1
**Input:**
```text
power_type_a = [9, 4, 2]
power_type_b = [5, 12, 10]
power_type_c = [11, 3, 13]
```
**Output:**
```text
2
```
**Explanation:**  
The players' boosters are:
- Player 1: `[9, 5, 11]` (sorted: `[5, 9, 11]`)
- Player 2: `[4, 12, 3]` (sorted: `[3, 4, 12]`)
- Player 3: `[2, 10, 13]` (sorted: `[2, 10, 13]`)

Player 1 and Player 3 can defeat all other players, so the answer is 2.

#### Example 2
**Input:**
```text
power_type_a = [3, 4, 1, 16]
power_type_b = [2, 11, 5, 6]
power_type_c = [8, 7, 9, 10]
```
**Output:**
```text
2
```
**Explanation:**  
The players' boosters are:
- Player 1: `[3, 2, 8]` (sorted: `[2, 3, 8]`)
- Player 2: `[4, 11, 7]` (sorted: `[4, 7, 11]`)
- Player 3: `[1, 5, 9]` (sorted: `[1, 5, 9]`)
- Player 4: `[16, 6, 10]` (sorted: `[6, 10, 16]`)

Player 2 and Player 4 can defeat all other players, so the answer is 2.

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ to store sorted boosters and player values.

##### Python Implementation
```python
def findCapableWinners(power_type_a, power_type_b, power_type_c):
    n = len(power_type_a)
    players = []
    
    for i in range(n):
        boosters = sorted([power_type_a[i], power_type_b[i], power_type_c[i]])
        players.append(boosters)
        
    # Find max and second max of the first and second booster categories
    # p[0] is the smallest, p[1] is the middle, p[2] is the largest booster of player
    max1, max1_2nd = -1, -1
    max2, max2_2nd = -1, -1
    
    for p in players:
        p1_val = p[0]
        p2_val = p[1]
        
        # Track max and 2nd max of first boosters
        if p1_val > max1:
            max1_2nd = max1
            max1 = p1_val
        elif p1_val > max1_2nd:
            max1_2nd = p1_val
            
        # Track max and 2nd max of second boosters
        if p2_val > max2:
            max2_2nd = max2
            max2 = p2_val
        elif p2_val > max2_2nd:
            max2_2nd = p2_val
            
    winners = 0
    for p in players:
        # Determine the maximum first booster of others
        limit1 = max1_2nd if p[0] == max1 else max1
        # Determine the maximum second booster of others
        limit2 = max2_2nd if p[1] == max2 else max2
        
        if p[1] > limit1 and p[2] > limit2:
            winners += 1
            
    return winners
```

##### C++ Implementation
```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findCapableWinners(vector<int> power_type_a, vector<int> power_type_b, vector<int> power_type_c) {
        int n = power_type_a.size();
        vector<vector<int>> players(n, vector<int>(3));
        
        for (int i = 0; i < n; ++i) {
            vector<int> boosters = {power_type_a[i], power_type_b[i], power_type_c[i]};
            sort(boosters.begin(), boosters.end());
            players[i] = boosters;
        }
        
        int max1 = -1, max1_2nd = -1;
        int max2 = -1, max2_2nd = -1;
        
        for (const auto& p : players) {
            int p1_val = p[0];
            int p2_val = p[1];
            
            if (p1_val > max1) {
                max1_2nd = max1;
                max1 = p1_val;
            } else if (p1_val > max1_2nd) {
                max1_2nd = p1_val;
            }
            
            if (p2_val > max2) {
                max2_2nd = max2;
                max2 = p2_val;
            } else if (p2_val > max2_2nd) {
                max2_2nd = p2_val;
            }
        }
        
        int winners = 0;
        for (const auto& p : players) {
            int limit1 = (p[0] == max1) ? max1_2nd : max1;
            int limit2 = (p[1] == max2) ? max2_2nd : max2;
            
            if (p[1] > limit1 && p[2] > limit2) {
                winners++;
            }
        }
        
        return winners;
    }
};
```

---

### Q8. Common Regex Wildcards

**Topic:** `strings`, `greedy`

**Question:**  
Amazon is developing a string matching library and you are to develop a service that finds a common regex pattern from the given set of regexes.

A regex pattern consists of lowercase English letters and wildcard characters (`?`). Two patterns are called intersecting if the wildcard characters in the respective strings can be changed in a way to form the same string from both patterns.

Given an array `patterns` of `n` regex strings of length `m`, find the minimum number of `?` characters possible in a pattern that intersects with all the patterns.

#### Input
- `patterns`: list of strings

#### Constraints
- $1 \le n \le 10^5$
- $1 \le m \le 10^5$
- Total characters $n \times m \le 10^6$

#### Example 1
**Input:**
```text
patterns = ["ha???rrank", "?a?ke?bank"]
```
**Output:**
```text
1
```
**Explanation:**  
The minimum wildcard pattern that intersects with both is `hacker?ank`, which has exactly 1 wildcard character `?` (at index 6).

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N \cdot m)$
- **Space Complexity:** $O(m)$ to store character states per index.

##### Python Implementation
```python
def minWildcardRegex(patterns):
    n = len(patterns)
    m = len(patterns[0])
    wildcards = 0
    
    for col in range(m):
        unique_char = None
        has_conflict = False
        
        for row in range(n):
            char = patterns[row][col]
            if char != '?':
                if unique_char is None:
                    unique_char = char
                elif unique_char != char:
                    has_conflict = True
                    break
                    
        if has_conflict:
            wildcards += 1
            
    return wildcards
```

##### C++ Implementation
```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int minWildcardRegex(const vector<string>& patterns) {
        int n = patterns.size();
        int m = patterns[0].size();
        int wildcards = 0;
        
        for (int col = 0; col < m; ++col) {
            char unique_char = '\0';
            bool has_conflict = false;
            
            for (int row = 0; row < n; ++row) {
                char ch = patterns[row][col];
                if (ch != '?') {
                    if (unique_char == '\0') {
                        unique_char = ch;
                    } else if (unique_char != ch) {
                        has_conflict = true;
                        break;
                    }
                }
            }
            if (has_conflict) {
                wildcards++;
            }
        }
        
        return wildcards;
    }
};
```

---

### Q9. Minimize Maximum Parcels

**Topic:** `arrays`, `math`, `greedy`

**Question:**  
To be efficient, Amazon must optimally distribute parcels among their delivery agents. Initially, there are `n` agents, and the number of parcels assigned to the `i`-th agent is `parcels[i]`. There are `extra_parcels` parcels that also need to be shipped. The extra parcels should be assigned such that the maximum number of parcels assigned to any one agent is minimized.

Given an integer array `parcels` and an integer `extra_parcels`, find the minimum possible value of the maximum number of parcels any agent must deliver.

#### Input
- `parcels`: list of integers
- `extra_parcels`: long integer ($1 \le extra\_parcels \le 10^{12}$)

#### Constraints
- $1 \le n \le 10^5$
- $1 \le parcels[i] \le 10^9$
- $1 \le extra\_parcels \le 10^{12}$

#### Example 1
**Input:**
```text
parcels = [7, 5, 1, 9, 1]
extra_parcels = 25
```
**Output:**
```text
10
```
**Explanation:**  
An optimal distribution adds 3, 5, 9, 1, 7 parcels respectively to get `[10, 10, 10, 10, 8]`. The maximum value is 10.

#### Example 2
**Input:**
```text
parcels = [1, 2, 3]
extra_parcels = 3
```
**Output:**
```text
3
```
**Explanation:**  
We can distribute the 3 extra parcels as `+2` to the first agent and `+1` to the second agent, resulting in `[3, 3, 3]`. The maximum value is 3.

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

##### Python Implementation
```python
def getMinMaxParcels(parcels, extra_parcels):
    n = len(parcels)
    total_sum = sum(parcels) + extra_parcels
    # Ceiling division for integer average
    avg = (total_sum + n - 1) // n
    return max(max(parcels), avg)
```

##### C++ Implementation
```cpp
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long getMinMaxParcels(const vector<int>& parcels, long long extra_parcels) {
        int n = parcels.size();
        long long total_sum = extra_parcels;
        int max_val = 0;
        
        for (int p : parcels) {
            total_sum += p;
            max_val = max(max_val, p);
        }
        
        long long avg = (total_sum + n - 1) / n;
        return max((long long)max_val, avg);
    }
};
```

---

### Q10. AWS Outlier Detection

**Topic:** `arrays`, `hash-map`, `math`

**Question:**  
AWS provides many services for outlier detection. A prototype small service to detect an outlier in an array of integers is under development.

Given an array of `n` integers, there are `(n - 2)` normal numbers and the sum of the `(n - 2)` numbers originally in this array. If a number is neither in the original numbers nor is it their sum, it is an outlier. Discover the potential outliers and return the greatest of them.

Note: It is guaranteed that the answer exists.

#### Input
- `arr`: list of integers

#### Constraints
- $3 \le n \le 10^5$
- $1 \le arr[i] \le 10^9$

#### Example 1
**Input:**
```text
arr = [4, 1, 3, 16, 2, 10]
```
**Output:**
```text
16
```
**Explanation:**  
The potential outliers are:
- `16`: Removing `16` leaves `[4, 1, 3, 2, 10]`. The sum of `[4, 1, 3, 2]` is `10`. So `16` is a potential outlier.
- `4`: Removing `4` leaves `[1, 3, 16, 2, 10]`. The sum of `[1, 3, 2, 10]` is `16`. So `4` is a potential outlier.

The maximum outlier is `16`.

#### Example 2
**Input:**
```text
arr = [2, 2, 4, 2]
```
**Output:**
```text
2
```
**Explanation:**  
The only potential outlier is `2`. Removing it leaves `[2, 4, 2]`, where the sum of `[2, 2]` is `4`.

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ for frequency counts.

##### Python Implementation
```python
def getOutlierValue(arr):
    total_sum = sum(arr)
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    max_outlier = float('-inf')
    
    for y in arr:
        # y is the assumed sum element
        # outlier x must satisfy: 2*y + x = total_sum => x = total_sum - 2*y
        x = total_sum - 2 * y
        
        if x in freq:
            # If outlier and sum element are equal, we need at least 2 occurrences
            if x == y:
                if freq[y] >= 2:
                    max_outlier = max(max_outlier, x)
            else:
                max_outlier = max(max_outlier, x)
                
    return max_outlier
```

##### C++ Implementation
```cpp
#include <vector>
#include <unordered_map>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getOutlierValue(const vector<int>& arr) {
        long long total_sum = 0;
        unordered_map<long long, int> freq;
        for (int num : arr) {
            total_sum += num;
            freq[num]++;
        }
        
        long long max_outlier = -1;
        for (int y : arr) {
            long long x = total_sum - 2LL * y;
            if (freq.count(x)) {
                if (x == y) {
                    if (freq[y] >= 2) {
                        max_outlier = max(max_outlier, x);
                    }
                } else {
                    max_outlier = max(max_outlier, x);
                }
            }
        }
        
        return max_outlier;
    }
};
```

---

## SQL Questions

### Q1. Second Highest Salary in January 2021

`[Latest]`

**Topic:** `SQL`

### Problem Description
An employer wants to know the second-highest salary paid to an employee in the month of January 2021.
Given five tables: `dept`, `emp`, `designation`, `compensation`, and `emp_dept` as shown in the ER diagram:

- `emp` (`emp_no`, `dob`, `first_name`, `last_name`, `gender`, `joining_date`)
- `dept` (`dept_no`, `dept_name`)
- `emp_dept` (`emp_no`, `dept_no`, `from_date`, `to_date`)
- `compensation` (`emp_no`, `credited_date`, `amount`)

Write a SQL query to get `emp_no`, `first_name`, `last_name`, `gender`, `dept_no`, `dept_name`, and the `salary` credited in January 2021 for the employees who received the second-highest salary.

---

### SQL Query

```sql
WITH RankedCompensation AS (
    SELECT 
        emp_no,
        amount,
        DENSE_RANK() OVER (ORDER BY amount DESC) as rnk
    FROM compensation
    -- Check if date format is Standard Date or String.
    -- Standard Date query:
    WHERE credited_date >= '2021-01-01' AND credited_date <= '2021-01-31'
)
SELECT 
    e.emp_no, 
    e.first_name, 
    e.last_name, 
    e.gender, 
    ed.dept_no, 
    d.dept_name, 
    rc.amount AS salary
FROM RankedCompensation rc
JOIN emp e ON rc.emp_no = e.emp_no
LEFT JOIN emp_dept ed ON e.emp_no = ed.emp_no AND (ed.to_date IS NULL OR ed.to_date >= '2021-01-01')
LEFT JOIN dept d ON ed.dept_no = d.dept_no
WHERE rc.rnk = 2;
```

