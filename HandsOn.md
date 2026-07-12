# Interview Questions

*Total questions: 1*

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

### Q1. Count Good Paths

**Topic:** `trees`, `math`, `number-theory`, `dfs`

#### Problem Description

You are given a tree $T$ of size $N$. You are given a 2D array $E$ of size $M$, where there exists an edge between $E[i][0]$ and $E[i][1]$ for all $1 \le i \le M$.

You are also given an array $A$ of size $N$, where the node $U$ has a value $A[U-1]$ (using 1-based indexing for node $U$).

A path $P$ is called a **good path** if the greatest common divisor (GCD) of all the values present on the path $P$ is equal to $1$. Two paths $P_1, P_2$ are considered the same if they have the same number of nodes and each node $X$ of path $P_1$ belongs to $P_2$ (i.e., they are undirected simple paths).

Find the total number of possible good paths present in $T$.

**Note:**
* The path $(U, U)$ is valid for all nodes $U$ (a path consisting of a single node $U$).

#### Input Format
* The first line contains an integer, $N$, denoting the number of elements in $A$.
* The next line contains an integer, $M$, denoting the number of rows in $E$.
* The next line contains an integer, $two$, denoting the number of columns in $E$ (always 2).
* Each line $i$ of the $N$ subsequent lines (where $0 \le i < N$) contains an integer describing $A[i]$.
* Each line $i$ of the $M$ subsequent lines (where $1 \le i \le M$) contains two space-separated integers each describing the row $E[i-1]$.

#### Constraints
* $1 \le N \le 5000$
* $M = N - 1$
* $two = 2$
* $1 \le A[i] \le 10^9$
* $1 \le E[i][j] \le N$

#### Sample Test Cases

##### Case 1
**Input:**
```text
5
4
2
1
1
1
1
1
1 2
2 3
3 4
4 5
```
**Output:**
```text
15
```
**Explanation:**
Given $N = 5, M = 4, two = 2, A = [1, 1, 1, 1, 1], E = [[1, 2], [2, 3], [3, 4], [4, 5]]$.
There exists in total 15 paths whose gcd is equal to one.
The possible paths of the tree are $(1,1), (2,2), (3,3), (4,4), (5,5), (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)$.
Hence, the answer for this case is equal to 15.

##### Case 2
**Input:**
```text
5
4
2
1
2
2
2
2
1 2
2 3
3 4
4 5
```
**Output:**
```text
5
```
**Explanation:**
Given $N = 5, M = 4, two = 2, A = [1, 2, 2, 2, 2], E = [[1, 2], [2, 3], [3, 4], [4, 5]]$.
There exists in total of 5 paths with gcd equals to 1 which are $(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)$.
Hence, the answer for this case is equal to 5.

##### Case 3
**Input:**
```text
5
4
2
3
5
7
2
4
1 2
2 3
3 4
4 5
```
**Output:**
```text
9
```
**Explanation:**
Given $N = 5, M = 4, two = 2, A = [3, 5, 7, 2, 4], E = [[1, 2], [2, 3], [3, 4], [4, 5]]$.
There exists a total of 9 paths with gcd equal to 1 which are $(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)$.
Hence, answer for this case is equal to 9.

---

#### Solution (Python)
An optimal solution using the **inclusion-exclusion principle / Mobius inversion** on trees.

##### Algorithm
1. **Total Paths**: The total number of undirected simple paths in a tree of size $N$ is $N(N+1)/2$.
2. **Path GCD**: We want to count the number of paths with $\text{GCD} = 1$. Let $g(d)$ be the number of paths whose GCD is exactly $d$. Let $f(d)$ be the number of paths whose GCD is a multiple of $d$.
3. **Mobius Inversion**: By Mobius inversion, the number of paths with GCD equal to 1 is given by:
   $$g(1) = \sum_{d \ge 1} \mu(d) f(d)$$
   where $\mu(d)$ is the Mobius function.
4. **Calculating $f(d)$**: A path has GCD divisible by $d$ if and only if all nodes on the path have values divisible by $d$.
   * We filter the tree to include only nodes $u$ where $A[u]$ is a multiple of $d$.
   * This forms a forest of connected components.
   * For each component of size $S$, the number of paths inside it is $S(S+1)/2$.
   * Thus, $f(d) = \sum \frac{S_i(S_i + 1)}{2}$ over all components.
