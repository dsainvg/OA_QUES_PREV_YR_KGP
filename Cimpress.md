# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Cimpress*
*Total questions: 1*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Maximum balls (Exclude One Element to Maximize GCD)

**Topic:** `Arrays`, `Number Theory`, `Prefix & Suffix Arrays`, `Greatest Common Divisor (GCD)`  

Bob is a math teacher with a class of `N` students. The marks obtained by the students are represented by the array `marks`. Bob wants to gift every student an equal number of balls. To do this, he needs to choose a number that is a factor of the marks of all `N` students.

In order to distribute the maximum number of balls, Bob can change the marks of at most one student to any positive number of his choice. Find the maximum number of balls Bob can give to every student after changing the marks of at most one student.

#### Function description
Complete the `max_balls` function. This function takes the following 2 parameters and returns an integer that represents the answer:
- `N`: Represents the number of students in the class
- `marks`: Represents the marks of `N` students

#### Constraints
- $2 \le N \le 10^5$
- $1 \le marks_i \le 10^9$

#### Example
**Input:**  
- `N: 3`  
- `marks: [12, 3, 11]`  
**Output:** `3`  
**Explanation:**  
- To distribute the maximum number of balls, Bob can change the marks of the 3rd student (with marks 11) to 39. 
- The array becomes `[12, 3, 39]`, and the GCD of the marks is `gcd(12, 3, 39) = 3`. 
- Thus, Bob can give 3 balls to every student.

#### Solution Explanation
Changing one element to any positive number of our choice means we can choose it to be a multiple of the GCD of all the remaining elements in the array. This effectively eliminates that element's constraint on the overall GCD.
Thus, the problem reduces to finding the maximum GCD of any $N-1$ elements in the array.

We can compute this efficiently in $O(N)$ time by maintaining:
1. A prefix GCD array `pref` where `pref[i] = gcd(marks[0], ..., marks[i])`.
2. A suffix GCD array `suff` where `suff[i] = gcd(marks[i], ..., marks[N-1])`.

For each index `i`, the GCD of the remaining elements is:
- If $i = 0$: `suff[1]`
- If $i = N-1$: `pref[N-2]`
- Otherwise: `gcd(pref[i-1], suff[i+1])`

We take the maximum value over all `i`.

```python
import math

def max_balls(N: int, marks: list[int]) -> int:
    if N < 2:
        return 0
        
    # Build prefix GCDs
    pref = [0] * N
    pref[0] = marks[0]
    for i in range(1, N):
        pref[i] = math.gcd(pref[i-1], marks[i])
        
    # Build suffix GCDs
    suff = [0] * N
    suff[N-1] = marks[N-1]
    for i in range(N-2, -1, -1):
        suff[i] = math.gcd(suff[i+1], marks[i])
        
    max_gcd = 0
    for i in range(N):
        if i == 0:
            current_gcd = suff[1]
        elif i == N-1:
            current_gcd = pref[N-2]
        else:
            current_gcd = math.gcd(pref[i-1], suff[i+1])
        max_gcd = max(max_gcd, current_gcd)
        
    return max_gcd
```

- **Time Complexity:** $O(N \log(\max(marks)))$ because we perform a constant number of $O(\log(\text{value}))$ GCD operations per element.
- **Space Complexity:** $O(N)$ to store prefix and suffix arrays.
