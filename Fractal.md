# Interview Questions

*Total questions: 55*

---

## Table of Contents

1. [Quantitative Aptitude](#quantitative-aptitude)
2. [Data Sufficiency](#data-sufficiency)
3. [Data Interpretation](#data-interpretation)
4. [Verbal Ability and Reading Comprehension](#verbal-ability-and-reading-comprehension)
5. [Logical and Critical Reasoning](#logical-and-critical-reasoning)
6. [SSC CGL Reference Paper - Quantitative Aptitude](#ssc-cgl-reference-paper-quantitative-aptitude)

---

## Quantitative Aptitude

### Q1. Prime Factor Count

**Topic:** `number-theory`, `factors`

What is the number of prime factors of $52,500$ that are between $1$ and $175$?

#### Solution
1. Find the prime factorization of $52,500$:
   $$52,500 = 525 \times 100 = (3 \times 175) \times (4 \times 25) = (3 \times 5^2 \times 7) \times (2^2 \times 5^2) = 2^2 \times 3^1 \times 5^4 \times 7^1$$
2. The distinct prime factors are $2, 3, 5, \text{ and } 7$.
3. All four prime factors ($2, 3, 5, 7$) fall between $1$ and $175$.
4. Thus, the count is **4**.

---

### Q2. Book Depot Day Crew Fraction

**Topic:** `work-and-rates`, `fractions`

A book depot has a day crew and a night crew. The night crew is $\frac{2}{3}$ the size of the day crew. The sorting rate of a day worker is $7$ books for every $3$ books sorted by a night worker (i.e., a night worker's rate is $\frac{3}{7}$ of a day worker's rate). What fraction of the total books sorted daily is sorted by the day crew?

#### Solution
1. Let the day crew size be $D$. Then the night crew size is $N = \frac{2}{3}D$.
2. Let a day worker's rate be $r$. Then a night worker's rate is $r_n = \frac{3}{7}r$.
3. Total books sorted by the day crew:
   $$\text{Work}_d = D \times r$$
4. Total books sorted by the night crew:
   $$\text{Work}_n = N \times r_n = \left(\frac{2}{3}D\right) \times \left(\frac{3}{7}r\right) = \frac{2}{7}Dr$$
5. Total books sorted by both crews:
   $$\text{Work}_{\text{total}} = Dr + \frac{2}{7}Dr = \frac{9}{7}Dr$$
6. Fraction sorted by the day crew:
   $$\text{Fraction}_d = \frac{Dr}{\frac{9}{7}Dr} = \frac{7}{9}$$

---

### Q3. Rectangular Garden Length

**Topic:** `mensuration`, `equations`

A rectangular garden's length is $5$ times its width. If the perimeter is $2160$ meters, what is the length of the garden?

#### Solution
1. Let the width be $W$. The length is $L = 5W$.
2. The perimeter $P$ is given by:
   $$P = 2(L + W) = 2(5W + W) = 12W = 2160$$
3. Solve for $W$:
   $$W = \frac{2160}{12} = 180 \text{ meters}$$
4. Calculate $L$:
   $$L = 5 \times 180 = 900 \text{ meters}$$

---

### Q4. 21st Decimal Digit of 7/11

**Topic:** `decimals`, `patterns`

What is the 21st decimal digit of $\frac{7}{11}$?

#### Solution
1. Convert $\frac{7}{11}$ to its decimal representation:
   $$\frac{7}{11} = 0.636363\dots = 0.\overline{63}$$
2. The decimal pattern repeating block has a length of 2 digits: `6` (at odd decimal positions) and `3` (at even decimal positions).
3. Since $21$ is an odd number, the 21st decimal digit is **6**.

---

### Q5. Final Grades Math Course

**Topic:** `fractions`, `equations`

Of the final grades received by the students in a certain math course, $\frac{1}{5}$ are A's, $\frac{1}{4}$ are B's, $\frac{1}{2}$ are C's, and the remaining $145$ grades are D's. What is the total number of students in the course?

#### Solution
1. Let $N$ be the total number of students.
2. Sum the fractions of students receiving A's, B's, and C's:
   $$\text{Fraction}_{A,B,C} = \frac{1}{5} + \frac{1}{4} + \frac{1}{2} = \frac{4 + 5 + 10}{20} = \frac{19}{20}$$
3. The remaining fraction of students receiving D's is:
   $$\text{Fraction}_D = 1 - \frac{19}{20} = \frac{1}{20}$$
4. Set up the equation and solve for $N$:
   $$\frac{1}{20} N = 145 \implies N = 145 \times 20 = 2900 \text{ students}$$

---

### Q6. Nancy's Savings AP

**Topic:** `arithmetic-progression`

In the first week of the year, Nancy saved $\$27$. In each of the next $51$ weeks, she saved $\$27$ more than she had saved in the previous week. What was the total amount that Nancy saved during the $52$ weeks?

#### Solution
1. This forms an Arithmetic Progression (AP) where:
   - First term $a = 27$
   - Common difference $d = 27$
   - Number of terms $n = 52$
2. The sum of the first $n$ terms $S_n$ is:
   $$S_n = \frac{n}{2} [2a + (n-1)d] = \frac{52}{2} [2(27) + 51(27)] = 26 \times 27 \times (2 + 51) = 26 \times 27 \times 53$$
3. Calculate the product:
   $$26 \times 27 = 702$$
   $$702 \times 53 = 37,206$$
4. Nancy saved a total of **$\$37,206$**.

---

### Q7. Machines Producing Bottles

**Topic:** `ratios`, `work-and-rates`

Running at the same constant rate, $3$ identical machines can produce a total of $90$ bottles per minute. At this rate, how many bottles could $9$ such machines produce in $5$ minutes?

#### Solution
1. Find the rate of 1 machine:
   $$\text{Rate}_1 = \frac{90 \text{ bottles/min}}{3} = 30 \text{ bottles/min per machine}$$
2. Find the rate of 9 machines:
   $$\text{Rate}_9 = 9 \times 30 = 270 \text{ bottles/min}$$
3. Total production in 5 minutes:
   $$\text{Production} = 270 \text{ bottles/min} \times 5 \text{ minutes} = 1350 \text{ bottles}$$

---

### Q8. Soap to Alcohol to Water Ratio

**Topic:** `ratios`, `mixture`

The ratio, by volume, of soap to alcohol to water in a certain solution is $2:70:140$. The solution will be altered so that the ratio of soap to alcohol is magnified two times while the ratio of soap to water is made half. If the altered solution contains $210\text{ cm}^3$ of alcohol, how many cubic centimeters of water will it contain?

#### Solution
1. Let the original volumes be $S, A, W$. The initial ratio is:
   $$S : A : W = 2 : 70 : 140 \implies \frac{S}{A} = \frac{2}{70} = \frac{1}{35}, \quad \frac{S}{W} = \frac{2}{140} = \frac{1}{70}$$
2. For the altered solution with volumes $S', A', W'$:
   - The soap to alcohol ratio is doubled:
     $$\frac{S'}{A'} = 2 \times \frac{S}{A} = 2 \times \frac{1}{35} = \frac{2}{35}$$
   - The soap to water ratio is halved:
     $$\frac{S'}{W'} = \frac{1}{2} \times \frac{S}{W} = \frac{1}{2} \times \frac{1}{70} = \frac{1}{70 \times 2} = \frac{1}{140}$$
3. We are given $A' = 210\text{ cm}^3$. Solve for $S'$:
   $$\frac{S'}{210} = \frac{2}{35} \implies S' = 210 \times \frac{2}{35} = 6 \times 2 = 12\text{ cm}^3$$
4. Solve for $W'$ using $S' = 12$:
   $$\frac{12}{W'} = \frac{1}{140} \implies W' = 12 \times 140 = 1680\text{ cm}^3$$
5. The altered solution contains **$1680\text{ cm}^3$** of water.

---

### Q9. Two Pumps Filling Pool

**Topic:** `work-and-rates`, `equations`

Two pumps, each working alone, can fill an empty pool in $28$ hours and $42$ hours, respectively. The first pump initially started alone for $h$ hours, after which the second pump was also started. If it took a total of $25$ hours for the pool to be filled completely, what is the value of $h$?

#### Solution
1. Let the rates of the two pumps be $\frac{1}{28}$ and $\frac{1}{42}$ pools per hour.
2. The first pump runs for the entire duration of $25$ hours.
3. The second pump runs for $25 - h$ hours.
4. Total work completed is $1$ pool:
   $$\frac{25}{28} + \frac{25 - h}{42} = 1$$
5. Multiply the entire equation by the LCM of $28$ and $42$, which is $84$:
   $$3(25) + 2(25 - h) = 84$$
   $$75 + 50 - 2h = 84$$
   $$125 - 2h = 84 \implies 2h = 41 \implies h = 20.5\text{ hours}$$

---

### Q10. Salespeople Remuneration

**Topic:** `percentage`, `overtime-calculation`

A clothing retailer employs $250$ salespeople. Each of them is paid $\$9$ per hour for the first $38$ hours worked during a week and $1\frac{1}{4}$ times that rate for hours worked in excess of $38$ hours. What was the total remuneration of the salespeople for a week in which $20\%$ of them worked $30$ hours, $50\%$ worked $38$ hours, and the rest worked $45$ hours?

#### Solution
1. Find the number of salespeople in each category:
   - Group 1 ($20\%$ of $250 = 50$ people): worked $30$ hours each.
   - Group 2 ($50\%$ of $250 = 125$ people): worked $38$ hours each.
   - Group 3 (Remaining $30\%$ of $250 = 75$ people): worked $45$ hours each.
2. Compute remuneration for each group:
   - **Group 1**: $50 \text{ people} \times 30 \text{ hours} \times \$9/\text{hour} = \$13,500$
   - **Group 2**: $125 \text{ people} \times 38 \text{ hours} \times \$9/\text{hour} = \$42,750$
   - **Group 3**: Each person works $38$ regular hours and $7$ overtime hours ($45 - 38 = 7$).
     - Regular rate = $\$9/\text{hour}$
     - Overtime rate = $1.25 \times 9 = \$11.25/\text{hour}$
     - Pay per person = $(38 \times 9) + (7 \times 11.25) = 342 + 78.75 = \$420.75$
     - Group 3 total = $75 \text{ people} \times \$420.75 = \$31,556.25$
3. Sum the total remuneration:
   $$\text{Total} = 13,500 + 42,750 + 31,556.25 = \$87,806.25 \approx \$87,806$$

---

## Data Sufficiency

### Q11. College Graduates

**Topic:** `data-sufficiency`, `percentages`

In a random sample of $120$ adults, how many are college graduates?

**Statements:**
1. In the sample, the number of adults who are not college graduates is $3$ times the number who are college graduates.
2. In the sample, the number of adults who are not college graduates is $90$ more than the number who are college graduates.

#### Solution
Let $C$ be the number of college graduates and $N$ be the number of non-graduates. We are given $C + N = 120$. We need to find $C$.
- **Statement (1):** $N = 3C$
  $$C + 3C = 120 \implies 4C = 120 \implies C = 30$$
  This statement alone is **sufficient**.
- **Statement (2):** $N = C + 90$
  $$C + (C + 90) = 120 \implies 2C = 30 \implies C = 15$$
  This statement alone is **sufficient**.
- **Answer:** **EACH statement ALONE is sufficient.**

---

### Q12. Median Value n

**Topic:** `data-sufficiency`, `statistics`

What is the value of $n$ in the list $n, 10, 8, 6, 12$?

**Statements:**
1. $n > 12$
2. The median of the numbers in the list is $9$.

#### Solution
The list consists of five numbers. The four known numbers are $6, 8, 10, 12$.
- **Statement (1):** $n > 12$
  The sorted list is $6, 8, 10, 12, n$. The median is the middle term, which is $10$. However, the exact value of $n$ cannot be determined (it can be $13, 14, 15$, etc.). Thus, Statement (1) alone is **not sufficient**.
- **Statement (2):** The median is $9$.
  Since $9$ is the median of a 5-element list, two numbers must be less than $9$ ($6$ and $8$) and two must be greater than $9$ ($10$ and $12$). Thus, the middle term $n$ must be exactly $9$. This statement alone is **sufficient**.
- **Answer:** **Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.**

---

### Q13. Positive j and k

**Topic:** `data-sufficiency`, `inequalities`

If $j$ and $k$ are positive, is $\frac{j}{k}$ greater than $1$?

**Statements:**
1. $j < k$
2. $jk > 1$

#### Solution
Since $k$ is positive, $\frac{j}{k} > 1$ is equivalent to asking: is $j > k$?
- **Statement (1):** $j < k$
  This directly tells us that $j$ is not greater than $k$ (i.e., $\frac{j}{k} \le 1$). We get a definitive "NO", which makes this statement **sufficient**.
- **Statement (2):** $jk > 1$
  We cannot determine the relative sizes of $j$ and $k$:
  - If $j = 2, k = 1$: $jk = 2 > 1$ and $j > k$ (YES).
  - If $j = 1, k = 2$: $jk = 2 > 1$ and $j < k$ (NO).
  Thus, Statement (2) alone is **not sufficient**.
- **Answer:** **Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.**

---

### Q14. Pat's Savings & Earnings

**Topic:** `data-sufficiency`, `percentages`

If Pat saved $\$1190$ of his earnings last month, how much did Pat earn last month?

**Statements:**
1. Pat spent $\frac{1}{4}$ of his earnings last month for living expenses and saved $\frac{1}{6}$ of the remainder.
2. Of his earnings last month, Pat paid the same amount in taxes as he saved.

#### Solution
Let $E$ be Pat's total earnings. We are given savings $S = 1190$. We need to find $E$.
- **Statement (1):**
  - Spent on living expenses: $\frac{1}{4} E$
  - Remainder: $E - \frac{1}{4} E = \frac{3}{4} E$
  - Savings: $\frac{1}{6} \left(\frac{3}{4} E\right) = \frac{3}{24} E = \frac{1}{8} E$
  - Since $S = 1190 \implies \frac{1}{8} E = 1190 \implies E = 9520$.
  This statement alone is **sufficient**.
- **Statement (2):**
  - Taxes = Savings = $\$1190$.
  This does not provide any relation between savings/taxes and the total earnings $E$. Thus, Statement (2) alone is **not sufficient**.
- **Answer:** **Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.**

---

## Data Interpretation

### Q15. Airline B Passengers Increase

**Topic:** `data-interpretation`, `percentages`

The table below shows passenger statistics for different airlines from Quarter 1 (Q1) to Quarter 4 (Q4). Which quarter showed the biggest percentage increase in the number of passengers for Airline B compared to the previous quarter?

| Quarter | Airline A | Airline B | Airline C |
|---------|-----------|-----------|-----------|
| Q1      | 510       | 340       | 420       |
| Q2      | 540       | 390       | 450       |
| Q3      | 590       | 425       | 480       |
| Q4      | 610       | 525       | 510       |

#### Solution
Calculate the percentage increase for Airline B for each quarter:
- **Q2 (from Q1):**
  $$\text{Increase} = \frac{390 - 340}{340} \times 100\% = \frac{50}{340} \times 100\% \approx 14.71\%$$
- **Q3 (from Q2):**
  $$\text{Increase} = \frac{425 - 390}{390} \times 100\% = \frac{35}{390} \times 100\% \approx 8.97\%$$
- **Q4 (from Q3):**
  $$\text{Increase} = \frac{525 - 425}{425} \times 100\% = \frac{100}{425} \times 100\% \approx 23.53\%$$
- **Answer:** **Quarter 4** shows the biggest percentage increase.

---

### Q16. Xeon vs Paragon Growth Rate

**Topic:** `data-interpretation`, `percentage-growth`

Based on the passenger Courier growth rate statistics from 2015 to 2018:
- **Paragon Couriers in 2016:** Growth rate = $12.5\%$
- **Paragon Couriers in 2017:** Growth rate = $15.56\%$
- **Xeon Couriers in 2017:** Growth rate = $11.2\%$
Which company had the highest annual growth rate and in which year?

#### Solution
By comparing the data:
- Paragon Couriers in 2017 achieved a growth rate of **$15.56\%$**, which is the maximum among the given data points.

---

### Q17. Interchanged Profit Margin

**Topic:** `data-interpretation`, `profit-margin`

The revenues and profit margins for three companies are given as:
- **SwiftPurchase:** Revenue = $\$1100$ million, Profit Margin = $25\%$ (Profit = $\$275$ million)
- **BayZ:** Revenue = $\$800$ million, Profit Margin = $15\%$
- **ClickBuy:** Revenue = $\$950$ million, Profit Margin = $18\%$

If the profit margins of BayZ and ClickBuy are interchanged, which company will have the highest profit?

#### Solution
1. Interchange the margins:
   - New Profit Margin for BayZ = $18\%$
     $$\text{New Profit}_{\text{BayZ}} = 800 \times 18\% = \$144 \text{ million}$$
   - New Profit Margin for ClickBuy = $15\%$
     $$\text{New Profit}_{\text{ClickBuy}} = 950 \times 15\% = \$142.5 \text{ million}$$
2. Compare with SwiftPurchase:
   - SwiftPurchase profit remains unchanged at **$\$275$ million**.
3. **Answer:** **SwiftPurchase** continues to have the highest profit.

---

### Q18. XYZ Company Highest Profit %

**Topic:** `data-interpretation`, `profitability`

For XYZ Company, the Cost and Revenue figures (in millions) over five years are:
- **2015:** Cost = 100, Revenue = 250 (Profit = 150, Profit % = 150%)
- **2016:** Cost = 120, Revenue = 360 (Profit = 240, Profit % = 200%)
- **2017:** Cost = 150, Revenue = 400 (Profit = 250, Profit % = 166.7%)
- **2018:** Cost = 200, Revenue = 480 (Profit = 280, Profit % = 140%)

In which year was the profit percentage the highest?

#### Solution
1. Calculate profit %: $\text{Profit \%} = \frac{\text{Revenue} - \text{Cost}}{\text{Cost}} \times 100\%$
2. The peak profit percentage occurred in **2016** with a profit percentage of **$200\%$**.

---

### Q19. Expenses Percentage Increase

**Topic:** `data-interpretation`, `percentage-increase`

Expenses (in millions) of a startup over four years are:
- **2019:** 45
- **2020:** 55
- **2021:** 68.5
- **2022:** 78
Which year recorded the highest percentage increase in expenses over the previous year?

#### Solution
- **2020 (from 2019):**
  $$\text{Increase} = \frac{55 - 45}{45} \times 100\% \approx 22.22\%$$
- **2021 (from 2020):**
  $$\text{Increase} = \frac{68.5 - 55}{55} \times 100\% = \frac{13.5}{55} \times 100\% \approx 24.55\%$$
- **2022 (from 2021):**
  $$\text{Increase} = \frac{78 - 68.5}{68.5} \times 100\% = \frac{9.5}{68.5} \times 100\% \approx 13.87\%$$
- **Answer:** **2021** recorded the peak percentage increase ($24.55\%$).

---

### Q20. XYZ Limited Qtr Profit Margin

**Topic:** `data-interpretation`, `profit-margin`

XYZ Limited's quarterly revenue and profit margins are given.
- **Q1:** Revenue = 150, Profit = 60 (Margin = 40%)
- **Q2:** Revenue = 180, Profit = 72 (Margin = 40%)
- **Q3:** Revenue = 200, Profit = 80 (Margin = 40%)
- **Q4:** Revenue = 220, Profit = 88 (Margin = 40%)

Which quarter had the highest profit margin?

#### Solution
- The profit margin remained constant at **$40\%$** across all quarters.

---

## Verbal Ability and Reading Comprehension

### Q21. Author Organization RC Passage (IPR)

**Topic:** `reading-comprehension`, `passage-structure`

**Passage:**
> The acceleration of economic globalization has increased the significance of intellectual property rights (IPRs) in today's marketplace. In an era of knowledge-based services, corporations guard their IPRs fiercely, highlighting the importance of patents, copyrights, and trademarks. Enterprises with significant IPRs often hold considerable power, particularly within the technology sector. The competitive advantage conferred by these rights is amplified in industries with reduced product life cycles or rapidly advancing technologies.
>
> Economists argue that the social benefits resulting from IPRs, such as the promotion of innovation and creativity, outweigh the monopolistic consequences. In contrast, critics of IPRs assert that these rights often stifle innovation by preventing the free dissemination of information. Firms also manipulate these IPRs to consolidate their market positions, leading to limited competition and high prices.
>
> The digital age is pushing the boundaries of traditional IPRs frameworks, prompting regulatory bodies to strike a balance between the need to reward innovation while mitigating the risks associated with monopolies.

**Question:** Which of the following best describes the author's organization of the passage?

**Options:**
- A) The author discusses the importance of Intellectual Property Rights, outlines its positive and negative consequences, and finally discusses the role of regulatory bodies.
- B) The author critiques Intellectual Property Rights before defending its importance in the modern economy.
- C) The author provides a brief introduction of Intellectual Property Rights, discusses its history and evolution, and wraps up with its future prospects.
- D) The author maintains a neutral stance, providing equal arguments for and against Intellectual Property Rights.

**Correct Answer:** **A**  
*Explanation:* The first paragraph introduces IPRs and their economic significance. The second paragraph outlines the benefits (proponents' views) and drawbacks (critics' views). The final paragraph highlights how the digital age forces regulatory bodies to adapt.

---

### Q22. Modern Marketing RC Passage

**Topic:** `reading-comprehension`, `passage-structure`

**Passage:**
> The integration of traditional marketing practices with digital media platforms has given rise to a new term - 'modern marketing.' Rather than replacing traditional methods, marketers are leveraging digital technology to enhance performance. This involves the use of technology for data collection, audience targeting, and analytics. It's been observed that modern marketing strategies are showing higher Return On Investment (ROI) due to their increased tenability and flexibility.
>
> A significant aspect of this transformation has been the dynamics of human resource management. HR in modern organizations isn't merely restricted to hiring and firing. They're now becoming key players in strategic decision making, helping organizations to adapt and foster technological developments. This means companies are considering employees not only as resources but also as innovators and drivers of change.
>
> On the economic front, the regulatory domains are increasingly grappling with the implications of digital technology. Traditional regulatory standards seem to lose their footing, making space for innovative and effective measures. Thus, modern marketing is a montage of technological changes reinforcing traditional business domains.

**Question:** What is the logical structure of the passage?

**Options:**
- A) Presentation of a concept followed by contrary ideas
- B) Presentation of an idea followed by critique and conclusion
- C) Introduction of a concept followed by elaborations, examples and implications
- D) Narration of an event from start to finish
- E) Discussion of two opposing concepts

