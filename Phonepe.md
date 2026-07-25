# Phonepe Online Assessment Questions

*Total questions: 6*

---

## Table of Contents
1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. XOR Subarrays with Even Number of Divisors

**Topic:** `Prefix XOR`, `Math / Divisors`, `Square Numbers`

#### Problem Statement
One day, the wise elders of the kingdom posed a challenge. They wanted to find special parts of the array where, if you did a special math operation called XOR on the numbers, the result would have an even number of divisors.

For example, numbers 2, 3, 5 or 6 have an even number of divisors, while 1, 4 have an odd number of divisors. (A number has an odd number of divisors if and only if it is a perfect square).

Brave adventurers stepped up to solve the puzzle. They searched through the array, looking for sections where the XOR of numbers had this special property. With each discovery, they counted the number of subarrays with XOR having an even number of divisors.

Print the number of such subarrays, whose XOR has an even number of divisors.

#### Input Format
- The first line of input contains a single integer $n$ ($2 \le n \le 2 \times 10^5$) — the length of the array $a$.
- The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le n$).

#### Constraints
- $2 \le n \le 2 \times 10^5$
- $1 \le a_i \le n$

#### Output Format
Print the number of subarrays whose XOR has an even number of divisors.

#### Sample Input 1
```
3
3 1 2
```

#### Sample Output 1
```
4
```

#### Explanation 1
There are 4 subarrays whose XOR has an even number of divisors (i.e. is not a perfect square):
`[3]` (XOR = 3), `[3, 1]` (XOR = 2), `[1, 2]` (XOR = 3), and `[2]` (XOR = 2).
The subarrays `[1]` (XOR = 1), and `[3, 1, 2]` (XOR = 3^1^2 = 0) are excluded since their XOR sums are perfect squares ($1^2 = 1, 0^2 = 0$) which have an odd number of divisors.

#### Sample Input 2
```
5
4 2 1 5 3
```

#### Sample Output 2
```
11
```

#### Explanation 2
There are 11 subarrays whose XOR has an even number of divisors:
`[4, 2]`, `[4, 2, 1]`, `[4, 2, 1, 5]`, `[2]`, `[2, 1]`, `[2, 1, 5]`, `[2, 1, 5, 3]`, `[1, 5, 3]`, `[5]`, `[5, 3]`, and `[3]`.

#### Solution (Python)
```python
def solve_xor_subarrays(n, arr):
    # Total number of subarrays is n * (n + 1) // 2.
    # A number has an odd number of divisors if and only if it is a perfect square.
    # Therefore, we want to find the number of subarrays whose XOR sum is NOT a perfect square.
    # We can count the number of subarrays whose XOR sum IS a perfect square and subtract it from the total.
    
    # Since a[i] <= n <= 2 * 10^5, the maximum possible value of any element is 2 * 10^5.
    # The prefix XOR values can be at most the next power of 2, which is 2^18 - 1 = 262143.
    # Thus, the maximum possible XOR sum is less than 2^18.
    
    # We compute the prefix XORs
    pref_vals = [0]
    pref = 0
    for x in arr:
        pref ^= x
        pref_vals.append(pref)
        
    max_pref = max(pref_vals)
    limit = 1
    while limit <= max_pref:
        limit <<= 1
        
    # Precompute all perfect squares up to the maximum possible XOR sum
    squares = []
    i = 0
    while i * i < limit:
        squares.append(i * i)
        i += 1
        
    # Count prefix XOR frequencies
    square_xor_subarrays = 0
    curr_freq = {0: 1}
    curr_pref = 0
    
    for x in arr:
        curr_pref ^= x
        for sq in squares:
            target = curr_pref ^ sq
            if target in curr_freq:
                square_xor_subarrays += curr_freq[target]
        curr_freq[curr_pref] = curr_freq.get(curr_pref, 0) + 1
        
    total_subarrays = n * (n + 1) // 2
    return total_subarrays - square_xor_subarrays

# Time Complexity: O(n * sqrt(max_XOR)), where sqrt(max_XOR) <= 512.
# Space Complexity: O(n) to store prefix XOR frequencies.
```

---

### Q2. The Lost Puzzle of Algoria

**Topic:** `Greedy`, `Bitwise XOR`, `Sorting`, `Connected Components`

#### Problem Statement
In the land of Algoria, you will be given an array of non-negative integers. Your task is to rearrange this array to make it lexicographically as small as possible. However, there's a catch! You can only swap two elements in the array if the bitwise XOR of those two elements is less than 4.

#### Input Format
- The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the length of the array.
- The second line contains $n$ integers $a_i$ ($0 \le a_i \le 10^9$) — the elements of the array.

