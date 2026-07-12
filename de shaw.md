# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/de shaw*
*Total questions: 1*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Minimize Max-Min Cost Difference

**Topic:** `Arrays`, `Binary Search`, `Prefix Sums`, `Greedy`  

There are `n` items in a shop, where the cost of the $i$-th item is represented by `cost[i]`. The shopkeeper wants to normalize the cost of the items, i.e., decrease the cost difference between the items with the maximum and minimum costs. However, the shopkeeper cannot change the cost of the items suddenly as it will affect the reputation of the shop.

The shopkeeper can choose to do the following operations for each of the `m` days:
- Decrease the cost of the item with the maximum cost by 1.
- Increase the cost of the item with the minimum cost by 1.

If there are multiple items with the maximum or minimum cost in the array, only one item's cost can be increased/decreased.

Given `n` items and an integer `m`, find the minimum possible difference between the maximum and minimum cost of the items in the array after `m` days.

#### Constraints
- $1 \le n \le 10^5$
- $1 \le cost[i] \le 10^9$
- $1 \le m \le 10^9$

#### Example
**Input:**  
- `cost: [1, 1, 4, 2]`  
- `m: 1`  
**Output:** `2`  
**Explanation:**  
- Initial costs: `[1, 1, 4, 2]`.
- Day 1: Decrease maximum (4) by 1 to get `[1, 1, 3, 2]`, and increase minimum (1) by 1 to get `[2, 1, 3, 2]`.
- The difference between maximum (3) and minimum (1) is $3 - 1 = 2$.

#### Solution Explanation
We can view this as two independent processes:
1. We have a budget of `m` increments of 1 to raise the smallest elements of the array. Let the maximum possible minimum value we can achieve be $L$.
2. We have a budget of `m` decrements of 1 to lower the largest elements of the array. Let the minimum possible maximum value we can achieve be $R$.

We can find $L$ and $R$ using binary search:
- To check if we can make all elements $\ge L$, the cost is $\sum_{x < L} (L - x)$. We can calculate this in $O(1)$ using prefix sums and binary search.
- To check if we can make all elements $\le R$, the cost is $\sum_{x > R} (x - R)$. We can also calculate this in $O(1)$ using prefix sums and binary search.

If $L \ge R$ after the binary search, the elements have crossed over or met. Since the total sum of elements remains constant, the minimum possible difference is:
- `0` if the total sum of costs is divisible by `n`.
- `1` if the total sum of costs is not divisible by `n`.

Otherwise, the minimum difference is $R - L$.

```python
import bisect

def getMinDiff(cost: list[int], m: int) -> int:
    cost.sort()
    n = len(cost)
    
    # Prefix sums of cost
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + cost[i]
        
    total_sum = pref[n]
    
    # Helper to check if we can make all elements >= L
    def can_make_min(L):
        idx = bisect.bisect_left(cost, L)
        required = idx * L - pref[idx]
        return required <= m
        
    # Helper to check if we can make all elements <= R
    def can_make_max(R):
        idx = bisect.bisect_right(cost, R)
        required = (total_sum - pref[idx]) - (n - idx) * R
        return required <= m

    # Binary search for L (max possible minimum)
    low_L = cost[0]
    high_L = cost[-1] + m
    L = low_L
    while low_L <= high_L:
        mid = (low_L + high_L) // 2
        if can_make_min(mid):
            L = mid
            low_L = mid + 1
        else:
            high_L = mid - 1
            
    # Binary search for R (min possible maximum)
    low_R = max(1, cost[0] - m)
    high_R = cost[-1]
    R = high_R
    while low_R <= high_R:
        mid = (low_R + high_R) // 2
        if can_make_max(mid):
            R = mid
            high_R = mid - 1
        else:
            low_R = mid + 1
            
    if L >= R:
        return 0 if total_sum % n == 0 else 1
    else:
        return R - L
```

- **Time Complexity:** $O(N \log N)$ to sort the array initially. The binary searches take $O(\log(\text{max\_val}) \log N)$ time, which is extremely fast.
- **Space Complexity:** $O(N)$ to store the prefix sums.
