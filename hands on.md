# Interview Questions

*Total questions: 12*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [MCQs](#mcqs)

---

## Coding Questions

### Q1. Rolling a Dice

**Topic:** `Simulation`, `3D Rotation`, `Matrix Traversal`  

A standard 6-sided dice starts at position $(0, 0)$ of an $R \times C$ grid. The top face is initially 1, the front face is 2, and the right face is 3. Since it is a standard dice, the sum of opposite faces is 7 (so bottom = 6, back = 5, left = 4).

The dice rolls from cell to cell. It traverses the grid in a boustrophedon (snake) pattern starting from $(0, 0)$:
- On row 0, it rolls East until column $C-1$.
- It rolls South to row 1, column $C-1$.
- On row 1, it rolls West until column 0.
- It rolls South to row 2, column 0.
- On row 2, it rolls East until column $C-1$.
- This snake pattern continues until the last cell of row $R-1$ is reached.

At each cell it visits (including the starting cell $(0,0)$), we add the value of its top face to a running sum. Write a function `calculateCubeSum(int R, int C)` to return the total sum of the top faces.

**Constraints:**
- $1 \le R, C \le 1000$

#### Sample Input 1
```
3 2
```

#### Sample Output 1
```
19
```

#### Sample Input 2
```
3 4
```

#### Sample Output 2
```
42
```

#### Solution (Python)
```python
def calculateCubeSum(R: int, C: int) -> int:
    # Initial state of the dice
    top, front, right = 1, 2, 3
    
    total_sum = top
    
    for r in range(R):
        # Roll within the row (C - 1 steps)
        for _ in range(C - 1):
            if r % 2 == 0:
                # Roll East: 
                # new_top comes from left (7 - right)
                # new_right comes from top
                # front remains unchanged
                top, right = 7 - right, top
            else:
                # Roll West: 
                # new_top comes from right
                # new_right comes from bottom (7 - top)
                # front remains unchanged
                top, right = right, 7 - top
            total_sum += top
            
        # Roll South to the next row (1 step)
        if r < R - 1:
            # Roll South: 
            # new_top comes from back (7 - front)
            # new_front comes from top
            # right remains unchanged
            top, front = 7 - front, top
            total_sum += top
            
    return total_sum
```

#### Solution (C++)
```cpp
#include <iostream>

int calculateCubeSum(int R, int C) {
    int top = 1, front = 2, right = 3;
    int total_sum = top;
    
    for (int r = 0; r < R; ++r) {
        for (int step = 0; step < C - 1; ++step) {
            if (r % 2 == 0) {
                // Roll East
                int next_top = 7 - right;
                right = top;
                top = next_top;
            } else {
                // Roll West
                int next_top = right;
                right = 7 - top;
                top = next_top;
            }
            total_sum += top;
        }
        if (r < R - 1) {
            // Roll South
            int next_top = 7 - front;
            front = top;
            top = next_top;
            total_sum += top;
        }
    }
    return total_sum;
}
```

---

### Q2. Salary Fluctuations

**Topic:** `Trees`, `Data Structures`, `Design`  

An organization has $N$ employees numbered $1$ to $N$. Employee $1$ is the CEO and has no supervisor. Every other employee has a unique immediate supervisor, forming a tree structure.

Each employee starts with an initial salary. We need to support two types of operations over $M$ operations:
1. `p u val`: Employee `u` modifies the salary of all their *immediate* subordinates by adding `val` (can be positive or negative).
2. `u u_id`: Print the current salary of employee `u_id`.

**Input Format:**
- The first line contains $N$ and $M$.
- The second line contains the salary of employee 1.
- The next $N - 1$ lines contain the salary and supervisor ID for employee $i$ (from $2$ to $N$).
- The next $M$ lines contain the operations.

**Output Format:**
- Print the salary for each query operation on a new line.

#### Sample Input
```
5 5
600
400 1
200 1
500 1
300 4
u 2
p 1 -200
u 5
p 3 500
u 4
```

#### Sample Output
```
400
300
300
```

#### Solution (Python)
```python
import sys

def solve_salary_fluctuations():
    # Read N and M
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    salaries = [0] * (N + 1)
    parent = [0] * (N + 1)
    
    # Employee 1
    salaries[1] = int(input_data[2])
    parent[1] = None
    
    idx = 3
    for i in range(2, N + 1):
        salaries[i] = int(input_data[idx])
        parent[i] = int(input_data[idx + 1])
        idx += 2
        
    parent_updates = [0] * (N + 1)
    
    # Process M operations
    for _ in range(M):
        op_type = input_data[idx]
        if op_type == 'p':
            u = int(input_data[idx + 1])
            val = int(input_data[idx + 2])
            parent_updates[u] += val
            idx += 3
        elif op_type == 'u':
            u_id = int(input_data[idx + 1])
            p = parent[u_id]
            curr_salary = salaries[u_id]
            if p is not None:
                curr_salary += parent_updates[p]
            print(curr_salary)
            idx += 2

if __name__ == '__main__':
    solve_salary_fluctuations()
```

#### Complexity Analysis
- **Time Complexity:** 
  - **Update (`p u val`):** $O(1)$ time by accumulating updates on the parent node.
  - **Query (`u u_id`):** $O(1)$ time by retrieving `initial_salary + parent_updates[parent[u_id]]`.
  - **Overall:** $O(N + M)$ for parsing input and executing all operations.
- **Space Complexity:** $O(N)$ auxiliary space to store parent pointers, initial salaries, and accumulated updates.

---

## MCQs

### Q3. Divisibility Test

**Topic:** `Probability`, `Modular Arithmetic`  

If the integers $m$ and $n$ are chosen at random between 1 and 50 (inclusive, with replacement), then the probability that a number of the form $4^m + 4^n$ is divisible by 5 is:

**Options:**
- A) $2/3$
- B) $5/26$
- C) $1/2$
- D) $1/24$

