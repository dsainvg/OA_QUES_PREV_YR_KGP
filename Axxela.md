# Interview Questions

*Total questions: 10*

---

## Table of Contents

1. [Coding Questions](#coding-questions)
2. [SQL Questions](#sql-questions)
3. [Theoretical Questions](#theoretical-questions)
4. [System Design Questions](#system-design-questions)
5. [Behavioral Questions](#behavioral-questions)
6. [MCQs](#mcqs)
7. [Puzzles](#puzzles)

---

## Coding Questions

No coding questions were found in the source files.

---

## SQL Questions

No SQL questions were found in the source files.

---

## Theoretical Questions

No theoretical questions were found in the source files.

---

## System Design Questions

No system design questions were found in the source files.

---

## Behavioral Questions

No behavioral questions were found in the source files.

---

## MCQs

### Q1. Mirror Image of Character Sequence

**Topic:** `logical-reasoning`, `mirror-image`

Choose the option which shows the correct mirror image of the characters given below.
`SJR9PZE7C18`

**Options:**
- A) Mirrored `81C7ZE9RJS`
- B) Mirrored `SJR9PZE7C18`
- C) Mirrored `SJR9PZE7C18` with slight variations
- D) Mirrored `SJR9PZE7C18` with other variations

**Correct Answer:** A (reverses the order of characters to start with `8` and end with `S`, with each character mirrored).

**Explanation:**
A vertical mirror placed to the right or left of a text reverses the order of characters (the last character becomes first, and the first character becomes last) and mirrors each individual character horizontally.
- Reversed order: `8`, `1`, `C`, `7`, `E`, `Z`, `P`, `9`, `R`, `J`, `S`
- Flipped horizontally, this corresponds to the sequence starting with `8` (Option A).

---

### Q2. Age Word Problem

**Topic:** `quantitative-aptitude`, `ages`

Aman, Ayaz and Ashwinder are members of a joint family. Among them, Aman is the eldest of all. Aman is six years elder than Ayaz. Ayaz is eight years elder than Ashwinder. The sum of the present ages of Aman and Ayaz is five times the age of Ashwinder four years ago. The present age of Aman is:

**Options:**
- A) 20
- B) 24
- C) 28
- D) 32

**Correct Answer:** C) 28

**Explanation:**
Let $A$, $Y$, and $S$ represent the present ages of Aman, Ayaz, and Ashwinder respectively.
1. Aman is 6 years elder than Ayaz:
   $$A = Y + 6 \implies Y = A - 6$$
2. Ayaz is 8 years elder than Ashwinder:
   $$Y = S + 8 \implies S = Y - 8 = A - 14$$
3. Sum of present ages of Aman and Ayaz is 5 times Ashwinder's age 4 years ago:
   $$A + Y = 5(S - 4)$$
   Substitute $Y$ and $S$:
   $$A + (A - 6) = 5((A - 14) - 4)$$
   $$2A - 6 = 5(A - 18)$$
   $$2A - 6 = 5A - 90$$
   $$3A = 84 \implies A = 28$$
Thus, the present age of Aman is 28.

---

## Puzzles

### Q3. Letter Series Completion

**Topic:** `logical-reasoning`, `series-completion`

Certain blank spaces are left in the following series. Which is the group of letters given below if put in the blank space in sequences, will complete the series?

`c _ ba _ cb _ cc _ ac _ ba`

**Answer:** `c, c, a, b, c` (forming `ccabc`)

**Explanation:**
The sequence consists of 16 characters. Let's group them into 4-letter repeating blocks:
- Block 1: `c [c] b a` (fills 1st blank with `c`)
- Block 2: `[c] c b [a]` (fills 2nd blank with `c` and 3rd with `a`)
- Block 3: `c c [b] a` (fills 4th blank with `b`)
- Block 4: `c [c] b a` (fills 5th blank with `c`)

Combining all blocks, we get the repeated pattern `c c b a` four times:
`c c b a | c c b a | c c b a | c c b a`
Hence, the filled letters in order are: `c, c, a, b, c`.

---

### Q4. Number Series Completion

**Topic:** `logical-reasoning`, `number-series`

Identify the missing number in the following series:

`2, 10, 30, 68, ___, 222`

**Answer:** `130`

**Explanation:**
Let $t_n$ be the $n$-th term of the series:
- $t_1 = 1^3 + 1 = 2$
- $t_2 = 2^3 + 2 = 10$
- $t_3 = 3^3 + 3 = 30$
- $t_4 = 4^3 + 4 = 68$
- $t_5 = 5^3 + 5 = 125 + 5 = 130$
- $t_6 = 6^3 + 6 = 216 + 6 = 222$

