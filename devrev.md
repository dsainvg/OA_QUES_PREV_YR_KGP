# Interview Questions

*Total questions: 6*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Wall Mural (Largest Rectangle in Histogram)

**Topic:** `arrays`, `stack`, `monotonic-stack`

Imagine a wall made of `n` vertical stone slabs placed side by side. Each slab has a width of 1 unit, but their heights are different.
You want to paint the largest possible rectangular mural (artwork) on this wall. What is the maximum area of the mural that can be painted on the slabs?

#### Example
**Input:**
```
8
4 1 5 3 3 2 4 1
```

**Output:**
```
10
```

#### Constraints
- `1 <= n <= 2 * 10^5`
- `1 <= heights[i] <= 10^9`
- Execution time limit: 4.0 seconds (Python) / 0.5 seconds (C++)
- Memory limit: 1 GB

```python
def solution(n: int, heights: list) -> int:
    """
    Finds the maximum area of a rectangular mural that can be painted on the stone slabs.
    Time Complexity: O(n) using a monotonic stack.
    Space Complexity: O(n)
    """
    stack = []
    max_area = 0
    # Append a height of 0 to flush all remaining elements in the stack at the end
    extended_heights = heights + [0]
    
    for i in range(len(extended_heights)):
        while stack and extended_heights[stack[-1]] >= extended_heights[i]:
            h = extended_heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
        
    return max_area
```

---

### Q2. Smallest Golden Elements Sub-chain (Minimum Window Subarray)

**Topic:** `two-pointers`, `sliding-window`, `hash-table`

As space explorers, we research different soil samples and extract chains of elements from them. There is a specific set of elements known as **Golden Elements**.

Write a function that finds the smallest contiguous sub-chain that includes all the golden elements. If no such sub-chain exists containing all the golden elements, return an empty sub-chain.

#### Example
- `chain = ["O", "C", "Ra", "Li", "Na"]`
- `elements = ["Li", "C"]`

**Output:**
`["C", "Ra", "Li"]`

#### Constraints
- `0 < chain.length < 10^6`
- `0 < elements.length < 10^3`
- Elements in the `elements` array will be unique.
- Execution time limit: 4.0 seconds (Python) / 1.0 seconds (C++)

```python
from collections import Counter

def solution(chain: list, elements: list) -> list:
    """
    Finds the smallest contiguous sub-chain containing all unique golden elements.
    Time Complexity: O(N + M) where N is chain length and M is elements length.
    Space Complexity: O(M) for counts tracking.
    """
    target_counts = Counter(elements)
    required = len(target_counts)
    
    window_counts = {}
    formed = 0
    
    l, r = 0, 0
    min_len = float('inf')
    best_range = (None, None)
    
    while r < len(chain):
        elem = chain[r]
        if elem in target_counts:
            window_counts[elem] = window_counts.get(elem, 0) + 1
            if window_counts[elem] == target_counts[elem]:
                formed += 1
                
        # Try to contract the window from the left
        while l <= r and formed == required:
            elem_l = chain[l]
            if r - l + 1 < min_len:
                min_len = r - l + 1
                best_range = (l, r)
                
            if elem_l in target_counts:
                window_counts[elem_l] -= 1
                if window_counts[elem_l] < target_counts[elem_l]:
                    formed -= 1
            l += 1
            
        r += 1
        
    if min_len == float('inf'):
        return []
    return chain[best_range[0]:best_range[1] + 1]
```

---

### Q3. Rhombic Cipher

**Topic:** `matrix`, `simulation`

Rhombic Cipher is an ingenious cipher that is used to encrypt rectangular tables of characters of size `2n x n`. The encryption process can be described as follows:

1. First create a rhombus out of the table's rows considering them one by one from top to bottom:
   - each row is written diagonally and goes from bottom to top and from left to right;
   - the $i$-th row begins at the $(i \text{ div } 2)$-th line of the rhombus, counting from bottom to top (where `div` means integer division);
   - each symbol of the row is written to the left of the symbols already present at that rhombus line.
2. Then the diagonals of the rhombus that go from bottom to top and from right to left are written down, which produces a new `2n x n` table.

