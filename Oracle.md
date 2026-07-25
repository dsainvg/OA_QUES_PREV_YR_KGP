# Interview Questions

*Total questions: 66 (26 Coding, 40 MCQs)*

---

## Table of Contents
- [Coding Questions](#coding-questions)
- [Multiple Choice Questions (MCQs)](#multiple-choice-questions-mcqs)

---

## Coding Questions

### Q1. Best Sum Any Tree Path
**Topic:** `Trees`, `Depth First Search`, `Dynamic Programming`

Given a tree of $N$ nodes where each node has a value, find the maximum path sum of any path in the tree. The path does not need to pass through the root or go to the leaves, and can be any sequence of nodes where each adjacent pair in the sequence has an edge.

```python
def bestSumAnyTreePath(parent, values):
    n = len(parent)
    adj = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        if parent[i] == -1:
            root = i
        else:
            adj[parent[i]].append(i)
    
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        current = values[node]
        max_upward = 0
        child_sums = []
        
        for child in adj[node]:
            child_sum = dfs(child)
            max_upward = max(max_upward, child_sum)
            child_sums.append(child_sum)
        
        # Path including this node going upwards
        max_including_node = max(current, current + max_upward)
        max_sum = max(max_sum, max_including_node)
        
        # Path combining two different children branches through this node
        if len(child_sums) >= 2:
            child_sums.sort(reverse=True)
            max_sum = max(max_sum, current + child_sums[0] + child_sums[1])
        elif len(child_sums) == 1:
            max_sum = max(max_sum, current + child_sums[0])
            
        return max_including_node
        
    dfs(root)
    return max_sum
```

---

### Q2. Best Sum Downward Tree Path
**Topic:** `Trees`, `Depth First Search`, `Memoization`

Given a tree of $N$ nodes where each node $i$ has a parent `parent[i]` and a value `values[i]`. Find the maximum path sum of any downward path (from parent to child).

```python
def bestSumDownwardTreePath(parent, values):
    n = len(parent)
    computed = [False] * n
    memo = [0] * n
    
    def find_max_path(node):
        if computed[node]:
            return memo[node]
        
        if parent[node] == -1:
            memo[node] = values[node]
        else:
            parent_path = find_max_path(parent[node])
            memo[node] = max(parent_path + values[node], values[node])
            
        computed[node] = True
        return memo[node]
        
    ans = float('-inf')
    for i in range(n):
        ans = max(ans, find_max_path(i))
    return ans
```

---

### Q3. Binary Manipulation (Minimum One Bit Operations to Zero)
**Topic:** `Bit Manipulation`, `Recursion`, `Gray Code`

Given an integer $n$, find the minimum number of operations to transform $n$ to $0$. The allowed operations are:
1. Change the rightmost (0th) bit.
2. Change the $i$-th bit if the $(i-1)$-th bit is $1$ and all bits from $(i-2)$ down to $0$ are $0$.

```python
def minimumOneBitOperations(n: int) -> int:
    # Standard Gray code to binary conversion (equivalent to LeetCode 1611)
    ans = 0
    while n > 0:
        ans ^= n
        n >>= 1
    return ans
```

---

### Q4. Bitwise Equations
**Topic:** `Bit Manipulation`, `Math`

Given two arrays $a$ and $b$, find for each pair $(a[i], b[i])$ if there exist integers $x$ and $y$ such that $x + y = a[i]$ and $x \oplus y = b[i]$. If they exist, find the value of $2x + 3y$. Otherwise, return $0$.

```python
def bitwiseEquations(a, b):
    # x + y = a, x ^ y = b
    # Since x + y = (x ^ y) + 2 * (x & y), we have x & y = (a - b) / 2
    n = len(a)
    ans = [0] * n
    for i in range(n):
        diff = a[i] - b[i]
        if diff < 0 or diff % 2 != 0:
            ans[i] = 0
            continue
        diff //= 2
        if (diff & b[i]) != 0:
            ans[i] = 0
            continue
        y = diff
        x = diff | b[i]
        ans[i] = 2 * x + 3 * y
    return ans
```

---

### Q5. Contiguous Substrings (Paper Cuttings)
**Topic:** `Binary Search`, `Sorting`

Given two arrays $A$ and $B$ representing cuts of a paper, and a length `len`. Find the number of pairs of paper cuttings that can be joined. An interval $j$ can be joined with interval $i$ if $A[j] > B[i]$.

```python
import bisect

def paperCuttings(length, A, B):
    # Remove duplicates by putting intervals into a set
    intervals = sorted(list(set(zip(A, B))))
    if not intervals:
        return 0
    
    # Filter intervals where B[i] <= length
    filtered_intervals = [p for p in intervals if p[1] <= length]
    
    N = len(filtered_intervals)
    NA = [p[0] for p in filtered_intervals]
    
    ways = 0
    for i in range(N):
        # Find intervals j such that A[j] > B[i]
        idx = bisect.bisect_right(NA, filtered_intervals[i][1])
        ways += (N - idx)
    return ways
```

---

### Q6. Do They Belong
**Topic:** `Geometry`, `Math`

Given three points $A(x_1, y_1)$, $B(x_2, y_2)$, and $C(x_3, y_3)$ representing a triangle. And two points $P(x_p, y_p)$ and $Q(x_q, y_q)$. Determine:
- `0`: If $ABC$ is not a valid triangle.
- `1`: If $P$ belongs inside the triangle, but $Q$ does not.
- `2`: If $Q$ belongs inside the triangle, but $P$ does not.
- `3`: If both $P$ and $Q$ belong inside the triangle.
- `4`: If neither $P$ nor $Q$ belongs inside the triangle.

```python
def area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

def is_inside(x1, y1, x2, y2, x3, y3, px, py):
    area_abc = area(x1, y1, x2, y2, x3, y3)
    area_pab = area(px, py, x1, y1, x2, y2)
    area_pac = area(px, py, x1, y1, x3, y3)
    area_pbc = area(px, py, x2, y2, x3, y3)
    return abs((area_pab + area_pac + area_pbc) - area_abc) < 1e-9

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    ab = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    bc = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    ac = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    if not (ab + bc > ac and bc + ac > ab and ab + ac > bc):
        return 0
        
    p_inside = is_inside(x1, y1, x2, y2, x3, y3, xp, yp)
    q_inside = is_inside(x1, y1, x2, y2, x3, y3, xq, yq)
    
    if p_inside and q_inside:
        return 3
    elif p_inside:
        return 1
    elif q_inside:
        return 2
    else:
        return 4
```

---

### Q7. Efficient Harvest
**Topic:** `Sliding Window`, `Arrays`

A circular field of size $n$ has harvest value `earnings[i]` at each plot $i$. You can harvest $m$ consecutive plots and also the plots opposite to them. That is, if you harvest plot $i$, you must also harvest plot $(i + n/2) \bmod n$. Find the maximum profit you can make by choosing $m$ consecutive plots.

```python
def maximumProfit(m, earnings):
    n = len(earnings)
    combined = [earnings[i] + earnings[(i + n // 2) % n] for i in range(n)]
    
    # Double the array to handle wrapping
    double_combined = combined + combined
    
    curr_sum = sum(double_combined[:m])
    max_sum = curr_sum
    for i in range(1, n):
        curr_sum = curr_sum - double_combined[i - 1] + double_combined[i + m - 1]
        max_sum = max(max_sum, curr_sum)
        
    return max_sum
```

---

### Q8. Element Swapping (Maximum Strength)
**Topic:** `Dynamic Programming`, `Arrays`

Given an array $a$, find the maximum strength that can be achieved. We can optionally swap adjacent elements. The strength of the array is computed as $\sum a[i] \times (i + 1)$.

```python
def getMaximumStrength(a):
    n = len(a)
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = a[0]
    dp[0][1] = a[0]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + a[i] * (i + 1)
        
        prev_prev = max(dp[i-2][0], dp[i-2][1]) if i - 2 >= 0 else 0
        dp[i][1] = a[i] * i + a[i-1] * (i + 1) + prev_prev
        
    return max(dp[n-1][0], dp[n-1][1])
```

---

### Q9. Intelligent Substring
**Topic:** `Sliding Window`, `Strings`

Given a string $s$, an integer $k$, and a string $cv$ of 26 characters of '0's and '1's. A character $c$ is "special" if $cv[c - 'a'] == '0'$. Find the length of the longest substring of $s$ containing at most $k$ special characters.

```python
def getSpecialSubstring(s, k, cv):
    n = len(s)
    l = 0
    special_count = 0
    max_len = 0
    for r in range(n):
        if cv[ord(s[r]) - ord('a')] == '0':
            special_count += 1
        
        while special_count > k:
            if cv[ord(s[l]) - ord('a')] == '0':
                special_count -= 1
            l += 1
            
        max_len = max(max_len, r - l + 1)
    return max_len
```

---

### Q10. K-means (Allocating Centers)
**Topic:** `Binary Search on Answer`, `Greedy`

Given sorted `location` of houses along a line. We want to place at most $k$ centers such that the distance from any house to its nearest center is minimized. Find the minimum possible maximum distance.

```python
def getMaximumDistance(location, k):
    location.sort()
    n = len(location)
    left = 0
    right = location[-1] - location[0]
    
    while left < right:
        mid = left + (right - left) // 2
        centers = 1
        prev = location[0]
        for i in range(1, n):
            if location[i] - prev > mid * 2:
                centers += 1
                prev = location[i]
        
        if centers <= k:
            right = mid
        else:
            left = mid + 1
    return left
```

---

### Q11. Quiz Competition
**Topic:** `Sliding Window`, `Hash Map`

Given a list of student talents `tList` and the number of distinct talents `tCount`. Find for each index $i$ the minimum length of a contiguous subarray starting at $i$ that contains all `tCount` distinct talents. If no such subarray exists starting at $i$, return `-1`.

```python
def findMinTeamLengths(tCount, tList):
    n = len(tList)
    res = [-1] * n
    t_map = {}
    d_count = 0
    l = 0
    for r in range(n):
        cur = tList[r]
        if t_map.get(cur, 0) == 0:
            d_count += 1
        t_map[cur] = t_map.get(cur, 0) + 1
        
        while d_count == tCount:
            res[l] = r - l + 1
            left_val = tList[l]
            t_map[left_val] -= 1
            if t_map[left_val] == 0:
                d_count -= 1
            l += 1
    return res
```

---

### Q12. Rearrange Students
**Topic:** `Greedy`, `Sorting`, `Hash Map`

Given two height arrays $a$ and $b$ of size $n$ representing students in two classrooms. You want to swap students between classroom $a$ and classroom $b$ such that the multiset of heights in both classrooms becomes identical. The cost of swapping student with height $x$ and height $y$ is $\min(x, y)$. Find the minimum cost to make the multisets identical. If it's impossible, return `-1`.

```python
def minCost(a, b):
    mp = {}
    n = len(a)
    for i in range(n):
        mp[a[i]] = mp.get(a[i], 0) + 1
        mp[b[i]] = mp.get(b[i], 0) - 1
        
    mini = min(min(a), min(b))
    x = []
    for val, diff in mp.items():
        if diff % 2 != 0:
            return -1
        for _ in range(abs(diff) // 2):
            x.append(val)
            
    x.sort()
    ans = 0
    m = len(x)
    for i in range(m // 2):
        ans += min(x[i], 2 * mini)
    return ans
```

---

### Q13. Social Network
**Topic:** `Hash Map`, `Arrays`

A social network has $n$ people. We are given an array `counts` of size $n$ where `counts[i]` is the size of the group that person $i$ belongs to. Group the people into valid groups. If a person $i$ says their group size is $c$, they must be in a group of size $c$. Print the members of each group.

```python
def socialGraph(counts):
    n = len(counts)
    groups = {}
    for i in range(n):
        groups.setdefault(counts[i], []).append(i)
        
    result = []
    for size, members in groups.items():
        for i in range(0, len(members), size):
            result.append(members[i:i+size])
    
    for r in result:
        print(*(r))
```

---

### Q14. String Subsequences
**Topic:** `Dynamic Programming`, `Strings`

Given two strings $s_1$ and $s_2$, determine the number of times $s_1$ appears as a subsequence in $s_2$.

```python
def countSubsequences(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(n + 1):
        dp[0][j] = 1
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[m][n]
```

---

### Q15. TTL Cache (getCacheSize)
**Topic:** `Difference Array`, `Sweep Line`, `Map`

Given cache entries with insertion time and TTL (Time To Live), and queries. Find the cache size at each query time.

```python
import bisect

def getCacheSize(d, q):
    # Sweep-line algorithm
    time_map = {}
    for entry in d:
        start = entry[0]
        end = entry[0] + entry[1] + 1
        time_map[start] = time_map.get(start, 0) + 1
        time_map[end] = time_map.get(end, 0) - 1
        
    sorted_times = sorted(time_map.keys())
    ans_at_time = []
    curr_size = 0
    for t in sorted_times:
        curr_size += time_map[t]
        ans_at_time.append(curr_size)
        
    ans = []
    for query in q:
        idx = bisect.bisect_right(sorted_times, query) - 1
        if idx >= 0:
            ans.append(ans_at_time[idx])
        else:
            ans.append(0)
    return ans
```

---

### Q16. Valid BST Permutations
**Topic:** `Dynamic Programming`, `Catalan Number`

Given an array of node values, for each node value $x$, find the number of structurally unique BSTs that can be formed with $x$ nodes. Return the answers modulo $10^8 + 7$.

```python
def numBST(nodeValues):
    MOD = 10**8 + 7
    max_val = max(nodeValues)
    dp = [0] * (max_val + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, max_val + 1):
        res = 0
        for j in range(i):
            res = (res + dp[j] * dp[i - j - 1]) % MOD
        dp[i] = res
        
    ans = [dp[val] % MOD for val in nodeValues]
    return ans
```

---

### Q17. Get the Groups
**Topic:** `Disjoint Set Union (DSU)`

Given $n$ students. We process queries of two types:
1. `"Friend"` between student1 and student2: they become friends.
2. `"Total"` between student1 and student2: find the sum of sizes of the friend groups of student1 and student2. If they are in the same group, return the size of their group (count it only once).

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            
    def get_size(self, i):
        return self.size[self.find(i)]

def getTheGroups(n, queryType, student1, student2):
    dsu = DSU(n)
    ans = []
    for q, s1, s2 in zip(queryType, student1, student2):
        if q == "Friend":
            dsu.union(s1, s2)
        elif q == "Total":
            r1 = dsu.find(s1)
            r2 = dsu.find(s2)
            if r1 == r2:
                ans.append(dsu.get_size(s1))
            else:
                ans.append(dsu.get_size(s1) + dsu.get_size(s2))
    return ans
```

---

### Q18. Server Cost Reduction
**Topic:** `Tree DP`, `Greedy`

We are given a tree of $N$ nodes where each edge has a weight. We want to select at most $k$ incident edges for each server node to minimize cost. This corresponds to the Tree DP formulation for degree-constrained maximum weight matching.

```python
def solveServerCostReduction(N, from_nodes, to_nodes, weight, k):
    adj = [[] for _ in range(N)]
    for f, t, w in zip(from_nodes, to_nodes, weight):
        adj[f].append((t, w))
        adj[t].append((f, w))
        
    def dfs(cur, parent):
        take_list = []
        skip_list = []
        diff = []
        
        for child, w in adj[cur]:
            if child != parent:
                child_not_full, child_full = dfs(child, cur)
                take_val = child_not_full + w
                skip_val = child_full
                take_list.append(take_val)
                skip_list.append(skip_val)
                diff.append(take_val - skip_val)
                
        sorted_diff = sorted(diff, reverse=True)
        sum_skip = sum(skip_list)
        
        ans_0 = sum_skip + sum(x for x in sorted_diff[:k] if x > 0)
        ans_1 = sum_skip + sum(x for x in sorted_diff[:k-1] if x > 0)
        
        return [ans_1, ans_0]
        
    ans = dfs(0, -1)
    return max(ans[0], ans[1])
```

---

### Q19. Subarray Having Odd Number of Divisors
**Topic:** `Math`, `Hash Map`, `Prime Factorization`

Given an array of integers, find the number of subarrays whose product has an odd number of divisors (i.e. the product is a perfect square).

```python
def countSubarraysWithOddDivisors(arr):
    # Represent prefix products by prime factor parity states
    def get_prime_factors_parity(val):
        factors = set()
        d = 2
        while d * d <= val:
            count = 0
            while val % d == 0:
                count += 1
                val //= d
            if count % 2 == 1:
                factors.add(d)
            d += 1
        if val > 1:
            factors.add(val)
        return factors

    state_counts = {frozenset(): 1}
    current_state = set()
    ans = 0
    
    for num in arr:
        num_factors = get_prime_factors_parity(num)
        current_state = current_state ^ num_factors
        state_key = frozenset(current_state)
        
        ans += state_counts.get(state_key, 0)
        state_counts[state_key] = state_counts.get(state_key, 0) + 1
        
    return ans
```

---

### Q20. Max Discounts
**Topic:** `Greedy`, `Bit Manipulation`

Given $n$ items and their base discounts. We can apply up to $k$ discount doublings. The $j$-th discount doubling on item $i$ increases the discount on item $i$ from $\text{base} \times 2^{j-1}$ to $\text{base} \times 2^j$. The total discount is the bitwise OR of the final discounts of all items. Find the maximum possible total discount.

```python
def maxDiscounts(discounts, k):
    n = len(discounts)
    times = [1] * n
    
    def calc(base, t):
        return base * (1 << (t - 1))
        
    for _ in range(k):
        max_increase = -1
        max_idx = -1
        for j in range(n):
            curr = calc(discounts[j], times[j])
            nxt = calc(discounts[j], times[j] + 1)
            increase = nxt - curr
            if increase > max_increase:
                max_increase = increase
                max_idx = j
        times[max_idx] += 1
        
    max_discount = 0
    for i in range(n):
        max_discount |= calc(discounts[i], times[i])
    return max_discount
```

---

### Q21. Backspace String Compare
**Topic:** `Stack`, `Strings`

Given two strings $s_1$ and $s_2$ containing lowercase letters and `#` representing backspaces. Compare if the two strings are equal when both are typed into empty text editors.

```python
def backspaceCompare(s1: str, s2: str) -> bool:
    def build(s):
        ans = []
        for c in s:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)
    return build(s1) == build(s2)
```

---

### Q22. Trilogy
**Topic:** `Brute Force`, `Math`

Given an integer $N$ and a binary flag $T$ (0 or 1). We can insert two distinct digits $d_1$ and $d_2$ ($d_1 \neq d_2$) into the string representation of $N$ at any positions. The new number must not start with '0' and must be divisible by 3. If $T = 0$, find the minimum possible value of the new number. If $T = 1$, find the maximum possible value.

```python
def solveTrilogy(N: int, T: int) -> int:
    num_str = str(N)
    candidates = []
    
    def is_divisible_by_3(s):
        return sum(int(c) for c in s) % 3 == 0
        
    for d1 in range(10):
        for d2 in range(10):
            if d1 == d2:
                continue
            s_d1 = str(d1)
            s_d2 = str(d2)
            
            for i in range(len(num_str) + 1):
                for j in range(i, len(num_str) + 1):
                    new_num_list = list(num_str)
                    new_num_list.insert(i, s_d1)
                    new_num_list.insert(j + 1, s_d2)
                    new_num = "".join(new_num_list)
                    
                    if new_num[0] != '0' and is_divisible_by_3(new_num):
                        candidates.append(int(new_num))
                        
    if not candidates:
        return -1
    return min(candidates) if T == 0 else max(candidates)
```

---

### Q23. Whole Minute Dilemma
**Topic:** `Hash Map`, `Math`

Given an array of song durations in seconds. Find the number of pairs of songs whose total duration in seconds is a multiple of 60.

```python
def playlist(songs):
    remainder_count = [0] * 60
    for song in songs:
        remainder_count[song % 60] += 1
        
    pairs = 0
    pairs += (remainder_count[0] * (remainder_count[0] - 1)) // 2
    pairs += (remainder_count[30] * (remainder_count[30] - 1)) // 2
    for i in range(1, 30):
        pairs += remainder_count[i] * remainder_count[60 - i]
    return pairs
```

---

### Q24. Modest Number
**Topic:** `Math`, `Brute Force`

A number is modest if it can be split into two parts (left and right) such that both parts are non-zero, and the number modulo the left part is equal to the right part. Given a range $[M, N]$, find all modest numbers in the range.

```python
def isModest(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        left = int(num_str[:i])
        right = int(num_str[i:])
        if left == 0 or right == 0:
            continue
        if num % left == right:
            return True
    return False

def findModestNumbers(M, N):
    ans = []
    for num in range(M, N + 1):
        if isModest(num):
            ans.append(num)
    return ans
```

---

### Q25. Number of Partitions
**Topic:** `Dynamic Programming`, `Parity`

Given an array of positive integers, find the number of ways to partition the array into contiguous subarrays such that the sums of these subarrays alternate in parity (odd, even, odd, even... or even, odd, even, odd...). Report the answer modulo $10^9 + 7$.

```python
def findNumberOfPartitions(arr):
    MOD = 10**9 + 7
    n = len(arr)
    pref = 0
    S = [0, 0]
    T = [0, 0]
    
    dp_even = 0
    dp_odd = 0
    for i in range(n):
        pref += arr[i]
        p = pref % 2
        
        if p == 0:
            dp_even = 1 + S[0]
            dp_odd = T[1]
        else:
            dp_even = S[1]
            dp_odd = 1 + T[0]
            
        dp_even %= MOD
        dp_odd %= MOD
        
        S[p] = (S[p] + dp_odd) % MOD
        T[p] = (T[p] + dp_even) % MOD
        
    return (dp_even + dp_odd) % MOD
```

---

### Q26. Build Subsequences
**Topic:** `Recursion`, `Strings`, `Sorting`

Given a string $s$ of distinct lowercase English alphabetic letters. Generate all distinct non-empty subsequences of $s$ and return them sorted lexicographically.

```python
def buildSubsequences(s):
    subsequences = set()
    n = len(s)
    
    def backtrack(index, current):
        if index == n:
            if current:
                subsequences.add(current)
            return
        backtrack(index + 1, current)
        backtrack(index + 1, current + s[index])
        
    backtrack(0, "")
    return sorted(list(subsequences))
```

---

## Multiple Choice Questions (MCQs)

### Q1. Virtual Memory Address
**Question:** Why is a virtual memory address called 'virtual'?
- **Option A:** This memory address does not map to actual memory cell that corresponds to address number.
- **Option B:** This memory is the same as physical memory.
- **Option C:** This memory cannot be accessed by applications at run time.
- **Option D:** This memory address is always present even after a system is restarted.
- **Answer:** **Option A**

---

### Q2. Semaphore Values
**Question:** Let $S$ be a binary semaphore initialized to $1$ (I-1) and a counting semaphore initialized to $10$ (I-2). Let $V1$ and $V2$ be the values of $X$ at the end... What are the final values?
- **Answer:** **15, 7**

---

### Q3. User vs Kernel Mode
**Question:** What is the main difference between "user mode" and "kernel mode"?
- **Option A:** User mode allows direct hardware access, kernel mode does not.
- **Option B:** Kernel mode can access protected memory regions.
- **Option C:** Kernel mode applications are given less priority.
- **Option D:** User mode instructions can switch the CPU to kernel mode directly.
- **Answer:** **Option B**

---

### Q4. Priority Queue Implementation
**Question:** Which data structure is best suited for implementing a priority queue?
- **Option A:** Array
- **Option B:** Stack (Slack)
- **Option C:** Heap
- **Option D:** Linked List
- **Answer:** **Option C**

---

### Q5. Memoization in Dynamic Programming
**Question:** In the context of Dynamic Programming, what is "memoization"?
- **Option A:** Writing an algorithm in a memo to remember it.
- **Option B:** Recomputing solutions to subproblems multiple times for accuracy.
- **Option C:** Storing solutions to subproblems to avoid recomputation.
- **Option D:** Optimizing a problem by breaking it into subproblems.
- **Answer:** **Option C**

---

### Q6. Selecting a Data Structure for Marathon Finishers
**Question:** A certain program must store the names of all the people who finish the City Marathon in order. After the race is over, the program must print a list containing the names. Which data structure would be the best choice for this program?
- **Option A:** A vector or resizable array
- **Option B:** A map (implemented as a binary tree of key/value pairs)
- **Option C:** A singly linked list
- **Option D:** A hash set (implemented as a hash table of keys)
- **Answer:** **Option A**

---

### Q7. C Pointer Increment Program
**Question:** What is the output of the following C program?
```c
#include <stdio.h>
int main() {
    char arr[] = "abcd";
    char *p = arr;
    printf("%c\t", ++*p);
    printf("%c\t", *p++);
    printf("%c\t", (*p)++);
    printf("%c\n", *p);
    return 0;
}
```
- **Option A:** b b b c
- **Option B:** b c c d
- **Option C:** b b c c
- **Option D:** b c c c
- **Answer:** **Option A**
- **Explanation:**
  1. `++*p` increments the character at `p` ('a' -> 'b') and prints it: `b`.
  2. `*p++` prints the character at `p` ('b') and then increments the pointer `p` to point to `arr[1]`.
  3. `(*p)++` increments the character at `p` (`arr[1]` 'b' -> 'c') but returns the old value ('b') for printing: `b`.
  4. `*p` prints the current character at `p` (which was incremented to 'c'): `c`.
  Thus, it prints `b b b c`.

---

### Q8. Cloud Database Example
**Question:** Which of the following is an example of Cloud Database?
- **Option A:** Oracle database service
- **Option B:** AWS RDS
- **Option C:** Azure SQL Database
- **Option D:** All of the above
- **Answer:** **Option D**

---

### Q9. Latest Oracle DB Release
**Question:** What is the latest long-term release of Oracle Database?
- **Option A:** 23ai
- **Option B:** 22ai
- **Option C:** 24ai
- **Option D:** 19ai
- **Answer:** **Option A**

---

### Q10. Relational Database Properties
**Question:** Which of the following is not a property of Relational Database transactions (ACID)?
- **Option A:** Atomicity
- **Option B:** Consistency
- **Option C:** Isolation
- **Option D:** Dependency
- **Answer:** **Option D** (The 'D' in ACID stands for Durability).

---

### Q11. SQL DEFAULT Constraint
**Question:** Which SQL constraint do we use to set some default value to a column when none is specified?
- **Option A:** NOT NULL
- **Option B:** DEFAULT
- **Option C:** CHECK
- **Option D:** UNIQUE
- **Answer:** **Option B**

---

### Q12. Truncate Classification
**Question:** Truncate table is classified as:
- **Option A:** Data Definition Language (DDL)
- **Option B:** Data Manipulation Language (DML)
- **Option C:** Data Control Language (DCL)
- **Option D:** Transaction Control Language (TCL)
- **Answer:** **Option A**

---

### Q13. Distributing Traffic
**Question:** How will you distribute incoming traffic to a set of Web Servers?
- **Option A:** By deploying a Firewall before the servers
- **Option B:** By deploying a router before the servers
- **Option C:** By deploying a load balancer before the servers
- **Option D:** By deploying a switch before the servers
- **Answer:** **Option C**

---

### Q14. CAP Theorem Definition
**Question:** In a distributed system, what is CAP theorem?
- **Option A:** It specifies the maximum allowable response time for a system.
- **Option B:** It describes the trade-offs between consistency, availability, and partition tolerance.
- **Option C:** It defines the minimum number of servers required for fault tolerance.
- **Option D:** It outlines the process for scaling a system horizontally.
- **Answer:** **Option B**

---

### Q15. Zombie Process in Linux
**Question:** What is a Zombie process in Linux?
- **Option A:** A process which is running in the background.
- **Option B:** A process which is running for a long time.
- **Option C:** A process whose execution has completed but it still has an entry in the process table.
- **Option D:** A process which has crashed due to memory corruption.
- **Answer:** **Option C**

---

### Q16. HTTP Method for Resource Creation
**Question:** Which HTTP method is suitable for resource creation in RESTful services?
- **Option A:** PUT
- **Option B:** PATCH
- **Option C:** POST
- **Option D:** CREATE
- **Answer:** **Option C**

---

### Q17. HTTP Server Error Category
**Question:** Which response status code category represents server error in HTTP/REST?
- **Option A:** 1xx
- **Option B:** 2xx
- **Option C:** 4xx
- **Option D:** 5xx
- **Answer:** **Option D**

---

### Q18. REST Subresource URL Pattern
**Question:** Which URL Pattern should you follow for accessing a subresource (employees) attached to a specific parent (company)?
- **Option A:** `/company/{companyId}/employees/{employeeId}`
- **Option B:** `/companies/employees/{companyId}/{employeeId}`
- **Option C:** `/companies/{companyId}/employee/{employeeId}`
- **Option D:** `/companies/{companyId}/employees/{employeeId}`
- **Answer:** **Option D**

---

### Q19. BGP Protocol
**Question:** What does the acronym BGP stand for in networking, and what layer of the OSI model does it operate on?
- **Option A:** Best Gateway Protocol, Network layer
- **Option B:** Border Gateway Protocol, Application layer
- **Option C:** Border Gateway Protocol, Network layer
- **Option D:** Backbone Gateway Protocol, Data Link layer
- **Answer:** **Option C** (Though it runs over TCP on the Application layer, standard networking questions classify it as a routing protocol belonging functionally to the Network layer).

---

### Q20. TCP Reliability Mechanism
**Question:** What mechanism does TCP use to ensure the data sent from one host to another is received reliably?
- **Option A:** Tunneling
- **Option B:** Handshaking
- **Option C:** Sequence numbers and acknowledgements
- **Option D:** Packet sniffing
- **Answer:** **Option C**

---

### Q21. System Call Interrupt in Linux
**Question:** Which interrupt is defined for system calls in Linux?
- **Option A:** 0x10
- **Option B:** 0x60
- **Option C:** 0x80
- **Option D:** 0x40
- **Answer:** **Option C** (0x80)

---

### Q22. Infix to Postfix Conversion
**Question:** What is the postfix expression for the corresponding infix expression? `a+b*c+(d*e)`
- **Option A:** abc*+de*+
- **Option B:** abc*+de*+
- **Option C:** a+bc*de*+
- **Option D:** abc*+(de)*+
- **Answer:** **Option A**

---

### Q23. C Macro Output
**Question:** What is the output of the following C program?
```c
#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
int main() {
    int x = 5, y = 10;
    printf("%d %d %d\n", MAX(x++, y++), x, y);
    return 0;
}
```
- **Option A:** 11 6 12
- **Option B:** 12 6 12
- **Option C:** 11 7 12
- **Option D:** 12 7 12
- **Answer:** **Option A**

---

### Q24. Java Array Reversal Method
**Question:** What is the function of this Java method?
```java
public static void function_1(int[] data, int low, int high) {
    if (low < high) {
        int temp = data[low];
        data[low] = data[high];
        data[high] = temp;
        function_1(data, low + 1, high - 1);
    }
}
```
- **Option A:** The sum of all elements of the array.
- **Option B:** The product of all elements of the array.
- **Option C:** The last element of the array.
- **Option D:** Reverses the contents of the array.
- **Answer:** **Option D**

---

### Q25. Database Range Partitioning SQL
**Question:** Which of the following SQL statements correctly creates a range partitioned table on `order_date`?
- **Option A:** `create table orders partition by range columns (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2);`
- **Option B:** `create table orders partition by range (order_date) ...`
- **Answer:** **Option A** (or **Option C** depending on the specific DBMS SQL dialect).

---

### Q26. Non-Relational Database Unsuitable Design Criteria
**Question:** Which of the following design criteria are not valid/suitable for Non-Relational Databases?
- **Option A:** Your application required super-low latency.
- **Option B:** Your data are unstructured without any relation between them.
- **Option C:** You only need to serialize & deserialize data.
- **Option D:** You need to store a very small amount of data.
- **Answer:** **Option D**

---

### Q27. Use of `/etc/hosts` in Linux
**Question:** What is the use of `/etc/hosts` file in Linux?
- **Option A:** It contains the list of all users.
- **Option B:** It contains a list of all files in the system.
- **Option C:** It contains the time and date information.
- **Option D:** It contains the FQDN to IP address mappings.
- **Answer:** **Option D**

---

### Q28. SQL HAVING Clause
**Question:** Which SQL Clause restricts the groups of rows returned to those groups for which the specified condition is True?
- **Option A:** Where clause
- **Option B:** Having Clause
- **Option C:** Distinct
- **Option D:** Exists
- **Answer:** **Option B**

---

### Q29. REST API Idempotency
**Question:** What does idempotency mean in REST API design?
- **Option A:** The ability of an API to handle multiple requests in parallel.
- **Option B:** The property that a method can be called multiple times without different outcomes.
- **Option C:** The capability of an API to update data.
- **Option D:** The feature of an API that allows it to delete resources.
- **Answer:** **Option B**

---

### Q30. HTTP Method for Metadata Retrieval
**Question:** Which is the HTTP request method used to retrieve the metadata associated with the resource's state?
- **Option A:** GET
- **Option B:** PUT
- **Option C:** HEAD
- **Option D:** POST
- **Answer:** **Option C**

---

### Q31. Ring Topology Failure
**Question:** In a ring topology network, if one device fails, how does it affect the network?
- **Option A:** Only the failed device is affected.
- **Option B:** All devices in the network are affected.
- **Option C:** Only the devices between which the failed device exists are affected.
- **Option D:** The network continues to function normally.
- **Answer:** **Option B**

---

### Q32. Address Resolution Protocol (ARP)
**Question:** What is the purpose of ARP (Address Resolution Protocol) in computer networking?
- **Option A:** To convert IP addresses to MAC addresses.
- **Option B:** To convert domain names to IP addresses.
- **Option C:** To establish a secure connection between client and server.
- **Option D:** To route packets between networks.
- **Answer:** **Option A**

---

### Q33. Symmetric Sparse Matrix Storage
**Question:** In what way can the Symmetric Sparse Matrix be stored efficiently?
- **Option A:** Heap
- **Option B:** Binary tree
- **Option C:** Hash table
- **Option D:** Adjacency List
- **Answer:** **Option D**

---

### Q34. 2-3 Tree vs Binary Search Tree
**Question:** Which of the following is false?
- **Option A:** 2-3 tree requires less storage than the BST.
- **Option B:** Lookup in 2-3 tree is more efficient than in BST.
- **Option C:** 2-3 tree is shallower than BST.
- **Option D:** 2-3 tree is a balanced tree.
- **Answer:** **Option A**

---

### Q35. Chef's Puzzle (Ingredients Logic)
**Question:** Out of the nine ingredients, a chef wants to use exactly five. Given the following statements:
1. If bacon is not used, then grapes, hazelnuts, and ice cream are not used.
2. If apricots are used, then bacon and cake are used.
3. If donuts are not used, apricots are not used.
4. Apricots and eggs are used.
How many of the 5 ingredients are known?
- **Answer:** **5**
- **Explanation:**
  - Statement 4 tells us Apricots and Eggs are used. (2 ingredients)
  - Statement 2 says if Apricots are used, then Bacon and Cake are used. (Now 4 ingredients: Apricots, Eggs, Bacon, Cake)
  - Statement 3 says if Donuts are not used, Apricots are not used. Since Apricots are used, Donuts must be used. (Now 5 ingredients: Apricots, Eggs, Bacon, Cake, Donuts)
  - Thus, all 5 ingredients are known.

---

### Q36. Eight Cities Journey (Eulerian Path)
**Question:** There is a network of eight cities connected by roads. A traveler must drive on each road segment once but can visit a city multiple times. If the journey begins at B, where will it end?
- **Answer:** **E**

---

### Q37. Painted Cube Puzzle
**Question:** A cube is painted green on all surfaces and is cut into 1000 identical cubes. How many of the smaller cubes have three faces painted?
- **Answer:** **8** (Only the corner cubes have 3 faces painted).

---

### Q38. Favorite Color Puzzle
**Question:** Five people (Jack, Matthew, Albert, Peter, Sebastian) play different sports (football, cricket, etc.) and come from different countries (UK, China, India, etc.) with different favorite colors.
Whose favorite color is black?
- **Answer:** **Matthew**

---

### Q39. Standing Order Puzzle
**Question:** Five people stand in a row. Tyson is leftmost. Richard is second from the right. Peter stands next to Quinn and Richard. Who is in the middle?
- **Answer:** **Peter** (The arrangement is: Tyson, Quinn, Peter, Richard, Steve).

---

### Q40. Synonyms and Antonyms
**Question:** Choose the correct answer:
1. A self-governing country or region: **Autonomy**
2. Farthest in meaning from "spawned": **Squelched**
3. Remainder of 1992 divided by 92: **60** (Answer option: "None of the above")
4. Percentage of students who like only cricket (60% like football, 40% like cricket, 12% like neither): **28%**
5. Which memory allocation scheme suffers from External Fragmentation? **Segmentation**
6. Time complexity to calculate the number of edges in a graph whose information is stored in form of an adjacency matrix: **O(V^2)**
7. Broadcast address for the subnet 172.16.10.128/27: **172.16.10.159**
*Total questions: 29*

---

## Table of Contents
1. [Coding Questions](#coding-questions)
2. [SQL Questions](#sql-questions)
3. [MCQ Questions](#mcq-questions)
4. [Puzzles](#puzzles)
5. [Logical & Aptitude Questions](#logical--aptitude-questions)
6. [Reading Comprehension](#reading-comprehension)

---

## Coding Questions

### Q1. Friend Circles (getTheGroups)

**Topic:** `disjoint-set-union`, `graphs`  

**Question:**  
There are $n$ students numbered $1$ to $n$. Initially, each student belongs to their own group of size 1.
We are given a series of queries processed via two types of operations:
1. `Friend`: Merge the groups of `student1[i]` and `student2[i]`. If they are already in the same group, do nothing.
2. `Total`: Find the sum of the group sizes of `student1[i]` and `student2[i]`. If they are in the same group, return that group's size.

Implement the function `getTheGroups(n, queryType, students1, students2)` which takes:
- An integer `n` representing the number of students.
- A list of strings `queryType` (`'Friend'` or `'Total'`).
- Two lists of integers `students1` and `students2` indicating the students involved in each query.

The function should return a list of integers representing the results of each `Total` query.

**C++ Solution:**
```cpp
#include <vector>
#include <string>
#include <numeric>

using namespace std;

class DSU {
private:
    vector<int> parent;
    vector<int> group_size;

public:
    DSU(int n) {
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        group_size.assign(n + 1, 1);
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]); // Path compression
    }

    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            // Union by size
            if (group_size[root_i] < group_size[root_j]) {
                swap(root_i, root_j);
            }
            parent[root_j] = root_i;
            group_size[root_i] += group_size[root_j];
        }
    }

    int get_size(int i) {
        return group_size[find(i)];
    }
};

vector<int> getTheGroups(int n, vector<string> queryType, vector<int> students1, vector<int> students2) {
    DSU dsu(n);
    vector<int> results;
    for (size_t i = 0; i < queryType.size(); ++i) {
        if (queryType[i] == "Friend") {
            dsu.unite(students1[i], students2[i]);
        } else if (queryType[i] == "Total") {
            int root1 = dsu.find(students1[i]);
            int root2 = dsu.find(students2[i]);
            if (root1 == root2) {
                results.push_back(dsu.get_size(root1));
            } else {
                results.push_back(dsu.get_size(root1) + dsu.get_size(root2));
            }
        }
    }
    return results;
}
```

**Python Solution:**
```python
def getTheGroups(n, queryType, students1, students2):
    parent = list(range(n + 1))
    group_size = [1] * (n + 1)
    
    def find(i):
        # Path compression
        curr = i
        while parent[curr] != curr:
            parent[curr] = parent[parent[curr]]
            curr = parent[curr]
        return curr
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            // Union by size
            if group_size[root_i] < group_size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            group_size[root_i] += group_size[root_j]

    results = []
    for q_type, s1, s2 in zip(queryType, students1, students2):
        if q_type == 'Friend':
            union(s1, s2)
        elif q_type == 'Total':
            root_s1 = find(s1)
            root_s2 = find(s2)
            if root_s1 == root_s2:
                results.append(group_size[root_s1])
            else:
                results.append(group_size[root_s1] + group_size[root_s2])
    return results
```

---

## SQL Questions

### Q2. Range Partitioning in SQL

**Topic:** `sql`, `partitioning`  

**Question:**  
Consider a database table `orders` with columns: `order_id` (Primary Key), `customer_id`, `order_date`, and `total_amount`. Which of the following SQL statements would correctly create a partitioned table based on the `order_date` column, partitioned by range?

**Options:**  
1. `create table orders partition by range columns (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2);`  
2. `create table orders partition by range (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2) primary key (order_id);`  
3. `create table orders partition by range (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2);`  
4. `create table orders partition by range (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2) ...`  

**Answer:**  
Option 3:  
```sql
create table orders partition by range (order_date) (
    partition p1 values less than ('2023-01-01') tablespace ts1, 
    partition p2 values less than ('2024-01-01') tablespace ts2
);
```

**Explanation:**  
In SQL range partitioning syntax (especially Oracle), the `PARTITION BY RANGE` clause specifies the column(s) on which range partitioning is applied. Individual partition ranges are defined with the `VALUES LESS THAN` clause. Option 3 presents the correct syntactic form.

---

### Q3. Having Clause in SQL

**Topic:** `sql`, `aggregations`  

**Question:**  
Which Clause restricts the groups of rows returned to those groups for which the specified condition is True?

**Options:**  
- `Where clause`  
- `Having Clause`  
- `Distinct`  
- `Exists`  

**Answer:**  
`Having Clause`

**Explanation:**  
The `HAVING` clause is used to filter groups of rows created by the `GROUP BY` clause. While the `WHERE` clause filters individual rows before grouping, the `HAVING` clause applies conditions to the aggregated values of the groups.

---

## MCQ Questions

### Q4. Virtual Memory Address Definition

**Topic:** `operating-systems`, `virtual-memory`  

**Question:**  
Why is a virtual memory address called 'virtual'?

**Options:**  
- This memory address does not map to actual memory cell that corresponds to address number.  
- This memory is the same as physical memory.  
- This memory cannot be accessed by applications at run time.  
- This memory address is always present even after a system is restarted.  

**Answer:**  
This memory address does not map to actual memory cell that corresponds to address number.

**Explanation:**  
Virtual memory addresses are logical references generated by the CPU. The Memory Management Unit (MMU) translates these logical addresses into actual physical addresses (RAM) via page tables. Hence, they do not directly correspond to a physical memory cell of the same address number.

---

### Q5. Infix to Postfix Conversion

**Topic:** `data-structures`, `stacks`  

**Question:**  
What is the postfix expression for the corresponding infix expression? `a+b*c+(d*e)`

**Options:**  
- `abc*+de*+`  
- `abc+*de*+`  
- `a+bc*de+*`  
- `abc*+(de)*+`  

**Answer:**  
`abc*+de*+`

**Explanation:**  
Let's follow operator precedence rules:
1. First evaluate sub-expressions: `d * e` becomes `de*`.
2. Multiplication has higher precedence: `b * c` becomes `bc*`.
3. Then evaluate addition left-to-right:
   - `a + (b*c)` becomes `abc*+`.
   - `(a + b*c) + (d*e)` becomes `abc*+ de* +`.
Hence, the final postfix expression is `abc*+de*+`.

---

### Q6. C Preprocessor Macro and Post-Increment Evaluation

**Topic:** `c-programming`, `preprocessor`  

**Question:**  
What is the output of the following C program?
```c
#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    int x = 5, y = 10;
    printf(" %d %d %d\n", MAX(x++, y++), x, y);
    return 0;
}
```

**Options:**  
- `11 6 12`  
- `12 6 12`  

**Answer:**  
`11 6 12`

**Explanation:**  
1. The macro `MAX(x++, y++)` expands directly to `((x++) > (y++) ? (x++) : (y++))`.
2. When evaluating `(x++) > (y++)`, the post-increments return the current values first: `5 > 10` is compared.
3. This comparison is false. However, as side effects of evaluation, both `x` and `y` are incremented: `x` becomes `6`, and `y` becomes `11`.
4. Because the condition is false, the expression goes to the second branch: `(y++)`.
5. The value of `y++` (with current `y = 11`) evaluates to `11`, which is returned as the value of the macro.
6. After evaluation, `y` is incremented once more, changing `y` to `12`.
7. Thus, `MAX(x++, y++)` evaluates to `11`, `x` is `6`, and `y` is `12`.

---

### Q7. Java Recursive Array Reversal

**Topic:** `java`, `recursion`  

**Question:**  
Consider the below Java method. What is the output/effect of this method?
```java
public static void function_1(int [] data, int low, int high) {
    if (low < high) {
        int temp = data[low];
        data[low] = data[high];
        data[high] = temp;
        function_1(data, low + 1, high -1);
    }
}
```

**Answer:**  
It reverses the elements of the `data` array in-place between the indices `low` and `high` (inclusive).

**Explanation:**  
The function swaps `data[low]` and `data[high]`, then recursively calls itself with `low + 1` and `high - 1`. The recursion stops when `low >= high`, effectively reversing the array segment.

---

### Q8. CAP Theorem Trade-offs

**Topic:** `system-design`, `cap-theorem`  

**Question:**  
What does CAP theorem describe with respect to System Design?

**Options:**  
- The relationship between CPU and memory usage  
- The trade-offs between consistency, availability, and partition tolerance  
- The process of data encryption  
- The principles of object-oriented programming  

**Answer:**  
The trade-offs between consistency, availability, and partition tolerance  

**Explanation:**  
The CAP theorem states that in a distributed computer system, it is impossible to simultaneously provide more than two out of three guarantees: Consistency (C), Availability (A), and Partition tolerance (P).

---

### Q9. Suitability of Non-Relational Databases

**Topic:** `databases`, `nosql`  

**Question:**  
Which of the following design criteria are not valid/suitable for Non-Relational Databases?

**Options:**  
- Your application required super-low latency  
- Your data are unstructured without any relation between them  
- You only need to serialize & deserialize data (JSON, XML, YAML)  
- You need to store a very small amount of data  

**Answer:**  
You need to store a very small amount of data  

**Explanation:**  
Non-Relational (NoSQL) databases are designed for low latency, horizontal scaling, unstructured data, and document storage formats. Storing a very small amount of data does not justify the architectural overhead of a NoSQL database; a simple relational database or local file is far simpler and more appropriate.

---

### Q10. Use of `/etc/hosts` in Linux

**Topic:** `operating-systems`, `linux`  

**Question:**  
What is the use of `/etc/hosts` file in Linux?

**Options:**  
- It contains the list of all users.  
- It contains a list of all files in the system.  
- It contains the time and date information.  
- It contains the FQDN to IP address mappings.  

**Answer:**  
It contains the FQDN to IP address mappings.

**Explanation:**  
The `/etc/hosts` file is a local operating system file that maps hostnames (FQDNs) to IP addresses. It provides a static DNS lookup facility that takes precedence over external DNS servers.

---

### Q11. Idempotency in REST API

**Topic:** `system-design`, `rest-apis`  

**Question:**  
What does idempotency mean in REST API design?

**Options:**  
- The ability of an API to handle multiple requests in parallel  
- The property that a method can be called multiple times without different outcomes  
- The capability of an API to update data  
- The feature of an API that allows it to delete resources  

**Answer:**  
The property that a method can be called multiple times without different outcomes  

**Explanation:**  
An API method is idempotent if executing it multiple times yields the exact same state as executing it a single time. Safe HTTP methods like `GET`, `PUT`, and `DELETE` are designed to be idempotent.

---

### Q12. Single Ring Topology Device Failure

**Topic:** `computer-networks`, `network-topologies`  

**Question:**  
In a ring topology network, if one device fails, how does it affect the network?

**Options:**  
- Only the failed device is affected  
- All devices in the network are affected  
- Only the devices between which the failed device exists are affected  
- The network continues to function normally  

**Answer:**  
All devices in the network are affected  

**Explanation:**  
In a standard, single unidirectional ring topology, a token or data frame passes through each device sequentially. If one device in the loop fails, the loop is broken, and communications between all nodes are disrupted.

---

### Q13. Address Resolution Protocol (ARP) Purpose

**Topic:** `computer-networks`, `network-protocols`  

**Question:**  
What is the purpose of ARP (Address Resolution Protocol) in computer networking?

**Options:**  
- To convert IP addresses to MAC addresses  
- To convert domain names to IP addresses  
- To establish a secure connection between client and server  
- To route packets between networks  

**Answer:**  
To convert IP addresses to MAC addresses  

**Explanation:**  
ARP resolves network layer IPv4 addresses to link layer physical MAC addresses within a local area network (LAN).

---

### Q14. Symmetric Sparse Matrix Storage Efficiency

**Topic:** `data-structures`, `matrices`  

**Question:**  
In what way the Symmetry Sparse Matrix can be stored efficiently?

**Options:**  
- Heap  
- Binary tree  
- Hash table  
- Adjacency List  

**Answer:**  
Adjacency List  

**Explanation:**  
A symmetric sparse matrix can be modeled as the adjacency matrix of an undirected graph. For sparse connections, storing it as an adjacency list is the most memory-efficient approach because it only stores non-zero entries (edges).

---

### Q15. Binary Search Trees vs 2-3 Trees Properties

**Topic:** `data-structures`, `trees`  

**Question:**  
Which of the following is false?

**Options:**  
- `2-3 tree requires less storage than the BST`  
- `lookup in 2-3 tree is more efficient than in BST`  
- `2-3 tree is shallower than BST`  
- `2-3 tree is a balanced tree`  

**Answer:**  
`2-3 tree requires less storage than the BST`  

**Explanation:**  
A 2-3 tree node requires more pointers (up to 3) and keys (up to 2), alongside balancing metadata, to accommodate multi-way search. Conversely, a BST node only has 2 pointers and 1 key. Thus, a 2-3 tree has higher storage overhead per node compared to a BST.

---

### Q16. Logical Figure Pattern Completion

**Topic:** `non-verbal-reasoning`, `pattern-matching`  

**Question:**  
Identify the missing figure (`?`) from the options to complete the pattern.

![Non Verbal Pattern](file:///R:/DSA/Company%20wise%20prep%20resource/Oracle/IMG-20240730-WA0095.jpg)

**Answer:**  
Option 4 (Option D in the sequence of options)

**Explanation:**  
- In the first transition (Box 1 to Box 2): The dots remain at the top. The lines connected to a bottom-center vertex change to fan out downward from a top-center vertex (pointing away from the dots). The star shifts to the bottom-center.
- In the second transition (Box 3 to Box 4): The 3 dots remain at the left-top. The lines connected to a bottom-right vertex must change to fan out downward/rightward from a left-top vertex (pointing away from the dots). The arc moves to the bottom-left. This matches Option D.

---

## Puzzles

### Q17. Chef's Ingredients Combination

**Topic:** `puzzles`, `deduction`  

**Question:**  
Out of nine ingredients, a chef wants to use exactly five. Given the following statements, how many of the 5 ingredients are known?
- The ingredients are: apricots, bacon, cake, donuts, eggs, figs, grapes, hazelnuts, and ice cream.
1. If bacon is not used, then grapes, hazelnuts, and ice cream are not used.
2. If apricots are used, then bacon and cake are used.
3. If donuts are not used, apricots are not used.
4. Apricots and eggs are used.

**Options:**  
- `2`  
- `3`  
- `4`  
- `5`  

**Answer:**  
`5`

**Explanation:**  
Let's deduce the ingredients step-by-step:
1. Statement 4: **Apricots** and **Eggs** are used (Count = 2).
2. Statement 2: Since apricots are used, **Bacon** and **Cake** must be used (Count = 4).
3. Statement 3: "If donuts are not used, apricots are not used" is equivalent to "If apricots are used, donuts are used." Since apricots are used, **Donuts** must be used (Count = 5).
We have identified exactly 5 ingredients: Apricots, Eggs, Bacon, Cake, and Donuts. Since the chef wants to use exactly five, all 5 are uniquely known.

---

### Q18. Eulerian Path (Paths in a Graph 2)

**Topic:** `puzzles`, `graph-theory`  

**Question:**  
There is a network of eight cities (represented by vertices) connected by roads. A traveler must drive on each road segment once but can visit a city multiple times if necessary. Furthermore, the starting and ending points do not have to match. New roads are constructed between C and G, and between H and F. If the journey begins at B, where will it end?

![Graph Diagram](file:///R:/DSA/Company%20wise%20prep%20resource/Oracle/IMG-20240730-WA0080.jpg)

**Answer:**  
`E`

**Explanation:**  
Driving on each road segment exactly once is equivalent to finding an **Eulerian Path**.
An Eulerian path exists in a connected graph if and only if exactly 0 or 2 vertices have odd degrees. If there are 2 vertices of odd degree, the path must start at one and end at the other.
Let's list the degrees after adding the edges (C, G) and (H, F):
- $A$: degree $2$ (even)
- $B$: degree $3$ (odd)
- $F$: degree $4$ (even)
- $G$: degree $4$ (even)
- $H$: degree $4$ (even)
- $C$: degree $4$ (even)
- $E$: degree $3$ (odd)
- Bottom-most vertex: degree $2$ (even)

Since $B$ and $E$ are the only vertices with odd degree, any Eulerian Path starting at $B$ must end at $E$.

---

### Q19. Painted Cube Puzzle (3 Faces Painted)

**Topic:** `puzzles`, `cubes`  

**Question:**  
A cube is painted green on all surfaces and is cut into 1000 identical cubes. How many of the smaller cubes have three faces painted?

**Options:**  
- `8`  
- `10`  
- `100`  
- `64`  

**Answer:**  
`8`

**Explanation:**  
The smaller cubes that have 3 faces painted are the corner cubes of the large cube. Any cube has exactly 8 corners, regardless of the number of cuts made.

---

### Q20. Favorite Color Allocation Logic (Who likes black?)

**Topic:** `puzzles`, `analytical-reasoning`  

**Question:**  
There are five people: Jack, Matthew, Albert, Peter, and Sebastian.
Each plays one sport: football, cricket, volleyball, badminton, or squash.
They are from: South Korea, the UK, India, China, or Russia.
Their favorite colors are: brown, green, red, black, or yellow.
Find whose favorite color is black given:
1. Jack's favorite color is red. He is not from India or China.
2. Albert plays football. His favorite color is not yellow, and he is not from the UK.
3. Peter and Sebastian have yellow and green as their favorite colors.
4. Matthew plays badminton. He is from Russia.
5. Peter and Sebastian are from China and UK.
6. Brown is the favorite color of the person from India.
7. Green is the favorite color of the person from China.
8. The person from South Korea plays squash and the person from the UK plays volleyball. One of them has yellow as his favorite color.

**Options:**  
- `Matthew`  
- `Albert`  
- `Peter`  
- `Sebastian`  

**Answer:**  
`Matthew`

**Explanation:**  
- From 1: Jack = Red (not India or China).
- From 4: Matthew = Russia, Badminton.
- From 3, 5, 7: Peter and Sebastian are from China and UK. Their colors are Yellow and Green. Since Green belongs to China (from 7), the UK person has Yellow.
- This leaves countries for Jack and Albert: South Korea and India.
- Since Jack is not from India, Jack is from South Korea. Thus, Albert is from India.
- From 6: The person from India has Brown. Since Albert is from India, Albert = Brown.
- Now, let's tally colors: Red (Jack), Yellow/Green (Peter/Sebastian), Brown (Albert). The only remaining color is Black, which must belong to Matthew.

---

### Q21. Standing Order 2 (Row Arrangement)

**Topic:** `puzzles`, `linear-arrangement`  

**Question:**  
There are five people - Peter, Tyson, Richard, Steve, and Quinn - standing in a row. Who is in the middle?
1. Peter is next to Quinn and Steve is next to Richard.
2. Steve is not next to Tyson.
3. Tyson is on leftmost position.
4. Richard is on the second position from the right.
5. Peter stands somewhere to the right of both Quinn and Tyson.
6. Peter and Richard are next to each other.

**Options:**  
- `Peter`  
- `Richard`  
- `Steve`  
- `Quinn`  

**Answer:**  
`Peter`

**Explanation:**  
Let the positions be 1 (leftmost) to 5 (rightmost).
- Tyson is leftmost: `[T, _, _, _, _]`
- Richard is second from right: `[T, _, _, R, _]`
- Peter is next to Richard (so Peter is at 3 or 5).
- If Peter is at 3: Quinn must be next to Peter (at 2), so `[T, Q, P, R, _]`.
- Steve must be next to Richard, so Steve must be at 5: `[T, Q, P, R, S]`.
- This satisfies all conditions: Steve is not next to Tyson, Peter is to the right of Quinn and Tyson, and Peter is next to Quinn.
Thus, the middle person (position 3) is Peter.

---

## Logical & Aptitude Questions

### Q22. English Vocabulary - Self-governing country

**Topic:** `aptitude`, `english`  

**Question:**  
Choose the correct option which can be substituted for the given sentence:  
*A self-governing country or region*

**Options:**  
- `Autonomy`  
- `Autocracy`  
- `Anarchy`  
- `Ethnology`  

**Answer:**  
`Autonomy`

---

### Q23. English Idiom - Candidate suitability

**Topic:** `aptitude`, `english`  

**Question:**  
I don't think we should hire him. He seems like _______.

**Options:**  
- `A fish out of water`  
- `The black sheep of the family`  
- `A wolf in sheep's clothing`  
- `The apple of my eye`  

**Answer:**  
`A wolf in sheep's clothing`

---

### Q24. English Idiom - Academic success

**Topic:** `aptitude`, `english`  

**Question:**  
I've been studying for this exam for months, so I'm hoping to _______.

**Options:**  
- `Hit the ground running`  
- `Have a field day`  
- `Be a dark horse`  
- `Have a lot on my plate`  

**Answer:**  
`Hit the ground running`

---

### Q25. Sports Enthusiasts Logic

**Topic:** `aptitude`, `logic`  

**Question:**  
In a company, 100 employees are randomly selected. 50 like watching football, 40 like watching hockey, and the rest like both. Find out the number of employees who like to watch at least one of the games.

**Options:**  
- `40`  
- `90`  
- `80`  
- `20`  

**Answer:**  
`80`

**Explanation:**  
Let $F$ be football and $H$ be hockey.
- Total employees = 100.
- Football total = 50.
- Hockey total = 40.
- "The rest" refers to those who are not in the individual sets, computed as: $100 - (50 + 40) = 10$.
- So, 10 employees like both ($F \cap H = 10$).
- The number of employees who like at least one of the games ($F \cup H$) is:
  $F \cup H = F + H - (F \cap H) = 50 + 40 - 10 = 80$.

---

### Q26. Football and Cricket Popularity Percentages

**Topic:** `aptitude`, `percentages`  

**Question:**  
In a group of students, 60% like football, 40% like cricket. What percentage of students like only cricket if 12% of the students like neither football nor cricket?

**Options:**  
- `28`  
- `14`  
- `56`  
- `42`  

**Answer:**  
`28`

**Explanation:**  
- Total students = 100%
- Football ($F$) = 60%, Cricket ($C$) = 40%
- Neither ($N$) = 12%
- Those who like at least one ($F \cup C$) = 100% - 12% = 88%
- Using Inclusion-Exclusion: $F \cup C = F + C - (F \cap C) \implies 88\% = 60\% + 40\% - (F \cap C) \implies F \cap C = 12\%$
- Percentage who like only cricket = $C - (F \cap C) = 40\% - 12\% = 28\%$.

---

### Q27. Interpret Charts - Brand Phone User Growth

**Topic:** `aptitude`, `data-interpretation`  

**Question:**  
Which brand/version phone had the highest percentage increase in user additions in September 2012 compared to August 2012?

**Data:**  
*Addition of customers (in millions):*
- **Aug-12:** Hington = 0.36, Euphore Version-1 = 1.24, Euphore Version-2 = 0.60
- **Sep-12:** Hington = 1.16, Euphore Version-1 = 1.08, Euphore Version-2 = 0.80
- **Oct-12:** Hington = 1.98, Euphore Version-1 = 0.84, Euphore Version-2 = 0.48

**Answer:**  
`Hington`

**Explanation:**  
Let's compute the percentage increase in customer additions from August to September:
- **Hington:** $\frac{1.16 - 0.36}{0.36} \times 100\% = \frac{0.80}{0.36} \times 100\% \approx 222.2\%$
- **Version-2:** $\frac{0.80 - 0.60}{0.60} \times 100\% = \frac{0.20}{0.60} \times 100\% \approx 33.3\%$
- **Version-1:** Decreased from 1.24 to 1.08.
Thus, Hington registered the highest percentage increase.

---

## Reading Comprehension

### Q28. Reading Comprehension: Second Industrial Revolution

**Topic:** `english`, `comprehension`  

**Question:**  
The word "spawned" in the passage is farthest in meaning from:

**Options:**  
- `fostered`  
- `begat`  
- `generated`  
- `squelched`  

**Answer:**  
`squelched`

**Explanation:**  
"Spawned" means to generate, create, or bring forth. The word "squelched" means to suppress, silence, or crush, making it the antonym (farthest in meaning).

---

### Q29. Reading Comprehension: French Revolution

**Topic:** `english`, `comprehension`  

**Question:**  
According to the passage, which of the following statements is incorrect?

**Options:**  
- King Louis XVI and Queen Marie Antoinette lived an extravagant lifestyle.  
- All the nobles were happy with the way King Louis XVI governed the country.  
- The execution of King Louis XVI and his queen resulted from a penchant for abusing power.  
- In June 1792, the king attempted to flee Paris for the Austrian frontier.  

**Answer:**  
`All the nobles were happy with the way King Louis XVI governed the country.`

**Explanation:**  
The passage explicitly states: *"Even some in the noble classes became disenchanted with the monarchy as their own access to a lavish lifestyle was curtailed."* Therefore, the statement that all nobles were happy is incorrect.
*Total questions: 56*

---

## Table of Contents
1. [Coding Questions](#coding-questions)
2. [SQL Questions](#sql-questions)
3. [Multiple Choice Questions (MCQs)](#multiple-choice-questions-mcqs)
   - [Operating Systems](#operating-systems)
   - [Data Structures & Algorithms](#data-structures--algorithms)
   - [DBMS & System Design](#dbms--system-design)
   - [Computer Networks](#computer-networks)
4. [Aptitude & Logical Reasoning](#aptitude--logical-reasoning)

---

## Coding Questions

### Q1. Best Sum Any Tree Path

**Topic:** `Tree`, `Dynamic Programming`, `Depth First Search`

**Question:**  
Given a tree rooted at node 0 and a value assigned to each node, determine the maximum sum of the values along any path in the tree. The path must not be empty, and in some cases it might not go through the root.

**Parameters:**
- `parent`: An integer array where `parent[i]` means that node `j` is a parent of node `i`. `parent[0]` is always `-1` to indicate that node 0 is the root.
- `values`: An integer array where `values[i]` denotes the value of node `i`.

**Constraints:**
- $1 \le n \le 10^5$
- `parent[0] = -1`
- $0 \le parent[i] < n$ for $1 \le i < n$
- $-1000 \le values[i] \le 1000$
- The parent array defines a valid tree.

**Example:**
- `parent` = `[-1, 0, 1, 2, 0]`
- `values` = `[-2, 10, 10, -3, 10]`

The tree looks like:
```
      0 (-2)
     /      \
   1 (10)   4 (10)
   /
  2 (10)
 /
3 (-3)
```
The path with the largest sum starts at node 2 and ends at node 4: `2 -> 1 -> 0 -> 4`. The sum of node values along this path is `10 + 10 + (-2) + 10 = 28`.

**Solution:**
```python
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def bestSumAnyTreePath(parent, values):
    """
    Finds the maximum sum of any non-empty path in a tree.
    Time Complexity: O(N log K) where K is the maximum branching factor (due to sorting children).
    Space Complexity: O(N) for the recursion stack and adjacency list.
    """
    n = len(parent)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        adj[parent[i]].append(i)
        
    max_path_sum = -float('inf')
    
    def dfs(u):
        nonlocal max_path_sum
        
        # Retrieve downward path sums for all children of u
        child_paths = []
        for v in adj[u]:
            child_paths.append(dfs(v))
            
        # Sort in descending order to easily find the largest sums
        child_paths.sort(reverse=True)
        
        # Select the two largest positive path sums from children
        d1 = child_paths[0] if len(child_paths) > 0 else 0
        d2 = child_paths[1] if len(child_paths) > 1 else 0
        
        # Calculate the max path sum where node u is the highest node (peak of the path)
        current_max = values[u] + max(0, d1) + max(0, d2)
        max_path_sum = max(max_path_sum, current_max)
        
        # Return the max downward path sum starting from u
        return values[u] + max(0, d1)
        
    dfs(0)
    return max_path_sum
```

---

## SQL Questions

### Q2. Database Partitioning

**Topic:** `SQL`, `Database Partitioning`, `Oracle`

**Question:**  
Consider a database table `orders` with columns: `order_id` (Primary Key), `customer_id`, `order_date`, and `total_amount`. Which of the following SQL statements would correctly create a partitioned table based on the `order_date` column, partitioned by range?

**Options:**
- A) `create table orders partition by range columns (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2);`
- B) `create table orders partition by range (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2) primary key (order_id);`
- C) `create table orders partition by range (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2);`
- D) `create table orders partition by range (order_date) (partition p1 values less than ('2023-01-01') tablespace ts1, partition p2 values less than ('2024-01-01') tablespace ts2) partition by range (order_id);`

**Answer:** C

**Explanation:**  
In standard SQL databases like Oracle, partitioning by range on a column uses the `PARTITION BY RANGE (column_name)` clause followed by the definitions of partitions enclosed in parentheses. Option C matches the correct syntactic structure.

---

## Multiple Choice Questions (MCQs)

### Operating Systems

#### Q3. Process Control Block
**Topic:** `Operating Systems`, `Process Management`  
**Question:** Operating system maintains the information about a process in which of the following?  
**Options:**
- A) Heap
- B) Process Control Block
- C) Stack
- D) TLB Cache  
**Answer:** B  
**Explanation:** The Process Control Block (PCB) is a data structure used by the OS kernel to store all execution state and metadata about a process (e.g., process state, program counter, scheduling parameters, memory limits, and open files).

#### Q4. Memory Allocation and External Fragmentation
**Topic:** `Operating Systems`, `Memory Management`  
**Question:** Which of the following memory allocation schemes suffers from External Fragmentation?  
**Options:**
- A) Paging
- B) Swapping
- C) Segmentation
- D) Pure Demand Paging  
**Answer:** C  
**Explanation:** Segmentation allocates variable-sized memory segments, leading to fragmented free space (external fragmentation) over time. Paging divides memory into fixed-size frames, which eliminates external fragmentation.

#### Q5. Operating System Loader
**Topic:** `Operating Systems`, `System Boot`  
**Question:** Which software loads an Operating System in memory?  
**Options:**
- A) Compiler
- B) Bootloader
- C) Kernel
- D) Device Driver  
**Answer:** B  
**Explanation:** The bootloader is a small, specialized program executed during system boot that initializes minimal hardware resources and loads the OS kernel into memory.

---

### Data Structures & Algorithms

#### Q6. Binary Tree Reconstruction
**Topic:** `Data Structures`, `Trees`  
**Question:** Which of the following pair's traversals on a binary tree can build the tree uniquely?  
**Options:**
- A) post-order and pre-order
- B) post-order and in-order
- C) post-order and level order
- D) level order and preorder  
**Answer:** B  
**Explanation:** Uniquely reconstructing a binary tree requires the in-order traversal (which distinguishes the left and right subtrees) combined with either the pre-order, post-order, or level-order traversal.

