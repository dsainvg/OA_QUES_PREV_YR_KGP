# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Hugo*
*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Searching Challenge (Bracket Matching)

**Topic:** `Strings`, `Stack`, `Parentheses`  

Have the function `SearchingChallenge(str)` take the `str` parameter being passed and return `"1"` if the brackets are correctly matched and each one is accounted for. Otherwise return `"0"`. For example: if `str` is `"(hello (world))"`, then the output should be `"1"`, but if `str` is `"((hello (world))"` the output should be `"0"` because the brackets do not correctly match up. Only `(` and `)` will be used as brackets. If `str` contains no brackets, return `"1"`.

#### Examples
- **Input:** `"(coder)(byte))"`  
  **Output:** `"0"`
- **Input:** `"(c(oder)) b(yte)"`  
  **Output:** `"1"`

```cpp
#include <iostream>
#include <string>
using namespace std;

string SearchingChallenge(string str) {
    int count = 0;
    for (char c : str) {
        if (c == '(') {
            count++;
        } else if (c == ')') {
            count--;
            if (count < 0) {
                return "0";
            }
        }
    }
    return count == 0 ? "1" : "0";
}
```

- **Time Complexity:** $O(N)$ where $N$ is the length of the string.
- **Space Complexity:** $O(1)$ auxiliary space.

---

### Q2. Array Challenge (Tetris Simulation)

**Topic:** `Arrays`, `Simulation`, `Tetris`  

Have the function `ArrayChallenge(strArr, arrLength)` take `strArr` parameter which will be an array containing one letter representing a Tetris piece (`I`, `J`, `L`, `O`, `S`, `T`, `Z`), followed by 12 numbers representing the fill levels for the 12 columns of the board. Calculate the greatest number of horizontal lines that can be completed when the piece arrives at the bottom, assuming it is dropped immediately after being rotated and moved horizontally from the top. Tricky combinations of vertical and horizontal movements are excluded. The piece types are represented by capital letters.

#### Examples
- **Input:** `{"L", "3", "4", "4", "5", "6", "2", "0", "6", "5", "3", "6", "6"}`  
  **Output:** `3`  
  **Explanation:** The board has 12 columns. The `L` piece can be rotated and dropped in columns 6–7 which will complete 3 full rows of blocks.
- **Input:** `{"I", "2", "4", "3", "4", "5", "2", "0", "2", "2", "3", "3", "3"}`  
  **Output:** `2`
- **Input:** `{"O", "4", "3", "2", "3", "5", "1", "0", "1", "2", "4", "3", "4"}`  
  **Output:** `0`

```python
def get_rotations(blocks):
    rotations = []
    current = list(blocks)
    for _ in range(4):
        # Rotate 90 degrees clockwise
        rotated = [(y, -x) for x, y in current]
        # Normalize: shift to start at 0
        min_x = min(x for x, y in rotated)
        min_y = min(y for x, y in rotated)
        normalized = sorted([(x - min_x, y - min_y) for x, y in rotated])
        if normalized not in rotations:
            rotations.append(normalized)
        current = normalized
    return rotations

def ArrayChallenge(strArr: list[str]) -> int:
    piece_type = strArr[0]
    board_heights = [int(x) for x in strArr[1:]]
    
    shapes = {
        'I': [(0,0), (0,1), (0,2), (0,3)],
        'O': [(0,0), (0,1), (1,0), (1,1)],
        'T': [(0,0), (1,0), (2,0), (1,1)],
        'S': [(0,0), (1,0), (1,1), (2,1)],
        'Z': [(0,1), (1,1), (1,0), (2,0)],
        'J': [(0,0), (1,0), (1,1), (1,2)],
        'L': [(0,0), (0,1), (0,2), (1,0)]
    }
    
    base_blocks = shapes[piece_type]
    rotations = get_rotations(base_blocks)
    
    max_lines = 0
    
    for rotation in rotations:
        # Find width of this rotation
        w = max(x for x, y in rotation) + 1
        # Try placing at each column c
        for c in range(12 - w + 1):
            # Initialize board grid
            grid = [[False]*12 for _ in range(30)]
            for col in range(12):
                for row in range(board_heights[col]):
                    grid[row][col] = True
                    
            # Simulate drop
            y = 20
            while y >= 0:
                overlap = False
                for dx, dy in rotation:
                    if y + dy < 0 or grid[y + dy][c + dx]:
                        overlap = True
                        break
                if overlap:
                    break
                y -= 1
            y_land = y + 1
            
            # Place piece
            for dx, dy in rotation:
                grid[y_land + dy][c + dx] = True
                
            # Count completed lines
            completed = 0
            for row in range(30):
                if all(grid[row]):
                    completed += 1
            max_lines = max(max_lines, completed)
            
    return max_lines
```

- **Time Complexity:** $O(\text{Rotations} \times C \times \text{Height} \times \text{Blocks}) = O(4 \times 12 \times 20 \times 4) \approx O(1)$ operations, which is extremely fast.
- **Space Complexity:** $O(\text{Height} \times C) \approx O(1)$ space.