**Correct Answer:** **C**  
*Explanation:* The passage introduces the concept of "modern marketing" in paragraph 1, then details its implications in HR (paragraph 2) and regulation (paragraph 3), concluding with a summary.

---

### Q23. Reyess Corporation HR RC Passage

**Topic:** `reading-comprehension`

**Passage:**
> Despite having risen up from a modest background, Reyess Corporation, a tech titan, has seen a consistent surge in market value in the face of aggressive competition. They attribute their success to their unique human resource (HR) approach, which emphasizes the long-term development of employees. Reyess understands that investing in talent helps build not just a loyal workforce, but also results in company-wide performance boosts. They believe the value of human capital is symmetrical with monetary economics. Hence, they established the 'Human Reservoir Initiative' which leverages their expansive financial resources to develop employees, with a distinct emphasis on nurturing their creative potential and leadership abilities. HR scholars view Reyess's strategy as unprecedented and are keen to analyze its long-term effects. While competitors focus on short-term, tangible growth often marked by skyrocketing revenues or pricey acquisitions, Reyess gambles on an abstract, long-term investment in employee talent. Economists note that such decisions could mark the dawn of a reshaping of corporate...

**Question:** What can be concluded about Reyess Corporation's strategy compared to its competitors?

**Options:**
- A) They invest heavily in employee development.
- B) They believe that human capital is a form of currency.
- C) They focus more on tangible growth and short-term strategies.
- D) They have a similar approach to HR management.
- E) They generally come from a modest background.

