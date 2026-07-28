# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Optimize Delivery Routes
**Topic:** `Linked List`, `Greedy` `[Latest]`

#### Description
To enhance the efficiency of delivery routes for logistics and delivery services, design a system that merges linked list routes, reducing the number of routes while maximizing the total delivery points.

Create the `OptimizeDeliveryRoutes` class with the following methods:
1. `void addRoute(const vector<int>& deliveryPoints)`:
   - Accepts an array of integers representing delivery points.
   - Converts this array into a singly linked list and stores the head of the linked list.
2. `vector<ListNode*> returnOptimizedRoutes()`:
   - Returns an array of route heads, where each head represents an optimized route according to specified rules.
   - The method must restore the original list structure modified during previous calls before applying the optimization logic (since `returnOptimizedRoutes` can be called repeatedly and new routes can be added in between).

#### Rules
- Begin with the first route head.
- Iterate through each subsequent route in the order they were added.
- For each subsequent route:
  - Identify a delivery point $p$ in the current active route (starting from the current route head) that can connect to the next route's head $h$, where the value at $h$ is strictly greater than the value at $p$ ($p.\text{value} < h.\text{value}$).
  - If multiple such nodes $p$ exist, pick the one with the maximum value. If there's a tie, pick the latest occurrence in the current active route.
  - If a matching node $p$ is found:
    - Connect $p$ to $h$ ($p.\text{next} = h$).
    - Any nodes after $p$ in the active route are disconnected and discarded.
    - The new route starting at $h$ becomes the new active segment to which subsequent routes will attempt to connect.
  - If no such node $p$ is found:
    - The current active route cannot be merged with the next route. Save the current route's head to the result.
    - The next route becomes the new active route, and its head becomes the start of the new active segment.

#### Constraints
- $2 \le \text{Total number of requests} \le 300$
- $1 \le \text{Total number of delivery points} \le 50000$
- $1 \le \text{deliveryPoints}[i] \le 10000$

#### Example
**Operations:**
```text
addRoute({10, 2, 7, 3})
addRoute({3, 3, 9, 2, 1})
returnOptimizedRoutes()  // First call
addRoute({4, 3, 9})
returnOptimizedRoutes()  // Second call
addRoute({3, 29, 20, 5})
addRoute({11, 3})
returnOptimizedRoutes()  // Third call
```

**Explanation & Trace:**
1. `addRoute({10, 2, 7, 3})`: Route 1 is $10 \to 2 \to 7 \to 3$.
2. `addRoute({3, 3, 9, 2, 1})`: Route 2 is $3 \to 3 \to 9 \to 2 \to 1$.
3. First `returnOptimizedRoutes()`:
   - Initial active segment is $10 \to 2 \to 7 \to 3$.
   - Next route head has value $3$. We look for nodes in $10 \to 2 \to 7 \to 3$ with value $< 3$.
   - The only candidate is node $2$. We connect $2$ to the second route's head $3$.
   - The combined route is $10 \to 2 \to 3 \to 3 \to 9 \to 2 \to 1$.
   - Returns `{ListNode(10)}`.
4. `addRoute({4, 3, 9})`: Route 3 is $4 \to 3 \to 9$.
5. Second `returnOptimizedRoutes()`:
   - First, the connections are restored to their original states.
   - Route 1: $10 \to 2 \to 7 \to 3$
   - Route 2: $3 \to 3 \to 9 \to 2 \to 1$
   - Route 3: $4 \to 3 \to 9$
   - Now we optimize:
     - Process Route 2 (head 3): Node $2$ from Route 1 connects to Route 2. Combined: $10 \to 2 \to 3 \to 3 \to 9 \to 2 \to 1$. Active segment becomes Route 2 ($3 \to 3 \to 9 \to 2 \to 1$).
     - Process Route 3 (head 4): Look for nodes in Route 2 with value $< 4$. Candidates are $3$ (index 0), $3$ (index 1), $2$ (index 3), $1$ (index 4).
     - The maximum value is $3$. We pick the latest occurrence, which is $3$ (index 1).
     - Connect $3$ (index 1) to the head of Route 3 ($4$).
     - The combined route becomes: $10 \to 2 \to 3 \to 3 \to 4 \to 3 \to 9$.
   - Returns `{ListNode(10)}`.

---

