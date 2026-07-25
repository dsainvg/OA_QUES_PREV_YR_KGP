# Interview Questions
*Total questions: 5*

---

## Table of Contents
1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Digit Swap to Minimize Absolute Difference

**Topic:** `Greedy`, `String`, `Math`

#### Question
In this task you are given two strings of digits $S$ and $T$, both of length $N$. Your goal is to make those numbers as close to one another as possible (i.e., minimize the absolute value of their difference). You can swap some of the corresponding digits (e.g., the $i$-th digit of the first number with the $i$-th digit of the second number). Swapping digits is a tiring task, so you want to make as few swaps as possible.

Write a function:
```python
def solution(S: str, T: str) -> int:
```
that, given two strings $S$ and $T$, both of length $N$, returns the minimum number of swaps needed to minimize the difference between the two numbers represented by the input strings.

#### Assumptions
- Lengths of $S$ and $T$ are equal and within the range $[1..100,000]$.
- $S$ and $T$ consist only of digits and no other characters.
- Neither $S$ nor $T$ contains leading zeroes.

#### Examples
1. Given $S = \text{"29162"}$ and $T = \text{"10524"}$, the function should return `2`.
   - We can swap the second and fourth digits and obtain $S = \text{"20122"}$ and $T = \text{"19564"}$.
   - The absolute difference between the numbers is $558$, which is the smallest possible.
   - The number of swaps is $2$.
   - Note that we could obtain the same difference by swapping the first, third, and fifth digits, but that solution requires $3$ swaps.

#### Solution
The algorithm runs in $O(N)$ time and $O(1)$ space.
```python
def solution(S: str, T: str) -> int:
    n = len(S)
    first_diff = -1
    for i in range(n):
        if S[i] != T[i]:
            first_diff = i
            break
            
    # If the strings are already identical, no swaps are needed.
    if first_diff == -1:
        return 0
        
    diff_count = 0
    case_a_swaps = 0
    
    # Case A: S becomes larger at the first difference index.
    # At first_diff: S[first_diff] should be max(S[first_diff], T[first_diff])
    # So we swap if S[first_diff] < T[first_diff]
    if S[first_diff] < T[first_diff]:
        case_a_swaps += 1
    diff_count += 1
    
    # For subsequent indices k > first_diff:
    # S[k] should be min(S[k], T[k]) to minimize the difference S - T.
    # So we swap if S[k] > T[k].
    for k in range(first_diff + 1, n):
        if S[k] != T[k]:
            diff_count += 1
            if S[k] > T[k]:
                case_a_swaps += 1
                
    # Case B is the complement where T becomes larger at first_diff.
    # The swaps required for Case B is simply (diff_count - case_a_swaps).
    return min(case_a_swaps, diff_count - case_a_swaps)
```

---

### Q2. Strongest Poker Hand (Card Set Detection)

**Topic:** `Implementation`, `Sorting`, `Hash Table`

#### Question
You are given $N$ cards. Each card consists of a suit and a rank. There are four suits: `S` (Spades), `H` (Hearts), `D` (Diamonds), and `C` (Clubs), and thirteen ranks, ordered from lowest to highest: `2, 3, 4, 5, 6, 7, 8, 9, 10, J` (Jack), `Q` (Queen), `K` (King), and `A` (Ace).

Each card is represented by a string in the format `"<rank><suit>"`. For example, $10$ of Spades is described as `"10S"`, and Queen of Hearts as `"QH"`.

There are six ranked card sets, ordered by their strength from weakest to strongest:
1. **single card**
   - **Description**: A single card of the highest rank; the suit does not matter.
   - **Example**: for `cards = ["2H", "4H", "7C", "9D", "10D", "KS"]`, returns `{ "set_name": "single card", "selected_cards": ["KS"] }`.
2. **pair**
   - **Description**: Two cards sharing the same rank; suits do not matter. If there are multiple pairs, return one with the highest rank.
   - **Example**: for `cards = ["AS", "10H", "8H", "10S", "8D"]`, returns `{ "set_name": "pair", "selected_cards": ["10H", "10S"] }`.
3. **triple**
   - **Description**: Three cards sharing the same rank; suits do not matter. If there are multiple triples, return one with the highest rank.
   - **Example**: for `cards = ["AS", "JS", "AH", "AD", "10D", "AC"]`, returns `{ "set_name": "triple", "selected_cards": ["AH", "AD", "AC"] }`.