Your task is to encrypt the given table with the Rhombic Cipher.

#### Example
**Input:**
```python
table = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r']
]
```

**Output:**
```python
[
    ['d', 'j', 'p'],
    ['a', 'g', 'm'],
    ['e', 'k', 'q'],
    ['b', 'h', 'n'],
    ['f', 'l', 'r'],
    ['c', 'i', 'o']
]
```

#### Constraints
- `0 <= table.length <= 20`
- `1 <= table[0].length <= 10`
- Execution time limit: 0.5 seconds (C++)

```python
def solution(table: list) -> list:
    """
    Encrypts a 2n x n matrix using the Rhombic Cipher.
    
    Mathematical simplification reveals that row pair (2k, 2k+1) maps directly 
    to column k in the output table, interleaved such that:
      output[2j][k]   = table[2k+1][j]
      output[2j+1][k] = table[2k][j]
    
    Time Complexity: O(H * W)
    Space Complexity: O(H * W)
    """
    if not table or not table[0]:
        return []
    
    h = len(table)
    w = len(table[0])
    n = h // 2
    
    out = [[''] * w for _ in range(h)]
    for k in range(n):
        row_even = table[2 * k]
        row_odd = table[2 * k + 1]
        for j in range(w):
            out[2 * j][k] = row_odd[j]
            out[2 * j + 1][k] = row_even[j]
            
    return out
```

---

### Q4. Blocks Grid (Min and Max Moves to Fill Column 0)

**Topic:** `matrix`, `search`, `breadth-first-search`, `depth-first-search`, `dynamic-programming`

You are given a rectangular board divided into a uniform grid (square cells). Some cells of the board are occupied with blocks (denoted by `#`), and others are empty (denoted by `.`). You are trying to add more and more blocks to the board, and your task is to fill the first column with them.

You can add a block to the field in the following way:
1. You choose a row index `r` where the leftmost cell is empty (`grid[r][0] == '.'`).
2. You throw the new block into the chosen row from the left.
3. The block appears in the leftmost cell of the row and starts moving to the right, until it reaches another block or the end of the row.
4. When that happens, the block starts falling down until it reaches another block or the last row.

Calculate the minimum and the maximum number of moves required to fill the first column of the board with blocks.

#### Example 1
**Input:**
```python
field = [
    ['.', '#', '#'],
    ['#', '.', '.'],
    ['.', '.', '.']
]
```

**Output:**
`[4, 4]` (We choose the first row once and the third row three times).

#### Example 2
**Input:**
```python
field = [
    ['.', '#', '#'],
    ['.', '.', '#'],
    ['.', '.', '.']
]
```

**Output:**
`[3, 6]`

#### Constraints
- `1 <= field.length <= 12`
- `1 <= field[0].length <= 12`
- It is guaranteed that the maximum number of moves doesn't exceed 12.
- Execution time limit: 0.5 seconds (C++)

```python
def solution(field: list) -> list:
    """
    Computes the minimum and maximum moves to fill the first column of the board.
    Uses DFS with memoization. The maximum depth of recursion is bounded by 12.
    
    Time Complexity: O(H * (H * W) * S) where S is the number of reachable board states.
    Space Complexity: O(S * H * W) for memoization storage.
    """
    H = len(field)
    W = len(field[0])
    
    # Represent grid as a tuple of strings for hashing/memoization
    initial_state = tuple("".join(row) for row in field)
    memo = {}
    
    def get_goal(state):
        return all(state[r][0] == '#' for r in range(H))
        
    def dfs(state):
        if get_goal(state):
            return 0, 0
        if state in memo:
            return memo[state]
            
        min_moves = float('inf')
        max_moves = float('-inf')
        
        # Try choosing each row r
        for r in range(H):
            # A block can only be thrown if the starting cell in row r is empty
            if state[r][0] == '.':
                # Find the first column c that has a block '#' in row r
                c = 0
                while c < W and state[r][c] == '.':
                    c += 1
                dest_c = c - 1  # stops right before the block or at the right boundary
                
                # Fall down column dest_c starting from row r
                dest_r = r
                while dest_r + 1 < H and state[dest_r + 1][dest_c] == '.':
                    dest_r += 1
                    
                # Build the next state
                next_state_list = list(state)
                row_str = next_state_list[dest_r]
                next_state_list[dest_r] = row_str[:dest_c] + '#' + row_str[dest_c+1:]
                next_state = tuple(next_state_list)
                
                mn, mx = dfs(next_state)
                min_moves = min(min_moves, 1 + mn)
                max_moves = max(max_moves, 1 + mx)
                
        memo[state] = (min_moves, max_moves)
        return min_moves, max_moves

    min_res, max_res = dfs(initial_state)
    return [min_res, max_res]
```

