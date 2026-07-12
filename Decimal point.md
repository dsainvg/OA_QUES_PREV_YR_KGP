# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Bob's Payment

**Topic:** `math`, `greedy`, `implementation`  

Bob needs to pay a certain amount of money, denoted by an integer $N$. However, Bob dislikes certain digits. He wants to find the minimum amount of money $X$ ($X \ge N$) that he needs to pay such that $X$ does not contain any of the digits Bob dislikes.

#### Input Format:
- The first line contains two integers $N$ and $k$ denoting the amount that Bob needs to pay and the number of digits that Bob dislikes, respectively.
- The next line contains $k$ space-separated integers denoting the digits that Bob dislikes.

#### Output Format:
- Print a single integer denoting the minimum amount of money that Bob needs to pay.

#### Constraints:
- $1 \le N < 10000$
- $0 \le k < 10$
- $0 \le d_1 < d_2 < d_3 < \dots < d_k < 10$
- $(d_1, d_2, \dots, d_k) \neq (1, 2, 3, 4, 5, 6, 7, 8, 9)$

#### Sample Input:
```
100 2
0 1
```

#### Sample Output:
```
222
```

#### Explanation:
Given $N = 100$, $k = 2$, and dislike_digits = `[0, 1]`.
Here Bob has to pay an amount greater than or equal to 100 by not using the digits `[0, 1]` that he dislikes.
222 is the minimum number that can be formed that doesn't contain `[0, 1]`.

```python
import sys

def main():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    k = int(input_data[1])
    dislikes = [int(x) for x in input_data[2:2+k]]
    
    # Store disliked digits as strings for fast checking
    dislike_set = set(str(d) for d in dislikes)
    
    # Find the smallest number >= N with no disliked digits
    curr = N
    while True:
        if not any(char in dislike_set for char in str(curr)):
            print(curr)
            return
        curr += 1

if __name__ == '__main__':
    main()
```

---

### Q2. Double XOR Pairs

**Topic:** `bit-manipulation`, `math`  

Given a positive integer $N$. Find all pairs of integers $(x, y)$ such that:
- $1 \le x, y \le N$
- $x + y = N$
- $x + y = 2 \cdot (x \oplus y)$, where $\oplus$ denotes the bitwise XOR operator.

Print all valid pairs $(x, y)$ in increasing order of $x$. If there are no such pairs, print a single line containing `-1 -1`.

#### Input Format:
- The first line contains $T$, which represents the number of test cases.
- For each testcase, the first line consists of a single integer $N$ denoting the value of $N$.

#### Output Format:
- For each testcase, print all valid pairs $(x, y)$ on a new line in increasing order of $x$. If there are no such pairs, print a single line containing `-1 -1`.

#### Constraints:
- $1 \le T \le 50$
- $1 \le N \le 10^9$

#### Sample Input:
```
3
4
7
144
```

#### Sample Output:
```
1 3
3 1
-1 -1
36 108
44 100
100 44
108 36
```

#### Explanation:
- **For $N = 4$:**
  $x + y = 4$, $x \oplus y = 2$.
  The only valid pairs are $(1, 3)$ and $(3, 1)$ since:
  $1 + 3 = 4$ and $2 \cdot (1 \oplus 3) = 2 \cdot 2 = 4$.
  $3 + 1 = 4$ and $2 \cdot (3 \oplus 1) = 2 \cdot 2 = 4$.
  Thus, we print:
  `1 3`
  `3 1`

- **For $N = 7$:**
  No valid pairs satisfy the conditions, so we print `-1 -1`.

- **For $N = 144$:**
  There are 4 pairs satisfying the conditions:
  $(36, 108), (44, 100), (100, 44), (108, 36)$.

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    out = []
    
    for t in range(1, T + 1):
        N = int(input_data[t])
        
        # Check divisibility by 4.
        # Since x + y = 2*(x ^ y) and x + y = (x ^ y) + 2*(x & y)
        # we have x ^ y = 2*(x & y), so N = 4*(x & y).
        # Thus, N must be a multiple of 4.
        if N % 4 != 0:
            out.append("-1 -1")
            continue
            
        A = N // 4
        two_A = N // 2
        
        # If A and two_A share set bits, no solution exists.
        if (A & two_A) != 0:
            out.append("-1 -1")
            continue
            
        # Extract set bits of two_A (which is the mask for x ^ y)
        bits = []
        for i in range(30):
            if (two_A & (1 << i)):
                bits.append(1 << i)
                
        # Generate all submasks of two_A in strictly increasing order
        submasks = [0]
        for b in bits:
            submasks.extend([s + b for s in submasks])
            
        # For each submask S, construct the pair (x, y)
        for S in submasks:
            x = A + S
            y = A + (two_A - S)
            out.append(f"{x} {y}")
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()
```

---