**Correct Answer:** **A**  
*Explanation:* The text contrasts competitors (who focus on short-term growth and acquisitions) with Reyess (which invests heavily in the long-term development of employees via the 'Human Reservoir Initiative').

---

### Q24. Darwinian Business World RC Passage

**Topic:** `reading-comprehension`, `main-idea`

**Passage:**
> In today's Darwinian world of business, it is not the academic qualifications, but the understanding of the fundamentals of economics, which determines the success of an entrepreneur. A deep comprehension of supply and demand dynamics, GDP, inflation, and interest rates plays a crucial role in the successful running of a business. However, a significant amount of academicians argue that the primary requirement to be a pro in the business is marketing skills. They state that marketing involves understanding the needs and wants of the customer, which forms the foundation of any business strategy. On the contrary, a set of researchers from the field of human resource management opines that the success of a company not only depends on the product or service they offer but also on the people who create, manage, and sell it. Over the years, the studies concluded that the three fields hold equitable significance. Nevertheless, in the practical business world, undue importance is given to one field over the other based on the requirements of the business environment.

**Question:** Which among the following best articulates the main point of the passage?

**Options:**
- A) The significance of human resources in a business
- B) The role of the marketing in business success
- C) The debate among different fields on their importance in running a successful business
- D) The changing emphasis in the business world depending on the requirements of the business environment
- E) The importance of economics in business