**Correct Answer:** C) $1/2$

**Explanation:**
The power of 4 modulo 5 behaves as follows:
- If $k$ is odd, $4^k \equiv 4 \pmod 5$.
- If $k$ is even, $4^k \equiv 1 \pmod 5$.

For $4^m + 4^n$ to be divisible by 5, we need $4^m + 4^n \equiv 0 \pmod 5$. Let's examine the possible combinations of parities for $m$ and $n$:
- Both $m, n$ are odd: $4 + 4 = 8 \equiv 3 \pmod 5$ (not divisible)
- Both $m, n$ are even: $1 + 1 = 2 \equiv 2 \pmod 5$ (not divisible)
- $m$ is odd and $n$ is even: $4 + 1 = 5 \equiv 0 \pmod 5$ (divisible)
- $m$ is even and $n$ is odd: $1 + 4 = 5 \equiv 0 \pmod 5$ (divisible)

Since the range $[1, 50]$ contains exactly 25 odd and 25 even integers, the probability that any selected integer is odd or even is exactly $1/2$.
Thus, the probability of selecting one odd and one even integer is:
$$P(\text{odd}) \times P(\text{even}) + P(\text{even}) \times P(\text{odd}) = \left(\frac{1}{2} \times \frac{1}{2}\right) + \left(\frac{1}{2} \times \frac{1}{2}\right) = \frac{1}{2}$$

---

### Q4. Possible Numbers

**Topic:** `Combinatorics`, `Stars and Bars`  

Sum of the digits of a six-digit number is 50. How many such six-digit numbers are possible?

**Options:**
- A) $36$
- B) $60$
- C) $120$
- D) $126$

**Correct Answer:** D) $126$

**Explanation:**
Let the 6-digit number be represented as $d_1 d_2 d_3 d_4 d_5 d_6$, where:
- $1 \le d_1 \le 9$ (since it is a 6-digit number, the leading digit cannot be 0)
- $0 \le d_i \le 9$ for $i \in \{2, 3, 4, 5, 6\}$
- $\sum_{i=1}^6 d_i = 50$

To find the number of non-negative integer solutions, we define the slack variable $x_i = 9 - d_i$ representing how far each digit is from its maximum value of 9:
- For $d_1 \ge 1 \implies x_1 \le 8$
- For $d_i \ge 0 \implies x_i \le 9$ for $i \ge 2$
- $x_i \ge 0$ for all $i$

Substituting $d_i = 9 - x_i$ into the sum equation:
$$(9 - x_1) + (9 - x_2) + (9 - x_3) + (9 - x_4) + (9 - x_5) + (9 - x_6) = 50$$
$$54 - \sum_{i=1}^6 x_i = 50 \implies \sum_{i=1}^6 x_i = 4$$