4. **five in a row**
   - **Description**: Five cards of consecutive ranks starting with the highest possible rank; suits do not matter. If there are multiple ways to choose five such cards, return any.
   - **Example**: for `cards = ["6H", "7S", "8S", "9S", "10S", "JD", "JC", "KC", "AC"]`, returns `{ "set_name": "five in a row", "selected_cards": ["7S", "8S", "9S", "10S", "JC"] }`.
5. **suit**
   - **Description**: Five cards sharing the same suit; the ranks do not matter. If there are multiple ways to choose five cards with the same suit, choose any set with the highest suit. The order of the suits (from highest to lowest) is `S, H, D, C`.
   - **Example**: for `cards = ["2D", "4D", "6D", "8D", "9D", "AC", "KC", "QC", "JC", "7C"]`, returns `{ "set_name": "suit", "selected_cards": ["2D", "4D", "6D", "8D", "9D"] }`.
6. **a triple and a pair**
   - **Description**: Five cards, consisting of a triple (three cards of the same rank) and a pair (two cards of the same rank). If there are multiple ways to choose this set, choose one with the highest rank of the triple, then one with the highest rank of the pair. The suits do not matter.
   - **Example**: for `cards = ["10D", "10H", "10C", "2S", "2H", "2D", "JH", "JC"]`, returns `{ "set_name": "a triple and a pair", "selected_cards": ["10D", "10H", "10C", "JH", "JC"] }`.

Write a function:
```python
def solution(cards: list[str]) -> dict:
```
that, given an array of strings `cards`, returns a dictionary representing the strongest card set that can be formed.

#### Assumptions
- $N$ is an integer within the range $[1..10]$.
- The elements of `cards` are all distinct.
- Each string in array `cards` is a correct representation of a card in `"<rank><suit>"` format.
- Focus is on correctness; performance is not the focus.

#### Solution
```python
import collections

RANK_MAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
SUIT_ORDER = {'S': 4, 'H': 3, 'D': 2, 'C': 1}

def check_triple_and_pair(cards):
    by_rank = collections.defaultdict(list)
    for c in cards:
        r = c[:-1]
        by_rank[r].append(c)
        
    best_r = -1
    best_p = -1
    best_cards = []
    
    for r in by_rank:
        if len(by_rank[r]) >= 3:
            for p in by_rank:
                if p != r and len(by_rank[p]) >= 2:
                    if (RANK_MAP[r], RANK_MAP[p]) > (best_r, best_p):
                        best_r = RANK_MAP[r]
                        best_p = RANK_MAP[p]
                        best_cards = by_rank[r][:3] + by_rank[p][:2]
                        
    if best_r != -1:
        return "a triple and a pair", best_cards
    return None

def check_suit(cards):
    by_suit = collections.defaultdict(list)
    for c in cards:
        s = c[-1]
        by_suit[s].append(c)
        
    for s in ['S', 'H', 'D', 'C']:
        if len(by_suit[s]) >= 5:
            return "suit", by_suit[s][:5]
    return None

def check_five_in_a_row(cards):
    by_rank = collections.defaultdict(list)
    for c in cards:
        r = c[:-1]
        by_rank[RANK_MAP[r]].append(c)
        
    for v in range(14, 5, -1):
        if all(val in by_rank for val in range(v, v-5, -1)):
            selected = [by_rank[val][0] for val in range(v, v-5, -1)]
            return "five in a row", selected
    return None

def check_triple(cards):
    by_rank = collections.defaultdict(list)
    for c in cards:
        r = c[:-1]
        by_rank[r].append(c)
        
    best_rank_val = -1
    best_cards = []
    for r in by_rank:
        if len(by_rank[r]) >= 3:
            if RANK_MAP[r] > best_rank_val:
                best_rank_val = RANK_MAP[r]
                best_cards = by_rank[r][:3]
                
    if best_rank_val != -1:
        return "triple", best_cards
    return None

def check_pair(cards):
    by_rank = collections.defaultdict(list)
    for c in cards:
        r = c[:-1]
        by_rank[r].append(c)
        
    best_rank_val = -1
    best_cards = []
    for r in by_rank:
        if len(by_rank[r]) >= 2:
            if RANK_MAP[r] > best_rank_val:
                best_rank_val = RANK_MAP[r]
                best_cards = by_rank[r][:2]
                
    if best_rank_val != -1:
        return "pair", best_cards
    return None

def check_single_card(cards):
    best_card = max(cards, key=lambda c: RANK_MAP[c[:-1]])
    return "single card", [best_card]

def solution(cards: list[str]) -> dict:
    res = check_triple_and_pair(cards)
    if res: return {"set_name": res[0], "selected_cards": res[1]}
    
    res = check_suit(cards)
    if res: return {"set_name": res[0], "selected_cards": res[1]}
    
    res = check_five_in_a_row(cards)
    if res: return {"set_name": res[0], "selected_cards": res[1]}
    
    res = check_triple(cards)
    if res: return {"set_name": res[0], "selected_cards": res[1]}
    
    res = check_pair(cards)
    if res: return {"set_name": res[0], "selected_cards": res[1]}
    
    res = check_single_card(cards)
    return {"set_name": res[0], "selected_cards": res[1]}
```

