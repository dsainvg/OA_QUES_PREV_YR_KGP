# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/flipkart oa*
*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Maximum Subset Sum with LSB Condition

**Topic:** `Arrays`, `Math`, `Bit Manipulation`  

You are given an array of integers `nums`. Your task is to find the subset of `nums` that has the maximum sum, subject to the condition that no two elements in the subset should have the same least significant bit (LSB) in their binary representation.

#### Input Format
A single line of input containing the array of integers, `nums`, with elements separated by spaces.

#### Output Format
Print an integer representing the maximum subset sum of `nums` that satisfies the LSB condition.

#### Example 1
**Input:** `2 5 7 3 9 11`  
**Output:** `13`  
**Explanation:** 
- Numbers with LSB = 0 (even): `[2]`, maximum is `2`.
- Numbers with LSB = 1 (odd): `[5, 7, 3, 9, 11]`, maximum is `11`.
- Max subset sum is `2 + 11 = 13`.

#### Example 2
**Input:** `3 5 7 9`  
**Output:** `9`  
**Explanation:** 
- Numbers with LSB = 1 (odd): `[3, 5, 7, 9]`, maximum is `9`.
- No even numbers exist.
- Max subset sum is `9`.

```python
def maxSubsetSumLSB(nums: list[int]) -> int:
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    
    max_even = max(evens) if evens else None
    max_odd = max(odds) if odds else None
    
    # Since we can choose any subset (including the empty subset), 
    # we take only non-negative maximums if possible, or return the max sum.
    ans = 0
    if max_even is not None:
        ans = max(ans, max_even)
    if max_odd is not None:
        ans = max(ans, max_odd)
    if max_even is not None and max_odd is not None:
        ans = max(ans, max_even + max_odd)
        
    return ans
```

- **Time Complexity:** $O(N)$ where $N$ is the number of elements.
- **Space Complexity:** $O(N)$ to store the partitioned lists of evens and odds.

---

### Q2. K-Sized Subarray Frequency Difference

**Topic:** `Arrays`, `Sliding Window`, `Heaps`, `Hash Map`  

Given an array `A` of size `N`. Find the sum of absolute differences between the maximum frequency and minimum frequency element in each $K$-sized subarray of array `A`.

If two elements have the same highest frequency, then consider the larger of the two in the case of the maximum element, and consider the smaller of the two in the case of the minimum element.

#### Input Format
- The first line contains two space-separated integers, `N` and `K`, representing the size of the array and the size of the subarrays, respectively.
- The second line contains `N` space-separated integers representing the elements of the array `A`.

#### Output Format
Print the sum of absolute differences between the maximum frequency and minimum frequency element in every subarray of size `K`.

#### Example
**Input:**
```
6 3
5 5 4 4 4 4
```
**Output:** `2`  
**Explanation:**
- First subarray `[5, 5, 4]`:
  - Frequencies: `{5: 2, 4: 1}`.
  - Max frequency element: `5` (frequency 2).
  - Min frequency element: `4` (frequency 1).
  - Absolute difference: `|2 - 1| = 1`.
- Second subarray `[5, 4, 4]`:
  - Frequencies: `{5: 1, 4: 2}`.
  - Max frequency element: `4` (frequency 2).
  - Min frequency element: `5` (frequency 1).
  - Absolute difference: `|2 - 1| = 1`.
- Third subarray `[4, 4, 4]`:
  - Frequencies: `{4: 3}`.
  - Max frequency element: `4` (frequency 3).
  - Min frequency element: `4` (frequency 3).
  - Absolute difference: `|3 - 3| = 0`.
- Fourth subarray `[4, 4, 4]`:
  - Absolute difference: `0`.
- Sum of absolute differences: `1 + 1 + 0 + 0 = 2`.

```python
import heapq

def solveSubarrayFreqDiff(n: int, k: int, a: list[int]) -> int:
    freq = {}
    
    # We store (frequency, element_value)
    # Python heapq is a min-heap.
    # To implement max-heap, we push (-frequency, -element_value).
    min_heap = []
    max_heap = []
    
    def add_freq(val):
        freq[val] = freq.get(val, 0) + 1
        f = freq[val]
        heapq.heappush(min_heap, (f, val))
        heapq.heappush(max_heap, (-f, -val))
        
    def remove_freq(val):
        if val in freq:
            freq[val] -= 1
            f = freq[val]
            if f == 0:
                del freq[val]
            else:
                heapq.heappush(min_heap, (f, val))
                heapq.heappush(max_heap, (-f, -val))

    # Initialize the first window
    for i in range(k):
        add_freq(a[i])
        
    total_diff_sum = 0
    
    # Process sliding windows
    for i in range(k, n + 1):
        # Clean stale values from min_heap
        while min_heap:
            f, val = min_heap[0]
            if freq.get(val, 0) == f:
                break
            heapq.heappop(min_heap)
            
        # Clean stale values from max_heap
        while max_heap:
            neg_f, neg_val = max_heap[0]
            f, val = -neg_f, -neg_val
            if freq.get(val, 0) == f:
                break
            heapq.heappop(max_heap)
            
        min_freq = min_heap[0][0]
        max_freq = -max_heap[0][0]
        total_diff_sum += abs(max_freq - min_freq)
        
        # Slide window
        if i < n:
            remove_freq(a[i - k])
            add_freq(a[i])
            
    return total_diff_sum
```

- **Time Complexity:** $O(N \log N)$ due to heap push/pop operations.
- **Space Complexity:** $O(N)$ to maintain the frequency map and heaps.

---

### Q3. Primal Compass (Prime Numbers with Digit Sum N)

**Topic:** `Number Theory`, `Sieve of Eratosthenes`, `Math`  

Each prime number has a digit sum equal to a given integer `N`. Your task is to generate the first `K` prime numbers whose digit sums are equal to `N`.

#### Input Format
- The first line of input contains an integer `N` representing the required digit sum.
- The second line of input contains an integer `K` representing the number of prime numbers to be generated.

#### Output Format
Print the first `K` prime numbers whose digit sums equal `N`, separated by spaces.
- If there are fewer than `K` such primes (searching up to $100,000$), print all the primes found.
- If no such prime numbers are found, print `-1`.

#### Example 1
**Input:**
```
10
5
```
**Output:** `19 37 73 109 127`  
**Explanation:** The first 5 primes with digit sum 10 are:
- `19` ($1+9=10$)
- `37` ($3+7=10$)
- `73` ($7+3=10$)
- `109` ($1+0+9=10$)
- `127` ($1+2+7=10$)

#### Example 2
**Input:**
```
12
4
```
**Output:** `-1`  
**Explanation:** Any number whose digit sum is 12 is a multiple of 3. The only prime divisible by 3 is 3 itself, which does not have a digit sum of 12. Thus, no such prime exists.

```python
def solvePrimeDigitSum(n: int, k: int) -> list[int] | int:
    LIMIT = 100000
    is_prime = [True] * LIMIT
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(LIMIT**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, LIMIT, i):
                is_prime[j] = False
                
    primes = []
    for i in range(LIMIT):
        if is_prime[i]:
            digit_sum = sum(int(d) for d in str(i))
            if digit_sum == n:
                primes.append(i)
                if len(primes) == k:
                    break
                    
    if not primes:
        return -1
    return primes
```

- **Time Complexity:** $O(L \log \log L)$ where $L = 100,000$ (Sieve Limit) to build primes, followed by digit sum check.
- **Space Complexity:** $O(L)$ to hold the boolean prime check array.