**Correct Answer:** **D**  
*Explanation:* The final sentences clarify that despite all three fields being equitably significant, the practical business world changes its emphasis from one field to another depending on the business environment's demands.

---

### Q25. Omnichannel Retail RC Passage

**Topic:** `reading-comprehension`

**Passage:**
> In the era of digitization, many entrepreneurs have started to reconsider the importance of brick-and-mortar shops due to the rapid growth of e-commerce. Physical stores, once viewed as the backbone of retail, are now considered alternatively due to compelling economic factors and an ever-increasing digital literacy rate among consumers. However, several marketing research suggests that consumers still prefer tangible shopping experiences, hinting at the co-existence and interplay between digital and physical retail. Economics also highlights the supply chain efficiencies and cost effectiveness that physical stores provide, especially for items requiring high logistic costs, such as furniture. Moreover, the human resource management aspect emphasizes the value of in-store personnel in providing personalized service and enhancing customer loyalty. It is therefore critical for businesses to balance their digital and physical presence by creating an integrated omnichannel framework supported by innovative marketing strategies, efficient logistics and superior customer service. Hence, the zeitgeist of entrepreneurial success in retail, it seems, may indeed be a blend of digital and physical platforms resonating with consumer trends, economic logic, and HR sensibilities.

**Question:** Which among the following is the main conclusion of the passage?