---

### Q3. Reorder Routes to Make All Paths Lead to City Zero

**Topic:** `Graph`, `DFS/BFS`, `Tree`

#### Question
There is a network with $N$ roads and $N + 1$ cities. The cities are labeled with distinct integers within the range $[0..N]$. Roads connect the cities in such a way that there is exactly one way to travel between any two of the cities. In other words, the network forms a tree.

The roads in the network are too narrow to accommodate two cars. For this reason, every road (that connects cities A and B) is oriented in one of two possible ways: either from A to B, or from B to A.

A big hospital was recently founded in the city labeled 0. For that reason, the citizens have decided to rearrange the orientation of the roads so that everyone can get to the hospital as quickly as possible. This means that the trip from every city to the 0th city should not go through any road that faces against the current direction of travel. In order to minimize the cost of this operation, they would like to reorient as few roads as possible.

Write a function:
```python
def solution(A: list[int], B: list[int], N: int) -> int:
```
that, given the description of the network as two arrays $A$, $B$ of $N$ integers each, returns the minimum number of roads that must be reoriented in order to make everyone's trip to the hospital as fast as possible. Arrays $A$ and $B$ describe the network in the following way: for each $K$ in the range $[0..N-1]$, there is a road between cities labeled $A[K]$ and $B[K]$ that is oriented from $A[K]$ to $B[K]$.

#### Assumptions
- $N$ is an integer within the range $[1..100,000]$.
- Elements of $A$ and $B$ are integers within the range $[0..N]$.

#### Examples
1. Given $A = [0, 1, 3]$, $B = [1, 2, 4]$, $N = 3$, the function should return `2`.
   - Node 0 is connected to 1 ($0 \to 1$), 1 is connected to 2 ($1 \to 2$), 3 is connected to 4 ($3 \to 4$).
   - Reordering routes so that everything points to 0.

#### Solution
The algorithm runs in $O(N)$ time and $O(N)$ space.
```python
from collections import deque

def solution(A: list[int], B: list[int], N: int) -> int:
    adj = [[] for _ in range(N + 1)]
    for i in range(N):
        u = A[i]
        v = B[i]
        adj[u].append((v, 1)) # Original directed edge: u -> v (1 means needs reversal if going away from 0)
        adj[v].append((u, 0)) # Incoming edge: v -> u (0 means already points towards 0)
        
    visited = [False] * (N + 1)
    queue = deque([0])
    visited[0] = True
    reorder_count = 0
    
    while queue:
        u = queue.popleft()
        for v, is_original in adj[u]:
            if not visited[v]:
                visited[v] = True
                reorder_count += is_original
                queue.append(v)
                
    return reorder_count
```

---

### Q4. Longest Matching Red-Green Tile Sequence

**Topic:** `Graph`, `Greedy`, `Eulerian Trail`

#### Question
There are $N$ tiles (numbered from $0$ to $N-1$). Each tile is made of two squares that are colored either red (represented by the letter `"R"`) or green (represented by `"G"`). A tile is described by a two-character string representing the respective colors of the left and right squares. The tiles cannot be rotated (which means that `"RG"` and `"GR"` tiles are different). Two tiles can be placed next to each other if the color of their adjacent squares is the same.

What is the length of the longest possible sequence that can be created using the provided tiles?

Write a function:
```python
def solution(A: list[str]) -> int:
```
that, given an array $A$ of $N$ strings representing the tiles, returns the maximum number of tiles that can be arranged in a sequence.

#### Assumptions
- $N$ is an integer within the range $[1..100,000]$.
- Each string in array $A$ is one of the following: `"RR"`, `"RG"`, `"GR"`, `"GG"`.

#### Examples
1. Given $A = [\text{"RR"}, \text{"GR"}, \text{"RG"}, \text{"GR"}, \text{"GR"}, \text{"RR"}]$, the function should return `5`.
   - We can select tiles 0, 2, 3, 4, 5 and arrange them into the sequence `GR - RR - RG - GR - RR`.
2. Given $A = [\text{"GG"}, \text{"GG"}, \text{"RR"}, \text{"GG"}, \text{"RR"}]$, the function should return `3`.
   - We can select tiles 0, 1, 3 and arrange them into the sequence `GG - GG - GG`.
