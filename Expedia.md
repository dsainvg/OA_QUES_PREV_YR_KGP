# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Expedia*
*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Maximum Efficiency of Testing System

**Topic:** `Arrays`, `Sorting`, `Two Pointers`, `Sliding Window`  

When evaluating a machine learning model, `n` test cases are provided. Each is associated with an `arrivalTime[i]` indicating the time each test case was given. The testing environment is activated once for some time, then enters an inactive state. If activated at time $t_1$ and deactivated at time $t_2$, tests with arrival times between $t_1$ and $t_2$ (inclusive) are executed. The total time the system was active is $t_2 - t_1$.

$$\text{Efficiency of testing system} = \text{number of test cases tested} - \text{total time the system was active}$$

Determine the maximum efficiency when the testing environment selects optimum activation and deactivation times. The environment must execute at least two test cases during its active period. Return the maximum possible efficiency.

#### Notes:
- Execution time for test cases is practically instantaneous; that is, it takes almost no time.
- If two test cases share the same arrival time, they are evaluated simultaneously.
- Efficiency may take negative values.

#### Constraints
- $2 \le n \le 2 \times 10^5$
- $1 \le arrivalTime[i] \le 10^9$

#### Example
**Input:** `arrivalTime = [9, 1, 3, 5, 6]`  
**Output:** `1`  
**Explanation:**  
- It is optimal to choose $t_1 = 5$ and $t_2 = 6$. 
- The 4th and 5th test cases (with arrival times 5 and 6) will be executed. 
- Number of test cases tested = 2.
- Active duration = $6 - 5 = 1$.
- Efficiency = $2 - 1 = 1$.

#### Solution Explanation
Let the sorted arrival times be $A[0] \le A[1] \le \dots \le A[n-1]$.
Any optimal active window $[t_1, t_2]$ must start at some $A[i]$ and end at some $A[j]$ ($i < j$).
- The number of test cases executed is $j - i + 1$.
- The duration is $A[j] - A[i]$.
- The efficiency is $(j - i + 1) - (A[j] - A[i]) = (A[i] - i) - (A[j] - j) + 1$.

To maximize this over all $i < j$, we can iterate $j$ from $1$ to $n-1$ and keep track of the maximum value of $(A[i] - i)$ for all $i < j$.

```python
def getMaxEfficiency(arrivalTime: list[int]) -> int:
    A = sorted(arrivalTime)
    n = len(A)
    
    max_efficiency = float('-inf')
    max_so_far = A[0] - 0  # stores max(A[i] - i) for i < j
    
    for j in range(1, n):
        eff = max_so_far - (A[j] - j) + 1
        max_efficiency = max(max_efficiency, eff)
        max_so_far = max(max_so_far, A[j] - j)
        
    return max_efficiency
```

- **Time Complexity:** $O(N \log N)$ to sort the arrival times.
- **Space Complexity:** $O(N)$ or $O(1)$ auxiliary space if sorted in place.

---

### Q2. Neural Network Layer Rearrangement

**Topic:** `Arrays`, `Greedy`, `Subsequences`  

Given two sets of data: `current` and `desired`, each represents the order of `n` layers within a neural network architecture. During the training of the model, an operation can be performed to adjust the arrangement of layers. In one step, a layer is selected from the end of the list and inserted at any arbitrary position within the list.

Determine the minimum number of steps required to transform the initial arrangement (`current`) into the desired arrangement (`desired`).

#### Constraints
- Both `current` and `desired` are permutations of size `n` containing elements from `1` to `n`.
- $1 \le n \le 10^5$.

#### Example
**Input:**
- `current = [2, 1, 3, 5, 4]`
- `desired = [2, 4, 1, 5, 3]`  
**Output:** `2`  
**Explanation:**  
- Step 1: Pick layer 4 (from the end of `current`) and insert it to get `[2, 4, 1, 3, 5]`.
- Step 2: Pick layer 5 (from the end) and insert it to get `[2, 4, 1, 5, 3]`.
- This matches the desired arrangement in 2 steps.

#### Solution Explanation
Since we can only select a layer from the end of the list and insert it anywhere, any element we decide *not* to move must remain in its relative order. These unmoved elements must form a prefix of `current` that is also a subsequence of `desired`.
To minimize the number of moves, we want to maximize the size of the unmoved prefix.
We can find the length of the longest prefix of `current` that is a subsequence of `desired` by iterating through `desired` and matching elements with `current` starting from index 0.
The answer is $n - \text{matched\_length}$.

```python
def getMinSteps(current: list[int], desired: list[int]) -> int:
    n = len(current)
    curr_ptr = 0
    
    for val in desired:
        if curr_ptr < n and val == current[curr_ptr]:
            curr_ptr += 1
            
    return n - curr_ptr
```

- **Time Complexity:** $O(N)$ as we iterate through both arrays exactly once.
- **Space Complexity:** $O(1)$ auxiliary space.