**Options:**
- A) Digital literacy among consumers will continue to increase.
- B) Logistic costs for e-commerce are high.
- C) All entrepreneurs are reconsidering the importance of physical stores.
- D) Consumer trends, economic logic, and HR sensibilities determine retail success.
- E) In-store personnel are not important in e-commerce.

**Correct Answer:** **D**  
*Explanation:* The final sentence explicitly summarizes that retail success (zeitgeist of entrepreneurial success) is a blend of physical and digital platforms that resonates with consumer trends, economic logic, and HR sensibilities.

---

### Q26. Digital Marketing Transition RC Passage

**Topic:** `reading-comprehension`

**Passage:**
> With the advent of the digital era, traditional marketing models have been significantly disrupted. Social Media, a tool of Web 2.0, has transformed how companies interact with consumers, remarkably broadening the parameters of consumer touchpoints. Economically, the phenomenon has reduced the entry barriers for small businesses, resulting in market saturation and intense competition. From a human resource perspective, the shift necessitates the development of new skills that empower employees to leverage these digital tools effectively. Despite these palpable changes, many enterprises remain reluctant to embrace this new medium fully. Instead, they supplement their traditional marketing efforts with digital channels, reflecting a transitional phase in the evolution of marketing strategies. Several theorists posit that this amalgamated approach, often resulting in inconsistent brand messages across channels, stems from the reluctance to abolish the frameworks that were once successful. In contrast, others believe that it is merely a strategic approach to maintain relevancy among multiple demographic groups with differential technology acceptance rates.

**Question:** What might be a logical conclusion that could be drawn from the passage?

**Options:**
- A) Businesses should disregard traditional marketing methods.
- B) Digital marketing strategies should cater to multiple demographic groups.
- C) Adopting a combined approach in transition can result in inconsistent brand messages.
- D) Small businesses have an advantage in the digital era.
- E) Increased market saturation will force businesses to embrace digital marketing.

**Correct Answer:** **C**  
*Explanation:* The text directly states: "...this amalgamated (combined) approach, often resulting in inconsistent brand messages across channels, stems from the reluctance to abolish..."

---

### Q27. Psychographic Profiling RC Passage

**Topic:** `reading-comprehension`

**Passage:**
> The global business market is an arena of intense competition, where organizations grapple to secure a significant market share. Consequently, marketing strategies have become increasingly sophisticated to maintain relevance. Traditionally, marketing experts relied on demographic segmentation; however, a new theory suggests that psychographic profiling may present a more comprehensive understanding of the consumer's mindset. This methodology prioritizes customer values, attitudes, interests, and lifestyle over traditional demographic data. Meanwhile, economists view this shift skeptically. Derived from the principles of behavioral economics, they argue that while psychographic profiling may present a deeper understanding of a consumer's psychology, it inevitably leads to increased data noise. Human Resource Management (HRM) has its viewpoint on this new trend. HRM professionals argue that an organization that invests in understanding the employees' psychological profile could implement similar strategies to enhance job satisfaction and productivity. However, the ethical implications of psychographic profiling, such as privacy invasion and manipulation, remain debatable within the social science...
*(Note: Question options were cut off in source image).*

---

## Logical and Critical Reasoning

### Q28. Flexible Work Hours

**Topic:** `critical-reasoning`, `strengthen-weaken`

A design agency is contemplating flexible work hours for its graphic designers within a time window from 8 a.m. to 8 p.m. This policy could likely undermine project completion if the designers' responsibilities involve them needing to...

**Options:**
- A) seek frequent input and feedback from their colleagues
- B) use specialized design software
- C) adhere to the established design principles
- D) ensure their designs meet client expectations
- E) deliver projects within tight deadlines

**Correct Answer:** **A**  
*Explanation:* Flexible work hours mean that designers can work at non-overlapping times. If their job requires constant communication and real-time feedback from colleagues, the lack of overlapping working hours will delay project coordination and undermine completion.

---

### Q29. Telecare Growth Plan

**Topic:** `critical-reasoning`, `strengthen-weaken`

Given the rapid growth of telecare in healthcare, traditional roles within the sector are transforming substantially. Within the next five years, healthcare professionals will require new skills to adapt effectively to these technologies.

Which of the following plans, if feasible, would enable a healthcare organization to prepare most effectively for this impending change?

**Options:**
- A) The organization commits to providing continuous necessary training to meet the evolving demand of its employees in the rapidly changing telecare-integrated healthcare field.
- B) The organization contemplates conducting periodic surveys to understand the impacts of telecare integration on its employees' role.
- C) Before telecare implementation, the organization intends to conduct an educational program to inform staff of the likely repercussions.
- D) The organization proposes offering specific telecare training to select employees six years into service.

**Correct Answer:** **A**  
*Explanation:* Option A directly addresses the gap ("require new skills") by establishing continuous training. Surveying (B) and informing about repercussions (C) do not build skills. Training employees 6 years into service (D) is too late and restrictive.