5. **Optimization**:
   * We only need to compute $f(d)$ for values of $d$ that divide at least one $A[i]$.
   * To find connected components of the induced subgraph for a divisor $d$ in $O(|V_d|)$ time:
     * Root the tree at node 0 and compute the parent of each node.
     * For each divisor $d$, the induced subgraph contains edges only between $u \in V_d$ and its parent $\text{parent}[u]$ if $\text{parent}[u] \in V_d$. This allows constructing the local graph and running BFS/DFS in $O(|V_d|)$ time.
   * The sum of $|V_d|$ over all divisors is bounded by $N \times (\text{max divisors of } A[i])$. Since $A[i] \le 10^9$, the number of divisors is at most 1344, and on average much smaller.
   * This algorithm runs well within the time limit.

```python
import collections

def solve(N, M, two, A, E):
    # Convert E (1-based) to 0-based adjacency list
    adj = [[] for _ in range(N)]
    for u, v in E:
        u_idx = u - 1
        v_idx = v - 1
        adj[u_idx].append(v_idx)
        adj[v_idx].append(u_idx)
    
    # Root the tree at node 0 and find parent of each node
    parent = [-1] * N
    visited = [False] * N
    queue = collections.deque([0])
    visited[0] = True
    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                parent[neighbor] = curr
                visited[neighbor] = True
                queue.append(neighbor)
                
    # Cache prime factorizations
    memo_factors = {}
    def factorize(n):
        if n in memo_factors:
            return memo_factors[n]
        factors = []
        temp = n
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                count = 0
                while temp % d == 0:
                    count += 1
                    temp //= d
                factors.append((d, count))
            d += 1
        if temp > 1:
            factors.append((temp, 1))
        memo_factors[n] = factors
        return factors

    # Generate all divisors of a number
    def get_divisors(n):
        factors = factorize(n)
        divisors = [1]
        for p, power in factors:
            current_len = len(divisors)
            for i in range(current_len):
                curr = divisors[i]
                p_pow = 1
                for _ in range(power):
                    p_pow *= p
                    divisors.append(curr * p_pow)
        return divisors

    # Cache Mobius values
    memo_mobius = {}
    def get_mobius(d):
        if d in memo_mobius:
            return memo_mobius[d]
        if d == 1:
            return 1
        factors = factorize(d)
        for p, power in factors:
            if power > 1:
                memo_mobius[d] = 0
                return 0
        count = len(factors)
        val = 1 if count % 2 == 0 else -1
        memo_mobius[d] = val
        return val

    # Map divisor to list of nodes whose values are divisible by it
    div_to_nodes = collections.defaultdict(list)
    for u in range(N):
        divs = get_divisors(A[u])
        for d in divs:
            div_to_nodes[d].append(u)

    total_good_paths = 0
    
    # Process each divisor
    for d, nodes in div_to_nodes.items():
        mu = get_mobius(d)
        if mu == 0:
            continue
            
        nodes_set = set(nodes)
        
        # Build local adjacency list for the induced subgraph
        adj_local = {u: [] for u in nodes}
        for u in nodes:
            p = parent[u]
            if p != -1 and p in nodes_set:
                adj_local[u].append(p)
                adj_local[p].append(u)
                
        # Find sizes of all connected components in the induced forest
        visited_local = set()
        sum_paths = 0
        for u in nodes:
            if u not in visited_local:
                comp_size = 0
                stack = [u]
                visited_local.add(u)
                while stack:
                    curr = stack.pop()
                    comp_size += 1
                    for neighbor in adj_local[curr]:
                        if neighbor not in visited_local:
                            visited_local.add(neighbor)
                            stack.append(neighbor)
                sum_paths += comp_size * (comp_size + 1) // 2
                
        total_good_paths += mu * sum_paths
        
    return total_good_paths
```