Therefore, the missing number is `130`.

---

### Q5. Star/Cross Grid Puzzle

**Topic:** `logical-reasoning`, `grid-puzzles`

Find the value of $W$, $X$, $Y$, and $Z$ in the given star/cross grid layout where numbers are arranged in 8 arms radiating from a central cell containing `1`.

**Answer:**
- $W = 8$
- $X = 9$
- $Y = 4$
- $Z = 1$

**Explanation:**
The grid contains 8 arms radiating from the center `1`. The values along each opposite arm (excluding the center `1`) sum to a constant value:
1. **Horizontal Line (West and East arms):**
   - Left (West) arm: `3, 9, 5, W` $\implies \text{Sum} = 3 + 9 + 5 + W = 17 + W$
   - Right (East) arm: `7, 6, 4, 8` $\implies \text{Sum} = 7 + 6 + 4 + 8 = 25$
   - Since opposite arms have equal sum:
     $$17 + W = 25 \implies W = 8$$

2. **Vertical Line (North and South arms):**
   - Top (North) arm: `9, 5, 4, Z` $\implies \text{Sum} = 9 + 5 + 4 + Z = 18 + Z$
   - Bottom (South) arm: `3, 8, 2, 6` $\implies \text{Sum} = 3 + 8 + 2 + 6 = 19$
   - Since opposite arms have equal sum:
     $$18 + Z = 19 \implies Z = 1$$

3. **North-West to South-East Diagonal:**
   - Top-Left (North-West) arm: `7, 8, 4, 2` $\implies \text{Sum} = 7 + 8 + 4 + 2 = 21$
   - Bottom-Right (South-East) arm: `9, Y, 3, 5` $\implies \text{Sum} = 9 + Y + 3 + 5 = 17 + Y$
   - Since opposite arms have equal sum:
     $$17 + Y = 21 \implies Y = 4$$

4. **North-East to South-West Diagonal:**
   - Top-Right (North-East) arm: `8, 2, X, 3` $\implies \text{Sum} = 8 + 2 + X + 3 = 13 + X$
   - Bottom-Left (South-West) arm: `4, 7, 6, 5` $\implies \text{Sum} = 4 + 7 + 6 + 5 = 22$
   - Since opposite arms have equal sum:
     $$13 + X = 22 \implies X = 9$$

---

### Q6. H-Shaped Blocks Puzzle

**Topic:** `logical-reasoning`, `grid-puzzles`

Identify the missing number `?` in the third block:
```
Block 1:             Block 2:             Block 3:
  8     5              2     12             10     8  
     44                   54                   80   
  3     9              4     3              6      ?  
```

**Answer:** `3` (or `13`)

**Explanation:**
The relationship between the corner numbers ($TL$: Top-Left, $TR$: Top-Right, $BL$: Bottom-Left, $BR$: Bottom-Right) and the center number is:
$$\text{Center} = (TL + BL) \times |TR - BR|$$

Let's verify this pattern:
- **Block 1:** $(8 + 3) \times |5 - 9| = 11 \times 4 = 44$.
- **Block 2:** $(2 + 4) \times |12 - 3| = 6 \times 9 = 54$.
- **Block 3:** $(10 + 6) \times |8 - ?| = 80 \implies 16 \times |8 - ?| = 80 \implies |8 - ?| = 5$.
  - If $8 - ? = 5 \implies ? = 3$.
  - If $? - 8 = 5 \implies ? = 13$.

Hence, the missing value is `3` (or `13` depending on options).

---

### Q7. Triangle Grid Puzzle

**Topic:** `logical-reasoning`, `grid-puzzles`

Identify the missing number `?` in the third triangle:
```
Triangle 1:          Triangle 2:          Triangle 3:
      7                    5                    9      
   5    12              6     8              ?     6   
      42                   24                   81     
```

**Answer:** `15` (or `27`)

**Explanation:**
There are two patterns that fit the first two triangles:

**Pattern A (Product-based):**
The center value is one-tenth of the product of all three corner values:
$$\text{Center} = \frac{\text{Top-Left} \times \text{Top-Right} \times \text{Bottom}}{10}$$
- **Triangle 1:** $\frac{7 \times 5 \times 12}{10} = \frac{420}{10} = 42$.
- **Triangle 2:** $\frac{5 \times 6 \times 8}{10} = \frac{240}{10} = 24$.
- **Triangle 3:** $\frac{9 \times ? \times 6}{10} = 81 \implies 54 \times ? = 810 \implies ? = 15$.