---

### Q30. AI DeepThought

**Topic:** `critical-reasoning`, `argument-flaw`

**AI Developer:** The AI model 'DeepThought' has shown promise in predictive analytics. However, the long-term impacts on data integrity are still unknown, and for that reason, I am not advocating for its wide use currently.
**Data Analyst:** Your viewpoint opposes your usual actions. You implement models that you know can potentially lead to data issues, so surely concern about impacts isn't why you won't endorse 'DeepThought'.

The data analyst's argument is flawed because it fails to consider that...

**Options:**
- A) the impacts of an AI model on data integrity can sometimes take time to manifest
- B) the AI developer could be uncertain that 'DeepThought' has been conclusively proven to be beneficial
- C) if left unchecked, widespread use of a defective AI model could lead to serious data integrity concerns
- D) known risks can be compared to known benefits, but unknown risks cannot
- E) the data impacts of 'DeepThought' might differ from other AI models

**Correct Answer:** **D**  
*Explanation:* The developer's reluctance is based on *unknown* long-term risks. The analyst points to the developer using models with *known* risks (data issues). The analyst fails to see that known risks can be evaluated against benefits, whereas unknown risks represent an unquantifiable hazard.

---

## SSC CGL Reference Paper - Quantitative Aptitude

This section contains solutions to the 25 quantitative aptitude questions found in the `ssc-cgl-13th-sep-shift-1_copy.pdf` file.

### Q31. Comparing Powers/Roots

Suppose $x = \sqrt{2} + \sqrt{3}$, $y = \sqrt{5} + 1$, and $z = 2\sqrt{2} + 1$. Which of the following is true?
- A) $x < y < z$
- B) $z < y < x$
- C) $y < x < z$
- D) $x < z < y$

#### Solution
Approximate the roots:
- $\sqrt{2} \approx 1.414$, $\sqrt{3} \approx 1.732$, $\sqrt{5} \approx 2.236$
- $x = 1.414 + 1.732 = 3.146$
- $y = 2.236 + 1 = 3.236$
- $z = 2(1.414) + 1 = 3.828$
Comparing the values: $3.146 < 3.236 < 3.828 \implies x < y < z$.
**Correct Option: A**

---

### Q32. Budget Allocation Change

The budget for a construction project is allocated to land acquisition, building materials, and labor in the ratio $5 : 3 : 2$. During the project, the cost of land acquisition rose by $5\%$, building materials rose by $10\%$, and labor fell by $20\%$. What is the percent change (increase or decrease) in the total project cost?

#### Solution
Let the initial costs be:
- $\text{Land} = 50$, $\text{Materials} = 30$, $\text{Labor} = 20$.
- Total Cost = $100$.
Apply the changes:
- $\text{New Land} = 50 \times 1.05 = 52.5$
- $\text{New Materials} = 30 \times 1.10 = 33$
- $\text{New Labor} = 20 \times 0.80 = 16$
- $\text{New Total Cost} = 52.5 + 33 + 16 = 101.5$
Percentage change:
$$\text{Change} = \frac{101.5 - 100}{100} \times 100\% = 1.5\% \text{ increase}$$
**Correct Option: 1.5% increase**

---

### Q33. Arithmetic Evaluation

Evaluate: $6 - \left[ \frac{2}{3} \div \left\{ \frac{1}{6} + \left( \frac{1}{2} \times \left( 1 - \frac{1}{3} \right) \right) \right\} \right]$.

#### Solution
1. Inner parentheses: $1 - \frac{1}{3} = \frac{2}{3}$
2. Multiplication: $\frac{1}{2} \times \frac{2}{3} = \frac{1}{3}$
3. Addition: $\frac{1}{6} + \frac{1}{3} = \frac{3}{6} = \frac{1}{2}$
4. Division: $\frac{2}{3} \div \frac{1}{2} = \frac{2}{3} \times 2 = \frac{4}{3}$
5. Subtraction: $6 - \frac{4}{3} = \frac{14}{3}$
**Correct Option: 14/3**

---

### Q34. Profit Sharing Partnership

X, Y, and Z invested ₹25,000, ₹35,000, and ₹40,000 respectively in a business. If the profit at the end of the year was ₹30,000, find Y's share.

#### Solution
Investment ratio X : Y : Z:
$$25,000 : 35,000 : 40,000 = 5 : 7 : 8$$
Sum of ratio parts: $5 + 7 + 8 = 20$.
Y's profit share:
$$\text{Share}_Y = \frac{7}{20} \times 30,000 = 7 \times 1,500 = \text{₹}10,500$$
**Correct Option: ₹10,500**

---

### Q35. Active Capital Adjustment

A and B started a business by investing ₹48,000 and ₹72,000 respectively. After 6 months, A withdrew half of his capital, while B increased his capital by ₹24,000. At the end of the year, they earned a total profit of ₹55,000. What is B's share in the profit?

#### Solution
Calculate equivalent monthly investments (capital $\times$ time):
- **For A:** ₹48,000 for 6 months + ₹24,000 for 6 months
  $$\text{Equivalent}_A = (48,000 \times 6) + (24,000 \times 6) = 288,000 + 144,000 = 432,000$$
- **For B:** ₹72,000 for 6 months + ₹96,000 (i.e., $72,000 + 24,000$) for 6 months
  $$\text{Equivalent}_B = (72,000 \times 6) + (96,000 \times 6) = 432,000 + 576,000 = 1,008,000$$
Ratio of profit sharing A : B:
$$432,000 : 1,008,000 = 432 : 1008 = 3 : 7$$
B's profit share:
$$\text{Share}_B = \frac{7}{10} \times 55,000 = \text{₹}38,500$$
**Correct Option: ₹38,500**

---

### Q36. Average Calculation from Table

The daily wages of 5 workers over 4 days are given. What is the average daily earning of Worker C?

| Day | A | B | C | D | E |
|---|---|---|---|---|---|
| Day 1 | 200 | 180 | 220 | 160 | 190 |
| Day 2 | 210 | 175 | 230 | 170 | 195 |
| Day 3 | 190 | 185 | 215 | 180 | 200 |
| Day 4 | 220 | 190 | 225 | 175 | 205 |

#### Solution
1. Sum C's earnings: $220 + 230 + 215 + 225 = 890$
2. Find the average over 4 days:
   $$\text{Average} = \frac{890}{4} = 222.5$$
**Correct Option: 222.5**

---

### Q37. Demographic Ratio Change

