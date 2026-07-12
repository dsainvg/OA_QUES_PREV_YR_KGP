# Interview Questions

*Generated from: `R:\DSA\Company wise prep resource\amazon`*  
*Total questions: 5*  

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Divisible Cost Pairs

**Topic:** `arrays`, `hash-map`, `math`, `two-pointers`

**Question:**  
Amazon is offering a discount on every purchase of a pair of products whose cost sum is divisible by `x`. Given the cost of `n` products in the store, find the number of pairs `(i, j)` where `i < j` and `cost[i] + cost[j]` is divisible by `x`.

#### Input
- `x`: integer ($1 \le x \le 2 \cdot 10^9$)
- `cost`: list of integers ($1 \le cost[i] \le 10^9$)

#### Constraints
- $1 \le n \le 10^5$
- $1 \le x \le 2 \cdot 10^9$
- $1 \le cost[i] \le 10^9$

#### Example 1
**Input:**
```text
x = 6
cost = [12, 2, 4]
```
**Output:**
```text
1
```
**Explanation:**  
The only pair whose sum is divisible by 6 is `(2, 4)` since `2 + 4 = 6`, which is divisible by 6.

#### Example 2
**Input:**
```text
x = 10
cost = [3, 7, 27, 23]
```
**Output:**
```text
4
```
**Explanation:**  
The pairs that get the discount are:
- `(3, 7)` since `3 + 7 = 10`
- `(3, 27)` since `3 + 27 = 30`
- `(23, 7)` since `23 + 7 = 30`
- `(23, 27)` since `23 + 27 = 50`

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ to store remainders in a hash map.

##### Python Implementation
```python
def findPairs(x, cost):
    remainder_counts = {}
    total_pairs = 0
    
    for c in cost:
        rem = c % x
        target = (x - rem) % x
        if target in remainder_counts:
            total_pairs += remainder_counts[target]
            
        remainder_counts[rem] = remainder_counts.get(rem, 0) + 1
        
    return total_pairs
```

##### C++ Implementation
```cpp
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    long long findPairs(int x, const vector<int>& cost) {
        unordered_map<int, int> remainder_counts;
        long long total_pairs = 0;
        
        for (int c : cost) {
            int rem = c % x;
            int target = (x - rem) % x;
            if (remainder_counts.count(target)) {
                total_pairs += remainder_counts[target];
            }
            remainder_counts[rem]++;
        }
        
        return total_pairs;
    }
};
```

---

### Q2. Duel Tournament Power Boosters

**Topic:** `arrays`, `sorting`, `greedy`

**Question:**  
Amazon games have recently launched a new multi-player tournament. Each game of the tournament has 3 rounds. The players are provided with exactly three power boosters at the start of the game. In each round, the player can choose to compete with any of the power boosters, and each power booster can be used at most once in a game. In any particular round, the player with the higher power booster wins.

A player `X` is considered to be capable of defeating player `Y` if there exists a pairing of X's boosters and Y's boosters such that X wins in at least 2 out of the 3 rounds.

Given the power boosters of `n` players defined by `power_type_a[i]`, `power_type_b[i]`, and `power_type_c[i]`, find the number of players who are capable of defeating all other players. All booster values of each player are distinct.

#### Input
- `power_type_a`: list of integers
- `power_type_b`: list of integers
- `power_type_c`: list of integers

#### Constraints
- $2 \le n \le 10^5$
- $1 \le power\_type\_a[i], power\_type\_b[i], power\_type\_c[i] \le 10^9$
- All power boosters of each player are pairwise distinct.

#### Example 1
**Input:**
```text
power_type_a = [9, 4, 2]
power_type_b = [5, 12, 10]
power_type_c = [11, 3, 13]
```
**Output:**
```text
2
```
**Explanation:**  
The players' boosters are:
- Player 1: `[9, 5, 11]` (sorted: `[5, 9, 11]`)
- Player 2: `[4, 12, 3]` (sorted: `[3, 4, 12]`)
- Player 3: `[2, 10, 13]` (sorted: `[2, 10, 13]`)

Player 1 and Player 3 can defeat all other players, so the answer is 2.

#### Example 2
**Input:**
```text
power_type_a = [3, 4, 1, 16]
power_type_b = [2, 11, 5, 6]
power_type_c = [8, 7, 9, 10]
```
**Output:**
```text
2
```
**Explanation:**  
The players' boosters are:
- Player 1: `[3, 2, 8]` (sorted: `[2, 3, 8]`)
- Player 2: `[4, 11, 7]` (sorted: `[4, 7, 11]`)
- Player 3: `[1, 5, 9]` (sorted: `[1, 5, 9]`)
- Player 4: `[16, 6, 10]` (sorted: `[6, 10, 16]`)

Player 2 and Player 4 can defeat all other players, so the answer is 2.

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ to store sorted boosters and player values.

