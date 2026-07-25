# Interview Questions
*Total questions: 7*

---

## Table of Contents
- [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Sun City
**Topic:** `Arrays`, `Prefix Sums`, `Optimization`

Bruce is the energy administrator in a city. He has set up N solar panels throughout the city which generate varying amounts of energy. The energy output of N solar panels is given in an integer array X.

The power output of a single solar panel in a day can be calculated by multiplying the energy output of a solar panel with its corresponding index. Bruce can reposition a solar panel by placing it either before or after another solar panel, but he can perform this repositioning only once as it is expensive to reinstall a solar panel.

Your task is to help Bruce find and return an integer value representing the maximum total power that the solar panels can produce in a day.

**Note:**
- Assume 1 based indexing.
- The energy output of a solar panel can be either negative or positive.

#### Input Specification
- **input1:** An integer value N, representing the number of solar panels.
- **input2:** An integer array X, representing the energy output of N solar panels.

#### Output Specification
- Return an integer value representing the maximum total power that the solar panels can produce in a day.

#### Examples
**Example 1:**
- **input1:** 5
- **input2:** `{8, 1, 6, 3, 4}`
- **Output:** 78
- **Explanation:** Originally, the energy output of the solar panels is `{8, 1, 6, 3, 4}` and the total power is:
  $(1 \times 8) + (2 \times 1) + (3 \times 6) + (4 \times 3) + (5 \times 4) = 60$.
  To maximize the total power production, Bruce can reposition the first solar panel (8) after the last solar panel (4). The new energy output array will be `{1, 6, 3, 4, 8}` and the total power produced will be:
  $(1 \times 1) + (2 \times 6) + (3 \times 3) + (4 \times 4) + (5 \times 8) = 78$.
  No other orientation can exceed this total power production.

**Example 2:**
- **input1:** 4
- **input2:** `{3, 5, -9, 10}`
- **Output:** 52
- **Explanation:** Originally, the energy output of the solar panels is `{3, 5, -9, 10}` and the total power is:
  $(1 \times 3) + (2 \times 5) + (3 \times -9) + (4 \times 10) = 26$.
  To maximize the total power production, Bruce can reposition the second last solar panel (-9) before the first solar panel (3). The new energy output array will be `{-9, 3, 5, 10}` and the total power produced will be:
  $(1 \times -9) + (2 \times 3) + (3 \times 5) + (4 \times 10) = 52$.

#### Solution
```python
def maxPowerProduction(N, X):
    # Original total power
    original_sum = sum((i + 1) * X[i] for i in range(N))
    
    # Prefix sums of X
    P = [0] * (N + 1)
    for i in range(N):
        P[i+1] = P[i] + X[i]
        
    max_delta = 0
    
    # Case 1: i < j (move X[i] to index j, shifting elements from i+1 to j left)
    # The change in sum is (j - i) * X[i] - sum(X[i+1...j])
    for i in range(N):
        for j in range(i + 1, N):
            delta = (j - i) * X[i] - (P[j+1] - P[i+1])
            if delta > max_delta:
                max_delta = delta
                
    # Case 2: i > j (move X[i] to index j, shifting elements from j to i-1 right)
    # The change in sum is (j - i) * X[i] + sum(X[j...i-1])
    for i in range(N):
        for j in range(i):
            delta = (j - i) * X[i] + (P[i] - P[j])
            if delta > max_delta:
                max_delta = delta
                
    return original_sum + max_delta
```

---

### Q2. Last One Standing
**Topic:** `Math`, `Josephus Problem`, `Simulation`

You are given an alphanumeric string S and an integer K. Consider a new string in which S is appended K-1 times.
Now, in this new string, the following operations are performed:-
1. Every alternate character starting from the first character is removed.
2. Every alternate character starting from the last character is removed.

The above two operations are repeated until one character remains.
Your task is to find and return a string representing the last remaining character after performing all the operations.

**Note:** Here, alphanumeric refers to the string that may contain alphabets (a-z and A-Z), numerals (0-9), and certain special characters such as '$', '#', '&', and '*'.

#### Input Specification
- **input1:** A string S, representing the alphanumeric string.
- **input2:** An integer value K.

#### Output Specification
- Return a string representing the last remaining character after performing all the operations mentioned.

#### Examples
**Example 1:**
- **input1:** `abcd`
- **input2:** 3
- **Output:** `b`
- **Explanation:**
  - $S = \text{"abcdabcdabcd"}$ (The string obtained after repeating $S$ $3$ times)
  - $S = \text{"bdbdbd"}$ (The string obtained after removing every alternate character from the beginning)
  - $S = \text{"bbb"}$ (The string obtained after removing every alternate character from the end)
  - $S = \text{"b"}$ (The string obtained after removing every alternate character from the beginning)
  - Return `b`.

**Example 2:**
- **input1:** `j#k&h`
- **input2:** 5
- **Output:** `&`

#### Solution
```python
def lastOneStanding(S, K):
    N = len(S)
    total_length = N * K
    
    # We represent the remaining characters using an Arithmetic Progression (AP):
    # start index (0-based in the repeated string), step, and count.
    A = 0
    D = 1
    C = total_length
    
    step_type = 1 # 1 for Operation 1, 2 for Operation 2
    
    while C > 1:
        if step_type == 1:
            # Remove every alternate character starting from the first.
            A = A + D
            D = 2 * D
            C = C // 2
            step_type = 2
        else:
            # Remove every alternate character starting from the last.
            if C % 2 == 0:
                D = 2 * D
                C = C // 2
            else:
                A = A + D
                D = 2 * D
                C = C // 2
            step_type = 1
            
    return S[A % N]
```

---

### Q3. Max OR Array
**Topic:** `Bitwise Operations`, `Two Pointers`, `Subarrays`

Jonathan is utilizing his summer vacations learning about arrays. He is solving a problem and gets stuck at some point so he asks you for help.

You are given an array A of size N containing non-negative integers. You can remove a subarray from array A, such that the bitwise OR of all the elements in the remaining array is the maximum possible.

Your task is to find and return an integer value the size of the maximum length subarray that can be removed.

#### Input Specification
- **input1:** An integer array A
- **input2:** An integer N denoting the size of the array

#### Output Specification
- Return an integer value the size of the maximum length subarray that can be removed.

#### Examples
**Example 1:**
- **input1:** `{1, 4, 24, 2}`
- **input2:** 4
- **Output:** 0
- **Explanation:** The bitwise OR of the whole array is 31 which is the maximum value possible and it cannot be achieved by removing any subarray. Hence, 0 is returned as the output.

**Example 2:**
- **input1:** `{2, 1, 1, 5, 4, 4, 8, 1}`
- **input2:** 8
- **Output:** 4
- **Explanation:** The maximum length subarray that can be removed is `{1, 1, 5, 4}` (indices 1 to 4). The bitwise OR of the remaining elements of the array `{2, 4, 8, 1}` is 15 which is the maximum value possible.

#### Solution
```python
def maxORArray(A, N):
    if N == 0:
        return 0
    
    total_or = 0
    for x in A:
        total_or |= x
        
    # prefix_or[i] stores OR of A[0...i]
    prefix_or = [0] * N
    curr = 0
    for i in range(N):
        curr |= A[i]
        prefix_or[i] = curr
        
    # suffix_or[i] stores OR of A[i...N-1]
    suffix_or = [0] * N
    curr = 0
    for i in range(N-1, -1, -1):
        curr |= A[i]
        suffix_or[i] = curr
        
    max_len = 0
    
    # Case 1: remove prefix A[0...R-1]. Remaining is A[R...N-1].
    for R in range(1, N):
        if suffix_or[R] == total_or:
            max_len = max(max_len, R)
            
    # Case 2: remove suffix A[L...N-1]. Remaining is A[0...L-1].
    for L in range(1, N):
        if prefix_or[L-1] == total_or:
            max_len = max(max_len, N - L)
            
    # Case 3: remove a middle subarray A[L...R-1].
    # Remaining is A[0...L-1] and A[R...N-1].
    # We want prefix_or[L-1] | suffix_or[R] == total_or.
    R = 1
    for L in range(1, N):
        while R < N and (prefix_or[L-1] | suffix_or[R]) == total_or:
            max_len = max(max_len, R - L)
            R += 1
        R = max(R, L + 1)
        
    return max_len
```

---

### Q4. Squirrel's Food
**Topic:** `Dynamic Programming`, `1D Clustering`, `Median`

You are given the position of N squirrels on a number line and K food packets for feeding these squirrels. Each squirrel must eat from the packet nearest to it such that the sum of the distances traveled by all the squirrels in reaching them is the minimum possible.

Your task is to find the optimal positions for all the food packets on the number line and return an integer value representing the minimum distance that needs to be traveled by the squirrels.

**Note:** You can place the packets anywhere on integer points of the number line, including at the positions of squirrels.

#### Input Specification
- **input1:** An integer value N denoting the number of squirrels ($1 \le N \le 100$).
- **input2:** An integer value K denoting the number of food packets ($1 \le K \le N$).
- **input3:** An integer array representing the position of N squirrels ($1 \le \text{input3}[i] \le 10^4$).

#### Output Specification
- Return an integer value representing the minimum distance that needs to be traveled by the squirrels.

#### Examples
**Example 1:**
- **input1:** 5
- **input2:** 2
- **input3:** `{2, 3, 5, 12, 19}`
- **Output:** 10
- **Explanation:** One of the optimal ways to choose the positions of food packets is 3 and 14 where the sum of the distances of all the squirrels is $|2-3| + |3-3| + |5-3| + |12-14| + |19-14| = 1 + 0 + 2 + 2 + 5 = 10$.

**Example 2:**
- **input1:** 6
- **input2:** 2
- **input3:** `{1, 2, 3, 4, 5, 100}`
- **Output:** 6
- **Explanation:** The food packets can be placed at indices 3 and 100. So, the sum of the distances will be $|1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |100-100| = 6$.

#### Solution
```python
def squirrelFood(N, K, positions):
    # Sort squirrel positions to ensure contiguous partitions
    positions.sort()
    
    # cost[i][j] stores the minimum cost of grouping squirrels from index i to j
    # around a single food packet.
    cost = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            median_idx = (i + j) // 2
            median_pos = positions[median_idx]
            cost[i][j] = sum(abs(positions[p] - median_pos) for p in range(i, j + 1))
            
    # dp[i][j] stores the min cost of placing j food packets for the first i squirrels
    dp = [[float('inf')] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for j in range(1, K + 1):
        for i in range(1, N + 1):
            for m in range(i):
                dp[i][j] = min(dp[i][j], dp[m][j-1] + cost[m][i-1])
                
    return dp[N][K]
```

---

### Q5. Tech Club
**Topic:** `Backtracking`, `N-Queens`

A group of students is planning to form a tech club and the club is open for recruitment. They are interviewing students and marking the skills level in Mathematics and Physics of the i-th student as $(M_i, P_i)$ respectively. They will be segregating the selected students into committees, and for better efficiency they have a few conditions:
- All the members of the committee should have different skill levels in Mathematics.
- All the members of the committee should have different skill levels in Physics.
- The difference in the skill level for Mathematics and Physics for two students should not be the same. $|M_1 - M_2|$ should not be equal to $|P_1 - P_2|$.

You are given an integer N, representing the size of a committee and an integer K, representing that $K \times K$ students are being interviewed. Your task is to return an integer value representing the number of ways in which the committees can be formed.

**Note:**
- The answer should be returned after performing the modulo operation with $10^4$.
- The skill level for $K \times K$ students ($K > 1$) will be $(0,0), (0,1) \dots (K-1, K-1)$ respectively.

#### Input Specification
- **input1:** An integer value N, representing the size of a committee.
- **input2:** An integer value K, representing that $K \times K$ students are being interviewed.

#### Output Specification
- Return an integer value representing the number of ways in which the committees can be formed.

#### Examples
**Example 1:**
- **input1:** 2
- **input2:** 3
- **Output:** 8
- **Explanation:** The number of students is $3 \times 3 = 9$ and committee size is 2. The 8 valid committees are:
  1. `{(0,0), (1,2)}`
  2. `{(0,0), (2,1)}`
  3. `{(0,1), (2,0)}`
  4. `{(0,1), (2,2)}`
  5. `{(0,2), (1,0)}`
  6. `{(0,2), (2,1)}`
  7. `{(1,0), (2,2)}`
  8. `{(1,2), (2,0)}`

**Example 2:**
- **input1:** 2
- **input2:** 2
- **Output:** 0

#### Solution
```python
def techClub(N, K):
    MOD = 10000
    ways = 0
    
    # Backtracking to place N queens on a K x K board
    def backtrack(row, queens_placed, cols_mask, diag1_mask, diag2_mask):
        nonlocal ways
        if queens_placed == N:
            ways = (ways + 1) % MOD
            return
        if row == K:
            return
        
        # Option 1: Skip the current row (do not place a queen here)
        if K - row >= N - queens_placed:
            backtrack(row + 1, queens_placed, cols_mask, diag1_mask, diag2_mask)
        
        # Option 2: Place a queen in the current row at column c
        for c in range(K):
            if not (cols_mask & (1 << c)):
                d1 = row - c + K
                d2 = row + c
                if not (diag1_mask & (1 << d1)) and not (diag2_mask & (1 << d2)):
                    backtrack(
                        row + 1,
                        queens_placed + 1,
                        cols_mask | (1 << c),
                        diag1_mask | (1 << d1),
                        diag2_mask | (1 << d2)
                    )
                    
    backtrack(0, 0, 0, 0, 0)
    return ways
```

---

### Q6. Employee of the Year
**Topic:** `Mathematics`, `Linear Algebra`, `GF(2) Vector Space`

Marie is a bank manager and has a team of N employees having ID numbers from 1 to N. Each employee has coins of different denominations M (1 to M). Marie is creating unique groups for the "Employee of the year" felicitation event. These groups can be formed subject to the following conditions:
1. The sum of all the coins of each denomination in the group is an even number.
2. Each unique group must have at least 1 member who is not common to any other group (i.e. groups must be distinct non-empty subsets of employees).

You are given a 2D integer array A, which represents the number of coins of each denomination for N employees. Your task is to help Marie find and return an integer value representing the number of possible unique groups.

**Note:**
- Each unique group must have at least one member.
- Each employee must have at least 1 coin.

#### Input Specification
- **input1:** An integer value N, representing the number of employees.
- **input2:** An integer value M, representing the number of different denominations.
- **input3:** A 2D integer array A of size N x M, representing the number of coins of each denomination for N employees.

#### Output Specification
- Return an integer value representing the number of possible unique groups.

#### Examples
**Example 1:**
- **input1:** 2
- **input2:** 2
- **input3:** `{{4, 4}, {6, 6}}`
- **Output:** 3
- **Explanation:** Employee 1 has 4 coins of both denominations, and employee 2 has 6 coins. The possible groups are:
  - `{Employee 1}`: coins sum is `{4, 4}` (both even)
  - `{Employee 2}`: coins sum is `{6, 6}` (both even)
  - `{Employee 1, Employee 2}`: coins sum is `{10, 10}` (both even)
  All 3 groups are valid.

#### Solution
```python
def employeeYear(N, M, A):
    # Represent the problem over GF(2)
    # We want to find the rank of the M x N matrix modulo 2
    matrix = [[A[i][j] % 2 for i in range(N)] for j in range(M)]
    
    rank = 0
    cols = N
    rows = M
    
    # Gaussian elimination to find the rank of the matrix in GF(2)
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        # Find pivot row
        pivot = -1
        for i in range(r, rows):
            if matrix[i][c] == 1:
                pivot = i
                break
        if pivot == -1:
            continue
        
        # Swap current row and pivot row
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        
        # Eliminate 1s in column c for other rows
        for i in range(rows):
            if i != r and matrix[i][c] == 1:
                for j in range(c, cols):
                    matrix[i][j] ^= matrix[r][j]
        r += 1
        rank += 1
        
    # The number of valid subsets is 2^(N - rank) - 1
    # We return this value modulo 10^9 + 7 since the result can be very large.
    MOD = 1000000007
    return (pow(2, N - rank, MOD) - 1 + MOD) % MOD
```

---

### Q7. Destroy All Monsters
**Topic:** `Dynamic Programming`, `Recursion with Memoization`

You are playing a video game in which there are N number of monsters present and each monster has a specific power which is stored in an integer array A. Now, your goal is to defeat all the monsters.

To successfully defeat all the monsters, certain guidelines must be followed:
Only two monsters can clash at the same time. After the clash, energy cost is equal to the greatest common divisor (GCD) of their powers. You can only clash monsters whose position is the start, middle or end of the array.

Your task is to find and return an integer value denoting the minimum total energy required to kill all the monsters.

**Note:** The length of N is always even, so always take the second middle monster.

#### Input Specification
- **input1:** An integer value N, denoting the total number of elements present in the array.
- **input2:** An integer Array A, denoting the power of each monster respectively.

#### Output Specification
- Return an integer value denoting the minimum total energy required to kill all the monsters.

#### Examples
**Example 1:**
- **input1:** 4
- **input2:** `{1, 2, 3, 4}`
- **Output:** 2
- **Explanation:**
  - Clash start (1) and end (4): cost = GCD(1, 4) = 1. Remaining array: `{2, 3}`.
  - Clash start (2) and end (3): cost = GCD(2, 3) = 1.
  - Total energy cost = 1 + 1 = 2.

**Example 2:**
- **input1:** 4
- **input2:** `{2, 4, 8, 6}`
- **Output:** 4
- **Explanation:**
  - Clash start (2) and middle (8): cost = GCD(2, 8) = 2. Remaining array: `{4, 6}`.
  - Clash start (4) and end (6): cost = GCD(4, 6) = 2.
  - Total energy cost = 2 + 2 = 4.

#### Solution
```python
import math

def destroyMonsters(N, A):
    memo = {}
    
    def solve(indices):
        if not indices:
            return 0
        if indices in memo:
            return memo[indices]
        
        m = len(indices)
        if m == 2:
            return math.gcd(A[indices[0]], A[indices[1]])
            
        start_idx = 0
        end_idx = m - 1
        mid_idx = m // 2  # Always the second middle monster (0-based index)
        
        # Choice 1: Clash Start and End
        cost1 = math.gcd(A[indices[start_idx]], A[indices[end_idx]]) + solve(indices[1:end_idx])
        
        # Choice 2: Clash Start and Middle
        rem2 = indices[1:mid_idx] + indices[mid_idx+1:]
        cost2 = math.gcd(A[indices[start_idx]], A[indices[mid_idx]]) + solve(rem2)
        
        # Choice 3: Clash Middle and End
        rem3 = indices[:mid_idx] + indices[mid_idx+1:end_idx]
        cost3 = math.gcd(A[indices[mid_idx]], A[indices[end_idx]]) + solve(rem3)
        
        res = min(cost1, cost2, cost3)
        memo[indices] = res
        return res

    return solve(tuple(range(N)))
```
