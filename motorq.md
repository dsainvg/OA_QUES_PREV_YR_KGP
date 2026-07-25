*Total questions: 1*

---

## Table of Contents
- [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Secret Recipe

**Topic:** `math`, `prefix-sums`  

There is a secret recipe with ingredients $I_1, I_2, \ldots, I_N$. We do not know the quantities of each ingredient, but we have another sequence $M_1, M_2, \ldots, M_{N-1}$ such that $M_j = I_j + I_{j+1}$ for each valid $j$. You should process $Q$ queries. In each query, you are given two indices $u$ and $v$; your task is to compute $I_u + I_v$ or determine that there is not enough information to uniquely determine this sum.

**Input**
* The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
* The first line of each test case contains two space-separated integers $N$ and $Q$.
* The second line contains $N-1$ space-separated integers $M_1, M_2, \ldots, M_{N-1}$.
* Each of the following $Q$ lines contains two space-separated integers $u$ and $v$ describing a query.

**Output**
For each query, if it is impossible to determine the required sum, print a single line containing the string `-1`. Otherwise, print a single line containing one integer — the required sum.

**Constraints**
* $1 \le T \le 100$
* $2 \le N \le 10^5$
* $1 \le Q \le 10^5$
* $1 \le u, v \le N$
* $1 \le M_i \le 10^9$ for each valid $i$
* The sum of $N$ over all test cases does not exceed $5 \cdot 10^5$
* The sum of $Q$ over all test cases does not exceed $5 \cdot 10^5$

**Sample Input**
```
1
4 3
1 2 3
1 2
1 3
1 4
```

**Sample Output**
```
1
-1
2
```

```python
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    T = int(input_data[idx])
    idx += 1
    
    out = []
    for _ in range(T):
        N = int(input_data[idx])
        Q = int(input_data[idx+1])
        idx += 2
        
        M = []
        for _ in range(N - 1):
            M.append(int(input_data[idx]))
            idx += 1
            
        # Compute the A array
        # A[1] = 0
        # A[k] = M[k-2] - A[k-1] for k in [2, N]
        A = [0] * (N + 1)
        for k in range(2, N + 1):
            A[k] = M[k - 2] - A[k - 1]
            
        for _ in range(Q):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            
            # If parities of u and v are different, the sum is determinable
            if (u % 2) != (v % 2):
                out.append(str(A[u] + A[v]))
            else:
                out.append("-1")
                
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
```