In a city, the current number of literate people is $25,000$. If the number of literate males decreases by $5\%$ and the number of literate females increases by $10\%$, the total literate population becomes $25,250$. What is the initial number of literate males in the city?

#### Solution
Let $M$ and $F$ be the initial literate males and females:
1. $M + F = 25,000 \implies F = 25,000 - M$
2. After changes: $0.95M + 1.10F = 25,250$
Substitute $F$:
$$0.95M + 1.10(25,000 - M) = 25,250$$
$$0.95M + 27,500 - 1.10M = 25,250$$
$$27,500 - 0.15M = 25,250 \implies 0.15M = 2,250 \implies M = 15,000$$
**Correct Option: 15,000**

---

### Q38. Inventory Error Ratios

A baker ordered $10\text{ kg}$ of premium flour and some additional kg of standard flour. The price of premium flour per kg was twice that of standard flour. Due to an ordering error, the quantities of the two types of flour were interchanged. This decreased the total cost by $25\%$. Find the ratio of the quantity of premium flour to standard flour in the original order.

#### Solution
Let premium flour price be $2P$ and standard flour price be $P$. Let $x$ be the original quantity of standard flour.
- Original Cost: $C_{\text{orig}} = (10 \times 2P) + (x \times P) = P(20 + x)$
- Interchanged Cost: $C_{\text{error}} = (x \times 2P) + (10 \times P) = P(2x + 10)$
Since the cost decreased by $25\%$:
$$C_{\text{error}} = 0.75 \times C_{\text{orig}}$$
$$2x + 10 = 0.75(20 + x) \implies 2x + 10 = 15 + 0.75x \implies 1.25x = 5 \implies x = 4\text{ kg}$$
Original ratio (Premium : Standard) = $10 : 4 = 5 : 2$.
**Correct Option: 5:2**

---

### Q39. Selling Price with Targeted Profits

A vendor sold $15$ toys for ₹3000 and gained a profit of $25\%$. How many toys should he sell for ₹2816 to make a profit of $10\%$?

#### Solution
1. Selling Price per toy originally: $\frac{3000}{15} = \text{₹}200$
2. Find Cost Price (CP) per toy:
   $$\text{CP} \times 1.25 = 200 \implies \text{CP} = \frac{200}{1.25} = \text{₹}160$$
3. Target SP per toy for $10\%$ profit:
   $$\text{SP}_{\text{target}} = 160 \times 1.10 = \text{₹}176$$
4. Number of toys to sell:
   $$\text{Toys} = \frac{2816}{176} = 16$$
**Correct Option: 16**

---

### Q40. Mixture Profit Margin

A trader sells one brand of tea at ₹150 per kg, incurring a $25\%$ loss. He also sells another brand of tea at ₹200 per kg, incurring a $20\%$ loss. If he mixes the two brands in equal proportions and sells the mixture at ₹175 per kg, what is his overall profit or loss percentage?

#### Solution
1. Find Cost Price (CP) for each brand per kg:
   - **Brand 1:** $\text{CP}_1 \times 0.75 = 150 \implies \text{CP}_1 = \text{₹}200/\text{kg}$
   - **Brand 2:** $\text{CP}_2 \times 0.80 = 200 \implies \text{CP}_2 = \text{₹}250/\text{kg}$
2. If mixed in equal proportions (e.g., $1\text{ kg}$ each):
   - Total $\text{CP} = 200 + 250 = \text{₹}450$ for $2\text{ kg}$
   - Selling Price (SP) of mixture = ₹175 per kg $\implies$ Total $\text{SP} = 175 \times 2 = \text{₹}350$
3. Loss amount = $450 - 350 = \text{₹}100$
4. Loss percentage:
   $$\text{Loss \%} = \frac{100}{450} \times 100\% = \frac{200}{9}\% = 22.22\% \text{ loss}$$
**Correct Option: Loss of 22.22%**

---

### Q41. Cooperative Work Time

A and B together can complete a work in $12$ days. B and C together can complete the same work in $15$ days. C and A together can do it in $20$ days. In how many days can A alone complete the job?

#### Solution
Let the individual rates be $a, b, \text{ and } c$:
1. $a + b = \frac{1}{12}$
2. $b + c = \frac{1}{15}$
3. $c + a = \frac{1}{20}$
Add the equations:
$$2(a + b + c) = \frac{1}{12} + \frac{1}{15} + \frac{1}{20} = \frac{5 + 4 + 3}{60} = \frac{12}{60} = \frac{1}{5}$$
$$a + b + c = \frac{1}{10}$$
Subtract equation (2) ($b+c = \frac{1}{15}$) to isolate $a$:
$$a = \frac{1}{10} - \frac{1}{15} = \frac{3 - 2}{30} = \frac{1}{30}$$
Thus, A alone can complete the work in **$30$ days**.
**Correct Option: 30 days**

---

### Q42. Dilution Formula

From a 64-liter container of pure spirit, $8$ liters are removed and replaced by water. This operation is performed a total of three times. What is the final quantity of spirit remaining in the container?

#### Solution
Use the dilution formula:
$$\text{Remaining Spirit} = \text{Initial Quantity} \times \left(1 - \frac{x}{V}\right)^n$$
Where:
- $V = 64\text{ liters}$
- $x = 8\text{ liters}$
- $n = 3$
Compute:
$$\text{Remaining Spirit} = 64 \times \left(1 - \frac{8}{64}\right)^3 = 64 \times \left(\frac{7}{8}\right)^3 = 64 \times \frac{343}{512} = \frac{343}{8} = 42.88\text{ liters}$$
**Correct Option: 42.88 liters**

---

### Q43. Mixture Pricing

A juice vendor mixes water with pure orange juice. If he sells the mixture at the cost price of pure orange juice and makes a profit of $20\%$, what is the ratio of water to pure orange juice in the mixture?

#### Solution
Let the Cost Price of pure juice be ₹1 per liter. Water is assumed to be free (₹0/liter).
- Let $W$ be volume of water and $J$ be volume of pure juice.
- Cost of mixture = $J \times 1 = \text{₹}J$
- Selling price of mixture = $(W + J) \times 1 = \text{₹}(W + J)$
- Profit percentage:
  $$\frac{(W + J) - J}{J} \times 100\% = 20\% \implies \frac{W}{J} = 0.20 = \frac{1}{5}$$
Ratio of water to orange juice is $1 : 5$.
**Correct Option: 1:5**

---