#### Q7. Adjacency Matrix Edge Count Complexity
**Topic:** `Algorithms`, `Graph Theory`  
**Question:** The time complexity to calculate the number of edges in a graph whose information is stored in form of an adjacency matrix is _____.  
**Options:**
- A) $O(V)$
- B) $O(E^2)$
- C) $O(E)$
- D) $O(V^2)$  
**Answer:** D  
**Explanation:** An adjacency matrix is a $V \times V$ grid. Counting edges requires scanning all $V^2$ entries, taking $O(V^2)$ time.

#### Q8. AVL Tree Rotations
**Topic:** `Data Structures`, `Balanced Trees`  
**Question:** In an AVL tree, what is the purpose of performing rotations?  
**Options:**
- A) To keep the tree complete
- B) To ensure that all leaf nodes have the same depth
- C) To maintain balance of the tree to ensure $O(\log n)$ height
- D) To facilitate easy in-order traversal  
**Answer:** C  
**Explanation:** AVL trees perform tree rotations during insertions and deletions to restore balancing properties, ensuring that search, insert, and delete operations maintain $O(\log n)$ time complexity.

#### Q9. BST Insertion Complexity
**Topic:** `Algorithms`, `BST`  
**Question:** In a binary search tree (BST), what is the time complexity of inserting an element in the average case?  
**Options:**
- A) $O(1)$
- B) $O(n)$
- C) $O(\log n)$
- D) $O(n \log n)$  
**Answer:** C  
**Explanation:** In the average case, a BST remains relatively balanced. Inserting a node involves traveling a path from the root to a leaf, which corresponds to the height of the tree: $O(\log n)$.