**Pattern B (Max corner-based):**
$$\text{Center} = \max(\text{Top-Left}, \text{Top-Right}) \times \frac{\text{Bottom}}{2}$$
- **Triangle 1:** $\max(7, 5) \times \frac{12}{2} = 7 \times 6 = 42$.
- **Triangle 2:** $\max(5, 6) \times \frac{8}{2} = 6 \times 4 = 24$.
- **Triangle 3:** $\max(9, ?) \times \frac{6}{2} = 81 \implies \max(9, ?) = 27 \implies ? = 27$.

Both patterns are valid, with `15` being the most standard arithmetic solution.

---

### Q8. Letter Coding/Decoding

**Topic:** `logical-reasoning`, `coding-decoding`

If `MOBILE` is coded as `DFBICE`, then `CHARGE` is coded as:

**Answer:** `CHAIGE`

**Explanation:**
First, map each letter of `MOBILE` to its 1-based alphabetical position:
- `M` = 13 $\implies 1 + 3 = 4$ (`D`)
- `O` = 15 $\implies 1 + 5 = 6$ (`F`)
- `B` = 2 $\implies 2$ (`B`)
- `I` = 9 $\implies 9$ (`I`)
- `L` = 12 $\implies 1 + 2 = 3$ (`C`)
- `E` = 5 $\implies 5$ (`E`)

The pattern is to sum the digits of the alphabetical position of each letter. If the sum is a single digit, it remains unchanged.

Applying the same logic to `CHARGE`:
- `C` = 3 $\implies 3$ (`C`)
- `H` = 8 $\implies 8$ (`H`)
- `A` = 1 $\implies 1$ (`A`)
- `R` = 18 $\implies 1 + 8 = 9$ (`I`)
- `G` = 7 $\implies 7$ (`G`)
- `E` = 5 $\implies 5$ (`E`)

Hence, the code for `CHARGE` is `CHAIGE`.

---

### Q9. Mean of 15 Natural Numbers

**Topic:** `quantitative-aptitude`, `averages`

The mean of fifteen different natural numbers is 13. The maximum value for the second largest of these numbers is:

**Answer:** `51`

**Explanation:**
Let the 15 distinct natural numbers in ascending order be $x_1 < x_2 < x_3 < \dots < x_{15}$.
The mean is 13, which means their sum is:
$$\sum_{i=1}^{15} x_i = 15 \times 13 = 195$$

To maximize the second largest number $x_{14}$, we must minimize the first 13 numbers.
Since they are distinct natural numbers, the minimum values for the first 13 numbers are:
$$x_1 = 1, x_2 = 2, \dots, x_{13} = 13$$
The sum of these first 13 numbers is:
$$\sum_{i=1}^{13} i = \frac{13 \times 14}{2} = 91$$

This leaves the remaining sum for $x_{14} + x_{15}$:
$$x_{14} + x_{15} = 195 - 91 = 104$$

Since the numbers are distinct, $x_{14} < x_{15}$.
To make $x_{14}$ as large as possible, we make $x_{14}$ and $x_{15}$ as close as possible:
$$2 \cdot x_{14} < 104 \implies x_{14} \le 51.5$$
Since $x_{14}$ must be an integer, the maximum value for $x_{14}$ is `51` (with $x_{15} = 53$).
Verification: All values $\{1, 2, \dots, 13, 51, 53\}$ are distinct, natural numbers, and their sum is $91 + 51 + 53 = 195$.

---

### Q10. Direction and Distance Word Problem

**Topic:** `quantitative-aptitude`, `direction-sense`

A person walked 100m straight from the point A in the North-East direction, walked 200m in the South-West direction from there, 100m in the North-East direction again, walked 100m east, 200m southward and 100m westward to reach at point B. Find the distance and direction of point B with respect to point A.

**Answer:** `200m South`

**Explanation:**
1. Let point A be at the origin $(0, 0)$.
2. Walking $100\text{ m}$ North-East, then $200\text{ m}$ South-West, and then $100\text{ m}$ North-East brings the person back to the starting point $(0, 0)$ because the North-East and South-West directions are exactly opposite:
   $$\text{Net Diagonal Displacement} = 100\text{ m (NE)} - 200\text{ m (SW)} + 100\text{ m (NE)} = 0\text{ m}$$
3. From $(0, 0)$, the person walks:
   - $100\text{ m}$ East
   - $200\text{ m}$ South
   - $100\text{ m}$ West
4. The $100\text{ m}$ East and $100\text{ m}$ West cancel each other out, leaving only the $200\text{ m}$ South displacement.
5. Therefore, point B is exactly $200\text{ m}$ directly South of point A.
