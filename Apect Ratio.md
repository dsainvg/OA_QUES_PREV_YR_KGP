# Interview Questions

  

*Generated from: [Apect Ratio](file:///R:/DSA/Company wise prep resource/Apect Ratio)*  

*Total unique questions: 9*  

  

---

  

## Table of Contents

1. [Theoretical Questions](#theoretical-questions)
2. [Puzzles / Logical Reasoning](#puzzles-logical-reasoning)

---

  

## Theoretical Questions

  

### Q2. Novartis Regulatory Shortcut

  

**Topic:** `verbal`, `vocabulary`, `fill-in-the-blank`  

**Source File:** [IMG-20240803-WA0063.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0063.jpg)

  

#### Question

Novartis is paying $100M for the opportunity to shorten the regulatory ___ of a rare disease drug candidate in the indeterminate future.

  

#### Solution/Answer

**Answer:** **pathway** (or **process** / **timeline** / **course**).  

*Explanation:* In pharmaceutical development and FDA approval contexts, "regulatory pathway" is the standard term used to describe the sequence of steps required to bring a drug candidate to market.

  

---

  

### Q5. Pharma Industry Privacy Regulations

  

**Topic:** `verbal`, `vocabulary`, `fill-in-the-blank`  

**Source Files:** [IMG-20240803-WA0066.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0066.jpg), [IMG-20240803-WA0067.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0067.jpg) *(seen in both files)*

  

#### Question

It is expected that the pharma industry, being an already highly ___ space, won't be affected as much as others due to the new, stringent privacy regulations.

  

#### Solution/Answer

**Answer:** **regulated** (or **compliant** / **monitored**).  

*Explanation:* Because the pharmaceutical industry is already heavily regulated by various government bodies, new privacy regulations will not require as much operational shift compared to less regulated sectors.

  

---

  

### Q6. Clinical Trial Significance

  

**Topic:** `verbal`, `vocabulary`, `fill-in-the-blank`  

**Source File:** [IMG-20240803-WA0068.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0068.jpg)

  

#### Question

Results from the clinical trials were statistically significant and clinically ___

  

#### Solution/Answer

**Answer:** **meaningful** (or **relevant** / **significant**).  

*Explanation:* The phrase "statistically significant and clinically meaningful" is standard terminology in clinical research, indicating that the trial results are not only mathematically sound but also have practical therapeutic value for patients.

  

---

  

### Q8. Pharma Digital Health Focus

  

**Topic:** `verbal`, `vocabulary`, `fill-in-the-blank`  

**Source File:** [IMG-20240803-WA0070.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0070.jpg)

  

#### Question

The pharma major shifted its focus towards digital health by ___ digital solutions based on AI and allied technologies.

  

#### Solution/Answer

**Answer:** **adopting** (or **integrating** / **developing** / **implementing**).  

*Explanation:* The context implies that the pharmaceutical company is incorporating new AI-based technological solutions into its operations.

  

---

  

### Q9. Cloud Computing Healthcare Stakeholders

  

**Topic:** `verbal`, `vocabulary`, `fill-in-the-blank`  

**Source File:** [IMG-20240803-WA0071.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0071.jpg)

  

#### Question

Cloud computing environments provide several benefits to all the ___ in the healthcare ecosystem.

  

#### Solution/Answer

**Answer:** **stakeholders** (or **participants** / **actors** / **entities**).  

*Explanation:* "Stakeholders" is the most appropriate term to describe all parties involved in the healthcare system (e.g., patients, doctors, insurers, pharmaceutical companies).

  

---

  

## Puzzles / Logical Reasoning

  

### Q3. Mathematical Ability Ranking

  

**Topic:** `logical-reasoning`, `ranking`, `puzzles`  

**Source File:** [IMG-20240803-WA0064.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0064.jpg)

  

#### Question

In a class, students are allocated a rank dependent on their mathematical ability. Alex has the 8th highest rank and Bob's rank is 20 places higher than the lowest ranked student. How many students are there in the class, if Bob has a higher rank than Alex and there is only 1 student ranked between Alex and Bob?

  

#### Solution/Answer

**Answer:** **26**

  

**Analytical Explanation:**

1. Alex's rank is 8 (8th from the top, where 1st is the highest).

2. Bob has a higher rank than Alex, which means Bob's rank number is smaller than 8.

3. There is exactly 1 student between Alex (8th) and Bob. This implies Bob must be 6th (since 7th would be between them).

4. Bob's rank is 20 places higher than the lowest ranked student. Let $N$ be the lowest rank (which equals the total number of students).

5. "20 places higher" means we subtract 20 from $N$:

   $$\text{Bob's Rank} = N - 20 \implies 6 = N - 20 \implies N = 26$$

6. Therefore, there are 26 students in the class.

  

**Python Verification Code:**

```python

def find_class_size():

    # Alex's rank (1-indexed from top)

    alex_rank = 8

    # Bob has a higher rank than Alex (i.e. rank number is smaller)

    # There is only 1 student between Alex and Bob

    bob_rank = alex_rank - 2  # Bob is 6th

    # Bob's rank is 20 places higher than the lowest ranked student (total students N)

    # Bob_rank = N - 20 -> N = Bob_rank + 20

    total_students = bob_rank + 20

    return total_students

  

print("Total students in the class:", find_class_size())  # Output: 26

```

  

---

  

### Q4. Male to Female Ratio Comparison

  

**Topic:** `logical-reasoning`, `ratio-comparison`, `puzzles`  

**Source File:** [IMG-20240803-WA0065.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0065.jpg)

  

#### Question

1. City P has a higher ratio of males to females than city Q.

2. City S has a lower ratio of males to females than city R.

3. The ratio of males to females is the same in city Q and city T.

4. City R has a lower ratio of females to males than city P.

5. City R has the highest ratio of males to females among the five cities.

  

If the first four statements are true, then the last statement is:

  

#### Solution/Answer

**Answer:** **True**

  

**Analytical Explanation:**

Let $R_X = \frac{\text{Males}_X}{\text{Females}_X}$ be the male-to-female ratio for city $X$.

1. Statement 1: $R_P > R_Q$

2. Statement 2: $R_S < R_R \implies R_R > R_S$

3. Statement 3: $R_Q = R_T$

4. Statement 4: "City R has a lower ratio of females to males than city P." The female-to-male ratio is $\frac{1}{R_X}$.

   So, $\frac{1}{R_R} < \frac{1}{R_P} \implies R_R > R_P$.

5. Let's combine the inequalities:

   $$R_R > R_P > R_Q = R_T$$

   We also know $R_R > R_S$.

6. This shows that $R_R$ is strictly greater than all other ratios ($R_P, R_Q, R_T, R_S$).

7. Thus, City R has the highest ratio of males to females among the five cities. Statement 5 is **True**.

  

**Python Verification Code:**

```python

def verify_ratio_statements():

    # Let's assign relative values that satisfy the first 4 statements and check Statement 5.

    # 1. R_P > R_Q

    # 2. R_R > R_S

    # 3. R_Q == R_T

    # 4. R_R > R_P

    # We can assign dummy values:

    R_R = 10

    R_P = 8

    R_Q = 5

    R_T = 5

    R_S = 3 # (Since R_R > R_S, we pick any value < 10)

    ratios = {'R': R_R, 'P': R_P, 'Q': R_Q, 'T': R_T, 'S': R_S}

    # Statement 5: Is R the highest?

    highest_city = max(ratios, key=ratios.get)

    return highest_city == 'R'

  

print("Is Statement 5 True?", verify_ratio_statements())  # Output: True

```

  

---

  

### Q7. Word Coding System

  

**Topic:** `logical-reasoning`, `coding-decoding`, `puzzles`  

**Source File:** [IMG-20240803-WA0069.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0069.jpg)

  

#### Question

If the code for 'raise your hands' is '1 2 3', the code for 'tap your feet' is '3 4 5' and the code for 'feet down' is '5 6', then what does the code '4' mean?

  

#### Solution/Answer

**Answer:** **tap**

  

**Analytical Explanation:**

1. Let's list the phrases and their respective code sets:

   - Phrase A: `"raise your hands"` $\rightarrow$ `{"1", "2", "3"}`

   - Phrase B: `"tap your feet"` $\rightarrow$ `{"3", "4", "5"}`

   - Phrase C: `"feet down"` $\rightarrow$ `{"5", "6"}`

2. Find the code for `"your"`:

   - The word `"your"` is the only common word between Phrase A and Phrase B.

   - The only common code between their code sets is `"3"`.

   - Therefore, `"your"` $\rightarrow$ `"3"`.

3. Find the code for `"feet"`:

   - The word `"feet"` is the only common word between Phrase B and Phrase C.

   - The only common code between their code sets is `"5"`.

   - Therefore, `"feet"` $\rightarrow$ `"5"`.

4. Decode `"tap"`:

   - In Phrase B (`"tap your feet"`), the codes are `{"3", "4", "5"}`.

   - Since `"your"` is `"3"` and `"feet"` is `"5"`, the remaining word `"tap"` must correspond to the remaining code `"4"`.

   - Therefore, `"4"` represents **"tap"**.

  

**Python Verification Code:**

```python

def decode_code_four():

    phrase_1 = "raise your hands".split()

    codes_1 = "1 2 3".split()

    phrase_2 = "tap your feet".split()

    codes_2 = "3 4 5".split()

    phrase_3 = "feet down".split()

    codes_3 = "5 6".split()

    # Map words to their unique codes by finding intersections

    # "your" is in 1 and 2

    common_words_1_2 = set(phrase_1) & set(phrase_2)  # {'your'}

    common_codes_1_2 = set(codes_1) & set(codes_2)    # {'3'}

    # "feet" is in 2 and 3

    common_words_2_3 = set(phrase_2) & set(phrase_3)  # {'feet'}

    common_codes_2_3 = set(codes_2) & set(codes_3)    # {'5'}

    # In phrase 2, "tap" corresponds to the code that is not 3 or 5

    known_codes = common_codes_1_2 | common_codes_2_3  # {'3', '5'}

    remaining_codes = set(codes_2) - known_codes      # {'4'}

    known_words = common_words_1_2 | common_words_2_3  # {'your', 'feet'}

    remaining_words = set(phrase_2) - known_words      # {'tap'}

    # Map the remaining code to the remaining word

    mapping = {code: word for code, word in zip(remaining_codes, remaining_words)}

    return mapping.get('4')

  

print("Code '4' means:", decode_code_four())  # Output: tap

```

  

---

  

### Q10. Shape Selection Logic Puzzle

  

**Topic:** `logical-reasoning`, `puzzles`  

**Source File:** [IMG-20240803-WA0072.jpg](file:///R:/DSA/Company wise prep resource/Apect Ratio/IMG-20240803-WA0072.jpg)

  

#### Question

Ross, Chandler and Joey each pick two of the following six shapes: rectangle, square, circle, hexagon, rhombus and star. Chandler does not pick the rectangle and square. Joey does not pick the square, rhombus or hexagon. Whoever picks the star, does not pick the circle.

If one of the three picks the hexagon and rhombus, then what does Joey who picks the star choose as his second shape?

  

#### Solution/Answer

**Answer:** **rectangle**

  

**Analytical Explanation:**

1. There are 6 distinct shapes distributed among 3 people, with each person choosing exactly 2 shapes (no shapes are shared).

2. Joey picks the **star**.

3. Constraint: "Whoever picks the star, does not pick the circle." Since Joey has the star, Joey cannot pick the circle.

4. Joey's disallowed shapes are: square, rhombus, hexagon, and circle.

5. This leaves only two possible shapes Joey can pick: **star** and **rectangle**.

6. Since Joey must pick two shapes, his choice is completely determined: **star** and **rectangle**.

7. Therefore, Joey's second shape is the **rectangle**.

  

*Let's verify the full assignment for consistency:*

- Joey: `{star, rectangle}`

- Remaining shapes: `{square, circle, hexagon, rhombus}`

- "One of the three picks the hexagon and rhombus." This must be Chandler or Ross.

- If Chandler picks `{hexagon, rhombus}`, then Ross must pick `{square, circle}`.

  - Chandler's disallowed: rectangle, square (Satisfied: Chandler has hexagon, rhombus).

  - Joey's disallowed: square, rhombus, hexagon (Satisfied: Joey has star, rectangle).

  - Star picker does not pick circle (Satisfied: Joey does not have circle).

  This is a fully valid, consistent solution.

- If Ross picks `{hexagon, rhombus}`, then Chandler must pick `{square, circle}`.

  - Chandler picks square, violating Chandler's constraint "Chandler does not pick the rectangle and square".

  - Thus, this configuration is invalid.

- So the unique assignment is: Joey = `{star, rectangle}`, Chandler = `{hexagon, rhombus}`, Ross = `{square, circle}`.

  

**Python Verification Code:**

```python

def solve_shapes_puzzle():

    import itertools

    shapes = ["rectangle", "square", "circle", "hexagon", "rhombus", "star"]

    people = ["Ross", "Chandler", "Joey"]

    # Generate all partitions of 6 shapes into 3 sets of 2

    for p in itertools.permutations(shapes):

        ross = {p[0], p[1]}

        chandler = {p[2], p[3]}

        joey = {p[4], p[5]}

        # 1. Chandler does not pick rectangle and square

        if "rectangle" in chandler or "square" in chandler:

            continue

        # 2. Joey does not pick square, rhombus, or hexagon

        if "square" in joey or "rhombus" in joey or "hexagon" in joey:

            continue

        # 3. Whoever picks the star, does not pick the circle

        valid_star = True

        for choices in (ross, chandler, joey):

            if "star" in choices and "circle" in choices:

                valid_star = False

        if not valid_star:

            continue

        # 4. Joey picks the star

        if "star" not in joey:

            continue

        # 5. One of the three picks hexagon and rhombus

        has_hex_rhombus = False

        for choices in (ross, chandler, joey):

            if "hexagon" in choices and "rhombus" in choices:

                has_hex_rhombus = True

        if not has_hex_rhombus:

            continue

        # Output Joey's second shape

        second_shape = list(joey - {"star"})[0]

        return {

            "Ross": list(ross),

            "Chandler": list(chandler),

            "Joey": list(joey),

            "Joey's Second Shape": second_shape

        }

  

solution = solve_shapes_puzzle()

print("Full Assignment:", solution)

# Output:

# Full Assignment: {

#   'Ross': ['circle', 'square'],

#   'Chandler': ['rhombus', 'hexagon'],

#   'Joey': ['rectangle', 'star'],

#   'Joey\'s Second Shape': 'rectangle'

# }

```