#### Q10. 2-3 Tree Storage
**Topic:** `Data Structures`, `Balanced Trees`  
**Question:** Which of the following statements is false?  
**Options:**
- A) 2-3 tree requires less storage than the BST
- B) lookup in 2-3 tree is more efficient than in BST
- C) 2-3 tree is shallower than BST
- D) 2-3 tree is a balanced tree  
**Answer:** A  
**Explanation:** A 2-3 tree node stores up to 2 keys and 3 pointers, requiring more space than a BST node (1 key and 2 pointers). Thus, a 2-3 tree has higher storage overhead per node.

#### Q11. Symmetric Sparse Matrix Storage
**Topic:** `Data Structures`, `Matrices`  
**Question:** In what way can a Symmetric Sparse Matrix be stored efficiently?  
**Options:**
- A) Heap
- B) Binary tree
- C) Hash table
- D) Adjacency List  
**Answer:** D  
**Explanation:** A sparse matrix can be modeled as a graph where elements represent edges. If the matrix is symmetric, the graph is undirected. Storing it as an Adjacency List eliminates the storage of zero elements, reducing space complexity to $O(V + E)$ where $V$ is the dimension and $E$ is the number of non-zero elements.

#### Q12. Recursive Array Reversal
**Topic:** `Algorithms`, `Recursion`  
**Question:** Consider the below Java method. What's the output of this method?
```java
public static void function_1(int [] data, int low, int high) {
    if (low < high) {
        int temp = data[low];
        data[low] = data[high];
        data[high] = temp;
        function_1(data, low + 1, high - 1);
    }
}
```
**Options:**
- A) The sum of all the elements of the array
- B) The product of all the elements in the array
- C) The last element of the array
- D) Reverses the contents of the array  
**Answer:** D  
**Explanation:** The method swaps the element at `low` with the element at `high`, then recursively calls itself moving inwards (`low + 1`, `high - 1`) until the pointers cross, effectively reversing the array in place.

