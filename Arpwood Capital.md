# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/Arpwood Capital*
*Total questions: 41*

---

## Table of Contents

1. [Quantitative & Logic Questions](#quantitative-logic-questions)
2. [Finance & Accounting Questions](#finance-accounting-questions)
3. [Economics Questions](#economics-questions)

---

## Quantitative & Logic Questions

### Q1. Expected Number of "HH" in 8 Coin Tosses

**Topic:** `Probability`, `Expected Value`

A coin is tossed 8 times and the output written as a string. What is the expected number of HH? Note that in HHH, the number of HH = 2.

#### Solution
Let $X$ be the number of "HH" substrings in a coin toss sequence of length 8. We can write $X$ as a sum of indicator random variables:
$$X = I_1 + I_2 + I_3 + I_4 + I_5 + I_6 + I_7$$
where $I_i = 1$ if the $i$-th and $(i+1)$-th tosses are both Heads, and $0$ otherwise.

By linearity of expectation:
$$E[X] = E[I_1] + E[I_2] + \dots + E[I_7]$$

Since the coin tosses are independent and fair:
$$P(\text{toss } i = H \text{ and } \text{toss } i+1 = H) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$$

So $E[I_i] = \frac{1}{4}$ for each $i$.
$$E[X] = 7 \times \frac{1}{4} = \frac{7}{4}$$

**Correct Answer:** `7/4`

---

### Q2. Die Roll Sum Probability

**Topic:** `Conditional Probability`

Suppose a fair six-sided die is rolled once. If the value on the die is 1, 2, or 3, the die is rolled a second time. What is the probability that the sum total of values that turn up is at least 6?

#### Solution
Let $X_1$ be the value of the first roll.
- If $X_1 \in \{4, 5, 6\}$, we do not roll a second time. The sum is $X_1$.
  - Only $X_1 = 6$ satisfies $\text{Sum} \ge 6$. Probability = $\frac{1}{6}$.
- If $X_1 \in \{1, 2, 3\}$, we roll a second time. Let $X_2$ be the value of the second roll. The sum is $X_1 + X_2$.
  - Case $X_1 = 1$: we need $X_2 \ge 5 \implies X_2 \in \{5, 6\}$ (prob = $2/6$).
    Combined probability = $\frac{1}{6} \times \frac{2}{6} = \frac{2}{36}$.
  - Case $X_1 = 2$: we need $X_2 \ge 4 \implies X_2 \in \{4, 5, 6\}$ (prob = $3/6$).
    Combined probability = $\frac{1}{6} \times \frac{3}{6} = \frac{3}{36}$.
  - Case $X_1 = 3$: we need $X_2 \ge 3 \implies X_2 \in \{3, 4, 5, 6\}$ (prob = $4/6$).
    Combined probability = $\frac{1}{6} \times \frac{4}{6} = \frac{4}{36}$.

Sum of all probabilities:
$$P(\text{Sum} \ge 6) = \frac{1}{6} + \frac{2}{36} + \frac{3}{36} + \frac{4}{36} = \frac{6}{36} + \frac{9}{36} = \frac{15}{36} = \frac{5}{12}$$

**Correct Answer:** `5/12`

---

### Q3. Expected Edges to Traverse a Cube

**Topic:** `Markov Chains`, `Random Walk`

An ant is standing on one corner of a cube & can only walk on the edges. The ant is drunk and from any corner, it moves randomly by choosing any edge! What is the expected number of edges the ant travels to reach the opposite corner?

#### Solution
Let the corners of the cube be classified by their shortest distance (number of edges) from the target (opposite) corner:
- State 3: The starting corner (opposite to target). Distance 3.
- State 2: Corners at distance 2.
- State 1: Corners at distance 1.
- State 0: The target corner (absorbing state).

Transitions:
- From State 3: 3 neighbors, all at distance 2.
  $$E_3 = 1 + E_2$$
- From State 2: 3 neighbors. 1 neighbor is at distance 3, 2 are at distance 1.
  $$E_2 = 1 + \frac{1}{3} E_3 + \frac{2}{3} E_1$$
- From State 1: 3 neighbors. 1 is the target (distance 0), 2 are at distance 2.
  $$E_1 = 1 + \frac{2}{3} E_2$$

Solving the system:
1. $E_2 = E_3 - 1$
2. $E_1 = 1 + \frac{2}{3} (E_3 - 1) = \frac{1}{3} + \frac{2}{3} E_3$
3. $E_3 - 1 = 1 + \frac{1}{3} E_3 + \frac{2}{3} (\frac{1}{3} + \frac{2}{3} E_3) = 1 + \frac{1}{3} E_3 + \frac{2}{2} + \frac{4}{9} E_3$
   $$E_3 - 1 = \frac{11}{9} + \frac{7}{9} E_3 \implies \frac{2}{9} E_3 = \frac{20}{9} \implies E_3 = 10$$

**Correct Answer:** `10`

---

### Q4. Continuous Ratio Probability

**Topic:** `Continuous Probability`

$p$ and $q$ are two points chosen at random between 0 & 1. What is the probability that the ratio $p/q$ lies between 1 & 2?

#### Solution
We need $P(1 < p/q < 2) = P(q < p < 2q)$.
This region in the unit square $[0, 1] \times [0, 1]$ is a triangle with vertices $(0,0)$, $(0.5, 1)$, and $(1, 1)$.
- The base of this triangle along the line $p = 1$ is from $q = 0.5$ to $q = 1$ (length = $0.5$).
- The height of this triangle is $1$.
$$\text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 0.5 \times 1 = 0.25 = \frac{1}{4}$$

**Correct Answer:** `1/4`

---

### Q5. Work and Time Systems

**Topic:** `Linear Equations`, `Rates`

A and B do a work in exactly 18 days, B and C do the same work in exactly 10 days while C and A do the same work in about 8 days. If A, B and C can together do the work in integral number of days, then C does the work alone in (round off to next highest integer):

#### Solution
Let the rates of A, B, and C be $a, b, c$ respectively.
- $a + b = 1/18 \approx 0.0556$
- $b + c = 1/10 = 0.1000$
- $c + a \approx 1/8 = 0.1250$

Summing these up:
$$2(a + b + c) \approx 0.2806 \implies a + b + c \approx 0.1403$$
The number of days for A, B, and C together is $\frac{1}{a + b + c} \approx 7.13$ days.
Since the problem states they do it in an integral number of days, we set $a + b + c = 1/7$.
$$c = (a + b + c) - (a + b) = \frac{1}{7} - \frac{1}{18} = \frac{11}{126}$$
Number of days C takes alone:
$$\frac{126}{11} \approx 11.45 \text{ days}$$
Rounding up to the next highest integer gives 12.

**Correct Answer:** `12`

---

### Q6. Surds and Conjugate Products

**Topic:** `Algebra`, `Roots`

If the product of $a + \sqrt{b}$ and its conjugate is 33 and the product $ab$ is 18, which of the following can be the value of $a$? ($b$ is not a perfect square)

#### Solution
The conjugate of $a + \sqrt{b}$ is $a - \sqrt{b}$.
$$(a + \sqrt{b})(a - \sqrt{b}) = a^2 - b = 33$$
Since $ab = 18 \implies b = \frac{18}{a}$.
$$a^2 - \frac{18}{a} = 33 \implies a^3 - 33a - 18 = 0$$
For $a = 6$:
$$6^3 - 33(6) - 18 = 216 - 198 - 18 = 0$$
This is a solution, giving $b = 3$ (which is not a perfect square).

**Correct Answer:** `6` (Note: the exam print has a checkmark on 3 which is mathematically incorrect).

---

### Q7. Inequality Combinations

**Topic:** `Algebraic Inequalities`

Given $-8 \le x \le -5$, $-4 \le y < 2$, $-1 \le z \le 5$, which of the following statements is/are always true?
- $9z + 5 > x + 2y$
- $6z > 5x + 9y$
- $2(x+y) < 5z$

#### Solution
- **Statement 1:** Minimum of $9z + 5 - x - 2y$ is $-9 + 5 - (-5) - 2(2) = -3 < 0$. So not always true.
- **Statement 2:** Minimum of $6z - 5x - 9y$ is $-6 - 5(-5) - 9(2) = -6 + 25 - 18 = 1 > 0$. Always true.
- **Statement 3:** Minimum of $5z - 2x - 2y$ is $-5 - 2(-5) - 2(2) = -5 + 10 - 4 = 1 > 0$. Always true.

**Correct Answer:** `More than one of the above` (Statements 2 and 3 are always true).

---

### Q8. Digit Sum Sequence

**Topic:** `Number Theory`

A function $y = f(n)$ is defined, for all natural numbers, as the sum of the digits of $n$. If $k$ is a natural number such that $f(f(f(f(k)))) = 1$ and $k > f(k) > f(f(k)) > f(f(f(k))) > 1$, what is the least number of digits that $k$ can have?

#### Solution
Let:
- $x_3 = f(f(f(k)))$. Smallest value $>1$ such that $f(x_3) = 1$ is $10$.
- $x_2 = f(f(k))$. Smallest value $>10$ such that $f(x_2) = 10$ is $19$.
- $x_1 = f(k)$. Smallest value $>19$ such that $f(x_1) = 19$ is $199$ (since $1+9+9 = 19$).
- We need $f(k) = 199$ with $k > 199$.
For a number $k$ to have digit sum 199, the minimum number of digits $d$ is:
$$d \ge \frac{199}{9} \approx 22.11 \implies d = 23 \text{ digits}$$

**Correct Answer:** `23`

---

### Q9. Coordinate Section Ratio

**Topic:** `Coordinate Geometry`

If $P(a^2, 2a)$ is a point on the line segment joining the points $A(2,0)$ and $B(0,4)$, what is the ratio of the distances AP and PB?

#### Solution
The equation of the line $AB$ is $2x + y = 4$.
Since $P(a^2, 2a)$ lies on this segment:
$$2(a^2) + 2a = 4 \implies a^2 + a - 2 = 0 \implies (a-1)(a+2) = 0$$
Since $P$ is on the *segment* between $A$ and $B$, $x \in [0, 2]$. Thus $a = 1 \implies P = (1, 2)$.
$$AP = \sqrt{(1-2)^2 + (2-0)^2} = \sqrt{5}$$
$$PB = \sqrt{(0-1)^2 + (4-2)^2} = \sqrt{5}$$
Ratio is $1:1$.

**Correct Answer:** `1:1`

---

### Q10. Chinese Remainder Theorem Application

**Topic:** `Number Theory`

What is the sum of the digits of the smallest number which when divided by 7 leaves a remainder of 6, when divided by 8 leaves a remainder of 7 and when divided by 9 leaves a remainder of 1?

#### Solution
Let the number be $x$.
- $x \equiv -1 \pmod 7$
- $x \equiv -1 \pmod 8$
- $x \equiv 1 \pmod 9$

From the first two, $x \equiv -1 \pmod{56} \implies x = 56k - 1$.
Using the third condition:
$$56k - 1 \equiv 1 \pmod 9 \implies 2k \equiv 2 \pmod 9 \implies k \equiv 1 \pmod 9$$
Smallest positive integer $k = 1 \implies x = 55$.
Sum of digits of 55 is $5 + 5 = 10$.

**Correct Answer:** `10`

---

### Q11. Linear System Word Problem

**Topic:** `Algebraic Systems`

The total cost of 2 pencils, 5 erasers and 7 sharpeners is Rs.30, while 3 pencils and 5 sharpeners cost Rs.15 more than 6 erasers. By what amount (in Rs.) does the cost of 39 erasers and 1 sharpener exceed the cost of 6 pencils?

#### Solution
Let $p, e, s$ be the costs of a pencil, eraser, and sharpener.
1. $2p + 5e + 7s = 30$
2. $3p - 6e + 5s = 15$

We want to find $E = 39e + s - 6p$.
Let $x(\text{Eq 1}) + y(\text{Eq 2}) = -6p + 39e + s$.
- $p$: $2x + 3y = -6$
- $e$: $5x - 6y = 39$
- $s$: $7x + 5y = 1$

Solving the first two gives $x = 3, y = -4$. Checking the third: $7(3) + 5(-4) = 1$. It works!
$$E = 3(30) - 4(15) = 90 - 60 = 30$$

**Correct Answer:** `30`

---

### Q12. Exponential Growth (Lotuses)

**Topic:** `Exponential Growth`

There are 25 lotuses in a pond each 1 square foot in area. The pond is 5300 sq ft. in area. Each lotus doubles its size everyday. How long until the pond is completely covered in lotus?

#### Solution
$$\text{Area} = 25 \times 2^t \ge 5300 \implies 2^t \ge 212$$
Since $2^7 = 128$ and $2^8 = 256$, it takes 8 days.

**Correct Answer:** `8 days`

---

### Q13. Algebra Solution Count

**Topic:** `Calculus`, `Graphing`

Find the number of solutions of the equation $6x^2 + 5x - 6 - e^x = 0$.

#### Solution
Let $f(x) = 6x^2 + 5x - 6 - e^x$.
- $f'(x) = 12x + 5 - e^x$, $f''(x) = 12 - e^x$.
- $f(x)$ is convex for $x < \ln 12 \approx 2.48$, and concave for $x > 2.48$.
- Testing key values shows 3 roots: one negative root (approx $-1.55$), one small positive root (approx $0.84$), and one large positive root (approx $3.46$).

**Correct Answer:** `3`

---

### Q14. Digit Counting in Ranges

**Topic:** `Combinatorics`

How many times would the digits 3 and 5 be printed if we listed all the numbers from 1000 to 10,000?

#### Solution
Since 3 and 5 are symmetric, count occurrences of 3 and multiply by 2.
For 4-digit numbers $[1000, 9999]$:
- Thousands place has 3: $1 \times 10^3 = 1000$ times.
- Hundreds place has 3: $9 \times 1 \times 10^2 = 900$ times.
- Tens place has 3: $9 \times 10 \times 1 \times 10 = 900$ times.
- Units place has 3: $9 \times 10 \times 10 \times 1 = 900$ times.
Total for digit 3 = 3700. For 3 and 5 combined: $3700 \times 2 = 7400$.

**Correct Answer:** `7,400`

---

### Q15. Faulty Clock Coincidence

**Topic:** `Rates`, `Clocks`

A faulty clock gains 15 minutes every hour. The time is set correctly between 3 PM and 4 PM, when the hour and minute hands of the clock coincide. How many times will the minute-hand and hour-hand meet in the next 30 hours?

#### Solution
In 30 hours of real time, the faulty clock elapses $30 \times 1.25 = 37.5$ hours.
On any clock, the hands coincide every $\frac{12}{11}$ hours of clock time.
$$\text{Number of meetings} = \lfloor \frac{37.5}{12/11} \rfloor = \lfloor 34.375 \rfloor = 34$$

**Correct Answer:** `34`

---

### Q16. Geometric Series (Magic Pot)

**Topic:** `Geometric Progressions`

A saint has a magic pot. He puts one gold ball of radius 1 mm daily inside it everyday for 10 days. If the weight of the first ball is 1 g and if the radius of a ball inside the pot doubles every day, how much gold has the saint made due to his magic pot? (in grams)

#### Solution
- Weight is proportional to volume, i.e., $r^3$.
- Doubling the radius increases the weight by $2^3 = 8$.
- Total final weight $S = 8^9 + 8^8 + \dots + 1 = \frac{8^{10} - 1}{7} = \frac{2^{30} - 1}{7}$.
- Net gold made (subtracting the 10 g put in): $S - 10 = \frac{2^{30} - 1 - 70}{7} = \frac{2^{30} - 71}{7}$.

**Correct Answer:** `((2^30) - 71)/7`

---

### Q17. Integer Triangles

**Topic:** `Geometry`

If one of the sides of a right-angled triangle with integer sides is 15cm, find the maximum possible area of the triangle (in sq. cm).

#### Solution
Let legs be $15, b$ and hypotenuse $c$.
$$c^2 - b^2 = 225 \implies (c-b)(c+b) = 225$$
To maximize area $\frac{15b}{2}$, we set $c-b = 1$ and $c+b = 225 \implies b = 112$.
$$\text{Max Area} = \frac{15 \times 112}{2} = 840 \text{ sq. cm.}$$

**Correct Answer:** `840`

---

### Q18. Venn Diagrams

**Topic:** `Set Theory`

A survey shows that 63% of the Indians like coffee, whereas 76% like tea. If $x\%$ of the Indians like both coffee and tea, then find the range of $x$.

#### Solution
$$C \cup T = 63 + 76 - x = 139 - x$$
Since $C \cup T \le 100\% \implies x \ge 39\%$. Also $x \le \min(63, 76) = 63\%$.
$$39 \le x \le 63$$

**Correct Answer:** `39 <= x <= 63`

---

### Q19. Number Theory Factors

**Topic:** `Factors`

Numbers A, B, C and D have 22, 37, 53 and 66 factors. Which of these could be a perfect cube?

#### Solution
For $N$ to be a perfect cube, all exponents in its prime factorization must be multiples of 3, meaning the number of factors must be of the form $\prod (3k_i + 1)$.
- A (22 factors): $22 \equiv 1 \pmod 3$. Can be $p^{21} = (p^7)^3$.
- B (37 factors): $37 \equiv 1 \pmod 3$. Can be $p^{36} = (p^{12})^3$.
- C (53 factors): $53 \equiv 2 \pmod 3$. Cannot.
- D (66 factors): $66 \equiv 0 \pmod 3$. Cannot.

**Correct Answer:** `A & B`

---

### Q20. Factorial Remainder

**Topic:** `Modular Arithmetic`

If $p = 1\cdot 1! + 2\cdot 2! + \dots + 10\cdot 10!$, then $p + 12$ when divided by 110 leaves a remainder of:

#### Solution
$$p = 11! - 1 \implies p + 12 = 11! + 11$$
- Modulo 11: $11! + 11 \equiv 0 \pmod{11}$.
- Modulo 10: $11! + 11 \equiv 0 + 1 \equiv 1 \pmod{10}$.
Using CRT, the remainder modulo 110 is 11.

**Correct Answer:** `11` (Note: the options are likely flawed as 11 is not listed).

---

## Finance & Accounting Questions

### Q21. Corporate Action Impact

**Topic:** `Corporate Finance`

Which Corporate action is least likely to cause a change in the market cap of a listed company?

**Correct Answer:** `Stock-split` (since it only changes share count and price proportionally).

---

### Q22. Prepaid Accounting

**Topic:** `Financial Accounting`

Anja has a December financial year-end. Her contract with her tax consultant is from April 1 to March 31. For the financial year ending March 31, 2023, the tax consultant has charged her 48,000. How much of this amount is shown as a prepaid item in the balance sheet as at December 31, 2022?

#### Solution
Remaining months = Jan, Feb, March (3 months).
$$\text{Prepaid Amount} = 48,000 \times \frac{3}{12} = 12,000$$

**Correct Answer:** `12,000`

---

### Q23. Balance Sheet Adjustments

**Topic:** `Double-entry Bookkeeping`

Inventory which originally cost 80.0 is sold for 120.0 in cash. Which answer best describes how this transaction would be reflected in the company's balance sheet?

**Correct Answer:** `Inventory decreases 80.0, cash increases 120.0, retained earnings increases 40.0`

---

### Q24. Merger Share Swap

**Topic:** `M&A Valuation`

Post the HDFC and HDFC Bank merger announcement, the shareholders of HDFC are offered a swap ratio of 25:40. As of date of merger, HDFC Bank trades at 1,000 and HDFC trades at 2,700 and your portfolio has 60 shares of HDFC Bank and 95 shares of HDFC. What would be the composition of your portfolio after the merger completion?

#### Solution
- Swap ratio = $25/40 = 0.625$.
- HDFC Bank shares received = $95 \times 0.625 = 59.375$.
- Fractional share (0.375) paid in cash: $0.375 \times 1,000 = 375$.
- Total HDFC Bank shares = $60 + 59 = 119$.

**Correct Answer:** `HDFC Bank shares - 119 & Cash - 375`

---

### Q25. Capital Budgeting

**Topic:** `IRR vs NPV`

Marico's management has to choose one project out of the four projects with IRR and NPV values. Which Project should Marico's management take up?

**Correct Answer:** `Project C` (having the highest NPV of $2,400 Mn, as the NPV rule is theoretically superior).

---

### Q26. Straight-Line Depreciation

**Topic:** `Accounting`

Calculate the net book value at the end of year 3 using the straight-line depreciation method. Cost of machine = 1,20,000, Estimated life = 5 years, Salvage value = 24,000.

#### Solution
- Annual Depreciation = $\frac{1,20,000 - 24,000}{5} = 19,200$.
- Accumulated Depreciation (3 years) = $57,600$.
- Net Book Value = $1,20,000 - 57,600 = 62,400$.

**Correct Answer:** `62,400`

---

### Q27. Profit Margins

**Topic:** `Corporate Finance`

Compute Gross and operating profit margin for: Revenue $4,000 Mn, Cost of Goods Sold $2,400 Mn, Operating Expenses $600 Mn.

#### Solution
- Gross Profit Margin = $\frac{4,000 - 2,400}{4,000} = 40\%$.
- Operating Profit Margin (EBIT) = $\frac{4,000 - 2,400 - 600}{4,000} = 25\%$.

**Correct Answer:** `40% and 25%`

---

### Q28. CAPM and Stock Valuation

**Topic:** `Asset Pricing`

Risk-free rate is 7%, expected market return is 12%. A stock with beta 1.1 sells for $35, pays $2 dividend next year, and is expected to price at $41. The stock is:

#### Solution
- Required Return = $7\% + 1.1(12\% - 7\%) = 12.5\%$.
- Expected Return = $\frac{2 + 41 - 35}{35} = 22.86\%$.
- Since Expected Return > Required Return, the stock is underpriced.

**Correct Answer:** `underpriced, so buy it`

---

### Q29. CapEx Calculation

**Topic:** `Corporate Finance`

Beginning fixed assets: 300,000. Ending: 370,000. Depreciation: 43,000. CapEx = ?

#### Solution
$$\text{Ending} = \text{Beginning} + \text{CapEx} - \text{Depreciation} \implies 370,000 = 300,000 + \text{CapEx} - 43,000 \implies \text{CapEx} = 113,000$$

**Correct Answer:** `113,000`

---

### Q30. Double-Entry Contribution

**Topic:** `Accounting Principles`

The owner of Affluent Co. contributes his personal truck to the business. Which effect is correct?

**Correct Answer:** `Increase in Asset, increase in Owner's Equity & no change in liabilities`

---

## Economics Questions

### Q31. Short-run Shutdown Point

**Topic:** `Microeconomics`

A company will shut down production in the short run if the total revenue is less than total variable costs.

**Correct Answer:** `variable costs`

---

### Q32. GDP Definition

**Topic:** `Macroeconomics`

Which of the following is the most appropriate description of GDP?

**Correct Answer:** `The total amount spent on all final goods and services produced within the economy over a given time period`

---

### Q33. Monopoly Regulation

**Topic:** `Industrial Organization`

A government entity regulating an authorized monopoly will most likely base regulated prices on:

**Correct Answer:** `long run average cost`

---

### Q34. Exchange Rate Appreciation

**Topic:** `Macroeconomics`

If CHF depreciated 12% against GBP, how much has GBP appreciated against CHF?

#### Solution
$$\text{New GBP value} = \frac{1}{1 - 0.12} - 1 = 13.64\% > 12\%$$

**Correct Answer:** `more than 12%`

---

### Q35. GDP Inclusions

**Topic:** `Macroeconomics`

Which of the following would be included in Canadian GDP for a given year?

**Correct Answer:** `wine grown in Canada by US citizen`

---

### Q36. Price Elasticity of Demand

**Topic:** `Microeconomics`

Price elasticity of demand for a good will most likely be greater if:

**Correct Answer:** `consumers consider the good as discretionary`

---

### Q37. Monetary Policy Components

**Topic:** `Macroeconomics`

Monetary policy is least likely to include:

**Correct Answer:** `enacting a transfer payment program` (this is fiscal policy).