##### Python Implementation
```python
def findCapableWinners(power_type_a, power_type_b, power_type_c):
    n = len(power_type_a)
    players = []
    
    for i in range(n):
        boosters = sorted([power_type_a[i], power_type_b[i], power_type_c[i]])
        players.append(boosters)
        
    # Find max and second max of the first and second booster categories
    # p[0] is the smallest, p[1] is the middle, p[2] is the largest booster of player
    max1, max1_2nd = -1, -1
    max2, max2_2nd = -1, -1
    
    for p in players:
        p1_val = p[0]
        p2_val = p[1]
        
        # Track max and 2nd max of first boosters
        if p1_val > max1:
            max1_2nd = max1
            max1 = p1_val
        elif p1_val > max1_2nd:
            max1_2nd = p1_val
            
        # Track max and 2nd max of second boosters
        if p2_val > max2:
            max2_2nd = max2
            max2 = p2_val
        elif p2_val > max2_2nd:
            max2_2nd = p2_val
            
    winners = 0
    for p in players:
        # Determine the maximum first booster of others
        limit1 = max1_2nd if p[0] == max1 else max1
        # Determine the maximum second booster of others
        limit2 = max2_2nd if p[1] == max2 else max2
        
        if p[1] > limit1 and p[2] > limit2:
            winners += 1
            
    return winners
```

##### C++ Implementation
```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findCapableWinners(vector<int> power_type_a, vector<int> power_type_b, vector<int> power_type_c) {
        int n = power_type_a.size();
        vector<vector<int>> players(n, vector<int>(3));
        
        for (int i = 0; i < n; ++i) {
            vector<int> boosters = {power_type_a[i], power_type_b[i], power_type_c[i]};
            sort(boosters.begin(), boosters.end());
            players[i] = boosters;
        }
        
        int max1 = -1, max1_2nd = -1;
        int max2 = -1, max2_2nd = -1;
        
        for (const auto& p : players) {
            int p1_val = p[0];
            int p2_val = p[1];
            
            if (p1_val > max1) {
                max1_2nd = max1;
                max1 = p1_val;
            } else if (p1_val > max1_2nd) {
                max1_2nd = p1_val;
            }
            
            if (p2_val > max2) {
                max2_2nd = max2;
                max2 = p2_val;
            } else if (p2_val > max2_2nd) {
                max2_2nd = p2_val;
            }
        }
        
        int winners = 0;
        for (const auto& p : players) {
            int limit1 = (p[0] == max1) ? max1_2nd : max1;
            int limit2 = (p[1] == max2) ? max2_2nd : max2;
            
            if (p[1] > limit1 && p[2] > limit2) {
                winners++;
            }
        }
        
        return winners;
    }
};
```

---

### Q3. Common Regex Wildcards

**Topic:** `strings`, `greedy`

**Question:**  
Amazon is developing a string matching library and you are to develop a service that finds a common regex pattern from the given set of regexes.

A regex pattern consists of lowercase English letters and wildcard characters (`?`). Two patterns are called intersecting if the wildcard characters in the respective strings can be changed in a way to form the same string from both patterns.

Given an array `patterns` of `n` regex strings of length `m`, find the minimum number of `?` characters possible in a pattern that intersects with all the patterns.

#### Input
- `patterns`: list of strings

#### Constraints
- $1 \le n \le 10^5$
- $1 \le m \le 10^5$
- Total characters $n \times m \le 10^6$

#### Example 1
**Input:**
```text
patterns = ["ha???rrank", "?a?ke?bank"]
```
**Output:**
```text
1
```
**Explanation:**  
The minimum wildcard pattern that intersects with both is `hacker?ank`, which has exactly 1 wildcard character `?` (at index 6).

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N \cdot m)$
- **Space Complexity:** $O(m)$ to store character states per index.

##### Python Implementation
```python
def minWildcardRegex(patterns):
    n = len(patterns)
    m = len(patterns[0])
    wildcards = 0
    
    for col in range(m):
        unique_char = None
        has_conflict = False
        
        for row in range(n):
            char = patterns[row][col]
            if char != '?':
                if unique_char is None:
                    unique_char = char
                elif unique_char != char:
                    has_conflict = True
                    break
                    
        if has_conflict:
            wildcards += 1
            
    return wildcards
```

##### C++ Implementation
```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int minWildcardRegex(const vector<string>& patterns) {
        int n = patterns.size();
        int m = patterns[0].size();
        int wildcards = 0;
        
        for (int col = 0; col < m; ++col) {
            char unique_char = '\0';
            bool has_conflict = false;
            
            for (int row = 0; row < n; ++row) {
                char ch = patterns[row][col];
                if (ch != '?') {
                    if (unique_char == '\0') {
                        unique_char = ch;
                    } else if (unique_char != ch) {
                        has_conflict = true;
                        break;
                    }
                }
            }
            if (has_conflict) {
                wildcards++;
            }
        }
        
        return wildcards;
    }
};
```

---

### Q4. Minimize Maximum Parcels

