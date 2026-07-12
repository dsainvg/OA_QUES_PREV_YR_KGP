# Interview Questions

*Total questions: 28*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [MCQs](#mcqs)

---

## Coding Questions

### Q1. Array Reversal Algorithm

**Topic:** `Arrays`, `Algorithms`, `Pseudocode`

The following pseudocode reverses the elements of an array of size 5:

```python
def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp
    return arr
```

#### Original Pseudocode:
```text
integer i, temp
integer arr[5] = {1, 2, 3, 4, 5}
for (i = 0; i < 5/2; i++)
{
   temp = arr[i]
   arr[i] = arr[5 - i - 1]
   arr[5 - i - 1] = temp
}
```

---

### Q2. Unit Matrix Detection

**Topic:** `Matrices`, `Algorithms`, `Pseudocode`

The following function determines whether a given $n \times n$ matrix is a unit (identity) matrix or not:

```python
def is_unit_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True
```

#### Original Pseudocode:
```text
integer i, j, flag = 1
for (i = 0; i < n; i++)
{
   for (j = 0; j < n; j++)
   {
      if (i == j && arr[i][j] != 1)
      {
         flag = 0
         break
      }
      if (i != j && arr[i][j] != 0)
      {
         flag = 0
         break
      }
   }
}
```

---

### Q3. Mid-Square Hash Key Generation

**Topic:** `Hashing`, `Algorithms`

Calculates the hash key of a number using the Mid-Square hashing technique (extracting the middle digits of the squared value).

```python
def mid_square_hash(key):
    # Square the key
    squared = key * key
    squared_str = str(squared)
    
    # Pad with leading zeros if necessary
    squared_str = squared_str.zfill(8)
    
    # Extract the middle 4 digits
    n = len(squared_str)
    mid_start = (n - 4) // 2
    mid_digits = squared_str[mid_start:mid_start + 4]
    
    return int(mid_digits)
```

---

### Q4. Max Heap Construction & Sibling Node

**Topic:** `Heap`, `Binary Trees`, `Data Structures`

Inserts elements one by one into a Max Heap and provides a function to query the sibling of a given node value.

```python
class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
        
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
            
    def get_sibling(self, val):
        try:
            idx = self.heap.index(val)
        except ValueError:
            return None
        if idx == 0:
            return None  # Root has no sibling
        if idx % 2 == 1:
            # Left child, sibling is right child
            sib_idx = idx + 1
        else:
            # Right child, sibling is left child
            sib_idx = idx - 1
        if sib_idx < len(self.heap):
            return self.heap[sib_idx]
        return None
```

---

### Q5. Circular Linked List Empty Condition

**Topic:** `Linked Lists`, `Data Structures`

Structure and check for an empty circular linked list where the pointer points to the last node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.current = None  # Pointer to the last node of the circular list
        
    def is_empty(self):
        return self.current is None
```

---

## MCQs

### Q1. Partnership Profit Sharing

**Topic:** `Quantitative Aptitude`, `Ratio and Proportion`  

Sujith and Punith entered into a partnership with an investment of Rs. 24,000 and Rs. 36,000 respectively. After 6 months, Vinith also joins them with an investment of Rs. 60,000. At the end of the year, they earned a profit of Rs. 2,40,000. What is the share of Punith in the profit?

**Options:**
- A) Rs. 96,000
- B) Rs. 50,000
- C) Rs. 85,000
- D) Rs. 1,00,000

**Correct Answer:** **A) Rs. 96,000**  
**Explanation:**
- Sujith's investment time = 12 months, investment = Rs. 24,000
- Punith's investment time = 12 months, investment = Rs. 36,000
- Vinith's investment time = 6 months, investment = Rs. 60,000
- Ratio of their profit shares = $(24000 \times 12) : (36000 \times 12) : (60000 \times 6) = 288 : 432 : 360 = 4 : 6 : 5$.
- Total ratio parts = $4 + 6 + 5 = 15$.
- Punith's share = $\frac{6}{15} \times 2,40,000 = \text{Rs. } 96,000$.

---

### Q2. Coding/Decoding (HALFTIME)

**Topic:** `Logical Reasoning`, `Coding-Decoding`  

If in a certain code language, "ABDUCTOR" is coded as "WFZYLIXG", then in the same code language, how will "HALFTIME" be coded?

**Options:**
- A) XW...
- B) OUSZNVGR
- C) SZOUGRNV
- D) SWOBITNV

**Correct Answer:** **B) OUSZNVGR**  
**Explanation:**
- Split the word "ABDUCTOR" into 4 pairs: `AB`, `DU`, `CT`, `OR`.
- Find the alphabetic opposites (A $\leftrightarrow$ Z, B $\leftrightarrow$ Y, C $\leftrightarrow$ X, etc.):
  - `AB` $\rightarrow$ `ZY`
  - `DU` $\rightarrow$ `WF`
  - `CT` $\rightarrow$ `XG`
  - `OR` $\rightarrow$ `LI`
- Swap pair 1 with pair 2, and pair 3 with pair 4:
  - `ZY` $\leftrightarrow$ `WF` $\rightarrow$ `WFZY`
  - `XG` $\leftrightarrow$ `LI` $\rightarrow$ `LIXG`
  - Combined code: `WFZYLIXG`.
- Applying the same logic to "HALFTIME":
  - Pairs: `HA`, `LF`, `TI`, `ME`
  - Opposites:
    - `HA` $\rightarrow$ `SZ`
    - `LF` $\rightarrow$ `OU`
    - `TI` $\rightarrow$ `GR`
    - `ME` $\rightarrow$ `NV`
  - Swap pair 1 with 2: `SZ` $\leftrightarrow$ `OU` $\rightarrow$ `OUSZ`
  - Swap pair 3 with 4: `GR` $\leftrightarrow$ `NV` $\rightarrow$ `NVGR`
  - Combined code: `OUSZNVGR`.

---

### Q3. Speed of Train (Guns Fired)

**Topic:** `Quantitative Aptitude`, `Speed, Distance and Time`  

Two guns were fired from the same place at an interval of 26 minutes but a person in a train approaching the place hears the second report 24 minutes after the first. If the speed of sound is 330 m/s, what is the speed of the train?

**Options:**
- A) 27.5 m/s
- B) 24 m/s
- C) 26 m/s
- D) 33 m/s

**Correct Answer:** **A) 27.5 m/s**  
**Explanation:**
- The distance traveled by the train in 24 minutes is equal to the distance traveled by sound in $(26 - 24) = 2$ minutes.
- Let $v_t$ be the speed of the train and $v_s = 330\text{ m/s}$ be the speed of sound.
- $v_t \times (24 \times 60) = v_s \times (2 \times 60)$
- $v_t \times 24 = 330 \times 2$
- $v_t = \frac{660}{24} = 27.5\text{ m/s}$.

---

### Q4. Sentence Ordering (Boeing B-17)

**Topic:** `Verbal Ability`, `Sentence Reordering`  

Choose the most logical order of the given sentences to construct a coherent paragraph.
- **A.** The airplane circled for a while, then turned for home.
- **B.** Two days earlier, a hurricane had wreaked havoc in Miami, but had since been treading water 350 miles off Jacksonville, where it seemed to wind down.
- **C.** For reasons as obscure as they were controversial, the hurricane followed.
- **D.** On the morning of October 13, 1947, a Boeing B-17 loaded with 180 pounds of crushed dry ice took off from MacDill Field in...
- **E.** The U.S. Air Force B-17 rendezvoused with the storm and climbed 500 feet above its dark upper clouds, where the crew dropped thousand white peas of dry ice (frozen carbon dioxide).

**Options:**
- A) DABEC
- B) DEBCA
- C) DEACB
- D) DBEAC

**Correct Answer:** **D) DBEAC**  
**Explanation:**
- **D** introduces the flight (departure time, plane model, cargo, takeoff location).
- **B** explains the target of the flight (the status and history of the hurricane).
- **E** describes the interaction with the hurricane (climbing above and dropping dry ice).
- **A** describes the end of the seeding operation (circling and heading home).
- **C** provides the unexpected and controversial consequence (the hurricane following the plane).
- Thus, the logical flow is **DBEAC**.

---

### Q5. Geometric Progression (6th term)

**Topic:** `Quantitative Aptitude`, `Progressions`  

The ninth term of the Geometric progression is 81 and the eighth term is 27. Find the 6th term of the GP.

**Options:**
- A) 3
- B) 9
- C) 1/3
- D) 1/9

**Correct Answer:** **A) 3**  
**Explanation:**
- The $n$-th term of a GP is $a_n = a r^{n-1}$.
- Given $a_9 = 81$ and $a_8 = 27$.
- The common ratio $r = \frac{a_9}{a_8} = \frac{81}{27} = 3$.
- The 6th term is $a_6 = \frac{a_8}{r^2} = \frac{27}{3^2} = \frac{27}{9} = 3$.

---

### Q6. Letter Pair Counting (ESCAPE)

**Topic:** `Logical Reasoning`, `Alphanumeric Series`  

How many such pairs of letters are there in the word ESCAPE each of which has as many letters between them in the word as they have between them in the English alphabetical series (in both forward and backward directions)?

**Options:**
- A) 3
- B) 1
- C) None
- D) 2

**Correct Answer:** **D) 2**  
**Explanation:**
- In the forward direction:
  - **C** and **E** (C $\rightarrow$ D $\rightarrow$ E): there is 1 letter between them in the word (A or P), and 1 letter between them in the English alphabet (D).
- In the backward direction:
  - **P** and **S** (P $\rightarrow$ Q $\rightarrow$ R $\rightarrow$ S): there are 2 letters between them in the word (A and C), and 2 letters between them in the English alphabet (Q and R).
- Thus, there are exactly 2 such pairs.

---

### Q7. Grammar Idiom (Sovereign over)

**Topic:** `Verbal Ability`, `Sentence Correction`  

Identify the correct preposition to complete the sentence:
"Every individual is sovereign [above his] own person and property."

**Options:**
- A) around his
- B) inside his
- C) over his
- D) No improvement

**Correct Answer:** **C) over his**  
**Explanation:** The correct standard English preposition used with "sovereign" in this context is "over" (i.e., "sovereign over").

---

### Q8. Average Speed (Pune to Kolkata)

**Topic:** `Quantitative Aptitude`, `Speed, Distance and Time`  

A person goes from Pune to Kolkata at a speed of 50 km/hr and returns at a speed of 75 km/hr. Find the average speed during the whole journey.

**Options:**
- A) 62.5 km/hr
- B) 57.5 km/hr
- C) 60 km/hr
- D) 72 km/hr

**Correct Answer:** **C) 60 km/hr**  
**Explanation:**
- For equal distances traveled at speeds $v_1$ and $v_2$, the average speed is given by:
  $$\text{Average Speed} = \frac{2 v_1 v_2}{v_1 + v_2} = \frac{2 \times 50 \times 75}{50 + 75} = \frac{7500}{125} = 60\text{ km/hr}.$$

---

### Q9. Word Substitution (Rapturous)

**Topic:** `Verbal Ability`, `One Word Substitution`  

Choose the word which can be substituted for the given sentence:
"A face filled with pleasure and excitement"

**Options:**
- A) Grinning face
- B) Rapturous face
- C) Joyous face
- D) Smiling face

**Correct Answer:** **B) Rapturous face**  
**Explanation:** "Rapturous" is defined as feeling or expressing great pleasure or enthusiasm. A face filled with pleasure and excitement is best described as a "rapturous face".

---

### Q10. Combinatorics Locker Code (Odd numbers)

**Topic:** `Quantitative Aptitude`, `Permutations and Combinations`  

How many odd numbers are there between 50 and 450 written with the digits {0, 1, 2, 3, 4, 5} without repetition?

**Options:**
- A) 82
- B) 92
- C) 62
- D) 72

**Correct Answer:** **D) 72**  
**Explanation:**
- Although the question specifies "without repetition", the options correspond to the case where **repetition of digits is allowed**:
  1. **2-digit odd numbers ($\ge 50$):**
     - Tens place: Must be $5$ (1 option).
     - Units place: Must be odd ($1, 3, 5$) (3 options).
     - Total = $1 \times 3 = 3$ numbers (51, 53, 55).
  2. **3-digit odd numbers ($100$ to $399$):**
     - Hundreds place: Must be $1, 2,$ or $3$ (3 options).
     - Tens place: Any digit from $\{0, 1, 2, 3, 4, 5\}$ (6 options).
     - Units place: Must be odd ($1, 3, 5$) (3 options).
     - Total = $3 \times 6 \times 3 = 54$ numbers.
  3. **3-digit odd numbers ($400$ to $450$):**
     - Hundreds place: Must be $4$ (1 option).
     - Tens place: Must be $0, 1, 2, 3,$ or $4$ (5 options).
     - Units place: Must be odd ($1, 3, 5$) (3 options).
     - Total = $1 \times 5 \times 3 = 15$ numbers.
  - **Total Odd Numbers** = $3 + 54 + 15 = 72$.
- If repetition were strictly not allowed, the total count would be **40** (which is not in the options).

---

### Q11. Venn Diagram (Science, Math, Hindi)

**Topic:** `Quantitative Aptitude`, `Set Theory`  

The percentage of students who passed all courses in the CBSE Board Exams last year was 52% in Science, 42% in Math, 63% in Hindi, 15% in Math and Science, 25% in Science and Hindi, 37% in Math and Hindi, and 10% in none. What is the percentage who passed in all?

**Options:**
- A) 40%
- B) 10%
- C) 30%
- D) 20%

**Correct Answer:** **B) 10%**  
**Explanation:**
- Let $S$, $M$, and $H$ represent the sets of students who passed Science, Math, and Hindi respectively.
- Total students who passed at least one subject = $100\% - 10\% = 90\%$.
- Using the principle of inclusion-exclusion:
  $$|S \cup M \cup H| = |S| + |M| + |H| - (|S \cap M| + |S \cap H| + |M \cap H|) + |S \cap M \cap H|$$
- Substitute the given values:
  $$90 = 52 + 42 + 63 - (15 + 25 + 37) + |S \cap M \cap H|$$
  $$90 = 157 - 77 + |S \cap M \cap H|$$
  $$90 = 80 + |S \cap M \cap H|$$
  $$|S \cap M \cap H| = 10\%$$
- Therefore, the percentage of students who passed in all subjects is 10%.

---

### Q12. Mid-Square Hash Key

**Topic:** `Hashing`, `Data Structures`  

What will be the hash key for 4352 if mid-square hashing is used?

**Options:**
- A) 9390
- B) 8939
- C) 9904
- D) 9399

**Correct Answer:** **D) 9399**  
**Explanation:**
- $4352^2 = 18939904$.
- The middle four digits of this 8-digit number are 9399 (since indices 2 to 5 in 18939904 are 9399: 18 **9399** 04).

---

### Q13. Array Reversal Code

**Topic:** `Computer Science`, `Pseudocode`  

Identify the output of the following pseudocode:
```text
integer i, temp
integer arr[5] = {1, 2, 3, 4, 5}
for (i = 0; i < 5/2; i++)
{
   temp = arr[i]
   arr[i] = arr[5 - i - 1]
   arr[5 - i - 1] = temp
}
```

**Options:**
- A) Finds the sum of the array elements
- B) Sorts the array
- C) Performs search on the array elements
- D) Reverse the array

**Correct Answer:** **D) Reverse the array**  
**Explanation:** The loop swaps elements from the beginning with elements from the end (first with last, second with second-to-last), which reverses the array.

---

### Q14. Max Heap Construction

**Topic:** `Heap`, `Data Structures`  

Construct a max heap for the following elements: 3, 5, 8, 88, 6, 45. Which of the following statement is true when 50 is inserted in the heap?

**Options:**
- A) Sibling of 5 is 3
- B) Sibling of 45 is 8
- C) Sibling of 8 is 50
- D) Sibling of 88 is 50

**Correct Answer:** **C) Sibling of 8 is 50**  
**Explanation:**
- Constructing the max heap by inserting elements one by one:
  1. Insert 3: `[3]`
  2. Insert 5: `[5, 3]` (heapify up)
  3. Insert 8: `[8, 3, 5]` (heapify up)
  4. Insert 88: `[88, 8, 5, 3]` (heapify up)
  5. Insert 6: `[88, 8, 5, 3, 6]` (heapify up)
  6. Insert 45: `[88, 8, 45, 3, 6, 5]` (heapify up)
- Inserting 50:
  - Add 50 at the end: `[88, 8, 45, 3, 6, 5, 50]`
  - Heapify up: 50 is compared and swapped with its parent 45: `[88, 8, 50, 3, 6, 5, 45]`
- In the final heap, the children of the root (88) are 8 (left) and 50 (right).
- Therefore, the sibling of 8 is 50.

---

### Q15. Circular Linked List Empty Condition

**Topic:** `Linked Lists`, `Data Structures`  

Let current be a pointer pointing to the last node of the circular linked list L. Which of the following condition is true if L is empty?

**Options:**
- A) current == NULL
- B) current.next == NULL
- C) current.next == head
- D) head == NULL

**Correct Answer:** **A) current == NULL**  
**Explanation:** If the list is empty, there are no nodes in the list, so the pointer `current` must be `NULL`.

---

### Q16. Graph Theory Complete Graph Degree

**Topic:** `Graph Theory`, `Computer Science`  

Choose the correct statement about a graph.

**Options:**
- A) A graph is collection of nodes and edges, where each edge has a weight.
- B) In a complete graph, the degree of each vertex is n-1.
- C) A tree is a graph with cycles.
- D) Every graph must be connected.

**Correct Answer:** **B) In a complete graph, the degree of each vertex is n-1.**  
**Explanation:** A complete graph with $n$ vertices has an edge between every pair of vertices. Hence, each vertex is connected to all other $n-1$ vertices, making its degree $n-1$.

---

### Q17. Unit Matrix Detection Algorithm

**Topic:** `Matrices`, `Pseudocode`  

What does the following pseudocode perform?
```text
integer i, j, flag = 1
for (i = 0; i < n; i++)
{
   for (j = 0; j < n; j++)
   {
      if (i == j && arr[i][j] != 1)
      {
         flag = 0
         break
      }
      if (i != j && arr[i][j] != 0)
      {
         flag = 0
         break
      }
   }
}
```

**Options:**
- A) Finds whether the given matrix is a unit matrix or not.
- B) Finds whether the given matrix is a diagonal matrix or not.
- C) Finds whether the given matrix is a symmetric matrix or not.
- D) Finds whether the given matrix is a skew-symmetric matrix or not.

**Correct Answer:** **A) Finds whether the given matrix is a unit matrix or not.**  
**Explanation:** The pseudocode checks if all diagonal elements ($i == j$) are equal to 1, and all non-diagonal elements ($i != j$) are equal to 0. This is the definition of a unit (identity) matrix.

---

### Q18. Die Roll Probability

**Topic:** `Probability`, `Quantitative Aptitude`  

A cubical die is marked 'x' on three faces, 'y' on two faces and 'z' on one face. It is rolled twice. What is the probability that both rolls yield the same result?

**Options:**
- A) 7/18
- B) 1/3
- C) 5/18
- D) 1/2

**Correct Answer:** **A) 7/18**  
**Explanation:**
- The probability of getting 'x' is $3/6 = 1/2$, 'y' is $2/6 = 1/3$, and 'z' is $1/6$.
- Probability of same result: $P(x, x) + P(y, y) + P(z, z) = (1/2)^2 + (1/3)^2 + (1/6)^2 = 1/4 + 1/9 + 1/36 = \frac{9+4+1}{36} = \frac{14}{36} = \frac{7}{18}$.

---

### Q19. Linear Arrangement (Class 8th, 9th, 10th)

**Topic:** `Logical Reasoning`, `Linear Arrangement`  

There are eight students standing in a row facing south. They are standing in such a way that the height decreases from right to extreme left end of the row. Three students are from class 8th, three are from 9th and the remaining are from class 10th.
i) A is the 2nd tallest but not from class 8th.
ii) E and B are from class 9th.
iii) C is shorter than G but taller than F and is not from class 10th.
iv) B is the 4th tallest and H is shorter than B.
v) Neither the shortest nor the 2nd shortest students are from class 8th.
vi) H is taller than G and D is shorter than A.

*Question: Which of the following pairs are from the same class and standing near each other?*

**Options:**
- A) A, D
- B) B, H
- C) A, C
- D) H, G

**Correct Answer:** **D) H, G**  
**Explanation:**
- Height order (tallest to shortest): $E(9), A(10), D(8), B(9), H(8), G(8), C(9), F(10)$.
- Students $H$ and $G$ are adjacent and both belong to class 8th.

---

### Q20. Blood Relation Expression

**Topic:** `Logical Reasoning`, `Blood Relations`  

If:
- `X % Y` means X is the daughter of Y.
- `X @ Y` means X is the son of Y.
- `X $ Y` means X is the mother of Y.
- `X & Y` means X is the brother of Y.

How is N related to Q in the expression `M % N & O $ P & Q @ S`?

**Options:**
- A) Father
- B) Brother-in-law
- C) Uncle
- D) Grandfather

**Correct Answer:** **C) Uncle**  
**Explanation:**
- `M % N` $\rightarrow$ M is daughter of N.
- `N & O` $\rightarrow$ N is brother of O.
- `O $ P` $\rightarrow$ O is mother of P.
- `P & Q` $\rightarrow$ P is brother of Q.
- So O is the mother of Q. N is the brother of O (Q's mother). Thus, N is Q's maternal uncle.

---

### Q21. Circle Radius (Circumference 25pi)

**Topic:** `Geometry`, `Quantitative Aptitude`  

The circumference of a circle is $25\pi$ cm. Find the radius of the circle.

**Options:**
- A) 11.5 cm
- B) 12 cm
- C) 12.5 cm
- D) 13.5 cm

**Correct Answer:** **C) 12.5 cm**  
**Explanation:**
- Circumference $C = 2\pi r = 25\pi \implies r = 12.5\text{ cm}$.

---

### Q22. Partnership Capital Contribution (X & Y)

**Topic:** `Partnership`, `Quantitative Aptitude`  

X started a business with Rs. 6500 and after 7 months, Y joined the business with X as a partner. After a year the profit was divided in the ratio 4 : 3. What is Y's contribution in the capital?

**Options:**
- A) Rs. 20,800
- B) Rs. 17,300
- C) Rs. 11,700
- D) Rs. 14,600

**Correct Answer:** **C) Rs. 11,700**  
**Explanation:**
- X invested for 12 months, Y invested for 5 months.
- $\frac{6500 \times 12}{C_y \times 5} = \frac{4}{3} \implies C_y = 11,700$.

---

### Q23. Rectangle Area Increase (Stretched wire)

**Topic:** `Mensuration`, `Quantitative Aptitude`  

A rectangle is made by tying the ends of four broken copper wires to each other. One copper wire is stretched from one end (three vertices remain in the same place) so that its length increases by 20%. By what percentage does the area of the quadrilateral increase if the three vertices remain in the same place?

**Options:**
- A) 44%
- B) 10%
- C) 20%
- D) Cannot be determined

**Correct Answer:** **B) 10%**  
**Explanation:**
- Let the initial area be $LW$. By shifting one vertex $A$ to $A'$ by 20% of the width $W$ (while $B, C, D$ stay fixed), the area of the new shape increases by $\frac{0.2W \times L}{2} = 0.1 LW$.
- So the area increases by 10%.

---

### Q24. Venn Diagram / Optimization (Engineering College)

**Topic:** `Set Theory`, `Quantitative Aptitude`  

In an Engineering college with 100 students, anyone who has chosen to study Electronics elects to do Communication. But no one does both Electronics and Computers, while 26 do Communication and Computers. All the students take at least one of the three subjects. The number of people who do exactly one of the three is more than twice the number of people who do more than one of the three. Find the maximum number of people who could have opted for Electronics only?

**Options:**
- A) 26
- B) 7
- C) 74
- D) 52

**Correct Answer:** **B) 7**  
**Explanation:**
- Let $c$, $p$, $e$, $cp$ be the counts. We have $c+p+e+26=100 \implies c+p=74-e$.
- Inequality: $c+p > 2(e+26) \implies 74-e > 2e+52 \implies 22 > 3e \implies e < 7.33$.
- The maximum integer value of $e$ is 7.

---

### Q25. Stock Dividend Investment

**Topic:** `Stocks and Shares`, `Quantitative Aptitude`  

Ben invests a total of Rs. 5000 in two different stocks, the first stock quoted at Rs. 154 gets a dividend of 7% and the second stock is quoted at Rs. 99 gets a dividend of 11%. If his total annual income is Rs. 375, find the amount he invested in the second stock which gives an 11% dividend.

**Options:**
- A) Rs. 3000
- B) Rs. 2000
- C) Rs. 2250
- D) Rs. 3500

**Correct Answer:** **C) Rs. 2250**  
**Explanation:**
- Let $y$ be the investment in stock 2.
- $\frac{5000 - y}{22} + \frac{y}{9} = 375 \implies y\left(\frac{13}{198}\right) = \frac{1625}{11} \implies y = 2250$.

---

### Q26. Blood Relation Riddle (E and B)

**Topic:** `Blood Relations`, `Logical Reasoning`  

Pointing to a photo of R, Mr. B said: "she is the daughter of my only sister's only son's only uncle." Pointing to the same photo, E said: "she is the daughter of my father's wife's only brother." How is E related to B?

**Options:**
- A) Nephew
- B) Uncle
- C) Niece
- D) Son

**Correct Answer:** **A) Nephew**  
**Explanation:**
- Mr. B's only sister's only son's only uncle is Mr. B himself. Thus, R is Mr. B's daughter.
- E says R is the daughter of E's mother's only brother (which is B). So B is E's maternal uncle.
- Since B's sister has an only son (E), E is B's nephew.
