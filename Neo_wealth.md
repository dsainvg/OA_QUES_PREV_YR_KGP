# Interview Questions

*Total questions: 1*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Log Analysis 2 (Count Zero Request Servers)
**Topic:** `Sliding Window`, `Two Pointers`, `Sorting` `[Latest]`

#### Description
Analyze logs of requests processed by $n$ servers. The servers are indexed from $1$ to $n$.
The logs are provided as a 2D array `log_data` where each entry `log_data[i] = [server_id, time]` indicates that a request was served by the server with ID `server_id` at `time`.

Given `log_data`, an integer $x$, and $q$ queries, determine for each query the number of servers that did not receive any request in the time interval $[query[i] - x, query[i]]$.

#### Input Format
- The first line contains $n$, the number of servers.
- The second line contains $m$, the number of logs.
- The third line contains the column count of logs (always $2$).
- The next $m$ lines each contain two space-separated integers: `server_id` and `time`.
- The next line contains $q$, the number of queries.
- The next $q$ lines each contain a query time.
- The last line contains the window size $x$.

#### Output Format
Print $q$ lines, where each line contains the number of servers that did not receive any requests in the corresponding query window.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le m \le 10^5$
- $1 \le q \le 10^5$
- $1 \le \text{server\_id} \le n$
- $1 \le \text{time} \le 10^9$
- $1 \le query[i] \le 10^9$
- $1 \le x \le 10^9$

#### Sample Case
**Input:**
```text
3
3
2
1 3
2 6
1 5
2
10
11
5
```

**Output:**
```text
1
2
```

**Explanation:**
- For Query 1 at time $10$: The interval is $[10 - 5, 10] = [5, 10]$. The requests in this interval are:
  - Server 2 at time 6
  - Server 1 at time 5
  Servers that received requests are $\{1, 2\}$. Servers that did not receive requests are $\{3\}$. Count is $1$.
- For Query 2 at time $11$: The interval is $[11 - 5, 11] = [6, 11]$. The request in this interval is:
  - Server 2 at time 6
  Servers that received requests are $\{2\}$. Servers that did not receive requests are $\{1, 3\}$. Count is $2$.

---

#### Python Solution
```python
import sys

def getStaleServerCount(n, log_data, query, x):
    # Sort logs by request time
    logs = sorted(log_data, key=lambda log: log[1])
    # Keep track of original query indices to return answers in correct order
    indexed_queries = sorted(enumerate(query), key=lambda q: q[1])
    
    ans = [0] * len(query)
    count = [0] * (n + 1)
    active = 0
    l = 0
    r = 0
    m = len(logs)
    
    for q_idx, q_val in indexed_queries:
        start = q_val - x
        # Expand window: add servers that received requests up to q_val
        while r < m and logs[r][1] <= q_val:
            s_id = logs[r][0]
            if count[s_id] == 0:
                active += 1
            count[s_id] += 1
            r += 1
        # Shrink window: remove servers whose request times are strictly less than start
        while l < m and logs[l][1] < start:
            s_id = logs[l][0]
            count[s_id] -= 1
            if count[s_id] == 0:
                active -= 1
            l += 1
        # Number of stale servers is total minus active
        ans[q_idx] = n - active
        
    return ans

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        m = int(input_data[1])
        idx = 3
        log_data = []
        for _ in range(m):
            log_data.append([int(input_data[idx]), int(input_data[idx+1])])
            idx += 2
        q = int(input_data[idx])
        idx += 1
        query = []
        for _ in range(q):
            query.append(int(input_data[idx]))
            idx += 1
        x = int(input_data[idx])
        res = getStaleServerCount(n, log_data, query, x)
        print('\n'.join(map(str, res)))
```

