# Interview Questions
*Total questions: 31*

---

## Table of Contents
- [Cognitive - Analytics](#cognitive---analytics)
- [Technology Concepts](#technology-concepts)

---

## Cognitive - Analytics

### Q1. Word Analogy: Liquor & Bartender

**Topic:** `Verbal Reasoning`, `Analogy`  

Choose the option for which the analogy between the pair of words is the same as the one given in the question.

**LIQUOR : BARTENDER ::**

- `lesson : student`
- `food : chef`
- `car : chauffeur`
- `cloth : weaver`

#### Solution
**Answer: `car : chauffeur`**

*Explanation:*
- A **bartender** is a professional whose job is to serve and handle **liquor**.
- A **chauffeur** is a professional whose job is to drive and handle a **car**.
- Note that a chef creates *food* and a weaver creates *cloth* (making them "Product : Creator" relationships), whereas a bartender and a chauffeur handle and operate pre-made items.

---

### Q2. Analytics Concepts: Predictive Analytics

**Topic:** `Data Analytics`, `Theoretical`  

Fill in the blank.

The type of analytics in which historical data is analyzed to identify the likelihood of future events is called __________ analytics.

- `Diagnostic`
- `Prescriptive`
- `Descriptive`
- `Predictive`

#### Solution
**Answer: `Predictive`**

*Explanation:*
- **Predictive** analytics uses historical data, statistical algorithms, and machine learning techniques to forecast the likelihood of future outcomes or events.
- **Descriptive** analytics describes what has happened.
- **Diagnostic** analytics explains why it happened.
- **Prescriptive** analytics suggests actions to take based on the predictions.

---

### Q3. Percentage & Ratio: Vehicle Composition

**Topic:** `Quantitative Aptitude`, `Pie Chart`  

In a society, there are cars of 6 different colors (Purple, Red, Pink, Black, Orange, and Green) and two-wheelers, all of the same color, Silver. The pie chart below shows the percentage breakup of the vehicles based on the color, present in the society.

- **Silver:** 20%
- **Purple:** 15%
- **Red:** 20%
- **Pink:** 10%
- **Black:** 5%
- **Orange:** 25%
- **Green:** 5%

Find the difference between the number of cars and two-wheelers in the society if there are 100 pink cars.

- `600`
- `800`
- `700`
- `1000`

#### Solution
**Answer: `600`**

*Explanation:*
1. Let $T$ be the total number of vehicles in the society.
2. Pink cars account for $10\%$ of the total vehicles.
   $$10\% \text{ of } T = 100 \implies T = 1000 \text{ vehicles}$$
3. Two-wheelers are all Silver, representing $20\%$ of the vehicles:
   $$\text{Two-wheelers} = 20\% \text{ of } 1000 = 200$$
4. Cars include all other colors (Purple, Red, Pink, Black, Orange, Green), representing the remaining $80\%$ of the vehicles:
   $$\text{Cars} = 80\% \text{ of } 1000 = 800$$
5. The difference between the number of cars and two-wheelers is:
   $$\text{Difference} = 800 - 200 = 600$$

---

### Q4. Statistics: Mean of Composite Numbers

**Topic:** `Basic Mathematics`, `Statistics`  

What is the mean of the first four composite numbers?

- `3`
- `4`
- `5`
- `6.75`

#### Solution
**Answer: `6.75`**

*Explanation:*
1. A composite number is a positive integer that has at least one divisor other than 1 and itself.
2. The number $1$ is neither prime nor composite.
3. The first few integers are:
   - $2, 3$: Prime numbers
   - $4$: Composite
   - $5$: Prime
   - $6$: Composite
   - $7$: Prime
   - $8$: Composite
   - $9$: Composite
4. The first four composite numbers are $4, 6, 8, \text{ and } 9$.
5. Sum of these numbers: $4 + 6 + 8 + 9 = 27$.
6. Mean: $\frac{27}{4} = 6.75$.

---

### Q5. Data Interpretation: Departmental Student Growth

**Topic:** `Data Interpretation`, `Graph Analysis`  

The following graph shows the percentage distribution of the number of students of a university who specialize in four subjects, namely History, Physics, Commerce, and Mathematics, across 4 years from 2011 to 2014. The university offers only these four specializations.

| Specialization | 2011 | 2012 | 2013 | 2014 |
| :--- | :---: | :---: | :---: | :---: |
| **History** (Blue) | 32% | 24% | 33% | 30% |
| **Physics** (Red) | 24% | 24% | 20% | 25% |
| **Commerce** (Green) | 30% | 32% | 24% | 28% |
| **Mathematics** (Purple) | 14% | 20% | 22% | 16% |

Assuming that the intake of the university never decreased, how many instances are there of the number of students in a department in a year definitely increasing over the previous year?

- `3`
- `4`
- `6`
- `7`

#### Solution
**Answer: `6`**

*Explanation:*
1. Let $N_t$ be the total university intake in year $t$. We are given that $N_t \ge N_{t-1} > 0$.
2. The number of students in department $D$ in year $t$ is $S_{D,t} = p_{D,t} \cdot N_t$.
3. For $S_{D,t}$ to *definitely* increase over $S_{D,t-1}$, the inequality $p_{D,t} \cdot N_t > p_{D,t-1} \cdot N_{t-1}$ must hold for any valid $N_t \ge N_{t-1}$.
4. If $p_{D,t} > p_{D,t-1}$, then:
   $$S_{D,t} = p_{D,t} N_t \ge p_{D,t} N_{t-1} > p_{D,t-1} N_{t-1} = S_{D,t-1}$$
   Thus, a strict increase in percentage $p_{D,t} > p_{D,t-1}$ guarantees a definite increase in student count.
5. If $p_{D,t} \le p_{D,t-1}$, it is possible that $N_t = N_{t-1}$, meaning $S_{D,t} \le S_{D,t-1}$ (the count could stay the same or decrease).
6. Let's count the instances where percentage increased over the previous year:
   - **History:** 2012 to 2013 (24% -> 33%) — **1 instance**
   - **Physics:** 2013 to 2014 (20% -> 25%) — **1 instance**
   - **Commerce:** 2011 to 2012 (30% -> 32%), 2013 to 2014 (24% -> 28%) — **2 instances**
   - **Mathematics:** 2011 to 2012 (14% -> 20%), 2012 to 2013 (20% -> 22%) — **2 instances**
7. Total instances = $1 + 1 + 2 + 2 = 6$.

---

## Technology Concepts

### Q6. Python Syntax: Spot the Error

**Topic:** `Python`, `Syntax`  

Spot the error in the given code.

```python
while True print('Welcome')
```

- `Syntax error`
- `Runtime error`
- `Math error`
- `Logical error`

#### Solution
**Answer: `Syntax error`**

*Explanation:*
In Python, control flow statements like `while` and `if` require a colon (`:`) to separate the condition from the body of the loop. The correct syntax is:
```python
while True:
    print('Welcome')
```
Without the colon, the parser throws a `SyntaxError: invalid syntax` at compile time.

---

### Q7. Python Programming: Range Output

**Topic:** `Python`, `Control Flow`  

What is the output of the code shown below?

```python
for num in range(15, -6, -4):
    print(num)
```

#### Solution
**Output:**
```text
15
11
7
3
-1
-5
```

*Explanation:*
- The `range(start, stop, step)` function starts generating values at `start` (inclusive), decrements by the absolute value of `step` (since `step = -4`), and stops before reaching `stop` (exclusive).
- The sequence generated is:
  1. $15$ (start)
  2. $15 - 4 = 11$
  3. $11 - 4 = 7$
  4. $7 - 4 = 3$
  5. $3 - 4 = -1$
  6. $-1 - 4 = -5$
- The next value would be $-5 - 4 = -9$, which is less than or equal to the stop value $-6$, so the loop terminates.

---

### Q8. Cloud Computing: Service Models

**Topic:** `Cloud Computing`, `PaaS`  

In which of the following cloud models does the customer use the programming languages and tools that are supported by this model supplier?

*Note: The customer has no control or management over the infrastructure but does have complete control over the applications and some of the configuration of the platform environment and makes their own choices for developing or buying them.*

- `IAAS`
- `SAAS`
- `PAAS`
- `None of the given options`

#### Solution
**Answer: `PAAS` (Platform as a Service)**

*Explanation:*
- Under **Platform as a Service (PaaS)**, the cloud provider delivers hardware, operating systems, storage, and network capacity over the internet.
- The consumer is responsible for deploying and maintaining applications created using programming languages, libraries, services, and tools supported by the provider.
- In **IaaS**, the consumer must manage the OS, middleware, and runtime themselves. In **SaaS**, the consumer only uses the fully functional application and has no control over application code or environment configuration.

---

### Q9. Operating Systems: I/O Device Interfaces

**Topic:** `Operating Systems`, `Computer Architecture`  

In an input-output operation, the Operating System sends commands or data to Input-output devices. Which of the following device parts accepts this kind of input?

- `Device Register`
- `Device Driver`
- `Index Register`
- `CPU Register`

#### Solution
**Answer: `Device Register`**

*Explanation:*
- **Device Registers** (like Control, Status, and Data registers) are hardware registers located inside the device controller of an I/O device. The CPU/OS writes commands and data directly into these registers to interact with the device.
- A **Device Driver** is the software module that manages the hardware controller.
- **Index Registers** and **CPU Registers** are located within the CPU, not on the I/O devices.

---

### Q10. Object-Oriented Programming: Java Abstract Classes

**Topic:** `Java`, `Object-Oriented Programming`  

The following is a simple program that defines abstract methods in the abstract classes. Determine its output.

```java
abstract class example1{
    example1( ){
        System.out.println("Constructor of abstract class called");
    }
    abstract void function( );
}
class example2 extends example1{
    example2( ){
        System.out.println("Constructor of derived class called");
    }
}
class main{
    public static void main(String args[ ]){
        example2 e = new example2( );
    }
}
```

- `Compilation error occurs. Class that extends the abstract class must override the methods in the abstract class. Here class example2 extends the abstract class example1 but it does not override the abstract method in it.`
- `Constructor of derived class called`
- `An instance should be created for the abstract class also when an object is created for the extended class. If we don't write it compilation error occurs.`
- `Compilation error occurs. Constructor should not be used inside the abstract class.`

#### Solution
**Answer: `Compilation error occurs. Class that extends the abstract class must override the methods in the abstract class. Here class example2 extends the abstract class example1 but it does not override the abstract method in it.`**

*Explanation:*
- Any non-abstract (concrete) class that extends an abstract class must provide concrete implementations for all inherited abstract methods.
- Here, `example2` extends `example1` but does not override `abstract void function()`, causing a compilation error: `example2 is not abstract and does not override abstract method function() in example1`.

---

### Q11. Object-Oriented Programming: C++ Access Specifiers

**Topic:** `C++`, `Inheritance`  

What is the output of the following program?

```cpp
#include <iostream>
using namespace std;
class parent1
{
    private:
    int p1;
    protected:
    int q1;
    public:
    int r1;
    parent1()
    {
        p1 = 50;
        q1 = 73;
        r1 = 62;
    }
};

class child1: public parent1
{
    public:
    void data()
    {
        cout << "p1: not accessible" << endl;
        cout << "value of q1 is " << q1 << endl;
        cout << "value of r1 is " << r1 << endl;
    }
};

int main()
{
    child1 c1;
    c1.data();
    return 0;
}
```

- `Compilation Error`
- `Runtime Error`
- `p1: not accessible \n value of q1 is 73 \n value of r1 is 62`
- `p1: 0 \n value of q1 is 0 \n value of r1 is 0`

#### Solution
**Answer: `p1: not accessible \n value of q1 is 73 \n value of r1 is 62`**

*Explanation:*
- The private member `p1` of `parent1` is not directly accessible within the derived class `child1`. However, the function `child1::data()` does not attempt to compile-access the variable `p1`; it simply prints the string literal `"p1: not accessible"`, which is fully valid.
- The protected member `q1` and public member `r1` are accessible in the derived class.
- When `c1` is instantiated, the default constructor of `parent1` is called first, initializing `q1 = 73` and `r1 = 62`.
- Output:
  ```text
  p1: not accessible
  value of q1 is 73
  value of r1 is 62
  ```

---

### Q12. C Programming: Pointer Syntax

**Topic:** `C Programming`, `Pointers`  

Which of the following expressions is the equivalent pointer expression for `arr[i][j][k]`?

- `(((a+i)+j)+k)`
- `*(*(*(a+i)+j)+k)`
- `((*(a+i)+j)+k)`
- `*(((*(a+i)+j)+k)`
- `None of the given options`

#### Solution
**Answer: `*(*(*(a+i)+j)+k)`**

*Explanation:*
In C and C++, array subscripts are defined in terms of pointer arithmetic:
- `arr[i]` is equivalent to `*(arr + i)`.
- `arr[i][j]` is equivalent to `*( *(arr + i) + j )`.
- `arr[i][j][k]` is equivalent to `*( *( *(arr + i) + j ) + k )`.

---

### Q13. Artificial Intelligence: Definitions

**Topic:** `Artificial Intelligence`, `Theoretical`  

What is Artificial Intelligence?

A. A very small part-time application of Machine Learning
B. A computer game
C. A virtual reality software
D. An area of computer science that aims to create intelligent machines

- `Only A`
- `Only D`
- `Only B`
- `Only C`
- `A and D`

#### Solution
**Answer: `Only D`**

*Explanation:*
- **Artificial Intelligence** is a broad field of computer science focused on building smart machines capable of performing tasks that typically require human intelligence.
- Statement A is incorrect; Machine Learning is actually a subset of Artificial Intelligence, not vice versa.
- B and C describe specific applications or technologies but do not define AI.

---

### Q14. Data Structures: Sorting Algorithms

**Topic:** `Data Structures`, `Sorting`  

Which sorting technique improves insertion sort by comparing elements separated by a gap of several positions?

- `Bucket sort`
- `Shell sort`
- `Radix sort`
- `Quick sort`

#### Solution
**Answer: `Shell sort`**

*Explanation:*
- **Shell sort** is a generalization and improvement of insertion sort. It compares elements that are separated by a gap of several positions, allowing elements to move toward their final position faster than the single-step swaps in insertion sort.
- The gap size is reduced gradually until it becomes $1$ (which is basic insertion sort).

---

### Q15. Data Structures & Algorithms: Convex Hull

**Topic:** `Algorithms`, `Computational Geometry`, `Divide and Conquer`  

Consider that you are developing a geographical information system (GIS) that needs to efficiently compute the convex hull of a set of points representing various landmarks in a region. You decide to implement the Divide and Conquer algorithm for this task. During the implementation, you encounter the problem of merging two convex hulls (one from the left half and one from the right half of the point set) by finding the upper and lower tangents between them.

Given this information, what is the time complexity of the overall Divide and Conquer algorithm for finding the convex hull of n points? Select the correct option from the given choices.

- `O(n^2)`
- `O(n^3)`
- `O(log n)`
- `O(n log n)`

#### Solution
**Answer: `O(n log n)`**

*Explanation:*
- The Preparata-Hong Divide and Conquer algorithm computes the convex hull of $n$ points by:
  1. Sorting the points by x-coordinates: $O(n \log n)$ time.
  2. Recursively dividing the points into left and right halves: $O(1)$ time.
  3. Merging the two disjoint convex hulls by finding the upper and lower tangents: $O(n)$ time.
- The recurrence relation for the recursive step is:
  $$T(n) = 2T\left(\frac{n}{2}\right) + O(n)$$
- By Master Theorem, this recurrence yields $O(n \log n)$. Thus, the overall time complexity remains $O(n \log n)$.

---

### Q16. C++ Standard Template Library: std::sort Arguments

**Topic:** `C++`, `STL`  

Consider the following code snippet:
```cpp
std::sort(vec.begin(), vec.end(), cmp);
```

The third argument used here is:

- `Object`
- `Functors`
- `Variable`
- `Function`

#### Solution
**Answer: `Function` or `Functors`**

*Explanation:*
- The third argument of `std::sort` is a custom comparator. It can be a regular pointer to a **Function** or a **Functor** (an object of a class that overloads the function call operator `operator()`).
- Both are widely accepted. Depending on the specific code context, either option is correct.

---

### Q17. Java Programming: Exception Unreachability

**Topic:** `Java`, `Exception Handling`  

What will be the output of the following code snippet?

```java
import java.io.IOException;

class Test{
    public static void main(String[] args) {
        try{
            throw new IOException();
        }
        catch (Exception e) {//line 8
            System.out.println("Exception");
        }catch(IOException e){//line 10
            System.out.println("IOException");
        }
        finally{
            
        }
    }
}
```

- `IOException`
- `Exception`
- `Compile time exception in line 10, as the catch block is unreachable`
- `Exception IOException`

#### Solution
**Answer: `Compile time exception in line 10, as the catch block is unreachable`**

*Explanation:*
- In Java's exception handling, specific catch blocks must appear before general catch blocks.
- Since `IOException` is a subclass of `Exception`, the first catch block (`catch (Exception e)`) handles all exceptions.
- This makes the second catch block (`catch (IOException e)`) completely unreachable, which the Java compiler flags as a compile-time error.

---

### Q18. Databases: Query By Example

**Topic:** `DBMS`, `SQL`  

Functionally which of the following is similar to SQL?

- `All of the given options`
- `DBMS`
- `Report generator`
- `QBE`

#### Solution
**Answer: `QBE` (Query By Example)**

*Explanation:*
- **QBE** is a graphical database query language for relational databases that is functionally equivalent to SQL.
- A **DBMS** is the overall software system managing the database.
- A **Report generator** is a tool to format and present retrieved data.

---

### Q19. Distributed Systems: Concurrency Control

**Topic:** `Distributed Systems`, `Data Structures`  

In a distributed transaction system, consider that multiple processes concurrently manipulate a doubly linked list with operations: insert at the beginning, delete from the end, search and modify, and rotate by K. What design strategy will best ensure consistency and correctness while minimizing contention?

- `Centralized concurrency lock for synchronization`
- `Optimistic concurrency control with version numbers`
- `Distributed lock manager for coordination`
- `Decentralized locking mechanism for independent process locks`

#### Solution
**Answer: `Decentralized locking mechanism for independent process locks`**

*Explanation:*
- Since operations occur at different parts of the list (e.g., insertion at the beginning and deletion from the end are independent), using a **Decentralized locking mechanism** (like node-level locks or independent head and tail locks) minimizes lock contention.
- Centralized locks or centralized coordinators create bottlenecks (high contention).

---

### Q20. Databases: Foreign Key Constraint Violation

**Topic:** `DBMS`, `SQL`  

Given the data in the `EMPLOYEES` and `DEPARTMENTS` tables:

**EMPLOYEES table:**
| EMP_ID | EMP_NAME | DEPT_ID | MGR_ID | JOB_ID | SALARY |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | Smith | 20 | 120 | SA_REP | 4000 |
| 102 | Martin | 10 | 105 | CLERK | 2500 |
| 103 | Chris | 20 | 120 | IT ADMIN | 4200 |
| 104 | John | 30 | 108 | HR_CLERK | 2500 |
| 105 | Diana | 30 | 108 | IT_ADMIN | 5000 |
| 106 | Smith | 40 | 110 | AD_ASST | 3000 |
| 108 | Jennifer | 30 | 110 | HR_DIR | 6500 |
| 110 | Bob | 40 | NULL | EX_DIR | 8000 |
| 120 | Ravi | 20 | 110 | SI_DIR | 6500 |

**DEPARTMENTS table:**
| DEPARTMENT_ID | DEPARTMENT_NAME |
| :--- | :--- |
| 10 | Admin |
| 20 | Education |
| 30 | IT |
| 40 | Human Resources |

On the `EMPLOYEES` table, `EMP_ID` is the primary key and `DEPT_ID` is a foreign key referencing the `DEPARTMENT_ID` column of the `DEPARTMENTS` table.

What will happen when you execute the following DELETE statement?
```sql
DELETE FROM departments WHERE department_id=40;
```

- `The row with department ID 40 is deleted from the DEPARTMENTS table. Also, the rows with employee IDs 106 and 110 and the employees working under employee 110 are deleted from the EMPLOYEES table.`
- `The statement fails because child record exists in the EMPLOYEES table with department ID 40.`
- `Only the row with department ID 40 is deleted from the DEPARTMENTS table.`
- `The row with department ID 40 is deleted from the DEPARTMENTS table. Also, the rows with employee IDs 110 and 106 are deleted from the EMPLOYEES table.`

#### Solution
**Answer: `The statement fails because child record exists in the EMPLOYEES table with department ID 40.`**

*Explanation:*
- By default, relational databases restrict the deletion of rows in a parent table (here, `DEPARTMENTS`) if dependent rows exist in the child table (here, `EMPLOYEES` has rows for `EMP_ID` 106 and 110 with `DEPT_ID = 40`).
- Because there is no mention of `ON DELETE CASCADE`, this operation triggers a foreign key constraint violation, causing the statement to fail.

---

### Q21. Java Programming: Exception Hierarchy

**Topic:** `Java`, `Exception Handling`  

Which of the following is the parent class for `Exception` and `Error`?

- `None of the given options`
- `Throwable class`
- `Throw class`
- `Throws class`

#### Solution
**Answer: `Throwable class`**

*Explanation:*
In Java's exception hierarchy:
- `java.lang.Throwable` is the root superclass of all errors and exceptions.
- It has two direct subclasses: `java.lang.Exception` (for conditions that a reasonable application might want to catch) and `java.lang.Error` (for serious problems that a reasonable application should not try to catch).

---

### Q22. Artificial Intelligence: Methodologies

**Topic:** `Artificial Intelligence`, `Theoretical`  

Which of the following approaches can be used in Artificial Intelligence?
A. Machine Learning
B. Knowledge Representation
C. Probabilistic Reasoning
D. Searching

- `A, B and C`
- `A, B and D`
- `A and B`
- `A, B, C and D`

#### Solution
**Answer: `A, B, C and D`**

*Explanation:*
Artificial Intelligence employs a variety of methodologies depending on the problem domain:
- **Searching:** Used in pathfinding and games.
- **Knowledge Representation:** Used in symbolic AI and expert systems.
- **Probabilistic Reasoning:** Used in uncertain environments.
- **Machine Learning:** Used for learning patterns from data.
All of these are valid subfields/approaches in AI.

---

### Q23. Databases: 1NF Rules

**Topic:** `DBMS`, `Database Normalization`  

Which of the following statements about 1NF is/are correct?

A. When we use 1NF data redundancy increases, as there will be many columns with same data in multiple rows but each row as a whole will be unique.
B. In 1NF, each column in the table that is not part of the primary key must depend upon the entire concatenated key for its existence.
C. Any row must not have a column in which more than one value is saved.

- `B and C`
- `Only B`
- `Only A`
- `A, B and C`
- `A and B`

#### Solution
**Answer: `A and C` (Theoretically)**

*Explanation:*
- **Statement C** is the fundamental rule of 1NF (atomicity: no multi-valued attributes).
- **Statement A** is a common observation; when flattening multi-valued fields into 1NF, rows are duplicated, which repeats non-key attributes across multiple rows, temporarily increasing data redundancy (which is later resolved in 2NF and 3NF).
- **Statement B** is incorrect for 1NF; it actually describes the requirement for **Second Normal Form (2NF)** (elimination of partial dependencies).
- *Note:* In some test environments, Statement B and C or others might be grouped, but theoretically A and C are the correct properties of 1NF.

---

### Q24. SQL: Group By & Having Constraints

**Topic:** `SQL`, `Queries`  

Which of the given queries will display department ID and name and the number of employees working in each department that has fewer than 3 employees?

#### Solution
**Correct SQL Query:**
```sql
SELECT d.dept_id, d.dept_name, count(*) 
FROM department d, employees e 
WHERE d.dept_id = e.dept_id 
GROUP BY d.dept_id, d.dept_name 
HAVING count(*) < 3;
```

*Explanation:*
- To filter group results using aggregate functions like `count(*)`, you must use a `HAVING` clause, not a `WHERE` clause.
- Any non-aggregated column in the `SELECT` list (like `d.dept_id` and `d.dept_name`) must be included in the `GROUP BY` clause.

---

### Q25. Computer Architecture: Multiprocessor Systems

**Topic:** `Operating Systems`, `Hardware`  

Identify the statement which is true in case of Multi processor systems.

- `They are cost saving and will increase the throughput of the work completion`
- `If one processor fails then other processor will stop working till the problem is resolved.`
- `With multi processor system they can do work in such a way that it is very efficient when compared to normal processor systems.`
- `They are good to share the work among different systems and change the files from different systems at a time`

#### Solution
**Answer: `They are cost saving and will increase the throughput of the work completion`**

*Explanation:*
- **Increased Throughput:** By executing processes in parallel, more work gets done.
- **Cost Saving (Economy of Scale):** Multiprocessor systems share peripherals, storage, power supply, and memory, making them cheaper than a set of equivalent single-processor systems.
- **Reliability:** If one processor fails, the system continues running in a degraded state (graceful degradation), rather than stopping completely.

---

### Q26. File Systems: Allocation Strategies

**Topic:** `Operating Systems`, `File Systems`  

An organization contains a lot of files that are stored in the system. The files are stored in a continuous allocation strategy. Now the system is at block number 7, and it wants to know 9th block allocation on secondary storage in the system. Can you identify that secondary storage allocation using 7 and 9 blocks from the below Choices?

- `10`
- `15`
- `8`
- `11`

#### Solution
**Answer: `15`**

*Explanation:*
- In a **contiguous (continuous) file allocation** strategy, blocks are allocated sequentially.
- If the file starts at block index $7$ (this is the 1st block), the index of the $N$-th block is:
  $$\text{Index} = \text{Start Block} + N - 1 = 7 + 9 - 1 = 15$$

---

### Q27. Cloud Computing: IaaS Model

**Topic:** `Cloud Computing`, `IaaS`  

You can use the given layers in IAAS cloud model.
A. Hardware is the equipment (servers, network resources, storage)
B. Virtualization is the software that makes it possible to create multiple or different environments, based on the hardware.
C. The platform is a runtime environment in which software can run (.NET, PHP, Apache, etc.)
D. An application is a software for the customer

Which of these layers is in-house (managed by the customer)?

- `Application`
- `Hardware`
- `Virtualization`
- `Platform`
- `None of the given options`

#### Solution
**Answer: `Platform` and `Application`**

*Explanation:*
- In an **Infrastructure as a Service (IaaS)** model, the cloud provider manages the physical infrastructure (Hardware and Virtualization).
- The customer (in-house) manages the operating system, middleware, runtime environment (**Platform**), and the deployed **Application**.

---

### Q28. Object-Oriented Programming: Associations

**Topic:** `Software Engineering`, `UML`  

Following statements are true for which of the following:
a) It is a special form of Association where it represents Has-A relationship.
b) It is a unidirectional association i.e. a one-way relationship.
c) In it both the entries can survive individually which means ending one entity will not affect the other entity.