3. Given $A = [\text{"RG"}, \text{"GR"}, \text{"RG"}, \text{"GR"}]$, the function should return `4`.
   - All tiles can be used without reordering them (`RG - GR - RG - GR`).
4. Given $A = [\text{"RG"}, \text{"RG"}, \text{"RG"}]$, the function should return `1`.

#### Solution
The algorithm runs in $O(N)$ time and $O(1)$ space.
```python
def solution(A: list[str]) -> int:
    counts = {"RR": 0, "GG": 0, "RG": 0, "GR": 0}
    for tile in A:
        if tile in counts:
            counts[tile] += 1
            
    n_rr = counts["RR"]
    n_gg = counts["GG"]
    a = counts["RG"]
    b = counts["GR"]
    
    ans = 0
    # Option 1: No transition edges (only loops at one color)
    ans = max(ans, n_rr)
    ans = max(ans, n_gg)
    
    # Option 2: Transition starting and ending at the same color (e.g. R -> G -> R -> G -> ... -> R)
    # Using k edges of RG and k edges of GR. If k >= 1, we visit both R and G,
    # so we can use all loops: n_rr + n_gg + 2*k.
    k = min(a, b)
    if k >= 1:
        ans = max(ans, n_rr + n_gg + 2 * k)
        
    # Option 3: Transition starting at R, ending at G (so x = y + 1)
    # x = k edges of RG, y = k - 1 edges of GR, where k <= min(a, b + 1).
    k = min(a, b + 1)
    if k >= 1:
        ans = max(ans, n_rr + n_gg + 2 * k - 1)
        
    # Option 4: Transition starting at G, ending at R (so y = x + 1)
    # y = k edges of GR, x = k - 1 edges of RG, where k <= min(a + 1, b).
    k = min(a + 1, b)
    if k >= 1:
        ans = max(ans, n_rr + n_gg + 2 * k - 1)
        
    return ans
```

---

### Q5. Shortest Non-Intersecting Path Back Home

**Topic:** `Geometry`, `Greedy`, `Pathfinding`

#### Question
You want to visit your friend, who lives abroad. It is time to plan the whole journey, both there and back. The trip will be long, so you would like to make it interesting. You do not want to revisit the same places or go along the same paths twice. Also, you do not want to head back from any point.

You will represent your planned path by a string containing four letters: `'N'` for north, `'S'` for south, `'E'` for east and `'W'` for west. For example, a path going north, east, east, north, west, south would be notated as `"NEENWS"`.

You have already made a plan of the outward part of your journey. How will you plan the shortest path back home, fulfilling the criteria described above?

Write a function:
```python
def solution(forth: str) -> str:
```
that, given a string `forth` of length $N$, which denotes the path leading to your friend, returns one of the shortest possible paths back home that fulfills the conditions. You can assume that you are heading north at both the beginning and the end of the first part of your journey (the first and the last element in `forth` are equal to `'N'`). Moreover, `forth` does not contain any occurrence of the letter `'S'`.

#### Assumptions
- $N$ is within range $[2..100,000]$.
- First and last characters of `forth` are `'N'`.
- `forth` does not contain `'S'`.

#### Examples
1. Given `forth = "NEENWN"`, the function may return `"WWSSSE"` (or `"WSWSSE"`).
2. Given `forth = "NWNENWNEN"`, the function may return `"ESSSSSW"`.
3. Given `forth = "NENENWWWWN"`, the function may return `"WSSSSEEE"`.

#### Solution
The algorithm runs in $O(N)$ time and $O(1)$ space.
```python
def solution(forth: str) -> str:
    x, y = 0, 0
    x_min, x_max = 0, 0
    for char in forth:
        if char == 'N':
            y += 1
        elif char == 'E':
            x += 1
        elif char == 'W':
            x -= 1
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        
    x_end, y_end = x, y
    
    # Left path: W * (x_end - x_min + 1) + S * y_end + E * (1 - x_min)
    left_w = x_end - x_min + 1
    left_s = y_end
    left_e = 1 - x_min
    left_len = left_w + left_s + left_e
    
    # Right path: E * (x_max + 1 - x_end) + S * y_end + W * (x_max + 1)
    right_e = x_max + 1 - x_end
    right_s = y_end
    right_w = x_max + 1
    right_len = right_e + right_s + right_w
    
    if left_len < right_len:
        return 'W' * left_w + 'S' * left_s + 'E' * left_e
    else:
        return 'E' * right_e + 'S' * right_s + 'W' * right_w
```

---