Since the sum of $x_i$ is 4, none of the upper bounds ($x_1 \le 8$ and $x_i \le 9$) can possibly be violated. Thus, the problem reduces to finding the number of non-negative integer solutions to $\sum_{i=1}^6 x_i = 4$.
Using the Stars and Bars formula:
$$\text{Number of solutions} = \binom{N + K - 1}{K - 1} = \binom{4 + 6 - 1}{6 - 1} = \binom{9}{5} = 126$$

---

### Q5. Anand VS Carlsen

**Topic:** `Probability`, `Binomial Distribution`  

Anand is playing a 9-match rapid exhibition against Carlsen. On average, Anand's probability of winning a game against Carlsen is $0.75$. If Anand is $3-2$ down after 5 games and there are no ties, then what is the probability that Anand will win the championship?

**Options:**
- A) $198/265$
- B) $59/263$
- C) $189/256$
- D) $53/144$

**Correct Answer:** C) $189/256$

**Explanation:**
- The championship consists of 9 games. The player who wins at least 5 games wins the championship.
- Currently, after 5 games, Anand is $3-2$ down, meaning Anand has won 2 games and Carlsen has won 3 games.
- There are $9 - 5 = 4$ games remaining.
- For Anand to win the championship, he needs to reach at least 5 wins. Since he already has 2 wins, he must win at least $5 - 2 = 3$ of the remaining 4 games.
- Let $X$ be the number of games Anand wins out of the remaining 4. The probability of Anand winning any single game is $p = 0.75 = 3/4$, and losing is $q = 1/4$.
- $X$ follows a Binomial distribution $X \sim \text{Binomial}(n=4, p=3/4)$.
- We need to compute $P(X \ge 3) = P(X = 3) + P(X = 4)$:
  $$P(X = 3) = \binom{4}{3} \left(\frac{3}{4}\right)^3 \left(\frac{1}{4}\right)^1 = 4 \times \frac{27}{64} \times \frac{1}{4} = \frac{108}{256}$$
  $$P(X = 4) = \binom{4}{4} \left(\frac{3}{4}\right)^4 \left(\frac{1}{4}\right)^0 = 1 \times \frac{81}{256} \times 1 = \frac{81}{256}$$
  $$P(X \ge 3) = \frac{108}{256} + \frac{81}{256} = \frac{189}{256}$$

---

### Q6. Java Function Parameters

**Topic:** `Java`, `OOP`, `Method Overloading`  

What will be the output of the program given below?

```java
class Vehicle {
    void drive(Vehicle v) {
        System.out.print("Vehicle");
    }
}
class Car extends Vehicle {
    void drive(Car c) {
        System.out.print("Car");
    }
}
class Bike extends Car {
    void drive(Bike b) {
        System.out.print("Bike");
    }
}
public class Main {
    public static void main(String[] args) {
        Vehicle vehicle1 = new Vehicle();
        Car car = new Car();
        Bike bike = new Bike();
        Bike bike1 = new Bike();
        bike1.drive(vehicle1);
        bike1.drive(car);
        bike1.drive(bike);
    }
}
```

**Options:**
- A) `VehicleCarBike`
- B) `CarBikeVehicle`
- C) `VehicleBikeCar`
- D) `Compile time error`

**Correct Answer:** A) `VehicleCarBike`

**Explanation:**
- In Java, overloaded methods are resolved at compile-time based on the static types of the arguments.
- `bike1` has type `Bike`.
- `bike1.drive(vehicle1)`: `vehicle1` has static type `Vehicle`. `Bike` inherits `drive(Vehicle)` from `Vehicle`. The compile-time resolved method is `drive(Vehicle)`, printing `Vehicle`.
- `bike1.drive(car)`: `car` has static type `Car`. `Bike` inherits `drive(Car)` from `Car`. The compile-time resolved method is `drive(Car)`, printing `Car`.
- `bike1.drive(bike)`: `bike` has static type `Bike`. `Bike` defines `drive(Bike)`. The compile-time resolved method is `drive(Bike)`, printing `Bike`.
- Output is `VehicleCarBike`.

---

### Q7. Java Inner Classes

**Topic:** `Java`, `OOP`, `Inner Classes`  

What will be the output of the program given below?

```java
public class King
{
    private int counter;
    class Queen
    {
        Queen()
        { counter++; }
        public String toString()
        { return String.valueOf(counter); }
    }
    private void method1()
    {
        Queen q = new Queen();
        this.new Queen();
        System.out.print(q);
        q = new King().new Queen();
        System.out.print(q);
    }
    public static void main(String args[])
    { new King().method1(); }
}
```

