# Interview Questions

*Total questions: 37 (7 Coding, 30 MCQs/Theoretical)*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [Theoretical Questions](#theoretical-questions)

---

## Coding Questions

### Q1. Ball Collision
**Topic:** `arrays`, `stack`, `simulation`  
**Difficulty:** Medium  

#### Problem Description
There are $n$ balls placed on a 1-dimensional axis with each of them moving with the same non-zero speed. 
- `direction[i]` represents the direction in which the $i$-th ball is moving, with `-1` meaning it is moving to the left and `1` meaning it is moving to the right.
- `strength[i]` represents the strength of the $i$-th ball.

If two balls collide, the one with the higher strength destroys the smaller one. If both have the same strength, both are destroyed. Return a list of the indices of the balls that remain after all collisions have occurred, in ascending order. Note that the arrays `direction` and `strength` are 0-indexed.

#### Example
- `direction = [1, -1]`
- `strength = [2, 1]`
- Output: `[0]`  
*Explanation:* Ball 0 is moving right and ball 1 is moving left. They collide. Since ball 0 has higher strength (2 > 1), it destroys ball 1. Only ball 0 remains.

#### Python Solution
```python
def findRemainingBalls(direction, strength):
    stack = []  # stores indices of active balls
    
    for i in range(len(direction)):
        current_dir = direction[i]
        current_str = strength[i]
        
        destroyed = False
        # Collision only occurs when top of stack is moving right (1) and current ball is moving left (-1)
        while stack and direction[stack[-1]] == 1 and current_dir == -1:
            top_idx = stack[-1]
            top_str = strength[top_idx]
            
            if top_str < current_str:
                # Top ball is destroyed, pop it and continue checking
                stack.pop()
            elif top_str > current_str:
                # Current ball is destroyed, stop checking
                destroyed = True
                break
            else:
                # Both are destroyed
                stack.pop()
                destroyed = True
                break
        
        if not destroyed:
            stack.append(i)
            
    return sorted(stack)
```

#### C++ Solution
```cpp
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

vector<int> findRemainingBalls(vector<int>& direction, vector<int>& strength) {
    vector<int> st; // Use vector as stack to easily access elements
    
    for (int i = 0; i < direction.size(); i++) {
        bool destroyed = false;
        while (!st.empty() && direction[st.back()] == 1 && direction[i] == -1) {
            int top_idx = st.back();
            if (strength[top_idx] < strength[i]) {
                st.pop_back();
            } else if (strength[top_idx] > strength[i]) {
                destroyed = true;
                break;
            } else {
                st.pop_back();
                destroyed = true;
                break;
            }
        }
        if (!destroyed) {
            st.push_back(i);
        }
    }
    return st;
}
```

---

### Q2. Minimum Cost New Service / Network Clusters
**Topic:** `graphs`, `union-find`, `minimum-spanning-tree`  
**Difficulty:** Medium  

#### Problem Description
A network provider wants to enable a new service in a city with $n$ clusters.
- The cost to host the new service in any cluster is $c_{\text{service}}$.
- The cost to add a link between two clusters is $c_{\text{link}}$.
- You are given a list of possible cluster pairs that can be connected.

Find the minimum cost required to enable the new service in all clusters. A cluster can access the service if it hosts the service itself, or if it is connected via links to another cluster that hosts the service.

#### Example
- `n = 5`, `c_link = 2`, `c_service = 3`
- Possible connections: `[[1, 2], [1, 3], [4, 5]]`
- Output: `12`  
*Explanation:* We can build a service in cluster 1 and cluster 4. Then build links (1, 2) and (1, 3) to connect clusters 2 and 3 to cluster 1, and link (4, 5) to connect cluster 5 to cluster 4. Total cost = $2 \times c_{\text{service}} + 3 \times c_{\text{link}} = 2 \times 3 + 3 \times 2 = 12$.

#### Python Solution
```python
def minCostNewService(n, c_service, c_link, connections):
    if c_service <= c_link:
        # If hosting a service is cheaper than linking, host service in all clusters
        return n * c_service
        
    # Standard Union-Find to find connected components
    parent = list(range(n + 1))
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False
        
    components = n
    links_built = 0
    for u, v in connections:
        if union(u, v):
            components -= 1
            links_built += 1
            
    # For each component of size k, we build 1 service and k - 1 links
    return (components * c_service) + (links_built * c_link)
```

---

### Q3. Minimum Size Subarray Sum
**Topic:** `arrays`, `sliding-window`, `two-pointers`  
**Difficulty:** Medium  

#### Problem Description
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

#### Example
- `target = 11`, `nums = [5, 6, 7, 8]`
- Output: `2`  
*Explanation:* The subarray `[5, 6]` or `[6, 7]` or `[7, 8]` has sum $\ge 11$. The minimum length is 2.

#### Python Solution
```python
def minSubArrayLen(target, nums):
    n = len(nums)
    min_len = float('inf')
    left = 0
    current_sum = 0
    
    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0
```

---

### Q4. Last Animal Name Length
**Topic:** `strings`, `parsing`  
**Difficulty:** Easy  

#### Problem Description
Given a sequence of characters and a separator character, an animal name is defined as a sequence of characters that does not contain the separator character. The function should ignore any trailing or leading separator characters. Find the length of the last animal name in the sequence.

#### Example
- `sequence = "cat#dog##lion#"`, `separator = '#'`
- Output: `4`  
*Explanation:* The animal names are `"cat"`, `"dog"`, `"lion"`. The last name is `"lion"` with length 4.

#### Python Solution
```python
def last_animal(sequence, separator):
    # Split by separator
    parts = sequence.split(separator)
    # Filter out empty strings caused by consecutive or leading/trailing separators
    names = [p for p in parts if p]
    if not names:
        return 0
    return len(names[-1])
```

---

### Q5. Dominoes Painting / Count Distinct Colorings
**Topic:** `dynamic-programming`, `combinatorics`  
**Difficulty:** Hard  

#### Problem Description
You are given a 2xN grid of dominoes, represented by two strings of equal length `domino[0]` and `domino[1]`.
- Each domino is of size 2x1 (vertical) or 1x2 (horizontal) and is represented by an English character.
- You want to color the dominoes using Red (R), Green (G), or Blue (B) such that:
  - Both halves of a domino have the same color.
  - No two adjacent dominoes have the same color.
Return the total number of valid colorings modulo $10^9+7$.

#### Example
- `domino = ["baa", "bcc"]`
- Output: `6`  
*Explanation:* The dominoes are 'b' (vertical, size 2x1), 'a' (horizontal, size 1x2), 'c' (horizontal, size 1x2). Valid colorings are 6.

#### Python Solution
```python
def countDistinctColorings(domino):
    MOD = 10**9 + 7
    n = len(domino[0])
    
    # Identify type of columns: 0 for vertical, 1 for horizontal
    types = []
    i = 0
    while i < n:
        if domino[0][i] == domino[1][i]:
            types.append(0) # Vertical
            i += 1
        else:
            types.append(1) # Horizontal
            i += 2
            
    # dp state: number of colorings up to i-th component
    # dp[i] represents valid colorings for components up to index i
    if not types:
        return 0
        
    if types[0] == 0:
        dp = 3
    else:
        dp = 6
        
    for idx in range(1, len(types)):
        prev_type = types[idx - 1]
        curr_type = types[idx]
        
        if prev_type == 0 and curr_type == 0:
            dp = (dp * 2) % MOD
        elif prev_type == 0 and curr_type == 1:
            dp = (dp * 2) % MOD
        elif prev_type == 1 and curr_type == 0:
            dp = (dp * 1) % MOD
        elif prev_type == 1 and curr_type == 1:
            dp = (dp * 3) % MOD
            
    return dp
```

---

### Q6. Youngest Missing Member
**Topic:** `arrays`, `hash-table`, `sorting`  
**Difficulty:** Easy  

#### Problem Description
You are given an array `ages` containing the ages of active members, and an array of strings `members` where each string is in the format `"Name,LastName,Age"`. The task is to find the name of the youngest missing member (whose age is not present in `ages` array).
- If all members' ages are present in `ages`, return `null`.
- If there are multiple youngest missing members, return the first occurrence of the youngest member.

#### Example
- `ages = [10, 8, 9]`
- `members = ["Ramp,T,10", "AdamJobs,Y,4", "Leena,Jack,7"]`
- Output: `"Leena"`  
*Explanation:* Missing ages are 4 (AdamJobs) and 7 (Leena). The youngest missing is 4, but wait! Leena's age is 7, AdamJobs' age is 4. The youngest is AdamJobs.

#### Python Solution
```python
def findYoungestMember(ages, members):
    present_ages = set(ages)
    missing_members = []
    
    for mem in members:
        parts = mem.split(',')
        if len(parts) < 3:
            continue
        first_name = parts[0]
        age = int(parts[-1])
        
        if age not in present_ages:
            missing_members.append((first_name, age))
            
    if not missing_members:
        return "null"
        
    # Find minimum age among missing members
    min_age = min(m[1] for m in missing_members)
    
    # Return first occurrence of member with min_age
    for name, age in missing_members:
        if age == min_age:
            return name
            
    return "null"
```

---

### Q7. Minimum Size Strongly Connected Group / minFriends
**Topic:** `graphs`, `clique`, `turan-theorem`, `binary-search`  
**Difficulty:** Hard  

#### Problem Description
Given $N$ nodes (people) and $M$ edges (relationships) in an undirected graph, find the minimum size of the largest fully connected group (clique) that must exist in the graph under any arrangement of edges.

#### C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

// Calculates maximum number of edges in a graph of size n with no clique of size r+1
long long turanEdges(long long n, long long r) {
    long long k = n / r;
    long long rem = n % r;
    long long sum_sq = rem * (k + 1) * (k + 1) + (r - rem) * k * k;
    return (n * n - sum_sq) / 2;
}

int minFriends(int numNodes, int numEdges) {
    int low = 1, high = numNodes;
    int ans = numNodes;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (turanEdges(numNodes, mid) >= numEdges) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
}
```

---

### Q8. Minimum Complexity of Lectures / Job Scheduling DP
**Topic:** `dynamic-programming`  
**Difficulty:** Hard  

#### Problem Description
Alex is attending $N$ lectures in a specific order. The $i$-th lecture has complexity `complexity[i]`. Alex wants to schedule these lectures into `days` days. Alex must attend at least one lecture every day, and the complexity of a day is the maximum complexity of any lecture attended that day. Find the minimum overall complexity (sum of complexities of each day) Alex can achieve.

#### Python Solution
```python
def findMinComplexity(complexity, days):
    n = len(complexity)
    if n < days:
        return -1
        
    # dp[i][j] represents min complexity to schedule first i jobs in j days
    dp = [[float('inf')] * (days + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for d in range(1, days + 1):
        for i in range(d, n + 1):
            max_val = 0
            for j in range(i, d - 1, -1):
                max_val = max(max_val, complexity[j - 1])
                dp[i][d] = min(dp[i][d], dp[j - 1][d - 1] + max_val)
                
    return dp[n][days] if dp[n][days] != float('inf') else -1
```

---

### Q9. GPU Shaders Idleness
**Topic:** `binary-search`, `dynamic-programming`, `sliding-window`  
**Difficulty:** Hard  

#### Problem Description
A game's shaders are rendered using two GPUs: `a` and `b`. The GPU used for each shader is represented by a string `shader`. The idleness of the system is the maximum number of consecutive shaders using the same GPU. You can flip at most `switchCount` shaders to minimize the idleness. Find the minimum possible idleness.

#### Python Solution
```python
def findMinimumIdleness(shader, switchCount):
    n = len(shader)
    
    def check(k):
        # DP with sliding window minimum to check if max run length <= k is possible in <= switchCount flips
        # dp[i][0]: min flips for prefix i ending with 'a'
        # dp[i][1]: min flips for prefix i ending with 'b'
        dp = [[float('inf')] * 2 for _ in range(n + 1)]
        dp[0][0] = dp[0][1] = 0
        
        # Deques for sliding window minimum of size k
        # deq0 stores values of dp[j][1] (since we transition from different char)
        # deq1 stores values of dp[j][0]
        from collections import deque
        deq0 = deque()
        deq1 = deque()
        
        for i in range(1, n + 1):
            # Maintain sliding window [i-k, i-1]
            if deq0 and deq0[0] < i - k:
                deq0.popleft()
            if deq1 and deq1[0] < i - k:
                deq1.popleft()
                
            # Add dp[i-1][1] and dp[i-1][0] to window
            val0 = dp[i-1][1]
            while deq0 and dp[deq0[-1]][1] >= val0:
                deq0.pop()
            deq0.append(i-1)
            
            val1 = dp[i-1][0]
            while deq1 and dp[deq1[-1]][0] >= val1:
                deq1.pop()
            deq1.append(i-1)
            
            # Transition
            cost_a = 0 if shader[i-1] == 'a' else 1
            cost_b = 0 if shader[i-1] == 'b' else 1
            
            dp[i][0] = cost_a + dp[deq0[0]][1]
            dp[i][1] = cost_b + dp[deq1[0]][0]
            
        return min(dp[n][0], dp[n][1]) <= switchCount

    # Binary search on idleness
    low, high = 1, n
    ans = n
    while low <= high:
        mid = low + (high - low) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
```

---

### Q10. Validate BST (Iterative)
**Topic:** `trees`, `binary-search-tree`, `stack`  
**Difficulty:** Medium  

#### Problem Description
Given a binary tree, determine whether it is a binary search tree (BST) without using recursion.

#### C++ Solution
```cpp
#include <stack>
#include <climits>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
};

bool isValidBST(TreeNode* root) {
    stack<TreeNode*> stk;
    TreeNode* curr = root;
    TreeNode* prev = nullptr;
    
    while (curr != nullptr || !stk.empty()) {
        while (curr != nullptr) {
            stk.push(curr);
            curr = curr->left;
        }
        curr = stk.top();
        stk.pop();
        
        if (prev != nullptr && curr->val <= prev->val) {
            return false;
        }
        prev = curr;
        curr = curr->right;
    }
    return true;
}
```

---

## Theoretical & MCQ Questions

### Q11. IP Subnet Mask Calculation
Consider the IP addresses:
- A. `201.119.1.30`
- B. `201.119.1.33`
- C. `201.119.1.46`

If the subnet mask is `255.255.255.240`, which IP addresses belong to the same subnet?

**Options:**
- A) A and B
- B) B and C
- C) A, B and C
- D) None

**Correct Answer:** **B) B and C**  
*Explanation:* The subnet mask `255.255.255.240` has a block size of 16 ($256 - 240 = 16$). Subnets are grouped in ranges of 16:
- Subnet 1: `201.119.1.16` to `201.119.1.31`
- Subnet 2: `201.119.1.32` to `201.119.1.47`
IP address A (.30) belongs to Subnet 1, whereas IP addresses B (.33) and C (.46) both belong to Subnet 2.

---

### Q12. Concept of Virtual Memory
Identify the concept of virtual memory in an operating system.

**Options:**
- A) Additional physical RAM
- B) Secondary storage (e.g., hard disk) used as an extension of RAM
- C) RAM allocated for system processes only
- D) Memory reserved for graphics processing

**Correct Answer:** **B) Secondary storage (e.g., hard disk) used as an extension of RAM**  
*Explanation:* Virtual memory allows an operating system to compensate for physical memory shortages by temporarily transferring data from random access memory (RAM) to disk storage.

---

### Q13. C Preprocessor Macros Scope and Behavior
Which one of the following statements is correct about C preprocessor macros?

**Options:**
- A) A macro must be defined in capital letters.
- B) Once preprocessing is over and the program is sent for compilation, the macros are removed from the expanded source code.
- C) Macros have a local scope.
- D) In a macro call, the control is passed to the macro.

**Correct Answer:** **B) Once preprocessing is over and the program is sent for compilation, the macros are removed from the expanded source code.**  
*Explanation:* Preprocessor macros are expanded and replaced directly in the source text during preprocessing. The compiler only sees the expanded source code, so macros themselves no longer exist in the compiled code.

---

### Q14. Linux Kernel Panic Triggers
Which scenario is most likely to trigger a kernel panic error in the Linux operating system?

**Options:**
- A) Initiating a system call that attempts to access a non-existent hardware device
- B) Inserting a corrupt kernel module that conflicts with the existing kernel version
- C) Running a multi-threaded application that exceeds the system's maximum thread limit
- D) Executing a memory-intensive scientific simulation with parallel processes

**Correct Answer:** **B) Inserting a corrupt kernel module that conflicts with the existing kernel version**  
*Explanation:* A kernel module runs inside the kernel space. A corrupt module can perform invalid operations (like writing to reserved kernel memory or dereferencing null pointers in ring 0), causing a fatal kernel error (Oops) that triggers a kernel panic.

---

### Q15. Secure File Transfer via SSH
A Linux system administrator needs to securely transfer a file named `myapp.log` from a local server to a remote server using SSH. The administrator has regular user privileges, and the `myapp.log` file can only be accessed by the root user. Which command should the administrator use?

**Options:**
- A) `sudo scp -i /root/.ssh/id_rsa /path/to/myapp.log ubuntu@10.0.1.34:/remote-dir/my-location/`
- B) `sudo -u root scp /path/to/myapp.log ubuntu@10.0.1.34:/remote-dir/my-location/`
- C) `sudo -u root chown root /path/to/myapp.log && sudo -u root scp /path/to/myapp.log ubuntu@10.0.1.34:/remote-dir/my-location/`
- D) `sudo -u root scp -i /root/.ssh/id_rsa /path/to/myapp.log ubuntu@10.0.1.34:/remote-dir/my-location/`

**Correct Answer:** **D) `sudo -u root scp -i /root/.ssh/id_rsa /path/to/myapp.log ubuntu@10.0.1.34:/remote-dir/my-location/`**  
*Explanation:* To read the log file, the `scp` command must run with root permissions (`sudo -u root`). Additionally, to authenticate using the root user's SSH private key `/root/.ssh/id_rsa`, it must run with root privileges to read the key.

---

### Q16. TCP Packet Exchange Validation
Which one of the following statements is FALSE?

**Options:**
- A) Three packets are sent to establish a TCP connection.
- B) The ACK packet from the receiver during TCP connection initiation has both SYN and ACK bits set.
- C) Four packets are sent to terminate the TCP connection.
- D) None of these

**Correct Answer:** **D) None of these**  
*Explanation:* All statements (A, B, C) are true. TCP connection establishment uses a 3-way handshake, the response packet (SYN-ACK) has both bits set, and termination uses a 4-way handshake.

---

### Q17. Maximum Keys in B-Tree
What is the maximum number of keys in a B-tree of order 6 and height 5?

**Options:**
- A) 7776
- B) 7775
- C) 16384
- D) 16383

**Correct Answer:** **B) 7775**  
*Explanation:* In a B-tree of order $m$ and height $h$, the maximum number of keys is $m^h - 1$. For $m = 6$ and $h = 5$, the maximum number of keys is $6^5 - 1 = 7776 - 1 = 7775$.

---

### Q18. Dynamic Memory Allocation Location in C/C++
The `malloc()` or `realloc()` function in C/C++ allocates memory at which time/location?

**Options:**
- A) Compilation time on stack
- B) Linking time on stack
- C) Load time on heap
- D) Execution time on heap
- E) Execution time on stack

**Correct Answer:** **D) Execution time on heap**  
*Explanation:* Both functions allocate memory dynamically on the heap during execution (runtime).

---

### Q19. Circular Linked List Applications
A circular linked list can be used to implement:

**Options:**
- A) A queue
- B) A stack
- C) Both a queue and a stack
- D) Neither

**Correct Answer:** **C) Both a queue and a stack**  
*Explanation:* Stacks and queues can be implemented with $O(1)$ operations on a circular linked list by maintaining a pointer to the last node.

---

### Q20. Concurrent Global Variable Access in Threads
Consider a Linux process with two threads sharing the same address space. If both threads execute the same function concurrently and attempt to modify a global variable within that function, what will happen?

**Options:**
- A) The global variable will be overwritten with the value from the thread that called the function last.
- B) The global variable will be unaffected, as each thread has its own stack.
- C) The final value will be unpredictable since the order of their executions cannot be determined.
- D) The global variable will automatically be protected, and only one thread can modify it at a time.

**Correct Answer:** **C) The final value will be unpredictable since the order of their executions cannot be determined.**  
*Explanation:* Concurrent access and modification of shared memory (global variables) without synchronization (like mutexes) leads to a data race. The final value depends on thread scheduling and is unpredictable.

---

### Q21. Bash Shell Default Environment Variables Location
Which file contains default environment variables when using the bash shell?

**Options:**
- A) `~/.profile`
- B) `~/.bash`
- C) `/etc/profile.d`
- D) `~/.bashrc`

**Correct Answer:** **A) `~/.profile`**  
*Explanation:* `~/.profile` is the default startup file for Bourne-compatible shells (like bash) to initialize environment variables upon login.

---

### Q22. Time Complexity of Linear Search
Determine the time complexity of linear search in an array of size $n$.

**Options:**
- A) $O(\log n)$
- B) $O(n)$
- C) $O(n^2)$
- D) $O(1)$

**Correct Answer:** **B) $O(n)$**  
*Explanation:* Linear search checks each element of the array sequentially, taking $O(n)$ time in the worst case.

---

### Q23. Storage Locations of Static/Local Variables in RAM
Consider the following C code snippet:
```c
static int a;
static int b = 10;
void func() {
    int c;
}
```
Where are the variables `a`, `b`, and `c` stored in RAM respectively?

**Options:**
- A) Stack, Heap, BSS
- B) Heap, Code, BSS
- C) BSS, Data, Stack
- D) Data, BSS, Stack

**Correct Answer:** **C) BSS, Data, Stack**  
*Explanation:* 
- `a` is an uninitialized static variable, stored in the BSS segment.
- `b` is an initialized static variable, stored in the Data segment.
- `c` is a local auto variable, stored on the Stack.

---

### Q24. Responsibilities of an Operating System
Which of the following are responsibilities of an operating system? (Select all that apply)

**Options:**
- A) Process Management
- B) Memory Management
- C) Security
- D) Performance

**Correct Answer:** **A, B, C, D (All options are correct)**  
*Explanation:* The OS manages processes, memory, files, security/access controls, and monitors system performance.

---

### Q25. Recurrence Relation Time Complexity
Consider the following recurrence relation:
$$R(n) = R(n-1) + O(1)$$
Find the time complexity of $R(n)$.

**Options:**
- A) $O(n)$
- B) $O(\log n)$
- C) $O(n \log n)$
- D) $O(\log \log n)$

**Correct Answer:** **A) $O(n)$**  
*Explanation:* Expanding the recurrence: $R(n) = R(n-1) + c = R(n-2) + 2c = \dots = R(0) + nc$. Thus, the time complexity is $O(n)$.

---

### Q26. Fast Binary Exponentiation Output
Guess the output for the following Java program:
```java
public static int fun(int x, int y) {
    if (y == 0) return 1;
    else if (y % 2 == 0) return fun(x * x, y / 2);
    else return x * fun(x * x, (y - 1) / 2);
}
public static void main() {
    int ans = fun(2, 10);
    System.out.println(ans);
}
```

**Options:**
- A) 1023
- B) 2048
- C) 1024
- D) None of these

**Correct Answer:** **C) 1024**  
*Explanation:* The function implements binary exponentiation (fast power) which computes $x^y$. For $x = 2$ and $y = 10$, it returns $2^{10} = 1024$.

---

### Q27. JavaScript Parameter Passing Semantics
Does JavaScript always pass parameters by value or by reference?

**Options:**
- A) depends on the parameter type
- B) value
- C) prefixing the parameter by '&' will pass it by reference

**Correct Answer:** **A) depends on the parameter type**  
*Explanation:* Primitive types (numbers, strings, booleans, etc.) are passed by value. Object types are passed by sharing (which behaves like passing a reference by value).

---

### Q28. Code Readability: Clean Conditional Expressions
What is a good way to clean the following conditional expression?
```javascript
if (user.experience > 6 && user.earnings > 5000 && user.contracts >= 60 && user.warnings == 0) {
    sendInvitation(user);
    user.risingTalent = true;
}
```

**Options:**
- A) Each component of the expression should be moved to a separate if statement.
- B) Remove 'user.warnings == 0' from the expression.
- C) Move the complex conditional into its own separate function.
- D) Add an else statement at the end.

**Correct Answer:** **C) Move the complex conditional into its own separate function.**  
*Explanation:* Extracting the complex condition to a well-named helper function (e.g. `isEligibleForInvitation(user)`) improves code readability and maintainability.

---

### Q29. JavaScript Object Creation Syntax
Which of the following are correct ways to create an object in JavaScript? (Select all that apply)

**Options:**
- A) `const data = { Name: "Tom", Roll: 35 };`
- B) `class data { this.Name = "Tom"; this.Roll = 35; }`
- C) `struct data { this.Name = "Tom"; this.Roll = 35; }`
- D) `function data() { this.Name = "Tom"; this.Roll = 35; }`

**Correct Answer:** **A and D**  
*Explanation:* Option A is an object limit, and Option D is a constructor function. Options B and C have invalid syntax.

---

### Q30. JavaScript Window and Document Objects
Which of the following statements about Window and Document objects are correct? (Select all that apply)

**Options:**
- A) Both window and document represent the same element.
- B) The window element can be used to affect and react to events related to browser behavior.
- C) A document element can be used to affect and react to events related to the webpage's DOM.
- D) Both window and document are singletons within a page.

**Correct Answer:** **B, C, and D**  
*Explanation:* Window represents the browser window, whereas Document represents the DOM tree loaded in that window. Both are singletons per page.

---

### Q31. JavaScript Objects Classification
Which of the following is considered an object in JavaScript? (Select all that apply)

**Options:**
- A) function
- B) true
- C) string
- D) array

**Correct Answer:** **A and D**  
*Explanation:* Functions and Arrays are specialized objects in JavaScript. Primitives like `true` (boolean) and `"string"` are not objects.

---

### Q32. JavaScript IIFE and Closure Output
Predict the output of the following JavaScript code:
```javascript
const func = (function() {
    let counter = 0;
    return function() {
        return counter++;
    };
})();
let result = func();
result = func();
result = func();
console.log(result);
```

**Options:**
- A) Error
- B) 0
- C) 2
- D) 3

**Correct Answer:** **C) 2**  
*Explanation:* The IIFE returns a closure that holds reference to `counter`. On consecutive calls:
- 1st call: returns 0, counter becomes 1.
- 2nd call: returns 1, counter becomes 2.
- 3rd call: returns 2, counter becomes 3.

---

### Q33. JavaScript Function Length Property
Predict the output of the following JavaScript code:
```javascript
function test(a, b = 1, c, ...args) {}
console.log(test.length);
```

**Options:**
- A) 4
- B) 1
- C) 2
- D) 3

**Correct Answer:** **B) 1**  
*Explanation:* The `length` property of a function returns the number of expected parameters. Parameters with default values, rest parameters, and parameters following them are excluded.

---

### Q34. JavaScript Prototype and instance properties (`hasOwnProperty`)
Predict the output of the following JavaScript code:
```javascript
class Test {
    name = "test";
    printName() {}
}
const obj1 = new Test();
const obj2 = new Test();
console.log(obj1.hasOwnProperty('name'), obj2.hasOwnProperty('name'));
console.log(obj1.hasOwnProperty('printName'), obj2.hasOwnProperty('printName'));
```

**Options:**
- A) `true true` and `false false`
- B) `true true` and `true true`
- C) `false false` and `false false`
- D) `false false` and `true true`

**Correct Answer:** **A) `true true` and `false false`**  
*Explanation:* Instance fields like `name` are created directly on the constructed objects, so `hasOwnProperty` returns `true`. Methods like `printName` are defined on the class prototype (`Test.prototype`), so `hasOwnProperty` returns `false`.

---

### Q35. Shared Resources between Process and Threads
Which section of RAM is shared between a process and its threads?

**Options:**
- A) Heap
- B) Stack
- C) Code
- D) Both Heap and Code

**Correct Answer:** **D) Both Heap and Code**  
*Explanation:* Threads of the same process share the same Address Space, including Code and Heap, but each thread has its own Stack.

---

### Q36. Venn Diagram Word Problem
In a company, 26 employees are in the HR department, 32 are in the technical department, and 30 are in the management department. Of these, 5 employees are in all three departments, and 37 are in only one of them. How many employees are in only two of the three departments?

**Options:**
- A) 36
- B) 18
- C) 88
- D) 15

**Correct Answer:** **B) 18**  
*Explanation:* Let $H = 26, T = 32, M = 30$.
Let $x$ be the number of employees in only one department ($x = 37$).
Let $y$ be the number of employees in only two departments.
Let $z$ be the number of employees in all three departments ($z = 5$).
We know that:
$$x + 2y + 3z = H + T + M$$
$$37 + 2y + 3(5) = 26 + 32 + 30$$
$$37 + 2y + 15 = 88$$
$$52 + 2y = 88 \implies 2y = 36 \implies y = 18$$

---

### Q37. C Preprocessing Directives
Which of the following are processed during the preprocessing stage in C? (Select all that apply)

**Options:**
- A) Macros (e.g. `#define`)
- B) Function calls
- C) Conditional Compilation (e.g. `#ifdef`)
- D) Include Guards (e.g. `#ifndef`)

**Correct Answer:** **A, C, and D**  
*Explanation:* Preprocessor directives start with `#` and are processed before actual compilation. Function calls are compiled and executed at runtime.
```