#### Constraints
- $1 \le n \le 2 \cdot 10^5$
- $0 \le a_i \le 10^9$
- It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.

#### Output Format
Output $n$ space-separated integers — the lexicographically smallest array that can be made with any number of swaps.

#### Sample Input 1
```
4
1 0 3 2
```

#### Sample Output 1
```
0 1 2 3
```

#### Sample Input 2
```
5
2 7 1 5 6
```

#### Sample Output 2
```
1 5 2 6 7
```

#### Explanation 2
1. As XOR of 1 and 2 is 3 ($3 < 4$), we can swap 1 and 2 $\to$ `[1, 7, 2, 5, 6]`
2. As XOR of 7 and 5 is 2 ($2 < 4$), we can swap 7 and 5 $\to$ `[1, 5, 2, 7, 6]`
3. As XOR of 7 and 6 is 1 ($1 < 4$), we can swap 7 and 6 $\to$ `[1, 5, 2, 6, 7]`

#### Solution (Python)
```python
from collections import defaultdict

def solve_algoria(n, arr):
    # Two elements x and y can be swapped if and only if x ^ y < 4.
    # This condition means that x and y must have the same bits at all positions
    # except possibly the last two bits (weights 1 and 2).
    # Mathematically, this is equivalent to x // 4 == y // 4.
    # Since swap is transitive, we can group elements by their key (x // 4).
    # Inside each group, we can sort the values and place them back at the sorted indices.
    
    groups = defaultdict(list)
    for i, x in enumerate(arr):
        groups[x // 4].append((x, i))
        
    result = [0] * n
    for g_id, elements in groups.items():
        # Sort values and indices
        vals = sorted([x[0] for x in elements])
        indices = sorted([x[1] for x in elements])
        
        # Place sorted values at the sorted indices
        for val, idx in zip(vals, indices):
            result[idx] = val
            
    return result

# Time Complexity: O(n log n) due to sorting within components.
# Space Complexity: O(n) to store components.
```

---

### Q3. The Paris Olympics (Hurdles)

**Topic:** `Dynamic Programming`, `Sliding Window / Deque`, `Monotonic Queue`

#### Problem Statement
The Paris Olympics are here and the Olympics committee has decided to introduce a new game. The game is as follows:
- There are $n$ ordered hurdles and an athlete can cross at most $k$ consecutive hurdles. (For example, if there are 3 hurdles and $k = 1$, the athlete must remove hurdles such that no two adjacent hurdles are kept).
- Each hurdle is associated with a non-negative score, and the athlete can decide which hurdles to remove to achieve the maximum score.
- The athlete wants your help in identifying the maximum score possible for a given $n$, $k$, and the hurdle scores.
- Note: Hurdles are ordered and cannot be reordered.

#### Input Format
- First line contains two space-separated integers $n$ (number of hurdles) and $k$ (maximum number of consecutive hurdles that the athlete can cross).
- Each line $i$ of the $n$ subsequent lines contains an integer denoting the score of hurdle $i$ where $0 \le i < n$.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le k \le n$
- $0 \le \text{score of a hurdle} \le 2 \cdot 10^9$

#### Output Format
Print a single integer denoting the maximum score that the athlete can achieve.

#### Sample Input 0
```
6 2
1
2
3
1
6
10
```

#### Sample Output 0
```
21
```

#### Explanation 0
There are 6 hurdles and the athlete can keep at most 2 consecutive hurdles. The athlete can remove the first and fourth hurdle, leaving the configuration `_ 2 3 _ 6 10` with a score of 2 + 3 + 6 + 10 = 21.

#### Sample Input 1
```
5 4
1
2
3
4
5
```

#### Sample Output 1
```
14
```

#### Explanation 1
There are 5 hurdles and the athlete can keep at most 4 consecutive hurdles. The athlete can remove the first hurdle, leaving `_ 2 3 4 5` with a score of 2 + 3 + 4 + 5 = 14.

#### Solution (Python)
```python
from collections import deque

def solve_hurdles(n, k, scores):
    # To maximize the score of kept hurdles such that at most k consecutive hurdles are crossed,
    # we can equivalent minimize the score of removed hurdles such that in any window of size k + 1,
    # at least one hurdle is removed.
    
    # Let dp[i] be the minimum cost of removed hurdles in the prefix of length i,
    # where the i-th hurdle is definitely removed.
    # dp[i] = scores[i] + min_{i - (k+1) <= j < i} dp[j]
    
    # We can add virtual removed hurdles at index 0 and index n + 1 (with score 0) to handle boundaries.
    A = [0] + scores + [0]
    n_padded = len(A)
    dp = [0] * n_padded
    
    # Window size is k + 1
    w = k + 1
    dq = deque([0]) # Monotonic queue storing indices of dp
    
    for i in range(1, n_padded):
        # Remove elements outside the sliding window
        while dq and dq[0] < i - w:
            dq.popleft()
            
        dp[i] = A[i] + dp[dq[0]]
        
        # Maintain monotonic increasing property in the deque
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
        
    total_sum = sum(scores)
    return total_sum - dp[-1]

# Time Complexity: O(n) because each index is pushed and popped from the deque at most once.
# Space Complexity: O(n) to store DP values.
```