#### C++ Solution
```cpp
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int value;
    ListNode* next;
    ListNode(int val) : value(val), next(nullptr) {}
};

class OptimizeDeliveryRoutes {
public:
    vector<ListNode*> original_heads;
    vector<ListNode*> modified_nodes;
    vector<ListNode*> original_nexts;

    // Adds a new route from array values
    void addRoute(const vector<int>& deliveryPoints) {
        if (deliveryPoints.empty()) {
            original_heads.push_back(nullptr);
            return;
        }
        ListNode* head = new ListNode(deliveryPoints[0]);
        ListNode* curr = head;
        for (size_t i = 1; i < deliveryPoints.size(); ++i) {
            curr->next = new ListNode(deliveryPoints[i]);
            curr = curr->next;
        }
        original_heads.push_back(head);
    }

    // Performs route optimization and returns the resulting route heads
    vector<ListNode*> returnOptimizedRoutes() {
        // Restore modifications from the previous runs
        for (size_t i = 0; i < modified_nodes.size(); ++i) {
            modified_nodes[i]->next = original_nexts[i];
        }
        modified_nodes.clear();
        original_nexts.clear();

        vector<ListNode*> result;
        if (original_heads.empty()) return result;

        ListNode* current_route_head = original_heads[0];
        ListNode* active_segment = original_heads[0];

        for (size_t i = 1; i < original_heads.size(); ++i) {
            ListNode* next_route = original_heads[i];
            if (!next_route) continue;

            int next_head_val = next_route->value;
            ListNode* best_node = nullptr;
            int max_val = -1;
            ListNode* curr = active_segment;

            // Search active segment for the best connection node
            while (curr) {
                if (curr->value < next_head_val) {
                    if (curr->value > max_val) {
                        max_val = curr->value;
                        best_node = curr;
                    } else if (curr->value == max_val) {
                        // Tie-breaking: pick the latest occurrence
                        best_node = curr;
                    }
                }
                curr = curr->next;
            }

            if (best_node) {
                // Save original pointer connection for future restoration
                modified_nodes.push_back(best_node);
                original_nexts.push_back(best_node->next);
                // Connect the node to the next route head
                best_node->next = next_route;
                // Update active segment
                active_segment = next_route;
            } else {
                // Could not merge: finalize current route and start a new one
                result.push_back(current_route_head);
                current_route_head = next_route;
                active_segment = next_route;
            }
        }
        result.push_back(current_route_head);
        return result;
    }
};
```

---

### Q2. Bitwise Recurrence
**Topic:** `Bit Manipulation`, `Recurrence Relations` `[Latest]`

#### Description
Consider the sequence where:
$$F_0 = a, \quad F_1 = b, \quad F_2 = c$$
$$F_i = (F_{i-1} \mid F_{i-2}) \oplus F_{i-3} \quad \text{for } i \ge 3$$

Here, $\mid$ is the bitwise OR operator and $\oplus$ is the bitwise XOR operator.
Given four long integers $a, b, c$, and $n$, find $F_n$.

#### Constraints
- $0 \le a, b, c, n \le 10^{12}$

#### Example
- $a = 4$
- $b = 1$
- $c = 10$
- $n = 4$

**Calculation:**
- $F_0 = 4$
- $F_1 = 1$
- $F_2 = 10$
- $F_3 = (F_2 \mid F_1) \oplus F_0 = (10 \mid 1) \oplus 4 = 11 \oplus 4 = 15$
- $F_4 = (F_3 \mid F_2) \oplus F_1 = (15 \mid 10) \oplus 1 = 15 \oplus 1 = 14$

**Output:** `14`

#### Approach
Because the operations are bitwise, each bit position transitions independently.
For a single bit, the state is determined by the last 3 bits: $(F_{i-3}, F_{i-2}, F_{i-1})$.
Since there are only $8$ possible states, the sequence of transitions must repeat. By checking the periods of all $8$ states:
- `(0, 0, 0)` transitions to `0` infinitely (period 1).
- `(0, 1, 0)` and `(1, 0, 1)` cycle with a period of 2:
  - `(0, 1, 0)` -> value at $n$ is $n \bmod 2$.
  - `(1, 0, 1)` -> value at $n$ is $1 - (n \bmod 2)$.
- Any other 3-tuple state cycles with a period of 5.

This allows us to solve the problem in $O(\log(\max(a, b, c)))$ time by processing each bit position independently.

#### Python Solution
```python
def bitwiseRecurrence(a, b, c, n):
    if n == 0: return a
    if n == 1: return b
    if n == 2: return c
    
    ans = 0
    # Process each bit index independently
    for i in range(max(a, b, c).bit_length()):
        x = (a >> i) & 1
        y = (b >> i) & 1
        z = (c >> i) & 1
        
        if (x, y, z) == (0, 0, 0):
            v = 0
        elif (x, y, z) == (0, 1, 0):
            v = n % 2
        elif (x, y, z) == (1, 0, 1):
            v = 1 - (n % 2)
        else:
            # Reconstruct the sequence up to period length of 5
            seq = [x, y, z]
            seq.append((seq[2] | seq[1]) ^ seq[0])
            seq.append((seq[3] | seq[2]) ^ seq[1])
            v = seq[n % 5]
            
        if v:
            ans |= (1 << i)
            
    return ans
```

