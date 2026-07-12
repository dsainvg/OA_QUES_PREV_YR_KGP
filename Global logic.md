# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Bills Bundle

**Topic:** `dynamic-programming`, `interval-dp`, `arrays`

Given a bundle of bills containing $N$ banknotes, each banknote ranging from 1 to 1000 dollars, represented by an array $A = [A_1, A_2, \dots, A_N]$.
If two banknotes have the same value $X$, one after the other, you can remove both banknotes and replace them with a single note with the value $X + 1$. This operation will reduce the size of the bundle by 1.

Find the minimum number of banknotes in the bundle you can obtain after performing such operations a certain number of times.

#### Constraints
* $1 \le N \le 400$
* $1 \le A[i] \le 1000$

#### Input Format
* The first line contains an integer $N$, denoting the number of denominations.
* The next line contains $N$ space-separated integers, denoting the notes.

#### Output Format
* The output contains an integer denoting the minimum number of banknotes in the bundle you can obtain after performing the given operations a certain number of times.

#### Sample Input
```
3
4 3 3
```

#### Sample Output
```
1
```

#### Explanation
* $N = 3$
* $A = [4, 3, 3]$
* For banknotes at index 2 and 3 (the two 3s), we can replace them with 4, which makes the bundle $[4, 4]$.
* For the new bundle, we can replace the notes at index 1 and 2 (the two 4s) with a single banknote of value 5. The bundle size becomes 1.
* Hence, the output is 1.

```python
def bankNotes(N, A):
    # dp[i][j] represents the minimum size of the subarray A[i..j] after optimal merges.
    # val[i][j] represents the value of the single banknote that A[i..j] can be reduced to,
    # or -1 if A[i..j] cannot be reduced to a single banknote.
    dp = [[0] * N for _ in range(N)]
    val = [[-1] * N for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = 1
        val[i][i] = A[i]
        
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            dp[i][j] = length  # Initialize to max possible size (no merges)
            
            for k in range(i, j):
                # Check if we can merge the left and right halves into a single banknote.
                # This is possible if both halves can be reduced to a single banknote each
                # and those two banknotes have the same value.
                if val[i][k] != -1 and val[i][k] == val[k+1][j]:
                    dp[i][j] = 1
                    val[i][j] = val[i][k] + 1
                    break
                else:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
                    
    return dp[0][N-1]
```

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int bankNotes(int N, int A[]) {
    vector<vector<int>> dp(N, vector<int>(N, 0));
    vector<vector<int>> val(N, vector<int>(N, -1));
    
    for (int i = 0; i < N; ++i) {
        dp[i][i] = 1;
        val[i][i] = A[i];
    }
    
    for (int length = 2; length <= N; ++length) {
        for (int i = 0; i <= N - length; ++i) {
            int j = i + length - 1;
            dp[i][j] = length;
            
            for (int k = i; k < j; ++k) {
                if (val[i][k] != -1 && val[i][k] == val[k+1][j]) {
                    dp[i][j] = 1;
                    val[i][j] = val[i][k] + 1;
                    break;
                } else {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]);
                }
            }
        }
    }
    
    return dp[0][N-1];
}
```

---

### Q2. Linked List: Odd-Even

**Topic:** `simulation`, `arrays`, `game-theory`

Two players are playing a game with a list of integers represented through a linked list (or array) of size $N$.
They take turns alternatively, with player 1 playing first. Player 1 takes away the first number in the list.
If the number taken by a player is odd, then the next player will take away the last number from the current list.
If the number taken by a player is even, then the next player will take away the first number from the current list.
This continues until the list is empty. This game will come to an end in exactly $N$ moves.
The score of a player is the sum of all numbers taken away by him during the entire game.
The winner is the player having a higher score. If both players end with the same score, it's a DRAW.

Given the list of numbers, print the score of the winning player, and if it is a DRAW, print 0.

#### Input Format
* The first line contains the integer $N$ denoting the size of the list.
* The next line contains $N$ space-separated integers of array $A$, denoting integers in the list.

#### Output Format
* The output contains a single integer denoting the score of the winning player, or 0 if it is a DRAW.

#### Sample Input
```
6
1 2 3 4 5 6
```

#### Sample Output
```
13
```

#### Explanation
* First Move: Player 1 takes 1 (first element). Remaining: `[2, 3, 4, 5, 6]`. Player 1 score: 1.
* Second Move: Since 1 is odd, Player 2 takes 6 (last element). Remaining: `[2, 3, 4, 5]`. Player 2 score: 6.
* Third Move: Since 6 is even, Player 1 takes 2 (first element). Remaining: `[3, 4, 5]`. Player 1 score: 1 + 2 = 3.
* Fourth Move: Since 2 is even, Player 2 takes 3 (first element). Remaining: `[4, 5]`. Player 2 score: 6 + 3 = 9.
* Fifth Move: Since 3 is odd, Player 1 takes 5 (last element). Remaining: `[4]`. Player 1 score: 3 + 5 = 8.
* Sixth Move: Since 5 is odd, Player 2 takes 4 (last element). Remaining: `[]`. Player 2 score: 9 + 4 = 13.
* Final Scores: Player 1 = 8, Player 2 = 13.
* Winner score = 13.

```python
def oddEven(N, A):
    if N == 0:
        return 0
        
    left = 0
    right = N - 1
    p1_score = 0
    p2_score = 0
    
    # First move: Player 1 takes the first number
    val = A[left]
    left += 1
    p1_score += val
    
    turn = 2
    
    while left <= right:
        if val % 2 != 0:
            # Odd: take from the end (right)
            val = A[right]
            right -= 1
        else:
            # Even: take from the front (left)
            val = A[left]
            left += 1
            
        if turn == 1:
            p1_score += val
            turn = 2
        else:
            p2_score += val
            turn = 1
            
    if p1_score > p2_score:
        return p1_score
    elif p2_score > p1_score:
        return p2_score
    else:
        return 0
```

```javascript
function oddEven(N, A) {
    if (N === 0) return 0;
    
    let left = 0;
    let right = N - 1;
    let p1_score = 0;
    let p2_score = 0;
    
    // Player 1 takes the first number
    let val = A[left];
    left++;
    p1_score += val;
    
    let turn = 2;
    
    while (left <= right) {
        if (val % 2 !== 0) {
            // Odd: take from the end (right)
            val = A[right];
            right--;
        } else {
            // Even: take from the front (left)
            val = A[left];
            left++;
        }
        
        if (turn === 1) {
            p1_score += val;
            turn = 2;
        } else {
            p2_score += val;
            turn = 1;
        }
    }
    
    if (p1_score > p2_score) {
        return p1_score;
    } else if (p2_score > p1_score) {
        return p2_score;
    } else {
        return 0;
    }
}
```