**Options:**
- A) `22`
- B) `21`
- C) `11`
- D) `12`

**Correct Answer:** B) `21`

**Explanation:**
- `new King().method1()` creates a `King` instance (let's call it `k1`) and runs `method1()`. `k1.counter` starts at 0.
- Inside `method1()`:
  - `Queen q = new Queen();` creates an inner class `Queen` instance associated with `k1`. Its constructor runs: `k1.counter++` -> `k1.counter` becomes 1.
  - `this.new Queen();` creates another `Queen` instance associated with `k1`. Its constructor runs: `k1.counter++` -> `k1.counter` becomes 2.
  - `System.out.print(q);` prints `q.toString()`, which returns `String.valueOf(k1.counter)` -> prints `2`.
  - `q = new King().new Queen();` creates a new `King` instance (`k2` with `k2.counter = 0`) and then instantiates a `Queen` associated with `k2`. Its constructor runs: `k2.counter++` -> `k2.counter` becomes 1.
  - `System.out.print(q);` prints `q.toString()`, which returns `String.valueOf(k2.counter)` -> prints `1`.
- Total output printed: `21`.

---

### Q8. Queue Underflow State

**Topic:** `Data Structures`, `Queue`, `Linked List`  

A queue is implemented using a linked list 'Q'. Enqueue operation is implemented by inserting element at the ending of the list and Dequeue operation is implemented by deleting an element from the beginning of the list. Which one of the options describes the underflow state of queue?

**Options:**
- A) `Q -> front != NULL and Q -> rear = NULL`
- B) `Q -> front = NULL and Q -> rear = NULL`
- C) `Q -> rear != NULL and Q -> front != NULL`
- D) `Q -> rear = NULL and Q -> front != NULL`

**Correct Answer:** B) `Q -> front = NULL and Q -> rear = NULL`

**Explanation:**
In a standard queue implementation using a linked list:
- `Q -> front` points to the head node (first element to be dequeued).
- `Q -> rear` points to the tail node (last element enqueued).
- An empty queue contains no elements, so both `front` and `rear` pointers are set to `NULL`. Attempting to dequeue from an empty queue triggers a queue underflow state.

---

### Q9. Min Heap Construction

**Topic:** `Data Structures`, `Min-Heap`  

Construct a min heap from the below given elements:
`85 12 36 96 88 14 75 36 99 10`

What will be the level order traversal of the resultant tree?

**Options:**
- A) `10 14 12 75 36 36 85 88 99 96`
- B) `10 14 75 36 36 88 12 85 96 99`
- C) `10 12 14 85 36 36 75 96 99 88`
- D) `10 12 85 36 96 99 88 14 36 75`

**Correct Answer:** C) `10 12 14 85 36 36 75 96 99 88`

**Explanation:**
Constructing a min-heap step-by-step using successive insertions:
1. **Insert 85:** `[85]`
2. **Insert 12:** `[85, 12]` $\rightarrow$ Swap(12, 85) $\rightarrow$ `[12, 85]`
3. **Insert 36:** `[12, 85, 36]` (no change)
4. **Insert 96:** `[12, 85, 36, 96]` (no change)
5. **Insert 88:** `[12, 85, 36, 96, 88]` (no change)
6. **Insert 14:** `[12, 85, 36, 96, 88, 14]` $\rightarrow$ Swap(14, 36) $\rightarrow$ `[12, 85, 14, 96, 88, 36]`
7. **Insert 75:** `[12, 85, 14, 96, 88, 36, 75]` (no change)
8. **Insert 36:** `[12, 85, 14, 96, 88, 36, 75, 36]` $\rightarrow$ Swap(36, 96) $\rightarrow$ swap with parent 85 $\rightarrow$ `[12, 36, 14, 85, 88, 36, 75, 96]`
9. **Insert 99:** `[12, 36, 14, 85, 88, 36, 75, 96, 99]` (no change)
10. **Insert 10:** `[12, 36, 14, 85, 88, 36, 75, 96, 99, 10]` $\rightarrow$ Swap(10, 88) $\rightarrow$ Swap(10, 36) $\rightarrow$ Swap(10, 12) $\rightarrow$ `[10, 12, 14, 85, 36, 36, 75, 96, 99, 88]`

The level order traversal of the heap is: `10 12 14 85 36 36 75 96 99 88`.

---

