# Interview Questions

*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Escalator Loop Detection

`[Latest]`

**Topic:** `Graph`, `Cycle Detection`, `Simulation`

### Problem Description
A shopping mall has an automated escalator system where people move between floors using escalators. Each floor is connected to the next floor via an escalator. Due to a malfunction, some escalators are causing people to enter an infinite loop, meaning instead of reaching an exit floor, they keep moving between a set of floors indefinitely.

Your task is to detect if the escalator system contains a loop, starting from floor `0`.

### Function Parameters
- `int N`: The number of floors in the escalator system.
- `int[] next_floor`: An array of size $N$, where:
  - `next_floor[i]` represents the next floor a person moves to from floor `i`.
  - If `next_floor[i] == -1`, it means the person exits the system from that floor.

### Return Values
- If a loop is detected, return `"Loop Detected at Floor X"`, where `X` is the first floor in the cycle visited twice.
- If the person exits successfully, return `"No Loop Detected"`.

---

### Python Solution

```python
import sys

def escalator_loop(N, next_floor):
    visited = [False] * N
    curr = 0
    while curr != -1:
        if visited[curr]:
            return f"Loop Detected at Floor {curr}"
        visited[curr] = True
        curr = next_floor[curr]
    return "No Loop Detected"

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        N = int(input_data[0])
        next_floor = [int(x) for x in input_data[1:]]
        print(escalator_loop(N, next_floor))

if __name__ == '__main__':
    main()
```

---

### Q2. Energy Path in Booster Graph (Minimum Booster Power)

`[Latest]`

**Topic:** `Graph`, `BFS`, `Dijkstra`, `DSU`, `Kruskal`

> [!NOTE]
> This question is identical to Amazon Q2 (Energy Path in Booster Graph).

### Problem Description
Bob is exploring an undirected, unweighted graph with $N$ nodes and $M$ edges. Among these nodes, there are $K$ special nodes known as energy boosters. Each booster node provides a power value $P$ whenever Bob visits it.
When Bob's current power is $x$, he can move across an edge by spending $1$ unit of power. If he reaches another energy booster node, his power is restored to $P$.

Bob wants to determine the minimum possible value of $P$ that allows him to travel from node $1$ to node $N$ without his power ever becoming negative, and such that his power never exceeds $P$ during the journey.
If it is impossible for Bob to reach node $N$, return $-1$.

You may assume:
- Node $1$ is always an energy booster node.
- Bob can revisit nodes any number of times.

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

---

### Q3. Extract Valid Scientific Codes

`[Latest]`

**Topic:** `String`, `Regex`

### Problem Description
A scientific research database stores experiment identifiers in a text file. Each identifier follows specific encoding rules, and only correctly formatted identifiers should be extracted for indexing.

You are given a list of strings, each possibly containing multiple experiment identifiers. Your task is to extract and return only those identifiers that match exactly one of the following valid formats, in the order they appear:

1. **Alpha Format:** `EX-[A-Z]{2}[0-9]{4}`
   - Starts with `EX-`
   - Followed by exactly 2 uppercase letters
   - Followed by exactly 4 digits
   - *Example:* `EX-AB1234`
2. **Beta Format:** `[0-9]{3}-[a-z]{3}-[A-Z]{2}`
   - Three digits, followed by a hyphen
   - Followed by exactly 3 lowercase letters, followed by a hyphen
   - Followed by exactly 2 uppercase letters
   - *Example:* `123-xyz-ZQ`
3. **Gamma Format:** `#G:[A-F0-9]{6}`
   - Starts with `#G:`
   - Followed by exactly 6 hexadecimal characters (digits 0-9 and uppercase letters A-F)
   - *Example:* `#G:12AF9B`

All other patterns should be ignored. The function ignores irrelevant text and malformed patterns.

### Constraints
- $1 \le N \le 100$ (where $N$ is the number of input strings)
- Each input string contains up to 200 printable ASCII characters.

### Sample Case
- **Input:**
  `Report EX-MN2384 and 789-xyz-ZQ were accepted. Also #G:1AF32C and EX-AA0000 were listed.`
- **Output:**
  `EX-MN2384 789-xyz-ZQ #G:1AF32C EX-AA0000`

---

### Python Solution

```python
import sys
import re

def extractValidScientificCodes(data):
    # Matches any of the three formats in order of appearance
    pattern = re.compile(
        r'EX-[A-Z]{2}[0-9]{4}'               # Alpha Format
        r'|[0-9]{3}-[a-z]{3}-[A-Z]{2}'       # Beta Format
        r'|#G:[A-F0-9]{6}'                    # Gamma Format
    )
    
    results = []
    for line in data:
        matches = pattern.findall(line)
        results.append(matches)
    return results

def main():
    # Read all lines from standard input
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
        
    # First line might specify N, or we just process all lines
    # Let's handle both cases gracefully
    try:
        N = int(input_lines[0].strip())
        data = input_lines[1:1+N]
    except ValueError:
        data = input_lines
        
    results = extractValidScientificCodes(data)
    for res in results:
        print(" ".join(res))

if __name__ == '__main__':
    main()
```