### Q44. Average Speed Calculations

A car covers $40\%$ of a certain distance at a pace of $20\text{ km/h}$ and the remaining distance at a pace of $30\text{ km/h}$. What is the average speed of the car for the entire journey?

#### Solution
Let total distance be $D$.
- Time taken for the first part: $t_1 = \frac{0.4D}{20} = \frac{D}{50}$
- Time taken for the second part: $t_2 = \frac{0.6D}{30} = \frac{D}{50}$
- Total time: $t_{\text{total}} = \frac{D}{50} + \frac{D}{50} = \frac{D}{25}$
Average speed:
$$\text{Speed}_{\text{avg}} = \frac{\text{Distance}}{\text{Total Time}} = \frac{D}{D/25} = 25\text{ km/h}$$
**Correct Option: 25 km/h**

---

### Q45. Circular Track Relatives

A and B are jogging around a park's circular track which has a perimeter of $1.2\text{ km}$. They start from the same point at 6:00 a.m. and run in opposite directions. A's speed is $5\text{ km/h}$, and B's speed is $7\text{ km/h}$. At what time will they meet for the fifth time?

#### Solution
1. Relative speed in opposite directions:
   $$\text{Speed}_{\text{rel}} = 5 + 7 = 12\text{ km/h}$$
2. Time taken to meet for the first time:
   $$t_1 = \frac{\text{Distance}}{\text{Speed}_{\text{rel}}} = \frac{1.2\text{ km}}{12\text{ km/h}} = 0.1\text{ hours}$$
3. Time taken to meet for the 5th time:
   $$t_5 = 5 \times 0.1 = 0.5\text{ hours} = 30\text{ minutes}$$
4. Meeting time: 6:00 a.m. + 30 minutes = **6:30 a.m.**
**Correct Option: 6:30 AM**

---

### Q46. Area of Circle Sector

The area of a sector of a circle with radius $7\text{ cm}$ and central angle $90^\circ$ is:

#### Solution
$$\text{Area} = \frac{\theta}{360} \times \pi r^2 = \frac{90}{360} \times \frac{22}{7} \times 7^2 = \frac{1}{4} \times 154 = 38.48\text{ cm}^2$$
**Correct Option: 38.48 cm²**

---

### Q47. Degree to Radian Conversion

What is the radian measure of $150^\circ$?

#### Solution
$$\text{Radian} = \theta \times \frac{\pi}{180} = 150 \times \frac{\pi}{180} = \frac{5\pi}{6}$$
**Correct Option: 5\pi/6**

---

### Q48. Area of Sector

What is the area of a sector with a central angle of $120^\circ$ and radius $8\text{ cm}$?

#### Solution
$$\text{Area} = \frac{\theta}{360} \times \pi r^2 = \frac{120}{360} \times \pi \times 8^2 = \frac{1}{3} \times 64\pi = \frac{64\pi}{3}\text{ cm}^2$$
**Correct Option: 64\pi/3 cm²**

---

### Q49. Parallel Lines Slopes

Which of these lines is parallel to $3x + 2y = 5$?
- A) $3x + 2y = 7$
- B) $2x + 3y = 5$
- C) $3x - 2y = 5$
- D) $x + y = 5$

#### Solution
Parallel lines must have identical coefficients for $x$ and $y$ (equal slopes of $-\frac{3}{2}$). Only $3x + 2y = 7$ is parallel to $3x + 2y = 5$.
**Correct Option: A**

---

### Q50. Trigonometric Equation

If $\sin(90^\circ - x) = \cos(2x)$, then what is $x$?

#### Solution
Using the identity $\sin(90^\circ - x) = \cos(x)$:
$$\cos(x) = \cos(2x)$$
So $2x = 360^\circ k \pm x$.
For $k=0$ (acute angle range):
$$2x = x \implies x = 0^\circ$$
**Correct Option: 0°**

---

### Q51. Algebraic Substitution

If $x = \sqrt{5} + 2$, find $x^2 - 4\sqrt{5}$.

#### Solution
Substitute $x$:
$$x^2 = (\sqrt{5} + 2)^2 = 5 + 4 + 4\sqrt{5} = 9 + 4\sqrt{5}$$
Then:
$$x^2 - 4\sqrt{5} = (9 + 4\sqrt{5}) - 4\sqrt{5} = 9$$
**Correct Option: 9**

---

### Q52. Triangle Congruence

In triangles ABC and XYZ, if the lengths of the sides are such that AB equals XY, BC equals YZ, and CA equals ZX, which congruence rule demonstrates that triangle ABC is congruent to triangle XYZ?

#### Solution
Since all three corresponding sides are equal, the triangles are congruent by the **Side-Side-Side (SSS)** congruence rule.
**Correct Option: SSS**

---

### Q53. Complementary Trigonometry

Given $A$ and $B$ are complementary angles, and $\sin A = \frac{3}{5}$, what is $\tan B$?

#### Solution
Since $A$ and $B$ are complementary, $A + B = 90^\circ \implies B = 90^\circ - A$.
- $\tan B = \tan(90^\circ - A) = \cot A$
- Since $\sin A = \frac{3}{5}$, the corresponding right triangle has opposite = $3$, hypotenuse = $5$, adjacent = $\sqrt{5^2 - 3^2} = 4$.
- $\cot A = \frac{\text{Adjacent}}{\text{Opposite}} = \frac{4}{3}$
- Therefore, $\tan B = \frac{4}{3}$.
**Correct Option: 4/3**

---

### Q54. Cyclic Quadrilateral Angles

In a cyclic quadrilateral ABCD, if angle A is $100^\circ$, what is the measure of angle C?

#### Solution
In a cyclic quadrilateral, the sum of opposite angles is $180^\circ$:
$$\angle A + \angle C = 180^\circ \implies 100^\circ + \angle C = 180^\circ \implies \angle C = 80^\circ$$
**Correct Option: 80°**

---

### Q55. Trigonometric Identity Solution

If $\sin^2 A - \cos^2 A = \frac{1}{4}$, find the value of $\cos^2 A$.

#### Solution
Use the identity $\sin^2 A = 1 - \cos^2 A$:
$$(1 - \cos^2 A) - \cos^2 A = \frac{1}{4}$$
$$1 - 2\cos^2 A = \frac{1}{4} \implies 2\cos^2 A = 1 - \frac{1}{4} = \frac{3}{4} \implies \cos^2 A = \frac{3}{8}$$
**Correct Option: 3/8**
