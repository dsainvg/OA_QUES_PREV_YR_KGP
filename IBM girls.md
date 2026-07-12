# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/IBM girls*
*Total questions: 3*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Validate Binary Search Tree (Iterative)

**Topic:** `Trees`, `Binary Search Tree (BST)`, `Stack`, `Iterative Traversal`  

Given a binary tree represented as a level-order traversal in a string array, write a function to determine whether it is a valid binary search tree (BST).

A binary search tree is defined as a binary tree in which:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

**Constraint:** Do not use recursion.

#### Function description
Complete the `is_valid_bst` function below. The function accepts `root_count` (integer) and `root` (array of strings) as parameters and returns a boolean.
```c
bool is_valid_bst(int root_count, char** root) {
    // Write code here
}
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct Node {
    int val;
    struct Node* left;
    struct Node* right;
} Node;

Node* create_node(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = NULL;
    n->right = NULL;
    return n;
}

bool is_empty(char* s) {
    if (s == NULL) return true;
    if (strcmp(s, "None") == 0) return true;
    if (strcmp(s, "#") == 0) return true;
    if (strcmp(s, "") == 0) return true;
    return false;
}

bool is_valid_bst(int root_count, char** root) {
    if (root_count == 0 || is_empty(root[0])) {
        return true;
    }
    
    // Reconstruct tree iteratively using a queue
    Node** queue = (Node**)malloc(root_count * sizeof(Node*));
    int head = 0, tail = 0;
    
    Node* root_node = create_node(atoi(root[0]));
    queue[tail++] = root_node;
    
    int idx = 1;
    while (head < tail && idx < root_count) {
        Node* curr = queue[head++];
        
        // Left child
        if (idx < root_count) {
            if (!is_empty(root[idx])) {
                curr->left = create_node(atoi(root[idx]));
                queue[tail++] = curr->left;
            }
            idx++;
        }
        
        // Right child
        if (idx < root_count) {
            if (!is_empty(root[idx])) {
                curr->right = create_node(atoi(root[idx]));
                queue[tail++] = curr->right;
            }
            idx++;
        }
    }
    
    // Iterative inorder traversal using a stack to validate BST
    Node** stack = (Node**)malloc(root_count * sizeof(Node*));
    int top = -1;
    
    Node* curr = root_node;
    Node* prev = NULL;
    bool valid = true;
    
    while (curr != NULL || top >= 0) {
        while (curr != NULL) {
            stack[++top] = curr;
            curr = curr->left;
        }
        curr = stack[top--];
        
        if (prev != NULL && curr->val <= prev->val) {
            valid = false;
            break;
        }
        prev = curr;
        curr = curr->right;
    }
    
    // Clean up memory
    free(queue);
    free(stack);
    
    return valid;
}
```

- **Time Complexity:** $O(N)$ where $N$ is the number of elements in the level-order traversal.
- **Space Complexity:** $O(N)$ to store the queue, stack, and reconstructed tree.

---

### Q2. Convert IPv4 to IPv6

**Topic:** `Strings`, `Hexadecimal`, `IP Address`  

Complete the function `convertToIpv6` to convert a given IPv4 address (as a string) to its IPv6 equivalent and print it to the console in all uppercase.

#### Rules of Conversion:
1. Any IPv4 address having the first octet as `127` (e.g. `127.x.x.x`) shall be considered a loopback address, and its IPv6 equivalent is `::1`.
2. For all other IPv4 addresses, convert each of the 4 octets to their 2-digit hexadecimal equivalents (e.g. 192 becomes `C0`, 10 becomes `0A`).
3. Concatenate the first and second hex values, and the third and fourth hex values.
4. The IPv6 address is formed as `::FFFF:<hex1><hex2>:<hex3><hex4>`.

#### Constraints:
- The IPv4 address will have exactly 4 octets.
- Each octet is an integer between 0 and 255.
- The output IPv6 address must be printed in all uppercase.

#### Examples
- **Input:** `192.168.10.92`  
  **Output:** `::FFFF:C0A8:0A5C`
- **Input:** `127.0.0.1`  
  **Output:** `::1`

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void convertToIpv6(char* ipv4address) {
    int octet1, octet2, octet3, octet4;
    if (sscanf(ipv4address, "%d.%d.%d.%d", &octet1, &octet2, &octet3, &octet4) == 4) {
        if (octet1 == 127) {
            printf("::1\n");
        } else {
            printf("::FFFF:%02X%02X:%02X%02X\n", octet1, octet2, octet3, octet4);
        }
    }
}
```

- **Time Complexity:** $O(1)$ constant time parsing and printing.
- **Space Complexity:** $O(1)$ auxiliary space.

---

### Q3. Small Triangles, Large Triangles (Sort by Area)

**Topic:** `Arrays`, `Sorting`, `Geometry`  

You are given `n` triangles, each characterized by the length of its three sides `a`, `b`, and `c`. Sort the triangles in-place based on their areas in ascending order.

The area of a triangle with sides `a`, `b`, and `c` is calculated using Heron's formula:
$$S = \sqrt{p(p-a)(p-b)(p-c)}$$
where $p = (a + b + c) / 2$.

#### Constraints:
- $1 \le n \le 100$
- $1 \le a, b, c \le 70$
- It is guaranteed that a triangle can be formed with the given sides, and all areas are distinct.

#### Example
**Input:**  
```
3
7 24 25
5 12 13
3 4 5
```
**Output:**  
```
3 4 5
5 12 13
7 24 25
```
**Explanation:**  
- Area of triangle (7, 24, 25) = 84
- Area of triangle (5, 12, 13) = 30
- Area of triangle (3, 4, 5) = 6
- Sorting them gives (3, 4, 5) then (5, 12, 13) then (7, 24, 25).

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle {
    int a;
    int b;
    int c;
};

typedef struct triangle triangle;

double get_area(triangle tr) {
    double p = (tr.a + tr.b + tr.c) / 2.0;
    return p * (p - tr.a) * (p - tr.b) * (p - tr.c);
}

int compare(const void* a, const void* b) {
    triangle trA = *(triangle*)a;
    triangle trB = *(triangle*)b;
    double areaA = get_area(trA);
    double areaB = get_area(trB);
    if (areaA < areaB) return -1;
    if (areaA > areaB) return 1;
    return 0;
}

int sort_by_area(triangle* tr, int n) {
    qsort(tr, n, sizeof(triangle), compare);
    return 0;
}
```

- **Time Complexity:** $O(N \log N)$ due to sorting.
- **Space Complexity:** $O(1)$ auxiliary space as the sorting is done in-place.
