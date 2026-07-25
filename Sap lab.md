# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [MCQs](#mcqs)

---

## Coding Questions

### Q1. Minimum Operations to Balance Array

**Topic:** `Arrays`, `Greedy`, `Two Pointers`

Given an array of positive integers, calculate the minimum number of operations required to make all adjacent element differences equal to a given target $K$.

#### Input
- `arr`: list of integers
- `k`: integer

#### Constraints
- $1 \le \text{len}(arr) \le 10^5$
- $1 \le k \le 10^9$

#### Example 1
**Input:** `arr = [2, 4, 6, 8], k = 2`  
**Output:** `0`  

---

#### Solution

##### Complexity
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

##### Python Implementation
```python
def minOperations(arr, k):
    ops = 0
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        if diff != k:
            ops += abs(diff - k)
    return ops
```

##### C++ Implementation
```cpp
#include <vector>
#include <cmath>
using namespace std;

int minOperations(vector<int>& arr, int k) {
    int ops = 0;
    for (size_t i = 1; i < arr.size(); ++i) {
        int diff = abs(arr[i] - arr[i-1]);
        if (diff != k) ops += abs(diff - k);
    }
    return ops;
}
```

---

## MCQs

### Q1. Time Complexity of Search in Balanced BST

**Topic:** `Data Structures`, `Trees`

What is the worst-case time complexity for searching an element in a balanced Binary Search Tree (BST) of $N$ nodes?

**Options:**
- A) $\mathcal{O}(1)$
- B) $\mathcal{O}(\log N)$
- C) $\mathcal{O}(N)$
- D) $\mathcal{O}(N \log N)$

**Correct Answer:** **B) $\mathcal{O}(\log N)$**  
**Explanation:** In a balanced BST, height is bounded by $\log_2 N$. Thus searching takes logarithmic time.