#### Q13. Preprocessor Macro Evaluation in C
**Topic:** `C Programming`, `Macros`  
**Question:** What is the output of the following program?
```c
#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    int x = 5, y = 10;
    printf("%d %d %d\n", MAX(x++, y++), x, y);
    return 0;
}
```
**Options:**
- A) 11 6 12
- B) 12 6 12
- C) 11 7 12
- D) 12 7 12  
**Answer:** A  
**Explanation:**
- The macro expands to `((x++) > (y++) ? (x++) : (y++))`.
- The condition compares $x=5$ and $y=10$ and increments both, making $x=6$ and $y=11$.
- The condition $5 > 10$ is false, so it evaluates the false branch `y++`.
- `y++` returns the current value 11, then increments $y$ to 12.
- The true branch is not evaluated, leaving $x=6$. Thus, the printed values are `11 6 12`.

---

### DBMS & System Design

#### Q14. Database Transaction Atomicity
**Topic:** `DBMS`, `Transactions`  
**Question:** What is the name of the following property of database transactions?  
*'Either all tasks of a transaction are performed or none of them are. There are no partial transactions.'*  
**Options:**
- A) Persistence
- B) Isolation
- C) Atomicity
- D) Consistency  
**Answer:** C  
**Explanation:** Atomicity is the 'all-or-nothing' property of transactions, ensuring that any crash or failure rolls back incomplete modifications.

