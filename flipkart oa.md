# Interview Questions

*Total questions: 6*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Automated Parking Fee Calculator

`[Latest]`

**Topic:** `Implementation`, `String Manipulation`, `Hashing`

#### Description
West Edmonton is a shopping center in Canada which holds the Guinness world record for the largest parking lot. It has parking for more than 20,000 vehicles. Naturally, an automated system for determining parking fees is needed.

A bar code scanner reads the car number plate at parking entry and exit, and sends the information to a terminal at the Exit point, which prints out the parking ticket. The parking fees are determined by the type of the car, as given in the table below.

The barcode information sent to the terminal consists of a single string made of the car number plate (length 2 to 10), the car type code, and the duration of stay (4 digits). The parking ticket contains the car number plate and the parking fees to be paid.

Write a program which can be installed at the terminal to receive the barcode information and print the parking ticket.

#### Car Type Rates Table
| Car Type | Car Type Code | Cost of parking (Per Hour) |
|---|---|---|
| Sedan 4 | S4 | 120 |
| Sedan Exterior | SE | 120 |
| Sedan Super | SS | 100 |
| Sedan Start | SD | 80 |
| Sedan quattro | SW | 90 |
| DeVille Touring Sedan | DTS | 130 |
| C-Series Touring Sedan | CTS | 150 |
| HatchBack | HTBK | 50 |

#### Constraints
- $1 \le N \le 10,000$, where $N$ is the number of exiting cars.
- The car number plate can contain numbers or letters, and its length varies from 2 to 10.
- Duration of stay is represented by the last 4 digits of the barcode.

#### Input Format
- The first line of input consists of an integer $N$, which determines the number of cars exiting the parking.
- The next $N$ lines each contain one car's barcode information.

#### Output Format
- $N$ lines of output, where each line contains the car number plate and the parking fees to be paid, separated by a single space.

#### Sample Input 1
```text
4
OB48SS0009
MZHTBK0007
UN25WTOOS40010
AN53WJ0099DTS0002
```

#### Sample Output 1
```text
OB48 900
MZ 350
UN25WTOO 1200
AN53WJ0099 260
```

#### Explanation 1
1. Car Number: `OB48`, Car Type: `SS` ($100$/hr), Duration: 9 hrs. Cost = $9 \times 100 = 900$
2. Car Number: `MZ`, Car Type: `HTBK` ($50$/hr), Duration: 7 hrs. Cost = $7 \times 50 = 350$
3. Car Number: `UN25WTOO`, Car Type: `S4` ($120$/hr), Duration: 10 hrs. Cost = $10 \times 120 = 1200$
4. Car Number: `AN53WJ0099`, Car Type: `DTS` ($130$/hr), Duration: 2 hrs. Cost = $2 \times 130 = 260$

#### Sample Input 2
```text
5
PV14DZ03DTS0010
OM1697SD0005
FF8EP35S40006
KU0AM92CTS0009
OY9CH15HTBK0002
```

#### Sample Output 2
```text
PV14DZ03 1300
OM1697 400
FF8EP35 720
KU0AM92 1350
OY9CH15 100
```

---

#### Python Solution
```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    barcodes = input_data[1:n+1]
    
    rates = {
        "S4": 120, "SE": 120, "SS": 100, "SD": 80, "SW": 90,
        "DTS": 130, "CTS": 150, "HTBK": 50
    }
    
    for s in barcodes:
        hours = int(s[-4:])
        rem = s[:-4]
        
        # Determine code and plate
        if rem.endswith("HTBK") and len(rem) >= 6:
            plate = rem[:-4]
            code = "HTBK"
        elif (rem.endswith("DTS") or rem.endswith("CTS")) and len(rem) >= 5:
            plate = rem[:-3]
            code = rem[-3:]
        else:
            plate = rem[:-2]
            code = rem[-2:]
            
        print(f"{plate} {hours * rates[code]}")

if __name__ == '__main__':
    solve()
```

