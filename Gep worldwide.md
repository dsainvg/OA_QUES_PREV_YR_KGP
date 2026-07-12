# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Gep worldwide*
*Total questions: 1*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Game of String Distribution

**Topic:** `Strings`, `Greedy`, `Sorting`, `Recursion`  

Joe has organized a party for `M` guests and has planned a party game. In the game, Joe gives everyone a string `S` and explains to them the rules to play the game. The rules to play the game are as follows:
- You need to distribute the string `S` amongst `M` guests in such a way that each guest gets at least one character.
- Compare all the strings and store the smallest lexicographical string among that distribution.
- Out of all the stored strings, find the largest lexicographical string which is the strongest string.

Your task is to find and return the strongest string among all smallest lexicographic strings that are stored for every distribution.

#### Function description
Complete the `strongString` function. This function takes the following 2 parameters and returns a string:
- `input1`: An integer `M`, representing the number of guests.
- `input2`: A string `S`, representing the string from which the characters are to be distributed.

#### Constraints
- $1 \le M \le |S| \le 10^5$
- $S$ contains only lowercase English letters.

#### Example 1
**Input:**  
- `input1: 3`  
- `input2: good`  
**Output:** `gd`  
**Explanation:**  
- The possible distributions of `"good"` among 3 guests are: `[("o", "o", "dg"), ("oo", "d", "g"), ("o", "do", "g"), ("o", "d", "go"), ("o", "d", "og"), ("o", "gd", "o"), ("o", "od", "g")]`.
- The lexicographically smallest strings for each distribution are `["dg", "d", "do", "d", "d", "gd", "g"]`.
- The lexicographically largest (strongest) among these is `"gd"`.

#### Example 2
**Input:**  
- `input1: 4`  
- `input2: abacadae`  
**Output:** `baaaa`  
**Explanation:**  
- One way to distribute `"abacadae"` among 4 guests is `["e", "d", "c", "baaaa"]`.
- The minimum string in this distribution is `"baaaa"`. This is the maximum possible minimum string we can obtain across all distributions.

#### Solution Explanation
We want to partition the multiset of characters of `S` into `M` strings to maximize the lexicographically smallest string.
Let the distinct characters in `S` be sorted in ascending order.
1. If $M = 1$, the best we can do is to sort the entire string in descending order.
2. Let $c$ be the largest character in `S` and $C$ be its frequency.
3. If $C < M$:
   - We cannot start all $M$ strings with $c$. To make the starting characters as large as possible, we must choose the $M$ largest characters from `S` as the starts.
   - The smallest of these $M$ starts will determine the lexicographical value of the minimum string.
   - To make this minimum string as large as possible, we should append all remaining characters to it in descending order.
4. If $C \ge M$:
   - All $M$ strings can start with $c$.
   - Since all strings share the common prefix $c$, the problem of maximizing the minimum of $c + T_i$ is equivalent to maximizing the minimum of $T_i$ on the remaining characters.
   - Thus, we can recursively solve the problem with $M$ and the remaining characters, prepending $c$ to the result.

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper functions to compare characters for qsort
int cmp_char_asc(const void* a, const void* b) {
    return (*(char*)a - *(char*)b);
}

int cmp_char_desc(const void* a, const void* b) {
    return (*(char*)b - *(char*)a);
}

void solve_rec(char* chars, int len, int M, char* res, int* res_len) {
    if (len < M) {
        return;
    }
    if (M == 1) {
        qsort(chars, len, sizeof(char), cmp_char_desc);
        memcpy(res + *res_len, chars, len);
        *res_len += len;
        return;
    }
    
    // Find max char
    char max_c = chars[0];
    for (int i = 1; i < len; i++) {
        if (chars[i] > max_c) {
            max_c = chars[i];
        }
    }
    
    // Count frequency of max char
    int count = 0;
    for (int i = 0; i < len; i++) {
        if (chars[i] == max_c) {
            count++;
        }
    }
    
    if (count < M) {
        qsort(chars, len, sizeof(char), cmp_char_asc);
        res[(*res_len)++] = chars[len - M];
        
        int rem_len = len - M;
        if (rem_len > 0) {
            qsort(chars, rem_len, sizeof(char), cmp_char_desc);
            memcpy(res + *res_len, chars, rem_len);
            *res_len += rem_len;
        }
    } else {
        res[(*res_len)++] = max_c;
        
        char* next_chars = (char*)malloc(len * sizeof(char));
        int next_len = 0;
        int removed = 0;
        for (int i = 0; i < len; i++) {
            if (chars[i] == max_c && removed < M) {
                removed++;
            } else {
                next_chars[next_len++] = chars[i];
            }
        }
        solve_rec(next_chars, next_len, M, res, res_len);
        free(next_chars);
    }
}

char* strongString(int input1, char* input2) {
    int len = strlen(input2);
    char* chars = (char*)malloc((len + 1) * sizeof(char));
    strcpy(chars, input2);
    
    char* res = (char*)calloc(len + 1, sizeof(char));
    int res_len = 0;
    
    solve_rec(chars, len, input1, res, &res_len);
    res[res_len] = '\0';
    
    free(chars);
    return res;
}
```

```python
# Python 3 Equivalent Solution
def solve(chars, M):
    if len(chars) < M:
        return ""
    if M == 1:
        return "".join(sorted(chars, reverse=True))
        
    c = max(chars)
    count = chars.count(c)
    
    if count < M:
        sorted_chars = sorted(chars)
        starts = sorted_chars[-M:]
        remaining = sorted_chars[:-M]
        return starts[0] + "".join(sorted(remaining, reverse=True))
    else:
        remaining_chars = list(chars)
        for _ in range(M):
            remaining_chars.remove(c)
        return c + solve(remaining_chars, M)

def strongString(input1: int, input2: str) -> str:
    return solve(list(input2), input1)
```

- **Time Complexity:** $O(N \log N)$ where $N$ is the length of string `S`, due to sorting characters at each step.
- **Space Complexity:** $O(N)$ auxiliary space for recursion stack and substring allocation.