---

### Q4. Help Mike Get Rich

**Topic:** `Binary Search`, `Queue / Simulation`, `Greedy`

#### Problem Statement
Mike Ross is a brilliant lawyer, and wins all his cases. But he is not a morning person.
His law firm brought up a new rule, wherein to be eligible for a bonus, a lawyer must go through one pending case doc every day. If that streak is broken, no bonus for that year.

To keep the case distribution fair, a few rules were laid out:
1. Whenever a lawyer enters the office, he/she would wait in line for the next case distribution event.
2. Every case distribution event in a day has a fixed number of cases.
3. At the distribution time, lawyers with the earliest entry times get the cases first.
4. If there are pending cases, and no lawyers are waiting, they are sent to senior partners and are considered as an opportunity lost.
5. Distribution times and batch size can change each day.

Also note, no two lawyers can arrive at the same time.
Overworked Mike started having visions that he also received the timestamps of the next day's case distribution events and the entry timestamps of other lawyers in random order.
Mike decided to take the help of his programmer friend. You have to help lazy Mike with the latest time he could reach the office without missing out on his case streak for that particular day.

Time of case distribution and lawyers' office entry times are denoted with integers, starting the day at time 0.
Do not expect the distribution schedule times array and lawyer arrival times array to be sorted.

#### Input Format
- First line consists of the number of distribution events for that day ($n$).
- Next line has space-separated timestamps for all events for that day.
- Next line has the number of lawyers who Mike is competing with ($m$).
- Next line has space-separated timestamps for the entry of other lawyers.
- Finally, the number of cases per distribution event ($C$) is given.

#### Constraints
- $1 \le n, m \le 10^5$
- $1 \le C \le 10^5$
- $2 \le \text{distributionEvent}[i], \text{lawyerEntryTime}[i] \le 10^9$
- Each element in the distribution timestamps array is unique.
- Each element in the lawyer entry timestamps array is unique.

#### Output Format
Print a single timestamp which is the latest Mike could reach the office and get a case assigned successfully. If no such time exists, return -1.

#### Sample Input 1
```
3
20 30 10
7
19 13 26 4 25 11 21
2
```

#### Sample Output 1
```
20
```

#### Explanation 1
Suppose Mike arrives at timestamp 20:
- At timestamp 10 distribution event: 1 case is assigned to the lawyer who arrived at timestamp 4. The second case is sent to a senior partner (ignored).
- At timestamp 20 distribution event: cases are assigned to lawyers who arrived at timestamps 11 and 13.
- At timestamp 30 distribution event: The queue has the remaining waiting lawyers [19, 20 (Mike), 21, 25, 26]. The two cases are assigned to the lawyer who arrived at 19 and Mike (who arrived at 20). Mike gets a case!
If Mike had entered any later, then the lawyer who entered at timestamp 21 would have received the case, and Mike would have lost his streak.

#### Sample Input 2
```
2
10 20
4
2 17 18 19
2
```

#### Sample Output 2
```
16
```

#### Explanation 2
- First distribution event at timestamp 10: The lawyer who entered at 2 will get a case, and 1 case will be ignored as no other lawyer is present.
- Second distribution event at timestamp 20: One case will be given to the lawyer who entered at 17. Since no two lawyers can have the same entry times, Mike could not enter at 17, 18, or 19. Mike must enter the office at timestamp 16 to be able to get the second case.