#### Solution (Java)
```java
import java.util.*;

public class Solution {
    
    private static Map<Integer, List<Integer>> divisorCache = new HashMap<>();
    private static Map<Integer, List<int[]>> factorCache = new HashMap<>();
    private static Map<Integer, Integer> mobiusCache = new HashMap<>();
    
    private static List<int[]> factorize(int n) {
        if (factorCache.containsKey(n)) {
            return factorCache.get(n);
        }
        List<int[]> factors = new ArrayList<>();
        int temp = n;
        for (int d = 2; d * d <= temp; d++) {
            if (temp % d == 0) {
                int count = 0;
                while (temp % d == 0) {
                    count++;
                    temp /= d;
                }
                factors.add(new int[]{d, count});
            }
        }
        if (temp > 1) {
            factors.add(new int[]{temp, 1});
        }
        factorCache.put(n, factors);
        return factors;
    }
    
    private static List<Integer> getDivisors(int n) {
        if (divisorCache.containsKey(n)) {
            return divisorCache.get(n);
        }
        List<int[]> factors = factorize(n);
        List<Integer> divisors = new ArrayList<>();
        divisors.add(1);
        for (int[] factor : factors) {
            int p = factor[0];
            int power = factor[1];
            int currentSize = divisors.size();
            for (int i = 0; i < currentSize; i++) {
                int curr = divisors.get(i);
                int pPow = 1;
                for (int j = 0; j < power; j++) {
                    pPow *= p;
                    divisors.add(curr * pPow);
                }
            }
        }
        divisorCache.put(n, divisors);
        return divisors;
    }
    
    private static int getMobius(int d) {
        if (mobiusCache.containsKey(d)) {
            return mobiusCache.get(d);
        }
        if (d == 1) {
            return 1;
        }
        List<int[]> factors = factorize(d);
        for (int[] factor : factors) {
            if (factor[1] > 1) {
                mobiusCache.put(d, 0);
                return 0;
            }
        }
        int count = factors.size();
        int val = (count % 2 == 0) ? 1 : -1;
        mobiusCache.put(d, val);
        return val;
    }

    public static int get_ans(int N, int M, int two, List<Integer> A, List<List<Integer>> E) {
        // Build adjacency list
        List<List<Integer>> adj = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            adj.add(new ArrayList<>());
        }
        for (List<Integer> edge : E) {
            int u = edge.get(0) - 1;
            int v = edge.get(1) - 1;
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        
        // Root tree at node 0 and find parents
        int[] parent = new int[N];
        Arrays.fill(parent, -1);
        boolean[] visited = new boolean[N];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);
        visited[0] = true;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int neighbor : adj.get(curr)) {
                if (!visited[neighbor]) {
                    parent[neighbor] = curr;
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }
        
        // Group nodes by their divisors
        Map<Integer, List<Integer>> divToNodes = new HashMap<>();
        for (int u = 0; u < N; u++) {
            List<Integer> divs = getDivisors(A.get(u));
            for (int d : divs) {
                divToNodes.computeIfAbsent(d, k -> new ArrayList<>()).add(u);
            }
        }
        
        long totalGoodPaths = 0;
        
        // Process each divisor
        for (Map.Entry<Integer, List<Integer>> entry : divToNodes.entrySet()) {
            int d = entry.getKey();
            List<Integer> nodes = entry.getValue();
            int mu = getMobius(d);
            if (mu == 0) {
                continue;
            }
            
            Set<Integer> nodesSet = new HashSet<>(nodes);
            
            // Build local adjacency list
            Map<Integer, List<Integer>> adjLocal = new HashMap<>();
            for (int u : nodes) {
                adjLocal.put(u, new ArrayList<>());
            }
            for (int u : nodes) {
                int p = parent[u];
                if (p != -1 && nodesSet.contains(p)) {
                    adjLocal.get(u).add(p);
                    adjLocal.get(p).add(u);
                }
            }
            
            // Find components
            Set<Integer> visitedLocal = new HashSet<>();
            long sumPaths = 0;
            for (int u : nodes) {
                if (!visitedLocal.contains(u)) {
                    long compSize = 0;
                    Queue<Integer> q = new LinkedList<>();
                    q.offer(u);
                    visitedLocal.add(u);
                    while (!q.isEmpty()) {
                        int curr = q.poll();
                        compSize++;
                        for (int neighbor : adjLocal.get(curr)) {
                            if (!visitedLocal.contains(neighbor)) {
                                visitedLocal.add(neighbor);
                                q.offer(neighbor);
                            }
                        }
                    }
                    sumPaths += compSize * (compSize + 1) / 2;
                }
            }
            
            totalGoodPaths += mu * sumPaths;
        }
        
        return (int) totalGoodPaths;
    }
}
```

---

## SQL Questions

No questions found in this category.

---

## Theoretical Questions

No questions found in this category.

---

## System Design Questions

No questions found in this category.

---

## Behavioral Questions

No questions found in this category.

---

## MCQs

No questions found in this category.

---

## Puzzles

No questions found in this category.
