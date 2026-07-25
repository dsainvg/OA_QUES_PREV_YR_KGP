# Interview Questions
*Total questions: 2*

---

## Table of Contents
- [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Word Grid Puzzle

**Topic:** `Matrix`, `String Matching`

Akash had recently bought a puzzle book. Each page in the book has a word puzzle in which a grid of letters from the English Alphabet (uppercase or lowercase) or digits between 0-9 are given. Akash has to figure out the number of occurrences of a particular word in the given grid. The grid is always a square, and the word can be present in any direction in the grid i.e. left to right, right to left, top to bottom, bottom to top, and the diagonals. Palindromic words (words which are read the same as the original word in the opposite direction too) if present in the grid will be counted twice.

Write a program to help Akash. Read the input from STDIN and print the output to STDOUT. Do not write arbitrary strings anywhere in the program, as these contribute to the standard output and testcases will fail.

**Input Format:**
- The first line of input has $N$, which is the number of rows/columns in the grid.
- The next $N$ lines each contain $N$-characters (alphabets or digits).
- The last line contains the word whose number of occurrences has to be found out.

**Output Format:**
- The output has the number of occurrences of the given word in the grid.

**Constraints:**
- $N \ge 3$

**Sample Input 1:**
```
3
ctt
cat
cct
cat
```

**Sample Output 1:**
```
4
```

**Explanation 1:**
Size of the grid, $N = 3$. The grid is:
```
c t t
c a t
c c t
```
The word `cat` occurs 4 times:
1. Horizontal (Row 1): `cat` (from (1,0) to (1,2))
2. Main Diagonal: `cat` (from (0,0) to (2,2))
3. Anti-Diagonal: `cat` (from (2,0) to (0,2))
4. Column 1 (Bottom to Top): `cat` (from (2,1) to (0,1))

**Sample Input 2:**
```
5
Jsmpu
spmuj
Pmjus
jumsp
ujpsM
jump
```

**Sample Output 2:**
```
2
```

**Explanation 2:**
Size of the grid, $N = 5$. The word `jump` occurs 2 times:
1. Row 1 (Right to Left): `jump` (from (1,4) to (1,1))
2. Column 1 (Bottom to Top): `jump` (from (4,1) to (1,1))

```python
import sys

def count_word_occurrences(grid, word):
    if not grid or not word:
        return 0
    R = len(grid)
    C = len(grid[0])
    L = len(word)
    count = 0
    
    # 8 possible directions
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (-1, -1), # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)   # Up-Right
    ]
    
    for r in range(R):
        for c in range(C):
            for dr, dc in directions:
                match = True
                for k in range(L):
                    nr, nc = r + dr * k, c + dc * k
                    if not (0 <= nr < R and 0 <= nc < C) or grid[nr][nc] != word[k]:
                        match = False
                        break
                if match:
                    count += 1
    return count

def main():
    # Read all lines from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # Parse N
    try:
        N = int(input_data[0].strip())
    except ValueError:
        return
        
    grid = []
    for i in range(1, N + 1):
        if i < len(input_data):
            grid.append(input_data[i].strip())
            
    if N + 1 < len(input_data):
        word = input_data[N + 1].strip()
    else:
        word = ""
        
    result = count_word_occurrences(grid, word)
    print(result)

if __name__ == '__main__':
    main()
```

---

### Q2. Super Nodes in a Binary Tree

**Topic:** `Tree`, `Depth First Search`

A binary tree is represented as a series of relationships between each node and the Root node. The relationships are denoted as combinations of 'L' and 'R', such as L, R, LL, LR, and so on, where each node is left (L) to Root or left-left (LL) or right-left (RL) to the Root node and so on.

In this tree, if the sum of digits of the left child node is equal to the sum of digits of the right child node, then their parent is called a **Super Node**.

Write a program to find all the Super Nodes in a given tree, and print the sum of all those Super nodes.

Read the input from STDIN and print the output to STDOUT. Do not write arbitrary strings anywhere in the program, as these contribute to the standard output and testcases will fail.

**Input Format:**
- The first line of input contains $N$, the number of nodes in the tree.
- The second line of input contains the value of the Root node.
- The next $N-1$ lines of input contain a string $S$ and an integer $X$, separated by a single white space, where $X$ is a node in the tree and $S$ is the relation (path) between the Root node and $X$.

**Output Format:**
- The output contains an integer, which is the sum of all Super Nodes.

**Constraints:**
- $3 \le N \le 100$

**Sample Input 1:**
```
8
21
L 14
R 23
LL 7
LR 70
RR 11
RRL 23
RRR 32
```

**Sample Output 1:**
```
46
```

**Explanation 1:**
The tree can be represented as follows:
```
        21
       /  \
     14    23
    /  \     \
   7   70     11
             /  \
            23  32
```
- Left child of `21` is `14` (digit sum = $1+4=5$) and Right child of `21` is `23` (digit sum = $2+3=5$). Since $5 = 5$, `21` is a Super Node.
- Left child of `14` is `7` (digit sum = $7$) and Right child is `70` (digit sum = $7+0=7$). Since $7 = 7$, `14` is a Super Node.
- Left child of `11` is `23` (digit sum = $2+3=5$) and Right child is `32` (digit sum = $3+2=5$). Since $5 = 5$, `11` is a Super Node.
- Other nodes do not have two child nodes, hence they cannot be Super Nodes.
- Sum of Super Nodes = $21 + 14 + 11 = 46$.

**Sample Input 2:**
```
6
11
L 14
R 23
LL 7
LR 8
RR 14
```

**Sample Output 2:**
```
11
```

**Explanation 2:**
The tree can be represented as follows:
```
        11
       /  \
     14    23
    /  \     \
   7    8     14
```
- Children of `11` are `14` (digit sum = $5$) and `23` (digit sum = $5$). Equal, so `11` is a Super Node.
- Children of `14` are `7` and `8`. $7 \neq 8$, so `14` is not a Super Node.
- Node `23` only has a right child (`14`), so it cannot be a Super Node.
- Only `11` is the Super Node, hence the sum is `11`.

```python
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def main():
    # Read all non-empty lines from standard input
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return
    
    try:
        N = int(lines[0])
    except ValueError:
        return
    
    if len(lines) < 2:
        return
        
    root_val = int(lines[1])
    nodes = {"": TreeNode(root_val)}
    
    # Read the N-1 relationships
    for i in range(2, min(2 + N - 1, len(lines))):
        parts = lines[i].split()
        if len(parts) == 2:
            path = parts[0]
            val = int(parts[1])
            nodes[path] = TreeNode(val)
            
    # Link nodes to form the binary tree
    for path, node in nodes.items():
        if path == "":
            continue
        parent_path = path[:-1]
        if parent_path in nodes:
            parent = nodes[parent_path]
            if path[-1] == 'L':
                parent.left = node
            elif path[-1] == 'R':
                parent.right = node
                
    # Traverse tree and sum Super Nodes
    super_nodes_sum = 0
    def dfs(curr):
        nonlocal super_nodes_sum
        if not curr:
            return
        if curr.left and curr.right:
            if digit_sum(curr.left.val) == digit_sum(curr.right.val):
                super_nodes_sum += curr.val
        dfs(curr.left)
        dfs(curr.right)
        
    dfs(nodes[""])
    print(super_nodes_sum)

if __name__ == '__main__':
    main()
```