### Q10. Tree Identification

**Topic:** `Data Structures`, `Trees`  

Below given tree is an example of _______.

```
      A
     / \
    B   C
   / \ / \
  D  E F  G
```

**Options:**
- A) Unbalanced binary tree
- B) Extended binary tree
- C) Strictly binary tree
- D) Perfect binary tree

**Correct Answer:** D) Perfect binary tree

**Explanation:**
- **Strictly binary tree (Full binary tree):** Every node has either 0 or 2 children.
- **Perfect binary tree:** A binary tree in which all interior nodes have exactly two children and all leaf nodes are at the same depth/level.
- In the diagram, all internal nodes ($A, B, C$) have exactly 2 children, and all leaves ($D, E, F, G$) are at level 2. Hence, it is a perfect binary tree.

---

### Q11. Stack Usage in DFS

**Topic:** `Graph Algorithms`, `DFS`  

In the Depth-First Search (DFS) algorithm, why is a stack utilized?

**Options:**
- A) To ensure nodes are processed in alphabetical order
- B) To simulate a queue for breadth-first traversal
- C) To store nodes being visited and aid in backtracking
- D) To sort nodes based on their degrees

**Correct Answer:** C) To store nodes being visited and aid in backtracking

**Explanation:**
DFS explores as deep as possible along each branch before backtracking. A Last-In-First-Out (LIFO) stack is the natural data structure to keep track of the path of nodes currently being explored, allowing the algorithm to return to previous decision points (backtrack) once a dead end is reached.

---

### Q12. Edge Identification

**Topic:** `Graph Algorithms`, `DFS`, `Tree Edges`  

Consider the graph given below:

```
      A --------> B --------> C
      |         ^ |         / |
      |        /  |        /  |
      |       /   v       v   v
      v      D ---------> E   D
      F <----/            ^   ^
      |                   |   |
      v                   |   |
      G -------> H -----> I <-/
      |        / |      ^ ^
      v       v  v     /  |
      L <---- K ----> M  /
```
*(Only the red-colored edges are traversed during the DFS starting at A, where neighbors are explored in alphabetical order)*

Identify how many "Tree Edges" are present.

**Options:**
- A) 12
- B) 8
- C) 9
- D) 20

**Correct Answer:** C) 9

**Explanation:**
We perform DFS starting at node A, visiting neighbors in alphabetical order:
1. **At A:** Neighbors are B and F. Alphabetically, visit B first $\rightarrow$ **A -> B (Tree Edge, red)**.
2. **At B:** Neighbor is C $\rightarrow$ **B -> C (Tree Edge, red)**.
3. **At C:** Neighbors are D and E. Alphabetically, visit D first $\rightarrow$ **C -> D (Tree Edge, black)**.
4. **At D:** Neighbors are B and E. B is already visited. Visit E $\rightarrow$ **D -> E (Tree Edge, black)**.
5. **At E:** No outgoing edges. Backtrack to D, then C, then B, then A.
6. **At A:** Neighbor F is unvisited $\rightarrow$ **A -> F (Tree Edge, red)**.
7. **At F:** Neighbor is G $\rightarrow$ **F -> G (Tree Edge, red)**.
8. **At G:** Neighbors are H and L. Alphabetically, visit H first $\rightarrow$ **G -> H (Tree Edge, red)**.
9. **At H:** Neighbors are I and K. Alphabetically, visit I first $\rightarrow$ **H -> I (Tree Edge, red)**.
10. **At I:** Neighbors are D and J. D is visited. Visit J $\rightarrow$ **I -> J (Tree Edge, red)**.
11. **At J:** No outgoing edges. Backtrack to I, then H.
12. **At H:** Neighbor K is unvisited $\rightarrow$ **H -> K (Tree Edge, red)**.
13. **At K:** Neighbors are L and M. Alphabetically, visit L first $\rightarrow$ **K -> L (Tree Edge, black)**.
14. **At L:** No outgoing edges. Backtrack to K.
15. **At K:** Neighbor M is unvisited $\rightarrow$ **K -> M (Tree Edge, red)**.
16. **At M:** Neighbors are H, I, F (all visited). Backtrack all the way to A. Done.

The red-colored tree edges traversed are:
1. A -> B
2. B -> C
3. A -> F
4. F -> G
5. G -> H
6. H -> I
7. I -> J
8. H -> K
9. K -> M

This results in exactly **9** red Tree Edges.