#### Q15. Relation Cardinality
**Topic:** `DBMS`, `Relational Model`  
**Question:** What is the term for the number of tuples in a relation?  
**Options:**
- A) Entity
- B) Column
- C) Cardinality
- D) None of the above  
**Answer:** C  
**Explanation:** In relational algebra, cardinality is the count of rows (tuples) in a table, whereas the degree is the count of columns (attributes).

#### Q16. Data Control Language Commands
**Topic:** `DBMS`, `SQL`  
**Question:** Which of the following commands are a part of Data Control Language (DCL)?  
**Options:**
- A) Revoke
- B) Grant
- C) Both A & B
- D) None of the above  
**Answer:** C  
**Explanation:** DCL comprises commands like `GRANT` (used to give user privileges) and `REVOKE` (used to withdraw privileges).

#### Q17. Database Transaction Consistency
**Topic:** `DBMS`, `Transactions`  
**Question:** Consider the following transaction involving two bank accounts $x$ and $y$:
```sql
read(x); 
x := x - 50; 
write(x); 
read(y); 
y := y + 50; 
write(y);
```
The constraint that the sum of the accounts $x$ and $y$ should remain constant is that of:  
**Options:**
- A) Durability
- B) Consistency
- C) Isolation
- D) Both b) and c)  
**Answer:** B  
**Explanation:** Consistency guarantees that a transaction moves the database from one valid state to another, maintaining integrity constraints (like total balance conservation).

#### Q18. DBaaS Full Form
**Topic:** `Cloud Computing`, `DBMS`  
**Question:** What is the full form of DBaaS?  
**Options:**
- A) Data as a Service
- B) Database as a Service
- C) Database as a System
- D) Data as a System  
**Answer:** B  
**Explanation:** DBaaS stands for Database as a Service.

#### Q19. Monolithic Architecture Challenge
**Topic:** `System Design`, `Software Architecture`  
**Question:** Which of the following is a potential challenge of using a monolithic architecture?  
**Options:**
- A) Complex deployment process
- B) Improved scalability
- C) Tight coupling between components
- D) High maintenance overhead  
**Answer:** C  
**Explanation:** Monoliths place all components in a single codebase, leading to tight coupling where changes in one domain can inadvertently impact or break another.

#### Q20. Cache Tier Database Design
**Topic:** `System Design`, `Caching`  
**Question:** Which of the following is NOT true when using a Cache tier in Database design?  
**Options:**
- A) A cache tier improves system performance.
- B) A cache tier reduces database workloads.
- C) A cache tier can be scaled up independently.
- D) A cache tier increases database workloads.  
**Answer:** D  
**Explanation:** A cache tier intercepts read requests and returns data from fast memory, reducing the database's query processing workload.

#### Q21. REST API URI Design
**Topic:** `System Design`, `Web Services`  
**Question:** You are designing a REST API for a blogging platform. What URI should you use for creating a new blog post?  
**Options:**
- A) /blog/posts/new
- B) /blog/create/post
- C) /blog/posts
- D) /blog/posts/create  
**Answer:** C  
**Explanation:** REST standard uses the HTTP method to specify action. To create a resource, a client sends a `POST` request to the collection resource `/blog/posts`.

#### Q22. Relational Database Properties
**Topic:** `DBMS`, `Relational Model`  
**Question:** Which of the following is NOT a property of Relational Databases?  
**Options:**
- A) Atomicity
- B) Consistency
- C) Isolation
- D) Dependency  
**Answer:** D  
**Explanation:** Relational databases adhere to ACID (Atomicity, Consistency, Isolation, Durability) properties. Dependency is not one of them.

#### Q23. Oracle Database Version
**Topic:** `DBMS`, `Oracle`  
**Question:** What is the latest long-term release of Oracle Database?  
**Options:**
- A) 23ai
- B) 22ai
- C) 24ai
- D) 19ai  
**Answer:** A  
**Explanation:** Oracle Database 23ai (23c) is the next long-term support release succeeding Oracle Database 19c.

#### Q24. Key-Value Store
**Topic:** `DBMS`, `NoSQL`  
**Question:** Which of the following is a key-value store NoSQL database system?  
**Options:**
- A) HBase
- B) MongoDB
- C) Redis
- D) Accumulo  
**Answer:** C  
**Explanation:** Redis is an in-memory key-value database. MongoDB is a document store; HBase and Accumulo are wide-column stores.

#### Q25. CAP Theorem
**Topic:** `System Design`, `Distributed Systems`  
**Question:** What does the CAP theorem describe with respect to System Design?  
**Options:**
- A) The relationship between CPU and memory usage
- B) The trade-offs between consistency, availability, and partition tolerance
- C) The process of data encryption
- D) The principles of object-oriented programming  
**Answer:** B  
**Explanation:** CAP theorem states that a distributed system can guarantee at most two out of: Consistency (C), Availability (A), and Partition Tolerance (P).

#### Q26. NoSQL Design Criteria
**Topic:** `DBMS`, `NoSQL`  
**Question:** Which of the following design criteria are NOT valid/suitable for Non-Relational Databases?  
**Options:**
- A) Your application requires super-low latency.
- B) Your data is unstructured without any relation between them.
- C) You only need to serialize & deserialize data (JSON, XML, YAML).
- D) You need to store a very small amount of data.  
**Answer:** D  
**Explanation:** While NoSQL can store small datasets, it is designed for horizontal scaling of massive data. Small, highly structured data volumes are better suited for relational databases.

---

### Computer Networks

#### Q27. Purpose of NAT
**Topic:** `Computer Networks`, `IP Routing`  
**Question:** What is the purpose of NAT (Network Address Translation) in networking?  
**Options:**
- A) To translate domain names to IP addresses
- B) To encrypt network traffic for secure communication
- C) To assign IP addresses dynamically to devices on a network
- D) To map private IP addresses to public IP addresses for internet access  
**Answer:** D  
**Explanation:** NAT maps private IP addresses inside local area networks to public IP addresses, allowing devices to access the internet using a shared public IP.

#### Q28. Broadcast Address Calculation
**Topic:** `Computer Networks`, `Subnetting`  
**Question:** What is the broadcast address for the subnet 172.16.10.128/27?  
**Options:**
- A) 172.16.10.159
- B) 172.16.10.191
- C) 172.16.10.224
- D) 172.16.10.255  
**Answer:** A  
**Explanation:** A /27 subnet mask has 5 host bits ($32 - 27$). The block size is $2^5 = 32$. The range of the subnet starting at `.128` is `.128` to `.159`. The last address (`.159`) is the broadcast address.

#### Q29. Purpose of ARP
**Topic:** `Computer Networks`, `Link Layer`  
**Question:** What is the purpose of ARP (Address Resolution Protocol) in computer networking?  
**Options:**
- A) To convert IP addresses to MAC addresses
- B) To convert domain names to IP addresses
- C) To establish a secure connection between client and server
- D) To route packets between networks  
**Answer:** A  
**Explanation:** ARP maps dynamic IP network addresses to physical MAC hardware addresses on a local subnet.

#### Q30. Ring Topology Failure
**Topic:** `Computer Networks`, `Topologies`  
**Question:** In a ring topology network, if one device fails, how does it affect the network?  
**Options:**
- A) Only the failed device is affected
- B) All devices in the network are affected
- C) Only the devices between which the failed device exists are affected
- D) The network continues to function normally  
**Answer:** B  
**Explanation:** In a single-ring topology, data moves sequentially. A failure in one node breaks the loop, disrupting all traffic across the network.

#### Q31. HTTP HEAD Method
**Topic:** `Computer Networks`, `HTTP`  
**Question:** Which is the HTTP request method used to retrieve the metadata associated with the resource's state?  
**Options:**
- A) GET
- B) PUT
- C) HEAD
- D) POST  
**Answer:** C  
**Explanation:** The `HEAD` method requests headers identical to a `GET` request, but without the response body, rendering it ideal for fetching metadata.

---

## Aptitude & Logical Reasoning

### Q32. Date Math
**Topic:** `Aptitude`, `Calendar`  
**Question:** If today is Monday, what day is it after 62 days?  
**Options:**
- A) Sunday
- B) Saturday
- C) Monday
- D) Wednesday  
**Answer:** A  
**Explanation:** Since $62 \equiv 6 \pmod 7$, adding 62 days is equivalent to adding 6 days to Monday, which lands on Sunday.

### Q33. Reading Comprehension - Machiavelli
**Topic:** `Aptitude`, `Verbal Ability`  
**Question:** According to the passage, ancient writers allegedly:  
**Options:**
- A) failed to establish a methodology for the study of political science
- B) did not put enough effort into establishing a discipline of political science.
- C) had a flawed understanding of how rules and laws came in to being and passed away.
- D) did not study the data of political life in a systematic manner.  
**Answer:** A  
**Explanation:** The text details that the failure of the ancients was a "charge of methodological naiveté", which points to a failure to establish a sound methodology.