#### Solution (Python)
```python
from collections import deque
from bisect import bisect_right

def solve_mike(n, D, m, L, C):
    # Sort distribution events and other lawyers' arrival times
    sorted_D = sorted(D)
    sorted_L = sorted(L)
    L_set = set(L)
    
    # Helper function to check if Mike gets a case if he arrives at time T.
    # If Mike arrives at T, since we want to place Mike last among people arriving at T,
    # we can use bisect_right to insert T into the sorted L list.
    def check(T):
        idx = bisect_right(sorted_L, T)
        # Mark Mike as True, others as False
        merged = [(t, False) for t in sorted_L[:idx]] + [(T, True)] + [(t, False) for t in sorted_L[idx:]]
        
        q = deque()
        ptr = 0
        n_merged = len(merged)
        
        for d in sorted_D:
            # Add all lawyers who arrived <= d
            while ptr < n_merged and merged[ptr][0] <= d:
                q.append(merged[ptr])
                ptr += 1
            
            # Distribute C cases
            for _ in range(C):
                if not q:
                    break
                lawyer = q.popleft()
                if lawyer[1]:  # If it's Mike, he gets a case!
                    return True
        return False

    # Binary search for the maximum T such that check(T) is True.
    # Note: T can be any integer in [0, max(D)].
    low = 0
    high = max(D)
    T_max = -1
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            T_max = mid
            low = mid + 1
        else:
            high = mid - 1
            
    if T_max == -1:
        return -1
        
    # Since Mike cannot arrive at a time that is already in L,
    # we decrement T_max until we find a time not in L.
    T = T_max
    while T in L_set:
        T -= 1
    return T

# Time Complexity: O((n + m) * log(max(D)) + m log m + n log n).
# For n, m <= 10^5 and max(D) <= 10^9, this takes ~30 simulations, each taking O(n + m) time,
# which is extremely fast and easily passes.
# Space Complexity: O(n + m) to store sorted lists.
```

---

### Q5. Dora The Explorer

**Topic:** `Graph Shortest Path`, `Dijkstra's Algorithm`

#### Problem Statement
Dora is vacationing on an archipelago of islands. The archipelago has $N$ islands. Dora has decided to start her vacation on Island $S$ and end it on Island $E$.

The archipelago offers travel between islands through a Boat and a Sea Plane. Being quite an explorer, Dora wants to travel using only Boat for one part of the vacation and using only Plane for the other part of the vacation. Dora must switch her mode of transportation exactly once.

For example, Dora can travel from Island $S$ to some island $I$ (either directly or through other islands) using the Boat only and then from island $I$ to $E$ (either directly or through other islands) using the Plane only. Alternatively, Dora can travel from Island $S$ to island $I$ using the Plane only and then from island $I$ to $E$ using the Boat only.

Dora has a chart showing the cost of travel from each island to other islands by both Boat and Plane. Help Dora minimize the cost of the vacation. Return the minimum cost, or return -1 if it's not possible to complete the journey.

#### Input Format
- First line contains $N$, a single integer indicating the number of islands in the archipelago.
- The next $N$ lines contain $N$ space-separated numbers. This is a matrix $B$, where $B_{ij}$ is the cost of travel from island $i$ to island $j$ by Boat.
- The next $N$ lines contain $N$ space-separated numbers. This is a matrix $P$, where $P_{ij}$ is the cost of travel from island $i$ to island $j$ by Plane.
- The last line contains 2 space-separated integers, $S$ and $E$, which are Dora's Start and End islands respectively.

#### Constraints
- $3 \le N \le 1250$
- $1 \le S, E \le N$ and $S \ne E$
- $1 \le B_{ij}, P_{ij} \le 100$, and $B_{ij}, P_{ij} = -1$ if Dora cannot travel from $i$ to $j$.

#### Output Format
A single number indicating the minimum cost of the vacation.

#### Sample Input 1
```
3
-1 1 2
3 -1 4
5 6 -1
-1 6 5
1 -1 4
3 2 -1
1 2
```

#### Sample Output 1
```
4
```

#### Explanation 1
Dora can go from Island 1 to Island 3 by Boat at the cost of 2, and then from Island 3 to Island 2 by Plane at the cost of 2.
Total Cost = 2 + 2 = 4.

#### Sample Input 2
```
5
-1 3 38 96 1
40 -1 16 24 73
5 52 -1 93 34
78 10 73 -1 84
50 15 51 53 -1
-1 67 30 50 45
96 -1 5 2 12
60 19 -1 51 46
-1 56 79 -1 2
83 2 30 5 -1
1 4
```

#### Sample Output 2
```
5
```

#### Explanation 2
Dora can go from Island 1 to Island 5 by Boat at the cost of 1. And from Island 5 to Island 2 at the cost of 2 and from Island 2 to Island 4 at the cost of 2 by Plane.
Total cost = 1 + 2 + 2 = 5.