---

### Q5. Sports Tournament (Maximum Exercise Gap / Binary Search on Answer)

**Topic:** `binary-search`, `greedy`, `prefix-sums`

In preparation for a sports tournament, you have `n` training exercises available. Completing the $i$-th exercise improves your skills by `arr[i]` points. You can only perform one exercise per day, and once you complete an exercise, you must wait `k` days before repeating it.

Given two targets: achieve at least `c` skill points within `d` days. Determine the maximum `k` that allows you to meet this goal. If no such `k` exists or `k` is arbitrarily large, output `-1`.

#### Example
**Input:**
```
2 5 4
1 2
```
(where $n=2, c=5, d=4$ and $arr = [1, 2]$)

**Output:**
`2` (One schedule is: Day 1 do ex 2, Day 2 do ex 1, Day 3 do nothing, Day 4 do ex 2. Points = 2 + 1 + 2 = 5).

#### Constraints
- `2 <= n <= 2 * 10^5`
- `1 <= c <= 10^16`
- `1 <= d <= 2 * 10^5`
- `1 <= arr[i] <= 10^9`
- Execution time limit: 0.5 seconds (C++) / 4.0 seconds (Python)

```python
def solution(n: int, c: int, d: int, arr: list) -> int:
    """
    Finds the maximum k days we can wait between repeating the same exercise.
    Uses binary search on the answer k.
    
    Time Complexity: O(N log N) for sorting, plus O(log d) for binary search.
    Space Complexity: O(N) for prefix sums.
    """
    # Sort exercise values descending
    arr.sort(reverse=True)
    
    # Precompute prefix sums for O(1) query range sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
        
    # Check if k can be arbitrarily large (i.e. each exercise used <= 1 time is sufficient)
    top_single_sum = prefix[min(n, d)]
    if top_single_sum >= c:
        return -1
        
    # Check if k = 0 is possible
    if arr[0] * d < c:
        return -1
        
    def possible(k: int) -> bool:
        limit = min(n, k + 1)
        q = d // (k + 1)
        r = d % (k + 1)
        
        num_q_plus_1 = min(limit, r)
        num_q = max(0, limit - r)
        
        s1 = prefix[num_q_plus_1]
        s2 = prefix[num_q_plus_1 + num_q] - s1
        total = s1 * (q + 1) + s2 * q
        return total >= c

    # Binary search k in [0, d - 1]
    low = 0
    high = d - 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if possible(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
```

---

### Q6. Rod Cutting (Serling Enterprises)

**Topic:** `dynamic-programming`

Serling Enterprises buys long steel rods and cuts them into shorter rods, which it then sells. Each cut is free. Given a rod of length `n` and an array of prices `v`, where `v[i]` stands for the price of a piece with a length of `i`, determine the maximum revenue that you can obtain by cutting up the rod and selling the pieces.

#### Example
- `n = 4`
- `v = [0, 2, 4, 7, 7]`

**Output:**
`9` (Cut into length 1 and length 3: revenue = 2 + 7 = 9).

#### Constraints
- Length of price array `v` is `n + 1`.
- `n <= 1000`

```python
def solution(n: int, v: list) -> int:
    """
    Solves the Rod Cutting problem to maximize revenue.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            if j < len(v):
                max_val = max(max_val, v[j] + dp[i - j])
        dp[i] = max_val
        
    return dp[n]
```