- `composition`
- `aggregation`
- `association`
- `Specialization`

#### Solution
**Answer: `aggregation`**

*Explanation:*
- Both **aggregation** and **composition** are specific forms of association representing a "Has-A" relationship.
- In **composition**, there is a strong ownership relationship; the child entity cannot survive if the parent is destroyed.
- In **aggregation**, the ownership is weak; child entities can survive independently of the parent container (e.g., a "Teacher" can survive if the "Department" is closed).

---

### Q29. Object-Oriented Programming: Polymorphism

**Topic:** `Object-Oriented Programming`  

Which of the following is not a type of Static Polymorphism?

- `Method Overriding`
- `Method Overloading`
- `Constructor Overloading`
- `Operator Overloading`

#### Solution
**Answer: `Method Overriding`**

*Explanation:*
- **Method Overriding** is a type of dynamic (runtime) polymorphism where the call is resolved during execution based on the actual object type.
- **Overloading** (methods, constructors, operators) is a type of static (compile-time) polymorphism resolved by the compiler based on the function signature.

---

### Q30. Cloud Computing: Characteristics

**Topic:** `Cloud Computing`  

A popular cloud provides the given characteristics. Which of the following observations regarding the given characteristics is correct?
A. Ubiquitous network access
B. Location-independent resource pooling
C. On-demand self-service