#### C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    unordered_map<string, int> rates = {
        {"S4", 120}, {"SE", 120}, {"SS", 100}, {"SD", 80}, {"SW", 90},
        {"DTS", 130}, {"CTS", 150}, {"HTBK", 50}
    };
    
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        
        int hours = stoi(s.substr(s.length() - 4));
        string rem = s.substr(0, s.length() - 4);
        string plate, code;
        int len = rem.length();
        
        if (len >= 6 && rem.compare(len - 4, 4, "HTBK") == 0) {
            plate = rem.substr(0, len - 4);
            code = "HTBK";
        } else if (len >= 5 && (rem.compare(len - 3, 3, "DTS") == 0 || rem.compare(len - 3, 3, "CTS") == 0)) {
            plate = rem.substr(0, len - 3);
            code = rem.substr(len - 3);
        } else if (len >= 4) {
            plate = rem.substr(0, len - 2);
            code = rem.substr(len - 2);
        }
        
        cout << plate << " " << (hours * rates[code]) << "\n";
    }
    return 0;
}
```

---

### Q2. Minimum Moves to Reach the End (Jaya's Stall Game)

`[Latest]`

**Topic:** `Greedy`, `Array`, `Dynamic Programming`

#### Description
At the village fair, all the children have been asked to participate in a game. A certain number of stalls are arranged in a straight line. All the children start at the first stall, and the child who reaches the last stall earliest wins. 

At each stall, a token number is displayed. If a token of $p$ is displayed at a stall, the child can then jump to any of the next $p$ stalls. At every stall the child visits, there is a wait time of five minutes, so the fewer stalls one visits, the more likely they are to win.

Write a program to determine the minimum number of moves Jaya needs to reach the last stall from the first.

#### Constraints
- $2 \le N \le 1000$
- $1 \le A_i \le 100$ for all $1 \le i \le N$

#### Input Format
- A single line of input consists of the array $A$, which has $N$ positive integers denoting the tokens. The input can be space-separated or a single string of concatenated single digits.

#### Output Format
- Print the minimum number of moves Jaya needs to make to reach the last stall from the first.

#### Sample Input 1
```text
44214412
```

#### Sample Output 1
```text
2
```

#### Explanation 1
The token array is $A = [4, 4, 2, 1, 4, 4, 1, 2]$:
Jaya is at the 1st stall (token number 4). She can jump to any of the next 4 stalls (up to index 4). She jumps to stall 5 (value 4). From stall 5, she can jump to any of the next 4 stalls (up to index 8). Since there are only 8 stalls, she can reach the last stall in 2 moves.

#### Sample Input 2
```text
2413211
```

#### Sample Output 2
```text
3
```

#### Explanation 2
The token array is $A = [2, 4, 1, 3, 2, 1, 1]$:
1. Start at index 0 (token 2). Jump to index 1 (token 4).
2. From index 1, jump to index 5 (token 1) or index 3 (token 3).
3. From either, reach the last stall (index 6).
Total minimum moves = 3.

---

#### Python Solution
```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Handle inputs where the array is represented by a single string of digits
    if len(input_data) == 1:
        A = [int(c) for c in input_data[0]]
    else:
        A = [int(x) for x in input_data]
        
    n = len(A)
    if n <= 1:
        print(0)
        return
    
    jumps = 0
    curr_end = 0
    farthest = 0
    
    for i in range(n - 1):
        farthest = max(farthest, i + A[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest
            if curr_end >= n - 1:
                break
                
    print(jumps)

if __name__ == '__main__':
    solve()
```

#### C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int numberOfShopsVisited(vector<int>& arr) {
    int n = arr.size();
    if (n == 1 && arr[0] > 9) {
        string s = to_string(arr[0]);
        arr.clear();
        for (char c : s) {
            arr.push_back(c - '0');
        }
        n = arr.size();
    }
    
    if (n <= 1) return 0;
    
    int jumps = 0;
    int curr_end = 0;
    int farthest = 0;
    
    for (int i = 0; i < n - 1; ++i) {
        farthest = max(farthest, i + arr[i]);
        if (i == curr_end) {
            jumps++;
            curr_end = farthest;
            if (curr_end >= n - 1) {
                break;
            }
        }
    }
    return jumps;
}

int main() {
    vector<int> arr;
    int num;
    while (cin >> num) {
        arr.push_back(num);
    }
    cout << numberOfShopsVisited(arr) << "\n";
    return 0;
}
```

---

### Q3. Sangeeta's Jogging Grid Traversal

`[Latest]`

**Topic:** `Math`, `Implementation`

#### Description
Sangeeta loves to jog every morning. She goes to a different park every day, and always runs across the park in a zigzag manner. The parks are represented as squares of size $N \times N$. The manner in which Sangeeta runs in a $4 \times 4$ sized park can be represented as follows:
```text
1  3  4 10
2  5  9 11
6  8 12 15
7 13 14 16
```
The values in each block represent the number of minutes Sangeeta takes to arrive there from her starting point. She always starts at the top left of the park $(0, 0)$ and takes one minute to move to the next block.

Given a park's dimensions and coordinates, write a program to figure out how much time Sangeeta will take to reach a particular block in the park.

#### Constraints
- $1 \le N \le 10,000$
- $0 \le x < N$ (row index)
- $0 \le y < N$ (column index)

#### Input Format
- A single line of input contains three space-separated integers: $N, x, y$, where $N$ indicates the size of the park, and $x, y$ indicate the 0-indexed position (row, column) of the block.

#### Output Format
- Print an integer representing the time Sangeeta takes to arrive at $(x, y)$.

#### Sample Input 1
```text
3 2 2
```

#### Sample Output 1
```text
9
```

#### Explanation 1
The destination block is $(2, 2)$ in a $3 \times 3$ grid:
```text
1 3 4
2 5 8
6 7 9
```
The value at index $(2, 2)$ is 9.

#### Sample Input 2
```text
4 2 3
```

#### Sample Output 2
```text
15
```

#### Explanation 2
The destination block is $(2, 3)$ in a $4 \times 4$ grid:
```text
1  3  4 10
2  5  9 11
6  8 12 15
7 13 14 16
```
The value at index $(2, 3)$ is 15.

---

#### Python Solution
```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    x = int(input_data[1])
    y = int(input_data[2])
    
    S = x + y
    if S < N:
        before = S * (S + 1) // 2
        idx = x if S % 2 == 0 else S - x
        print(before + idx + 1)
    else:
        S_rev = 2 * N - 2 - S
        after = S_rev * (S_rev + 1) // 2
        r_min = S - N + 1
        r_max = N - 1
        idx = x - r_min if S % 2 == 0 else r_max - x
        print(N * N - after - S_rev + idx)

if __name__ == '__main__':
    solve()
```

#### C++ Solution
```cpp
#include <iostream>

using namespace std;

long long calculateTime(int N, int x, int y) {
    long long n_val = N;
    long long x_val = x;
    long long y_val = y;
    long long S = x_val + y_val;
    
    if (S < n_val) {
        long long before = S * (S + 1) / 2;
        long long idx = (S % 2 == 0) ? x_val : (S - x_val);
        return before + idx + 1;
    } else {
        long long S_rev = 2 * n_val - 2 - S;
        long long after = S_rev * (S_rev + 1) / 2;
        long long r_min = S - n_val + 1;
        long long r_max = n_val - 1;
        long long idx = (S % 2 == 0) ? (x_val - r_min) : (r_max - x_val);
        return n_val * n_val - after - S_rev + idx;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, x, y;
    if (cin >> N >> x >> y) {
        cout << calculateTime(N, x, y) << "\n";
    }
    return 0;
}
```

---

### Q4. Maximum Subset Sum with LSB Condition

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

### Q5. K-Sized Subarray Frequency Difference

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

### Q6. Primal Compass (Prime Numbers with Digit Sum N)

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