### Q34. Integer Division Remainder
**Topic:** `Aptitude`, `Arithmetic`  
**Question:** What is the remainder of 1992 divided by 92?  
**Options:**
- A) 0
- B) 1
- C) 40
- D) None of the above  
**Answer:** D  
**Explanation:**  
$1992 = 92 \times 21 + 60$. The remainder is 60, which is not in options A, B, or C.

### Q35. Reading Comprehension - Louis XVI
**Topic:** `Aptitude`, `Verbal Ability`  
**Question:** Louis XVI being unable to establish himself as an "enlightened absolutist" was a result of?  
**Options:**
- A) the rising cost of bread in France
- B) citizens' refusal to embrace proposed ideals
- C) nobles impeding the implementation of the monarch's ideals
- D) the burden of tax payment on the citizens  
**Answer:** C  
**Explanation:** The text indicates that the nobility classes impeded reform as they wanted to protect their privileges and lavish lifestyles, curbing the king's ideals.

### Q36. Logic Puzzles - Work Rates
**Topic:** `Aptitude`, `Time and Work`  
**Question:** A and B together can do a piece of work in 10 days. B and C together can do the same piece of work in 5 days. C and D together can do it in 4 days. A can do it in 40 days, alone. Which is the correct statement?  
**Options:**
- A) A and B do the work at the same rate.
- B) B and D do the work at the same rate.
- C) C and D do the work at the same rate.
- D) A and D do the work at the same rate.  
**Answer:** C  
**Explanation:**  
Let the total work be 40 units.
- Rate(A) = $40 / 40 = 1$ unit/day
- Rate(A + B) = $40 / 10 = 4 \implies$ Rate(B) = 3 units/day
- Rate(B + C) = $40 / 5 = 8 \implies$ Rate(C) = 5 units/day
- Rate(C + D) = $40 / 4 = 10 \implies$ Rate(D) = 5 units/day  
Since Rate(C) = Rate(D) = 5 units/day, they work at the same rate.

### Q37. Logic - Sports Enthusiasts
**Topic:** `Aptitude`, `Set Theory`  
**Question:** In a company, 100 employees are randomly selected. 50 like watching football, 40 like watching hockey, and the rest like both. Find out the number of employees who like to watch at least one of the games.  
**Options:**
- A) 40
- B) 90
- C) 80
- D) 20  
**Answer:** C  
**Explanation:**  
"The rest" who like both = $100 - (50 + 40) = 10$.  
At least one = Football + Hockey - Both = $50 + 40 - 10 = 80$.

### Q38. Sum of Semicircular Angles
**Topic:** `Aptitude`, `Geometry`  
**Question:** A, B, C, D, E are five points marked in order on the circumference of a semi-circle while traversing clockwise. A and E are the ends of the diameter. What is the sum of angles ABC and CDE?  
**Options:**
- A) 135 Degrees
- B) 180 Degrees
- C) 225 Degrees
- D) 315 Degrees
- E) 270 Degrees  
**Answer:** E  
**Explanation:**  
Connect A to D. Since A, B, C, D, E lie on the circle, ABCD is a cyclic quadrilateral. Thus, $\angle ABC + \angle ADC = 180^\circ$.  
Also, AE is the diameter, so the angle subtended by the diameter at D is $\angle ADE = 90^\circ$.  
$\angle CDE = \angle ADC + \angle ADE = \angle ADC + 90^\circ$.  
Therefore, $\angle ABC + \angle CDE = (\angle ABC + \angle ADC) + 90^\circ = 180^\circ + 90^\circ = 270^\circ$.

### Q39. Set Cardinality
**Topic:** `Aptitude`, `Set Theory`  
**Question:** Consider a set S that consists of positive integer values of $x$ that satisfy the equation $(x^2-5x+4)/(x^2-7x+12) \le 0$, where $x \neq 3, 4$. What is the cardinality of S?  
**Options:**
- A) 0
- B) 1
- C) 2
- D) 3  
**Answer:** C  
**Explanation:**  
Factor the equation: $\frac{(x-1)(x-4)}{(x-3)(x-4)} \le 0$. For $x \neq 4$, this simplifies to $\frac{x-1}{x-3} \le 0 \implies 1 \le x < 3$.  
The positive integers in this range are $x = 1, 2$. So $S = \{1, 2\}$, which has cardinality 2.

### Q40. Distance From Start
**Topic:** `Aptitude`, `Directions`  
**Question:** A hiker walks 50m north, turns left, and walks 30m. The hiker turns left and walks for 50m, then turns left and walks 50m more. How far is the hiker from the starting point?  
**Options:**
- A) 25m
- B) 50m
- C) 35m
- D) None of the above  
**Answer:** D  
**Explanation:**  
Start at (0,0).  
1. 50m North: (0, 50)  
2. 30m West (turn left): (-30, 50)  
3. 50m South (turn left): (-30, 0)  
4. 50m East (turn left): (20, 0)  
Distance from (0,0) to (20,0) is 20m. Since 20m is not in the options, the answer is "None of the above".

### Q41. Digit Sum Reduction
**Topic:** `Aptitude`, `Number Theory`  
**Question:** The digit sum of a number is found by repeatedly summing the digits until a single-digit number is reached. Find the digit sum of 25! (25 factorial).  
**Options:**
- A) 6
- B) 7
- C) 8
- D) 9  
**Answer:** D  
**Explanation:**  
A number is divisible by 9 if and only if its repeated digit sum (digital root) is 9. Since 25! contains the factors 9 and 18, it is a multiple of 9, and thus its digital root is 9.

### Q42. Mean Probability Distribution
**Topic:** `Aptitude`, `Probability`  
**Question:** In a group of 50 people, 20 are vegetarian. If two people are selected at random, what is the expected number of vegetarians?  
**Options:**
- A) 197/245
- B) 198/245
- C) 196/245
- D) 191/245  
**Answer:** C  
**Explanation:**  
By linearity of expectation, the expected number of vegetarians is $2 \times (20/50) = 4/5 = 0.8$.  
Dividing 196 by 245 yields: $\frac{196}{245} = \frac{4 \times 49}{5 \times 49} = \frac{4}{5}$.

### Q43. English Grammar Error
**Topic:** `Aptitude`, `Verbal Ability`  
**Question:** Find out which underlined part of the sentence below has an error and mark the option accordingly:  
*"I regret that I wasn't aware that you **have lost** your job when you visited me last week."*  
**Options:**
- A) I wasn't aware
- B) Have lost your
- C) When you visited me
- D) None of the options  
**Answer:** B  
**Explanation:** Since the action of losing the job occurred prior to another past event ("visited me last week"), it should use past perfect tense ("had lost") instead of present perfect ("have lost").

### Q44. English Idioms - Fill in the Blank 1
**Topic:** `Aptitude`, `Verbal Ability`  
**Question:** I've been studying for this exam for months, so I'm hoping to ____.  
**Options:**
- A) Hit the ground running
- B) Have a field day
- C) Be a dark horse
- D) Have a lot on my plate  
**Answer:** A  
**Explanation:** "Hit the ground running" means to immediately start operating at a highly effective, successful level.

### Q45. English Idioms - Fill in the Blank 2
**Topic:** `Aptitude`, `Verbal Ability`  
**Question:** I don't think we should hire him. He seems like ____.  
**Options:**
- A) A fish out of water
- B) The black sheep of the family
- C) A wolf in sheep's clothing
- D) The apple of my eye  
**Answer:** C  
**Explanation:** "A wolf in sheep's clothing" refers to someone who seems friendly or harmless but is actually hostile or deceitful.

### Q46. One-word Substitution
**Topic:** `Aptitude`, `Verbal Ability`  
**Question:** In the following question, choose the correct option which can be substituted for the given sentence: *"A self-governing country or region"*  
**Options:**
- A) Autonomy
- B) Autocracy
- C) Anarchy
- D) Ethnology  
**Answer:** A  
**Explanation:** Autonomy represents the right or condition of self-government.

### Q47. Non-Verbal Reasoning - Pattern Prediction
**Topic:** `Aptitude`, `Non-Verbal Reasoning`  
**Question:** Predict the figure in (?) place.
```
Problem Figures:
[ Box 1 ] -> 5-prong fan pointing UP, with a black circle at the end of each prong. Star at bottom-right.
[ Box 2 ] -> 5 black circles in a row at the top. 5-prong fan pointing DOWN (no circles). Star at bottom-center.
[ Box 3 ] -> 3-prong fan pointing UP-RIGHT, with a black circle at the end of each prong. Arc at bottom-right.
[ Box 4 ] -> ?
```
**Options:** (1), (2), (3), (4)  
**Answer:** (4)  
**Explanation:**  
The pattern detaches the circles from the prongs and shifts them to a separate group, rotates the fan 180 degrees, and keeps the other corner feature (arc). In Box 3, we have 3 circles on a 3-prong fan pointing up-right, so in Box 4 we need 3 separated circles, a 3-prong fan pointing down-left, and the corner arc at the bottom-left, which matches option (4).

### Q48. Standing Order - Seating Arrangement
**Topic:** `Aptitude`, `Logical Reasoning`  
**Question:** There are five people - Peter, Tyson, Richard, Steve and Quinn - standing in a row. Given the following statements, who is in the middle?
1. Peter is next to Quinn and Steve is next to Richard.
2. Steve is not next to Tyson.
3. Tyson is on leftmost position.
4. Richard is on the second position from the right.
5. Peter stands somewhere to the right of both Quinn and Tyson.
6. Peter and Richard are next to each other.  
**Options:**
- A) Peter
- B) Richard
- C) Steve
- D) Quinn  
**Answer:** A  
**Explanation:**  
- From 3: Position 1 = Tyson.
- From 4: Position 4 = Richard.
- From 1 & 6: Steve and Peter are next to Richard, so they must occupy positions 3 and 5.
- This leaves Position 2 = Quinn.
- From 1: Peter is next to Quinn, so Peter must be at Position 3.
- This leaves Position 5 = Steve.
- The order is Tyson, Quinn, Peter, Richard, Steve. Peter is in the middle.

### Q49. Favorite Color Grid Puzzle
**Topic:** `Aptitude`, `Logical Reasoning`  
**Question:** There are five people: Jack, Matthew, Albert, Peter, and Sebastian. Each plays one sport out of football, cricket, volleyball, badminton, and squash. They are from South Korea, the UK, India, China, and Russia. Their favorite colors are brown, green, red, black, and yellow.
1. Jack's favorite color is red. He is not from India or China.
2. Albert plays football. His favorite color is not yellow, and he is not from the UK.
3. Peter and Sebastian have yellow and green as their favorite colors, not necessarily in that order.
4. Matthew plays badminton. He is from Russia.
5. Peter and Sebastian are from China and UK, not necessarily in that order.
6. Brown is the favorite color of the person from India.
7. Green is the favorite color of the person from China.
8. The person from South Korea plays squash and the person from the UK plays volleyball. One of them has yellow as his favorite color.
Whose favorite color is black?  
**Options:**
- A) Matthew
- B) Albert
- C) Peter
- D) Sebastian  
**Answer:** A  
**Explanation:**  
- Matthew is from Russia (given).
- Peter and Sebastian are from China and UK.
- Jack and Albert are from South Korea and India. Jack is not from India, so Jack is from South Korea, and Albert is from India.
- Albert's color is Brown (since he is from India).
- The person from China has Green, so either Peter or Sebastian has Green. The other has Yellow (from UK).
- Jack's color is Red.
- Thus, the remaining color, Black, must belong to Matthew.

### Q50. Painted Cube
**Topic:** `Aptitude`, `Logical Reasoning`  
**Question:** A cube is painted green on all surfaces and is cut into 1000 identical cubes. How many of the smaller cubes have exactly three surfaces painted?  
**Options:**
- A) 8
- B) 10
- C) 100
- D) 64  
**Answer:** A  
**Explanation:** The only cubes with three painted surfaces are the corner cubes. A cube always has exactly 8 corners.

### Q51. Paths in a Graph - Eulerian Path
**Topic:** `Aptitude`, `Graph Theory`  
**Question:** There is a network of eight cities (represented by vertices) connected by roads. A traveler must drive on each road segment once but can visit a city multiple times. If necessary, starting and ending points do not have to match. New roads are constructed between C and G, and between H and F. If the journey begins at B, where will it end?  
**Options:**
- A) E
- B) B
- C) H
- D) G  
**Answer:** A  
**Explanation:**  
The traveler must drive on each road exactly once, which requires an Eulerian path.
- In the original graph, the degrees are: A: 2, B: 3, C: 3, D: 2, E: 3, F: 3, G: 3, H: 3.
- After adding (C, G) and (H, F), the degrees of C, G, H, F each increase by 1, making them all even (C: 4, G: 4, H: 4, F: 4).
- The remaining vertices maintain their original degrees: A: 2 (even), B: 3 (odd), D: 2 (even), E: 3 (odd).
- An Eulerian path in a graph with exactly two odd-degree vertices must start at one odd vertex (B) and end at the other (E).

### Q52. Chef's Puzzle - Logic Constraint
**Topic:** `Aptitude`, `Logical Reasoning`  
**Question:** Out of the nine ingredients, a chef wants to use exactly five. Given the following statements, how many of the 5 ingredients are known?
*The ingredients are apricots, bacon, cake, donuts, eggs, figs, grapes, hazelnuts, and ice cream.*
1. If bacon is not used, then grapes, hazelnuts, and ice cream are not used.
2. If apricots are used then bacon and cake are used.
3. If donuts are not used, apricots are not used.
4. Apricots and eggs are used.  
**Options:**
- A) 2
- B) 3
- C) 4
- D) 5  
**Answer:** D  
**Explanation:**  
- From 4: Apricots = YES, Eggs = YES.
- From 2: Since Apricots = YES $\implies$ Bacon = YES, Cake = YES.
- From 3: Since Apricots = YES $\implies$ Donuts = YES (by contrapositive).
- We have 5 ingredients: {apricots, eggs, bacon, cake, donuts}. Since the chef uses exactly 5, all 5 ingredients are uniquely known.

### Q53. Father and Son Vacation Age
**Topic:** `Aptitude`, `Ages`  
**Question:** A man spent 1/3rd of his life as a bachelor. After ten years of his marriage a son was born to him. The father and son went on a vacation together at the time the father's age was double that of his son. What was the father's age at the time of the vacation?  
**Options:**
- A) 50
- B) 60
- C) 70
- D) 80  
**Answer:** B  
**Explanation:**  
Let the father's age at the vacation be $V$ and his total life span be $L$. Since this vacation marks the end of the timeline corresponding to his life, $V = L$.
- The father was a bachelor for $L/3$ years.
- The son was born 10 years later, so when the father was $L/3 + 10$ years old.
- The age difference is constant and equals the father's age when the son was born: $L/3 + 10$.
- At the time of the vacation, the father's age ($L$) was double the son's age. This means the son's age was $L/2$, and the age difference is $L - L/2 = L/2$.
- Thus, $L/2 = L/3 + 10 \implies L/6 = 10 \implies L = 60$. The father's age at the vacation was 60.

### Q54. Diagrammatic Reasoning 1
**Topic:** `Aptitude`, `Logical Reasoning`  
**Question:** Which option will replace the question mark (?) in the sequence of hexagons?  
**Options:** (1), (2), (3), (4)  
**Answer:** (1)  
**Explanation:**  
- **Rule 1 (Position):** The group of three symbols rotates counter-clockwise by 1 vertex at each step. In Hexagon 1, they occupy the top-left, left, and bottom-left vertices. In Hexagon 2, they must occupy the left, bottom-left, and bottom-right vertices.
- **Rule 2 (Style):** Odd-numbered steps (1, 3, 5) have filled symbols, while even-numbered steps (2, 4) have outlined/empty symbols.
- **Rule 3 (Chevron Orientation):** The chevron rotates 90 degrees clockwise at each step (pointing left `<` in 1, down `v` in 2).  
This corresponds to Option (1).

### Q55. How Many Like Cricket?
**Topic:** `Aptitude`, `Set Theory`  
**Question:** In a group of students, 60% like football and 40% like cricket. What percentage of students like only cricket if 30% of the students who like cricket also like football?  
**Options:**
- A) 28
- B) 14
- C) 56
- D) 42  
**Answer:** A  
**Explanation:**  
- Football = 60%, Cricket = 40%.
- 30% of cricket-liking students also like football, so the overlap (both) is $40\% \times 30\% = 12\%$.
- Those who like only cricket = $40\% - 12\% = 28\%$.

### Q56. Interpret Charts - Brand Phone Customers
**Topic:** `Aptitude`, `Data Interpretation`  
**Question:** The following table shows the number of customers (in millions) using Hington and Euphore brand phones in France from August to October 2012. Only these two brands of phones are available in the market.
  
