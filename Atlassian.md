# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Atlassian*
*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Confluence Text Editor Parity Check

**Topic:** `Strings`, `Bit Manipulation`, `Parity`  

Atlassian has a collaborative text editor called Confluence. Let's assume the text editor receives an array of strings `s`. Each string is considered as a zero-indexed array of characters. All characters in the strings fall within the ASCII range of lowercase letters (`a-z`), with decimal ordinal values ranging from 97 to 122 (e.g., `ord('a') = 97`).

Given an array of strings `s` of size `k`, and an integer `m`, we calculate the value of each string `s[i]` of length `len(s[i])` as:
$$\text{value}[i] = (\text{ord}[s[i][0]])^m \times (\text{ord}[s[i][1]])^m \times \dots \times (\text{ord}[s[i][\text{len}(s[i]) - 1]])^m$$

Perform this calculation on each string, sum them up, and determine whether their sum is `EVEN` or `ODD`.

#### Constraints
- $1 \le t \le 50$ (number of test cases)
- $2 \le k \le 20$ (number of strings per test case)
- $1 \le |s[i]| \le 10^5$ (length of each string)
- $0 \le m \le 10^9$ (exponent)

#### Example 1 (Sample Case 0, Test 1)
**Exponent ($m$):** `50`  
**Strings:** `['aceace', 'ceceaa', 'abdbdbdbakjkljhkjh']`  
**Output:** `EVEN`

#### Example 2 (Sample Case 0, Test 2)
**Exponent ($m$):** `47`  
**Strings:** `['azbde', 'abcher', 'acegk']`  
**Output:** `ODD`

#### Solution Explanation
Computing the exact values would require massive power calculations and big-number multiplication, which is highly inefficient. We can solve this in $O(k \times L)$ time (where $L$ is the string length) using parity arithmetic (modulo 2):
1. For any character $c$, if $\text{ord}(c)$ is even, then $(\text{ord}(c))^m \pmod 2 \equiv 0$ (for $m \ge 1$). If $\text{ord}(c)$ is odd, then $(\text{ord}(c))^m \pmod 2 \equiv 1$.
2. The product of ordinals $(\text{ord}[s[i][j]])^m$ for a string $s[i]$ is odd if and only if **all characters in the string have odd ordinal values** (e.g., `a, c, e, g, i, k, m, o, q, s, u, w, y`). If there is even one character with an even ordinal (e.g., `b, d, f, h, j, l, n, p, r, t, v, x, z`), the product becomes even.
3. The sum of the values is odd if and only if the number of strings with odd values is odd.

*(Note: If $m = 0$, every string value is 1, so all strings are odd).*

```python
def checkParity(m: int, s: list[str]) -> str:
    if m == 0:
        return "ODD" if len(s) % 2 != 0 else "EVEN"
        
    even_chars = set("bdfhjlnprtvxz")
    odd_string_count = 0
    
    for string in s:
        # If no even character exists in the string, it is odd
        if not any(char in even_chars for char in string):
            odd_string_count += 1
            
    return "ODD" if odd_string_count % 2 != 0 else "EVEN"
```

- **Time Complexity:** $O(k \times L)$ where $L$ is the maximum string length.
- **Space Complexity:** $O(1)$ auxiliary space.

---

### Q2. Rearrange Students (Height Balance)

**Topic:** `Arrays`, `Greedy`, `Sorting`, `Math`  

In a school, two lines of students, `A` and `B`, are arranged with `N` students in each line, facing each other. The Physical Education teacher aims to make the heights of students standing across from each other equal. This can be achieved by swapping students between the two lines. Any student in one line can be swapped with any student in the other line.

Each swap, regardless of the students involved, incurs a cost equal to the height of the shorter student in the swap. Rearranging students within the same line does not incur any cost.

Find the minimal cost to rearrange the students so that the lines can be sorted to be identical, or return `-1` if it is impossible.

#### Constraints
- $1 \le n \le 2 \times 10^5$
- $1 \le \text{arrA}[i], \text{arrB}[i] \le 10^9$

#### Example
**arrA:** `[4, 2, 2, 2]`  
**arrB:** `[1, 4, 1, 2]`  
**Output:** `1`  
**Explanation:** 
- If we sort the combined set, we get: `[1, 1, 2, 2, 2, 2, 4, 4]`.
- The target multiset for each array is `[1, 2, 2, 4]`.
- `arrA` has one excess `2`, and `arrB` has one excess `1`.
- Swapping a `2` in `arrA` with a `1` in `arrB` costs $\min(2, 1) = 1$. This swap is sufficient.

#### Solution Explanation
1. Count the frequencies of all heights across both arrays. If any height has an odd total count, it's impossible to balance them equally, so return `-1`.
2. Determine the target count for each height, which is half of its total count.
3. Identify the excess heights in `arrA` and `arrB` (heights that exceed their target count). Let the sorted excess lists be `excess_A` (ascending) and `excess_B` (descending).
4. Pair up the excess elements: $u \in \text{excess\_A}$ and $v \in \text{excess\_B}$.
5. For each pair, we can either swap them directly at cost $\min(u, v)$, or swap them using the global minimum element in the entire school as a helper at cost $2 \times \text{min\_val}$. We take the minimum of these two options.

```python
from collections import Counter

def rearrangeStudents(arrA: list[int], arrB: list[int]) -> int:
    countA = Counter(arrA)
    countB = Counter(arrB)
    all_elements = set(arrA) | set(arrB)
    
    excess_A = []
    excess_B = []
    
    for val in all_elements:
        total_count = countA[val] + countB[val]
        if total_count % 2 != 0:
            return -1
        target = total_count // 2
        if countA[val] > target:
            excess_A.extend([val] * (countA[val] - target))
        elif countB[val] > target:
            excess_B.extend([val] * (countB[val] - target))
            
    if len(excess_A) != len(excess_B):
        return -1
        
    excess_A.sort()
    excess_B.sort(reverse=True)
    
    min_val = min(min(arrA), min(arrB))
    
    total_cost = 0
    for u, v in zip(excess_A, excess_B):
        total_cost += min(min(u, v), 2 * min_val)
        
    return total_cost
```

- **Time Complexity:** $O(N \log N)$ due to sorting the excess arrays.
- **Space Complexity:** $O(N)$ to store counts and excess arrays.