#### Solution (Python)
```python
def solve_dora(n, B, P, S, E):
    # S and E are 1-based, convert them to 0-based
    S -= 1
    E -= 1
    
    # Dijkstra function for dense graphs: O(N^2)
    def dijkstra(start, adj):
        dist = [float('inf')] * n
        dist[start] = 0
        visited = [False] * n
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                    u = i
            if dist[u] == float('inf'):
                break
            visited[u] = True
            for v in range(n):
                weight = adj[u][v]
                if weight != -1 and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        return dist

    # Create transpose matrices for finding shortest paths TO E
    B_transpose = [[B[j][i] for j in range(n)] for i in range(n)]
    P_transpose = [[P[j][i] for j in range(n)] for i in range(n)]
    
    # Calculate shortest distances
    dist_boat_from_S = dijkstra(S, B)
    dist_plane_from_S = dijkstra(S, P)
    dist_boat_to_E = dijkstra(E, B_transpose)
    dist_plane_to_E = dijkstra(E, P_transpose)
    
    ans = float('inf')
    # Try every possible intermediate island I (where I != S and I != E)
    for I in range(n):
        if I == S or I == E:
            continue
        # Option 1: Boat from S to I, Plane from I to E
        ans = min(ans, dist_boat_from_S[I] + dist_plane_to_E[I])
        # Option 2: Plane from S to I, Boat from I to E
        ans = min(ans, dist_plane_from_S[I] + dist_boat_to_E[I])
        
    return ans if ans != float('inf') else -1

# Time Complexity: O(N^2) for running Dijkstra 4 times on a graph with N nodes.
# Space Complexity: O(N^2) to store transpose graphs.
```

---

### Q6. Fun Friday

**Topic:** `Greedy`, `Sorting`, `Math`

#### Problem Statement
As a fun Friday activity, Harsh and Pranay decided to play a new game. The game begins with Harsh giving a list of $n$ numbers to Pranay.

In each iteration,
1. Pranay adds up all the numbers in the list and adds that sum to his points. Then, he returns the list of numbers to Harsh.
2. Harsh performs the following actions:
   - If Harsh gets a list with only one number, he throws it out of the game.
   - If Harsh gets a list consisting of more than one number, he divides the list into two non-empty subsequences and gives both subsequences to Pranay one by one.

After Harsh and Pranay complete all iterations, Pranay checks his total points. Determine the maximum possible points Pranay can get.

#### Input Format
- The first line contains a single integer $n$ ($1 \le n \le 3 \cdot 10^5$) — the number of initial elements.
- The second line contains $n$ space-separated integers $a_i$ ($1 \le a_i \le 10^6$) — the initial numbers given to Pranay.

#### Constraints
- $1 \le n \le 3 \cdot 10^5$
- $1 \le a_i \le 10^6$

#### Output Format
Print a single integer — the maximum possible points Pranay can get.

#### Sample Input 0
```
3
4 2 6
```

#### Sample Output 0
```
34
```

#### Explanation 0
Pranay's Turn:
- Pranay adds the sum of initial numbers (4 + 2 + 6) = 12 to his points. Points = 12. Returns `(4, 2, 6)` to Harsh.
Harsh's Turn:
- Harsh splits the list into `(2)` and `(4, 6)`.
Pranay's Turn:
- Pranay adds 2 to his points. Points = 14.
- Pranay adds 4 + 6 = 10 to his points. Points = 24.
Harsh's Turn:
- `(2)` is thrown out (size 1).
- `(4, 6)` is split into `(4)` and `(6)`.
Pranay's Turn:
- Pranay adds 4 to his points. Points = 28.
- Pranay adds 6 to his points. Points = 34.
Harsh's Turn:
- Both `(4)` and `(6)` are thrown out.
Game Ended. Total points = 34.

#### Sample Input 1
```
1
11
```

#### Sample Output 1
```
11
```

#### Explanation 1
Pranay adds 11 to points. Harsh throws `(11)` out since it is size 1. Game ended with 11 points.

#### Solution (Python)
```python
def solve_fun_friday(n, arr):
    # If there is only 1 element, Pranay gets exactly that element's value.
    if n == 1:
        return arr[0]
        
    # To maximize the points, we want to keep the largest elements in the game for as long as possible.
    # This means at each split, we should separate the smallest element from the rest.
    # For a sorted array a_0 <= a_1 <= ... <= a_{n-1}:
    # - a_0 is split off first (present in root and its own leaf): multiplier = 2
    # - a_1 is split off next: multiplier = 3
    # - ...
    # - a_{n-2} and a_{n-1} are left together at the last split: multiplier = n for both.
    
    arr_sorted = sorted(arr)
    total_points = 0
    for i in range(n - 2):
        total_points += (i + 2) * arr_sorted[i]
    total_points += n * arr_sorted[n - 2]
    total_points += n * arr_sorted[n - 1]
    
    return total_points

# Time Complexity: O(n log n) due to sorting.
# Space Complexity: O(n) to store sorted list.
```