| Month | Hington | Euphore |
|---|---|---|
| Aug-12 | 46.18 | 47.28 |
| Sep-12 | 47.34 | 48.91 |
| Oct-12 | 49.32 | 49.27 |

If the total number of phone users in November 2012 increased by 5% compared to October 2012, and Hington brand users increased by 2%, what is the number of Euphore brand users in November 2012?  
**Answer:** 53.21 million  
**Explanation:**  
- Total users in October 2012 = $49.32 + 49.27 = 98.59$ million.
- Total users in November 2012 = $98.59 \times 1.05 = 103.5195$ million.
- Hington users in November 2012 = $49.32 \times 1.02 = 50.3064$ million.
- Euphore users in November 2012 = Total - Hington = $103.5195 - 50.3064 = 53.2131$ million.
*Total questions: 36*

---

## Table of Contents
- [Coding Questions](#coding-questions)
- [SQL & DBMS Questions](#sql-dbms-questions)
- [Operating Systems Questions](#operating-systems-questions)
- [Data Structures & Algorithms MCQs](#data-structures-algorithms-mcqs)
- [Computer Networks & System Design MCQs](#computer-networks-system-design-mcqs)
- [C Programming MCQs](#c-programming-mcqs)
- [Puzzles & Aptitude MCQs](#puzzles-aptitude-mcqs)
- [Data Interpretation MCQs](#data-interpretation-mcqs)
- [Verbal Ability MCQs](#verbal-ability-mcqs)

---

## Coding Questions

### Q1. K-Means Clustering (1D K-Center Problem)

**Topic:** `Binary Search`, `Greedy`  

In a k-means clustering problem, a dataset contains $n$ data points, where the $i^{th}$ data point is represented by the feature vector `location[i]`. The goal is to create $k$ clusters, where the cluster centers or the cluster centroids can be placed at any point in the feature space. The overall quality of the clustering is measured by the maximum distance between any data point and its nearest cluster center.

The best possible quality is achieved by optimally placing the cluster centers to minimize this maximum distance. Determine this maximum distance between any data point and its nearest cluster center.

*Note:* The distance between two feature points $x$ and $y$ is defined as $|x - y|$, where $|x|$ denotes the absolute value of $x$.

**Example:**
* Input:
  * $n = 5$
  * `location` = `[4, 1, 6, 7, 2]`
  * $k = 2$
* Output: `2`
* Explanation: Let the cluster centers be placed at points 3 and 7.
  * Current Location 4: closest center 3, distance = 1
  * Current Location 1: closest center 3, distance = 2
  * Current Location 6: closest center 7, distance = 1
  * Current Location 7: closest center 7, distance = 0
  * Current Location 2: closest center 3, distance = 1
  * Hence, the maximum of all distances is 2.

**Constraints:**
* $1 \le n \le 10^5$
* $1 \le k \le n$
* $1 \le location[i] \le 10^9$

```python
def getMaximumDistance(location: list[int], k: int) -> int:
    location.sort()
    low = 0
    high = location[-1] - location[0]
    ans = high
    
    def is_feasible(d: int) -> bool:
        count = 1
        last_placed = location[0]
        for loc in location[1:]:
            if loc - last_placed > 2 * d:
                count += 1
                last_placed = loc
        return count <= k

    while low <= high:
        mid = low + (high - low) // 2
        if is_feasible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
```

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int getMaximumDistance(vector<int>& location, int k) {
    sort(location.begin(), location.end());
    int n = location.size();
    int left = 0, right = location.back() - location.front();
    int result = right;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int clusters = 1;
        int center = location[0];
        
        for (int i = 1; i < n; i++) {
            if (location[i] - center > 2 * mid) {
                clusters++;
                center = location[i];
            }
        }
        
        if (clusters <= k) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return result;
}
```

---

## SQL & DBMS Questions

### Q2. SQL Constraint for Default Values

**Topic:** `SQL`, `Database`  

Which SQL constraint do we use to set some value to a field whose value has not been added explicitly?

**Options:**
* A. `NOT NULL`
* B. `DEFAULT`
* C. `CHECK`
* D. `UNIQUE`

**Answer:** B. `DEFAULT`  
**Explanation:** The `DEFAULT` constraint is used to set a default value for a column if no value is specified when inserting a record.

---

### Q3. Classification of TRUNCATE TABLE

**Topic:** `SQL`, `Database`  

Truncate table is classified as:

**Options:**
* A. Data Definition Language (DDL)
* B. Data Manipulation Language (DML)
* C. Data Control Language (DCL)
* D. Transaction Control Language (TCL)

**Answer:** A. Data Definition Language (DDL)  
**Explanation:** `TRUNCATE` is a DDL command because it alters the database schema (by dropping and recreating the storage structures or tables) and cannot be rolled back in standard SQL, and it does not fire delete triggers.

---

### Q4. Properties of a Relational Database

**Topic:** `Database`, `DBMS`  

Which of the following is not a property of Relational Database?

**Options:**
* A. Atomicity
* B. Consistency
* C. Isolation
* D. Dependency

**Answer:** D. Dependency  
**Explanation:** Atomicity, Consistency, and Isolation are three of the four ACID properties of a relational database (the fourth is Durability). "Dependency" is not an ACID property.

---

### Q5. Oracle Database Latest Long-Term Release

**Topic:** `Database`, `Oracle`  

What is the latest long-term release of Oracle Database?

**Options:**
* A. 23ai
* B. 22ai
* C. 24ai
* D. 19ai

**Answer:** A. 23ai  
**Explanation:** Oracle Database 23ai is the latest Long-Term Support (LTS) release of Oracle Database, following 19c.

---

### Q6. Example of Cloud Database Service

**Topic:** `Cloud Computing`, `Database`  

Which of the following is an example of Cloud Database service?

**Options:**
* A. Oracle database service
* B. AWS RDS
* C. Azure SQL Database
* D. All of the above

**Answer:** D. All of the above  
**Explanation:** Oracle Database Service, AWS Relational Database Service (RDS), and Microsoft Azure SQL Database are all well-known cloud-based managed database services.

---

## Operating Systems Questions

### Q7. Why is a Virtual Memory Address Called 'Virtual'

**Topic:** `OS`, `Virtual Memory`  

Why is a virtual memory address called 'virtual'?

**Options:**
* A. This memory address does not map to actual memory cell that corresponds to address number.
* B. This memory is the same as physical memory.
* C. This memory cannot be accessed by applications at run time.
* D. This memory address is always present even after a system is restarted.

**Answer:** A. This memory address does not map to actual memory cell that corresponds to address number.  
**Explanation:** A virtual memory address is called "virtual" because it represents a logical address space that is translated (mapped) by the MMU to a physical address (which might be in physical RAM or swapped to disk), meaning the logical address number does not directly correspond to a physical memory cell of the same number.

---

### Q8. Minimum Value of Semaphore-Controlled Shared Variable

**Topic:** `OS`, `Semaphore`, `Concurrency`  

Consider the two functions `incr` and `decr` shown below:

```c
incr() {
    wait(s);
    X = X + 1;
    signal(s);
}

decr() {
    wait(s);
    X = X - 1;
    signal(s);
}
```

There are 5 threads each invoking `incr` once, and 3 threads each invoking `decr` once, on the same shared variable `X`. The initial value of shared variable `X` is 10. Suppose there are two implementations of the semaphore `S` as follows:
* `I-1`: `S` is a binary semaphore initialized to 1.
* `I-2`: `S` is a counting semaphore initialized to 2.

Let `V1` and `V2` be the values of `X` at the end of execution of all the threads with implementations `I-1` and `I-2` respectively. Which one of the following choices corresponds to the minimum possible values of `V1` and `V2` respectively?

**Options:**
* A. 15, 7
* B. 7, 7
* C. 12, 7
* D. 12, 12

**Answer:** C. 12, 7  
**Explanation:**
1. Under `I-1` (binary semaphore initialized to 1): Strict mutual exclusion is maintained. All operations on `X` are serialized, so there are no race conditions. The final value `V1` is always $10 + 5 - 3 = 12$.
2. Under `I-2` (counting semaphore initialized to 2): Two threads can enter the critical section concurrently, allowing for race conditions. To minimize `V2`, we can hide the increments:
   - The first `incr` thread reads $X = 10$.
   - A `decr` thread also enters and reads $X = 10$.
   - All other 4 `incr` threads execute sequentially to completion, bringing $X$ to $15$.
   - The first `incr` thread writes back $11$.
   - The first `decr` thread (which read $10$) writes back $9$, erasing the effect of all other increments.
   - The remaining two `decr` threads run normally, bringing $X$ down to $7$.

---

### Q9. User Mode vs. Kernel Mode

**Topic:** `OS`, `Kernel`  

What is the main difference between "user mode" and "kernel mode" in an operating system?

**Options:**
* A. User mode allows direct hardware access, kernel mode does not.
* B. Kernel mode can access protected memory regions, user mode cannot.
* C. Kernel mode applications are given less priority than user mode applications.
* D. User mode instructions can switch the CPU to kernel mode, but not vice-versa.

**Answer:** B. Kernel mode can access protected memory regions, user mode cannot.  
**Explanation:** The operating system runs in kernel mode (privileged mode) which has unrestricted access to the hardware and all memory locations (including protected system memory), whereas applications run in user mode which has restricted access to prevent them from corrupting the system.

---

### Q10. What is a Zombie Process in Linux

**Topic:** `OS`, `Linux`  

What is a Zombie process in Linux?

**Options:**
* A. A process which is running in the background.
* B. A process which is running for a long time.
* C. A process whose execution has completed but it still has an entry in the process table.
* D. A process which has crashed due to memory corruption.

**Answer:** C. A process whose execution has completed but it still has an entry in the process table.  
**Explanation:** A zombie process (or defunct process) is a process that has completed execution (via the exit system call) but still has an entry in the process table because its parent process has not yet read its exit status via the wait system call.

---

## Data Structures & Algorithms MCQs

### Q11. Best Data Structure for Priority Queue

**Topic:** `Data Structures`, `Heap`  

Which data structure is best suited for implementing a priority queue?

**Options:**
* A. Array
* B. Stack
* C. Heap
* D. Linked List

**Answer:** C. Heap  
**Explanation:** A binary heap provides $O(\log n)$ time for both insertion and extraction of the maximum/minimum element, making it the most optimal standard data structure for implementing a priority queue.

---

### Q12. Concept of Memoization in Dynamic Programming

**Topic:** `Dynamic Programming`, `Algorithms`  

In the context of Dynamic Programming, what is "memoization"?

**Options:**
* A. Writing an algorithm in a memo to remember it.
* B. Recomputing solutions to subproblems multiple times for accuracy.
* C. Storing solutions to subproblems to avoid recomputation.
* D. Optimizing a problem by breaking it into subproblems and solving iteratively.

**Answer:** C. Storing solutions to subproblems to avoid recomputation.  
**Explanation:** Memoization is a top-down dynamic programming technique where we store the results of expensive function calls to subproblems and return the cached result when the same inputs occur again.

---

### Q13. Best Data Structure for Marathon Competitor Tracking

**Topic:** `Data Structures`, `Design`  

A certain program must store the names of all the people who finish the City Marathon. The names are entered by an official at the finish line as the competitors finish. After the race is over the program must print a list only containing the names of competitors who placed 1 to 10 and then 100, 200, 300 and so on, as these competitors will receive a special medallion. Which data structure would be the best choice for this program?

**Options:**
* A. A vector or resizable array
* B. A map (implemented as a binary tree of key/value pairs)
* C. A singly linked list
* D. A hash set (implemented as a hash table of keys)

**Answer:** A. A vector or resizable array  
**Explanation:** Since names are appended in the order they finish, insertion in a vector takes $O(1)$ time. After the race, we need to access elements at specific 1-based indices (1 to 10, then 100, 200, 300, etc.), which takes $O(1)$ time per lookup in a vector. A singly linked list would require $O(n)$ time to traverse to index 100, 200, etc., and a map would take $O(\log n)$ for both insertions and lookups.

---

## Computer Networks & System Design MCQs

### Q14. Distributing Traffic to Web Servers

**Topic:** `Networking`, `System Design`  

How will you distribute incoming traffic to a set of Web Servers?

**Options:**
* A. By deploying a Firewall before the servers
* B. By deploying a router before the servers.
* C. By deploying a load balancer before the servers.
* D. By deploying a switch before the servers.

**Answer:** C. By deploying a load balancer before the servers.  
**Explanation:** A load balancer is specifically designed to distribute network or application traffic across a number of servers to ensure reliability, high availability, and optimal resource utilization.

---

### Q15. CAP Theorem in Distributed Systems

**Topic:** `Distributed Systems`, `System Design`  

In a distributed system, what is CAP theorem?

**Options:**
* A. It specifies the maximum allowable response time for a system.
* B. It describes the trade-offs between consistency, availability, and partition tolerance.
* C. It defines the minimum number of servers required for fault tolerance.
* D. It outlines the process for scaling a system horizontally.

**Answer:** B. It describes the trade-offs between consistency, availability, and partition tolerance.  
**Explanation:** The CAP theorem states that a distributed data store can simultaneously provide at most two of the three guarantees: Consistency, Availability, and Partition tolerance.

---

### Q16. HTTP Method for Resource Creation

**Topic:** `Web Development`, `Networking`  

Which HTTP method is suitable for resource creation?

**Options:**
* A. PUT
* B. PATCH
* C. POST
* D. CREATE

**Answer:** C. POST  
**Explanation:** In REST API design, the `POST` method is standard for creating new resources on the server.

---

### Q17. HTTP Response Category for Server Errors

**Topic:** `Web Development`, `Networking`  

Which response status code category represents server error in REST paradigm?

**Options:**
* A. 1xx
* B. 2xx
* C. 4xx
* D. 5xx

**Answer:** D. 5xx  
**Explanation:** In HTTP status codes, the `5xx` category is reserved for server-side errors (e.g., 500 Internal Server Error, 502 Bad Gateway). `4xx` represents client-side errors, `2xx` represents success, and `1xx` represents informational status.

---

### Q18. REST URL Pattern for Subresources

**Topic:** `Web Development`, `System Design`  

Which URL Pattern should you follow for accessing a subresource attached to a specific resource?

**Options:**
* A. `/company/{companyId}/employees/{employeeId}`
* B. `/companies/employees/{companyId}/{employeeId}`
* C. `/companies/{companyId}/employee/{employeeId}`
* D. `/companies/{companyId}/employees/{employeeId}`

**Answer:** D. `/companies/{companyId}/employees/{employeeId}`  
**Explanation:** Standard RESTful API practices dictate using plural nouns for collections (`/companies` and `/employees`). To fetch a specific subresource (an employee) belonging to a specific parent resource (a company), the path structure should represent the parent-child hierarchy: `/companies/{companyId}/employees/{employeeId}`.

---

### Q19. Border Gateway Protocol (BGP) OSI Layer

**Topic:** `Networking`  

What does the acronym BGP stand for in networking, and what layer of the OSI model does it operate at?

**Options:**
* A. Best Gateway Protocol, Network layer
* B. Border Gateway Protocol, Application layer
* C. Border Gateway Protocol, Network layer
* D. Backbone Gateway Protocol, Data Link layer

**Answer:** B. Border Gateway Protocol, Application layer  
**Explanation:** BGP stands for Border Gateway Protocol. Because BGP runs on top of TCP (port 179) as a routing information exchange application, it is classified at the Application layer (Layer 7) of the OSI model.

---

### Q20. TCP Reliability and Order Mechanism

**Topic:** `Networking`  

What mechanism does TCP use to ensure the data sent from one host to another is received correctly and in order?

**Options:**
* A. Tunneling
* B. Handshaking
* C. Sequence numbers and acknowledgements
* D. Packet sniffing

**Answer:** C. Sequence numbers and acknowledgements  
**Explanation:** TCP assigns a sequence number to each byte of data transmitted. The receiver uses these sequence numbers to reassemble the bytes in the correct order and sends acknowledgements (ACKs) to the sender to verify successful delivery.

---

## C Programming MCQs

### Q21. C Pointer Manipulation Output

**Topic:** `C Programming`, `Pointers`  

What is the output of the following C code?

```c
#include <stdio.h>
int main() {
    char arr[] = "abcd";
    char *p = arr;
    printf("%c\t", ++*p);
    printf("%c\t", *p++);
    printf("%c\t", (*p)++);
    printf("%c\n", *p);
    return 0;
}
```

**Options:**
* A. `b b b c`
* B. `b c c d`
* C. `b b c c`
* D. `b c c c`

**Answer:** A. `b b b c`  
**Explanation:**
1. `char arr[] = "abcd"; char *p = arr;` -> `p` points to `'a'`.
2. `printf("%c\t", ++*p);` -> Increments the value at `p` from `'a'` to `'b'`. Prints `'b'`. `arr` is now `"bbcd"`.
3. `printf("%c\t", *p++);` -> Evaluates `*p` which is `'b'`, and then increments pointer `p` to point to `arr[1]`. Prints `'b'`.
4. `printf("%c\t", (*p)++);` -> Evaluates `*p` which is `'b'`, and then increments the value at `arr[1]` from `'b'` to `'c'`. Prints `'b'`. `arr` is now `"bccd"`.
5. `printf("%c\n", *p);` -> Prints the value at `p` (which is `arr[1]`), which is now `'c'`.
The overall printed output is `b\tb\tb\tc\n`, which corresponds to `b b b c`.

---

## Puzzles & Aptitude MCQs

### Q22. Three Ants on a Triangle (Probability)

**Topic:** `Puzzles`, `Probability`  

Three ants are sitting at the three corners of an equilateral triangle. Each ant randomly picks a direction and starts to move along the edge of the triangle. What is the probability that none of the ants collide?

**Options:**
* A. 0.2
* B. 0.25
* C. 0.33
* D. 0.5

**Answer:** B. 0.25  
**Explanation:** Each ant has 2 choices of direction (clockwise or counterclockwise), resulting in $2^3 = 8$ total outcomes. A collision is avoided if and only if all three ants choose the same direction (either all clockwise or all counterclockwise). There are 2 such configurations. Thus, the probability of no collision is $\frac{2}{8} = 0.25$.

---

### Q23. Clock Hand Overlap (Aptitude)

**Topic:** `Puzzles`, `Aptitude`  

A regular clock has an hour and minute hand. At 12 midnight the hands are exactly aligned. How many times a day will they overlap?

**Options:**
* A. 24
* B. 23
* C. 22
* D. 21

**Answer:** C. 22  
**Explanation:** The minute hand makes 24 revolutions in a day, while the hour hand makes 2. Their relative number of overlaps is $24 - 2 = 22$. Hence, they overlap exactly 22 times a day.

---

### Q24. Egg Dropping Puzzle (2 Eggs, 100 Floors)

**Topic:** `Puzzles`, `Dynamic Programming`  

There is a building of 100 floors. If an egg drops from the Nth floor or above it will break. If it's dropped from any floor below, it will not break. You're given 2 eggs. How many drops do you need to make in the worst case to determine the threshold floor N?

**Options:**
* A. 12
* B. 14
* C. 17
* D. 20

**Answer:** B. 14  
**Explanation:** Let $x$ be the number of drops. The maximum number of floors we can cover with $x$ drops is given by the sum: $x + (x-1) + (x-2) + \dots + 1 = \frac{x(x+1)}{2}$. We need this sum to be at least 100:
$$\frac{x(x+1)}{2} \ge 100 \implies x^2 + x - 200 \ge 0$$
For $x = 13$, $\frac{13 \times 14}{2} = 91 < 100$.
For $x = 14$, $\frac{14 \times 15}{2} = 105 \ge 100$.
So, 14 drops are required in the worst case.

---

### Q25. Finding the Odd Coin (9 Coins, 1 Weighing Scale)

**Topic:** `Puzzles`, `Aptitude`  

There are 9 coins. Out of which one is an odd one i.e. its weight is less. How many iterations of weighing on a balance scale are required to find the odd coin?

**Options:**
* A. 2
* B. 3
* C. 4
* D. 5

**Answer:** A. 2  
**Explanation:**
1. Group the coins into 3 sets of 3: Set A, Set B, Set C.
2. Weigh Set A against Set B. If they balance, the lighter coin is in Set C. If they do not balance, it is in the lighter set on the scale.
3. Take the 3 coins from the identified lighter set. Place one on each side of the scale, leaving one aside. If they balance, the one left aside is the lighter coin. If they do not, the lighter side of the scale holds the odd coin.
Exactly 2 weighings are needed.

---

### Q26. Modulo Arithmetic: Remainder of $2000^{1000}$ Divided by 13

**Topic:** `Puzzles`, `Aptitude`, `Mathematics`  

What is the remainder when $2000^{1000}$ is divided by 13?

**Options:**
* A. 3
* B. 4
* C. 8
* D. 11

**Answer:** A. 3  
**Explanation:**
1. First, simplify 2000 modulo 13:
   $$2000 \equiv 11 \equiv -2 \pmod{13}$$
2. Thus, we need to find $(-2)^{1000} \equiv 2^{1000} \pmod{13}$.
3. By Fermat's Little Theorem:
   $$2^{12} \equiv 1 \pmod{13}$$
4. Express the exponent 1000 as $12 \times 83 + 4$:
   $$2^{1000} \equiv (2^{12})^{83} \cdot 2^4 \equiv 1^{83} \cdot 16 \equiv 16 \equiv 3 \pmod{13}$$
The remainder is 3.

---

### Q27. Cyclical Sequence Product

**Topic:** `Puzzles`, `Mathematics`  

A number sequence has 100 elements. Any of its elements (except for the first and last elements) is equal to the product of its neighbors. The product of the first 50 elements is 27, and the product of all 100 elements is 27. What is the sum of the first and the second element?

**Options:**
* A. 6
* B. 7
* C. 10
* D. 12

**Answer:** D. 12  
**Explanation:** Let the sequence be $a_1, a_2, \dots, a_{100}$. The relation is $a_n = a_{n-1} \cdot a_{n+1}$, which means $a_{n+1} = a_n / a_{n-1}$.
Let $a_1 = p$ and $a_2 = q$. The sequence is:
$$p, q, \frac{q}{p}, \frac{1}{p}, \frac{1}{q}, \frac{p}{q}, p, q, \dots$$
This sequence repeats every 6 terms. The product of any 6 consecutive terms is:
$$p \cdot q \cdot \frac{q}{p} \cdot \frac{1}{p} \cdot \frac{1}{q} \cdot \frac{p}{q} = 1$$
* The product of the first 50 terms is the product of 8 full 6-term cycles (which equals 1) and the first 2 terms ($a_1 \cdot a_2 = p \cdot q$):
  $$P_{50} = p \cdot q = 27$$
* The product of all 100 terms is the product of 16 full cycles (which equals 1) and the first 4 terms ($a_1 \cdot a_2 \cdot a_3 \cdot a_4 = p \cdot q \cdot \frac{q}{p} \cdot \frac{1}{p} = \frac{q^2}{p}$):
  $$P_{100} = \frac{q^2}{p} = 27$$
* Solving the two equations:
  $$p \cdot q = 27 \implies p = \frac{27}{q}$$
  $$\frac{q^2}{p} = 27 \implies \frac{q^2}{27/q} = 27 \implies q^3 = 27^2 = 729 \implies q = 9$$
  $$p = \frac{27}{9} = 3$$
The sum of the first and second elements is $p + q = 3 + 9 = 12$.

---

### Q28. Calendar Problem: Day of the Week Last Year

**Topic:** `Puzzles`, `Aptitude`  

December 8, 2007 was a Saturday. What day of the week was December 8, 2006?

**Options:**
* A. Sunday
* B. Thursday
* C. Tuesday
* D. Friday

**Answer:** D. Friday  
**Explanation:** The period from December 8, 2006 to December 8, 2007 is exactly 365 days (neither 2006 nor 2007 was a leap year). Since $365 \pmod 7 = 1$, December 8, 2007 is exactly 1 day of the week ahead of December 8, 2006. Since Dec 8, 2007 was Saturday, Dec 8, 2006 must have been Friday.

---

### Q29. Expected Number of Surviving Animals (Binomial Probability)

**Topic:** `Puzzles`, `Aptitude`, `Probability`  

There are 729 farmers in a state, each owning 6 animals. The animals are either cows or hens. Last year there was a flood. The probability of survival of a hen was 1/3 and that of a cow was 2/3. How many families (farmers) have exactly 2 hens and 4 cows surviving?

**Options:**
* A. 95
* B. 240
* C. 80
* D. None of the above

**Answer:** B. 240  
**Explanation:** For each farmer owning 6 animals, the probability of exactly 2 hens and 4 cows surviving is modeled by a binomial distribution:
$$P(\text{2 hens, 4 cows}) = \binom{6}{2} \cdot \left(\frac{1}{3}\right)^2 \cdot \left(\frac{2}{3}\right)^4$$
$$P = 15 \cdot \frac{1}{9} \cdot \frac{16}{81} = 15 \cdot \frac{16}{729} = \frac{240}{729}$$
Multiplying the probability by the total number of farmers (729):
$$\text{Expected families} = \frac{240}{729} \cdot 729 = 240$$

---

## Data Interpretation MCQs

### Q30. Hington and Euphore Phone Users (DI)

**Topic:** `Aptitude`, `Data Interpretation`  

The following table shows the number of customers (in millions) using Hington and Euphore brand phones in France from August to October 2012:

| Month | Hington | Euphore |
|---|---|---|
| Aug-12 | 46.18 | 47.28 |
| Sep-12 | 47.34 | 48.91 |
| Oct-12 | 49.32 | 49.27 |

The following table shows the addition of customers (in millions) of Hington and Euphore in each of the three months. There are two versions of the Euphore brand phones: Version-1 and Version-2.

| Month | Hington | Version-1 | Version-2 |
|---|---|---|---|
| Aug-12 | 0.36 | 1.24 | 0.6 |
| Sep-12 | 1.16 | 1.08 | 0.8 |
| Oct-12 | 1.98 | 0.84 | 0.48 |

What was the total number of people using either of the two brands in July 2012?

**Options:**
* A. 91.21 million
* B. 6.87 million
* C. 98.23 million
* D. None of these

**Answer:** D. None of these  
**Explanation:**
1. Total customers in August 2012 = $46.18 \text{ (Hington)} + 47.28 \text{ (Euphore)} = 93.46 \text{ million}$.
2. Total customer additions in August 2012 = $0.36 \text{ (Hington)} + 1.24 \text{ (Version-1)} + 0.6 \text{ (Version-2)} = 2.20 \text{ million}$.
3. Therefore, the total number of users at the end of July 2012 was:
   $$93.46 - 2.20 = 91.26 \text{ million}$$
Since 91.26 million is not among the options (91.21 million, 6.87 million, 98.23 million), the correct option is "None of these".

---

### Q31. Pollution Index Ranking of Cities (DI)

**Topic:** `Aptitude`, `Data Interpretation`  

The graph shows the pollution index of 7 cities (A, B, C, D, E, F, and G) from 2006 to 2010:

| City | 2006 | 2007 | 2008 |
|---|---|---|---|
| **A** | 13 | 21 | 24 |
| **B** | 15 | 17 | 11 |
| **C** | 34 | 35 | 29 |
| **D** | 56 | 57 | 56 |
| **E** | 57 | 45 | 45 |
| **F** | 12 | 12 | 13 |
| **G** | 11 | 15 | 17 |

If for each year, the cities are ranked in terms of ascending order of pollution index (the city with the least pollution index stands first), then how many cities do not change their ranking more than once from 2006 to 2008?

**Options:**
* A. 1
* B. 2
* C. 3
* D. 4

**Answer:** D. 4  
**Explanation:** Let's calculate the ranking for each city from 2006 to 2008 based on ascending pollution indices:

* **2006 Rankings:** G(11)->rank 1, F(12)->rank 2, A(13)->rank 3, B(15)->rank 4, C(34)->rank 5, D(56)->rank 6, E(57)->rank 7.
* **2007 Rankings:** F(12)->rank 1, G(15)->rank 2, B(17)->rank 3, A(21)->rank 4, C(35)->rank 5, E(45)->rank 6, D(57)->rank 7.
* **2008 Rankings:** B(11)->rank 1, F(13)->rank 2, G(17)->rank 3, A(24)->rank 4, C(29)->rank 5, E(45)->rank 6, D(56)->rank 7.

Let's count the number of ranking changes for each city from 2006 to 2008:
* **City A:** rank 3 -> rank 4 -> rank 4 (1 change)
* **City B:** rank 4 -> rank 3 -> rank 1 (2 changes)
* **City C:** rank 5 -> rank 5 -> rank 5 (0 changes)
* **City D:** rank 6 -> rank 7 -> rank 7 (1 change)
* **City E:** rank 7 -> rank 6 -> rank 6 (1 change)
* **City F:** rank 2 -> rank 1 -> rank 2 (2 changes)
* **City G:** rank 1 -> rank 2 -> rank 3 (2 changes)

The cities that do not change their ranking more than once (i.e., $\le 1$ change) are **A**, **C**, **D**, and **E**. There are exactly **4** such cities.

---

## Verbal Ability MCQs

### Q32. Sentence Improvement: Present Perfect Continuous

**Topic:** `English`, `Grammar`  

Improve the Sentence: *My father is suffering from diabetes for the past three years.*

**Options:**
* A. has been suffering
* B. has suffered
* C. is suffer
* D. No improvement

**Answer:** A. has been suffering  
**Explanation:** Because the sentence specifies a time duration that started in the past and continues into the present ("for the past three years"), we must use the present perfect continuous tense ("has been suffering") instead of the present continuous tense ("is suffering").

---

### Q33. Grammatical Correctness (Possessive "its" vs. "it's")

**Topic:** `English`, `Grammar`  

Which of the following four sentences is grammatically correct?

**Options:**
* A. The Board of Directors will hold its next meeting in July.
* B. The Board of Directors will hold it's next meeting in July.
* C. The Board of Directors shall hold the next meeting in July.
* D. The Board of Directors shall hold it's next meeting in July.

**Answer:** A. The Board of Directors will hold its next meeting in July.  
**Explanation:** "Board of Directors" is a singular collective noun, so the possessive pronoun "its" is appropriate. Option B uses "it's" (contraction of "it is" or "it has"), which is incorrect.

---

### Q34. Spotting the Grammatical Error (Past Perfect vs. Present Perfect)

**Topic:** `English`, `Grammar`  

Find out which underlined part of the sentence below has an error and mark the option accordingly.
*I regret that I wasn't aware that you <u>have lost your</u> job when you visited me last week.*

**Options:**
* A. I wasn't aware
* B. Have lost your
* C. When you visited me
* D. None of the options

**Answer:** B. Have lost your  
**Explanation:** The visiting and regret occur in the past ("wasn't aware", "visited"). Since the losing of the job happened prior to these past events, it must be in the past perfect tense: "had lost your" instead of the present perfect "have lost your".

---

### Q35. Reading Comprehension: Twitter 140-Character Limit Impact

**Topic:** `English`, `Verbal Ability`  

According to the passage, Twitter only allows 140 characters per tweet. What edge do you think it gives the app over other social media applications that allow for more use of characters?

**Options:**
* A. Correction can be easily made to tweets before uploading them.
* B. It ensures that users can share their thoughts in little time even when busy.
* C. More people will get to consume information far more quickly.
* D. No other app can boast of having such a unique design.

**Answer:** C. More people will get to consume information far more quickly.  
**Explanation:** The passage states: "Twitter's maximum brevity further ensures more users read the entire message because a 140-character remark only takes a few seconds to read and retweet." This directly corresponds to people consuming information far more quickly.

---

### Q36. Reading Comprehension: Vocabulary Usage ("weaned off")

**Topic:** `English`, `Vocabulary`  

Which of the following does not correctly utilize a phrase or other similar terms to "weaned off" as used in the passage?

**Options:**
* A. Some seal pups are taken off their mothers' teats after only two weeks.
* B. I'm trying to encourage people to eat fruits and vegetables.
* C. The medication helps dissuade patients from taking alcohol by simulating its effects on the brain.
* D. I want to curtail my kids' interest in T.V. and video games.

**Answer:** B. I'm trying to encourage people to eat fruits and vegetables.  
**Explanation:** In the passage, "weaned off" is used to describe customers being gradually drawn away from or stopping a service/habit.
* "taken off" (A), "dissuade from taking" (C), and "curtail interest in" (D) are all semantically related to stopping, reducing, or withdrawing from something.
* "encourage people to eat..." (B) is the opposite of withdrawing/stopping, and has no similarity to the concept of weaning off.