- `On-demand self-service cloud services are controlled and monitored by the cloud provider. This is crucial for billing, access control, resource optimization, capacity planning, and other tasks.`
- `All the above options are correctly defined.`
- `Ubiquitous network access means the cloud provider's capabilities are available over the network and can be accessed through standard mechanisms by both thick and thin clients.`
- `Resource pooling allows the cloud provider to serve its consumers via a multi-tenant model. Physical and virtual resources are assigned and reassigned according to consumer demand.`

#### Solution
**Correct Observations:**
- `Ubiquitous network access means the cloud provider's capabilities are available over the network and can be accessed through standard mechanisms by both thick and thin clients.`
- `Resource pooling allows the cloud provider to serve its consumers via a multi-tenant model. Physical and virtual resources are assigned and reassigned according to consumer demand.`

*Explanation:*
- The first option incorrectly defines *Measured Service* (controlled, monitored, metered for billing) as "On-demand self-service" (which is the ability to provision resources automatically without human interaction with the provider). Therefore, the "All the above options are correctly defined" option is false.

---

### Q31. Machine Learning: Applications

**Topic:** `Machine Learning`, `Theoretical`  

Which of the following problems are best suited for Machine learning?

1. Determining the horizontal range of a projectile
2. Automatic translation of text from one language to another
3. Distinguishing between prime and composite numbers
4. Detecting potential anomaly in an aircraft engine

- `1, 2 and 4`
- `1, 2, 3 and 4`
- `2 and 4`
- `2, 3 and 4`

#### Solution
**Answer: `2 and 4`**

*Explanation:*
- **Machine translation** (2) and **anomaly detection** (4) are complex problems requiring pattern recognition from unstructured/large data, making them perfect fits for machine learning.
- **Projectile range** (1) and **prime number checking** (3) are solved using exact mathematical equations and deterministic algorithms, making ML unnecessary.