**Topic:** `arrays`, `math`, `greedy`

**Question:**  
To be efficient, Amazon must optimally distribute parcels among their delivery agents. Initially, there are `n` agents, and the number of parcels assigned to the `i`-th agent is `parcels[i]`. There are `extra_parcels` parcels that also need to be shipped. The extra parcels should be assigned such that the maximum number of parcels assigned to any one agent is minimized.

Given an integer array `parcels` and an integer `extra_parcels`, find the minimum possible value of the maximum number of parcels any agent must deliver.

#### Input
- `parcels`: list of integers
- `extra_parcels`: long integer ($1 \le extra\_parcels \le 10^{12}$)

#### Constraints
- $1 \le n \le 10^5$
- $1 \le parcels[i] \le 10^9$
- $1 \le extra\_parcels \le 10^{12}$

#### Example 1
**Input:**
```text
parcels = [7, 5, 1, 9, 1]
extra_parcels = 25
```
**Output:**
```text
10
```
**Explanation:**  
An optimal distribution adds 3, 5, 9, 1, 7 parcels respectively to get `[10, 10, 10, 10, 8]`. The maximum value is 10.

#### Example 2
**Input:**
```text
parcels = [1, 2, 3]
extra_parcels = 3
```
**Output:**
```text
3
```
**Explanation:**  
We can distribute the 3 extra parcels as `+2` to the first agent and `+1` to the second agent, resulting in `[3, 3, 3]`. The maximum value is 3.

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

##### Python Implementation
```python
def getMinMaxParcels(parcels, extra_parcels):
    n = len(parcels)
    total_sum = sum(parcels) + extra_parcels
    # Ceiling division for integer average
    avg = (total_sum + n - 1) // n
    return max(max(parcels), avg)
```

##### C++ Implementation
```cpp
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long getMinMaxParcels(const vector<int>& parcels, long long extra_parcels) {
        int n = parcels.size();
        long long total_sum = extra_parcels;
        int max_val = 0;
        
        for (int p : parcels) {
            total_sum += p;
            max_val = max(max_val, p);
        }
        
        long long avg = (total_sum + n - 1) / n;
        return max((long long)max_val, avg);
    }
};
```

---

### Q5. AWS Outlier Detection

**Topic:** `arrays`, `hash-map`, `math`

**Question:**  
AWS provides many services for outlier detection. A prototype small service to detect an outlier in an array of integers is under development.

Given an array of `n` integers, there are `(n - 2)` normal numbers and the sum of the `(n - 2)` numbers originally in this array. If a number is neither in the original numbers nor is it their sum, it is an outlier. Discover the potential outliers and return the greatest of them.

Note: It is guaranteed that the answer exists.

#### Input
- `arr`: list of integers

#### Constraints
- $3 \le n \le 10^5$
- $1 \le arr[i] \le 10^9$

#### Example 1
**Input:**
```text
arr = [4, 1, 3, 16, 2, 10]
```
**Output:**
```text
16
```
**Explanation:**  
The potential outliers are:
- `16`: Removing `16` leaves `[4, 1, 3, 2, 10]`. The sum of `[4, 1, 3, 2]` is `10`. So `16` is a potential outlier.
- `4`: Removing `4` leaves `[1, 3, 16, 2, 10]`. The sum of `[1, 3, 2, 10]` is `16`. So `4` is a potential outlier.

The maximum outlier is `16`.

#### Example 2
**Input:**
```text
arr = [2, 2, 4, 2]
```
**Output:**
```text
2
```
**Explanation:**  
The only potential outlier is `2`. Removing it leaves `[2, 4, 2]`, where the sum of `[2, 2]` is `4`.

---

#### Solution

##### Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ for frequency counts.

##### Python Implementation
```python
def getOutlierValue(arr):
    total_sum = sum(arr)
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    max_outlier = float('-inf')
    
    for y in arr:
        # y is the assumed sum element
        # outlier x must satisfy: 2*y + x = total_sum => x = total_sum - 2*y
        x = total_sum - 2 * y
        
        if x in freq:
            # If outlier and sum element are equal, we need at least 2 occurrences
            if x == y:
                if freq[y] >= 2:
                    max_outlier = max(max_outlier, x)
            else:
                max_outlier = max(max_outlier, x)
                
    return max_outlier
```

##### C++ Implementation
```cpp
#include <vector>
#include <unordered_map>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getOutlierValue(const vector<int>& arr) {
        long long total_sum = 0;
        unordered_map<long long, int> freq;
        for (int num : arr) {
            total_sum += num;
            freq[num]++;
        }
        
        long long max_outlier = -1;
        for (int y : arr) {
            long long x = total_sum - 2LL * y;
            if (freq.count(x)) {
                if (x == y) {
                    if (freq[y] >= 2) {
                        max_outlier = max(max_outlier, x);
                    }
                } else {
                    max_outlier = max(max_outlier, x);
                }
            }
        }
        
        return max_outlier;
    }
};
```
