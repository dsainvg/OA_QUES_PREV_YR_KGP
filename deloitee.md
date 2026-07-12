# Interview Questions

*Generated from: R:/DSA/Company wise prep resource/deloitee*
*Total questions: 18*

---

## Table of Contents

1. [Theoretical Questions](#theoretical-questions)
2. [MCQs](#mcqs)

---

## Theoretical Questions

### Q1. HTML5 optgroup tag

**Topic:** `HTML5`, `Web Development`  

Complete the following HTML5 markup to group related options in a dropdown list as shown:
```html
<label for="workshop">Select Workshop:</label>
<select id="workshop" name="workshop">
  <______ label="Technology">
    <option value="webdev">Web Development</option>
    <option value="appdev">Machine Learning</option>
  </______>
  <______ label="Sports">
    <option value="tennis">Badminton</option>
    <option value="swimming">Swimming</option>
  </______>
</select>
```

#### Answer
The correct tag is `<optgroup>`.
```html
<label for="workshop">Select Workshop:</label>
<select id="workshop" name="workshop">
  <optgroup label="Technology">
    <option value="webdev">Web Development</option>
    <option value="appdev">Machine Learning</option>
  </optgroup>
  <optgroup label="Sports">
    <option value="tennis">Badminton</option>
    <option value="swimming">Swimming</option>
  </optgroup>
</select>
```

---

## MCQs

### Q2. MS Word Find & Replace Access

**Topic:** `MS Office`  

Where can you access the 'Find and Replace' feature to search for specific text in Microsoft Word?

**Options:**
- A) Edit menu
- B) Format menu
- C) Insert menu
- D) View menu

**Correct Answer:** A) Edit menu *(In classic versions of Word. In modern versions, it is accessed via the Home tab in the Editing group or using `Ctrl + H`).*

---

### Q3. HTML5 Logical Sections

**Topic:** `HTML5`  

Which one of the given options is the most appropriate tag in HTML5 to divide the document into logical document sections?

**Options:**
- A) `<section></section>`
- B) `<span></span>`
- C) `<div></div>`
- D) `<frame></frame>`

**Correct Answer:** A) `<section></section>`

---

### Q4. Spyware Protection

**Topic:** `Networking and Cyber Security`  

Which one of the given options is used to protect the system from Spyware and other similar programs?

**Options:**
- A) Windows Active Icons
- B) Windows Defender
- C) Windows Firewall
- D) Windows Spyware

**Correct Answer:** B) Windows Defender

---

### Q5. C++ Exception Handling

**Topic:** `C++`, `Exception Handling`  

What is the output of the following C++ program?
```cpp
#include <iostream>
using namespace std;

void Q(int x) {
    try {
        if (x < 0)
            throw x + 5;
        else
            throw x;
    } catch (int x) {
        cout << " A " << x;
    }
}

int main() {
    Q(-2);
    cout << " C ";
    return 0;
}
```

**Options:**
- A) `A -3 C`
- B) `A 3 C`
- C) `A -4 C`
- D) `A 4 C`

**Correct Answer:** B) `A 3 C`  
**Explanation:**  
- `Q(-2)` passes `x = -2` to the function.
- Since `-2 < 0`, it throws `x + 5` which is `-2 + 5 = 3`.
- The exception is caught by the `catch (int x)` block, printing ` A 3`.
- After returning to `main()`, it prints ` C `, yielding ` A 3 C `.

---

### Q6. SQL INNER JOIN Tuples

**Topic:** `SQL`, `Relational Algebra`  

Given the following tables:
**Active_Players:**
| shirt_no | player_name | match_played |
|---|---|---|
| 99 | ABC | 86 |
| 89 | CDE | 98 |
| 79 | EFG | 100 |

**Retired_Players:**
| shirt_no | player_name | match_played |
|---|---|---|
| 28 | XYZ | 120 |
| 38 | PQR | 135 |

How many tuples will be displayed in the output, if the following query is executed?
```sql
SELECT Active_Players.*, Retired_Players.* FROM Active_Players INNER JOIN Retired_Players;
```

**Options:**
- A) 6
- B) 3
- C) 8
- D) 2

**Correct Answer:** A) 6  
**Explanation:** An `INNER JOIN` without an `ON` condition functions as a Cartesian product (Cross Join). Therefore, the number of resulting rows is $3 \text{ players} \times 2 \text{ players} = 6$.

---

### Q7. CSS Background Blend Mode

**Topic:** `HTML5`, `CSS`  

To adjust the blend mode for each background layer of an element, which of the following CSS properties is used?

**Options:**
- A) `background-collapse` property
- B) `background-transform` property
- C) `background-blend-mode` property
- D) `background-origin` property

**Correct Answer:** C) `background-blend-mode` property

---

### Q8. SQL Retrieving First and Last Record

**Topic:** `SQL`  

Consider the table `STUDENTS` given below:
| ROLLNO | NAME | MARKS |
|---|---|---|
| 57 | Ramgopal | 49 |
| 53 | Rakesh | 89 |
| 47 | Ananda | 59 |
| 73 | Pradeep | 68 |
| 78 | Santosh | 93 |
| 97 | Laxmi | 73 |
| 63 | Prashant | 55 |
| 76 | Sukhdev | 47 |

Which of the query/queries given below will retrieve the first and last record from the `STUDENTS` table?
- I) `SELECT * FROM (SELECT ROWNUM R, STUDENTS.* FROM STUDENTS) WHERE R=1 OR R=COUNT(*);`
- II) `SELECT ROWNUM R, STUDENTS.* FROM STUDENTS WHERE R=1 OR R=(SELECT COUNT(*) FROM STUDENTS);`
- III) `SELECT * FROM (SELECT ROWNUM R, STUDENTS.* FROM STUDENTS) WHERE R=1 OR R=(SELECT COUNT(*) FROM STUDENTS);`

**Options:**
- A) All (I), (II) and (III)
- B) Only (III)
- C) Only (II) and (III)
- D) None of the above

**Correct Answer:** B) Only (III)  
**Explanation:**  
- (I) is invalid because aggregate functions like `COUNT(*)` cannot be evaluated in the `WHERE` clause without subqueries.
- (II) is invalid because `ROWNUM` cannot be queried with values $>1$ directly in the same block (`ROWNUM=COUNT(*)` will fail).
- (III) is correct because it assigns a fixed alias `R` to `ROWNUM` inside the subquery and filters it externally.

---

### Q9. Distinct Count SQL Queries

**Topic:** `SQL`  

Given the table `STUDENT`:
| Stud_id | Name | Subject | Marks |
|---|---|---|---|
| 101 | Rajesh | Maths | 89 |
| 102 | Ram | Sanskrit | 78 |
| 103 | Vikranth | English | 98 |
| 104 | Jyothi | Physics | 56 |
| 105 | Meena | Sanskrit | 90 |
| 106 | Preeti | Chemistry | 65 |
| 107 | Anil | Sanskrit | 90 |

Which of the queries given below will give the same output?
- I) `SELECT COUNT(DISTINCT SUBJECT) FROM STUDENT;`
- II) `SELECT COUNT(DISTINCT(SUBJECT)) FROM STUDENT;`
- III) `SELECT DISTINCT(COUNT(*)) FROM STUDENT;`
- IV) `SELECT COUNT(*) FROM (SELECT DISTINCT(Subject) from STUDENT) std;`

**Options:**
- A) Only (I) and (IV)
- B) Only (III) and (IV)
- C) Only (II) and (III)
- D) Only (I) and (II)

**Correct Answer:** A) Only (I) and (IV) *(Note: II also yields the same result syntactically, but Option A is the standard answer provided).*

---

### Q10. Java Scanner Token Parsing

**Topic:** `Java`, `IO Streams`  

What is the output of the following Java program?
```java
try {
    FileWriter fw = new FileWriter("Test.txt");
    fw.write("check = 1, test = 5");
    fw.close();
    FileReader fr = new FileReader("Test.txt");
    Scanner s_obj = new Scanner(fr);
    while(s_obj.hasNext()) {
        System.out.print(s_obj.next() + ",");
    }
} catch(IOException e) {
    System.out.println("I/O exception is raised");
}
```

**Options:**
- A) `I/O exception is raised`
- B) `check,=,1, test,=,5,`
- C) `check,=,1,,test,=,5,`
- D) `check =1, test =5,`

**Correct Answer:** C) `check,=,1,,test,=,5,`  
**Explanation:** `Scanner.next()` splits the input string by whitespace. 
- Token 1: `check` -> prints `check,`
- Token 2: `=` -> prints `=,`
- Token 3: `1,` -> prints `1,,`
- Token 4: `test` -> prints `test,`
- Token 5: `=` -> prints `=,`
- Token 6: `5` -> prints `5,`

---

### Q11. MS Excel Date Year Formula

**Topic:** `MS Office`  

Which formula can one use to derive the year from a given Date in column A and print in column B?

**Options:**
- A) `=TEXT(A2,"YYYY")`
- B) `=YEAR(A2, "YYYY")`
- C) `=DATE(A2,YEAR(A2))`
- D) `=TEXT(A2,YEAR(A2))`

**Correct Answer:** A) `=TEXT(A2,"YYYY")` *(Note: Excel's `=YEAR(A2)` is correct, but `=YEAR(A2, "YYYY")` is syntactically invalid because YEAR accepts only one argument).*

---

### Q12. Cloud Computing Multi-tenancy

**Topic:** `Cloud Computing`  

What does the term "Multi-tenancy" mean in Cloud Computing?

**Options:**
- A) ability to increase or decrease infrastructure resources abruptly depending on demand.
- B) the capacity of an organization to operate effectively with a growing or increased workload.
- C) the act of dividing up workloads among multiple computing resources.
- D) the same computing resources are being used by various clients of the cloud provider.

**Correct Answer:** D) the same computing resources are being used by various clients of the cloud provider.

---

### Q13. SQL JOIN syntax

**Topic:** `SQL`  

Which of the queries given in options will display the Student name and DeptNo from the tables `Student` and `Deptinfo`?

**Options:**
- A) `SELECT sname,DeptNo FROM stud INNER JOIN deptinfo stud.sno=deptinfo.sno ORDER BY stud.sname;`
- B) `SELECT stud.sname,deptinfo.DeptNo FROM stud INNER JOIN deptinfo ON stud.sno=deptinfo.sno ORDER BY stud.sname;`
- C) `SELECT stud.sname,deptinfo.DeptNo FROM stud OUTER JOIN deptinfo ON stud.sno=deptinfo.sno ORDER BY stud.sname;`
- D) `SELECT stud.sname,deptinfo.DeptNo FROM stud Where deptinfo ON stud.sno=deptinfo.sno ORDER BY stud.sname;`

**Correct Answer:** B) `SELECT stud.sname,deptinfo.DeptNo FROM stud INNER JOIN deptinfo ON stud.sno=deptinfo.sno ORDER BY stud.sname;`

---

### Q14. C++ Post-Increment & Static Variables

**Topic:** `C`  

What will be the output of the C program given below?
```c
main() {
    auto int p = 4 - 2;
    p++;
    static int s;
    s = (p = ++s) + p;
    printf("%d", s++);
}
```

**Options:**
- A) 3
- B) 4
- C) 2
- D) 1

**Correct Answer:** C) 2  
**Explanation:**  
- `p` is initialized to $4 - 2 = 2$, then `p++` makes it 3.
- `static int s` defaults to 0.
- `++s` increments `s` to 1.
- `p = ++s` assigns 1 to `p`.
- `s = (p) + p` calculates $1 + 1 = 2$.
- `printf("%d", s++)` prints the current value of `s` (2) and then post-increments `s` to 3.

---

### Q15. SQL Alter Table

**Topic:** `SQL`  

Which of the queries given below will add `type` column to `Cake` table?

**Options:**
- A) `Alter table Cake add column type varchar2(30);`
- B) `Modify table Cake add column type varchar2(30);`
- C) `Alter table Cake add type varchar2(30);`
- D) `Modify table Cake add type varchar2(30);`

**Correct Answer:** C) `Alter table Cake add type varchar2(30);` *(Standard Oracle SQL syntax).*

---

### Q16. Cloud Reliability vs Scalability

**Topic:** `Cloud Computing`  

"My cloud cannot expand based on demand, but it can perform intended functions without interruptions." Under this scenario, my cloud is:
- i) Scalable
- ii) Reliable

**Options:**
- A) Both i and ii
- B) Only i
- C) Only ii
- D) Neither i Nor ii

**Correct Answer:** C) Only ii

---

### Q17. HTML5 Session Storage Access

**Topic:** `HTML5`, `Javascript`  

How can you create and access a `sessionStorage` Object in HTML5?

**Options:**
- A) `<script type="text/javascript"> sessionStorage.name="DGTECH"; document.write(sessionStorage.name); </script>`
- B) `<script type="text/javascript"> sessionStorage.name="DGTECH"; document.read(sessionStorage.name); </script>`
- C) `<script type="text/javascript"> session.name="DGTECH"; document.write(sessionStorage.name); </script>`
- D) `<script type="text/javascript"> sessionStorage.name="DGTECH"; document.write(sessionSession.name); </script>`

**Correct Answer:** A

---

### Q18. Cloud Task Division

**Topic:** `Cloud Computing`  

The method of dividing computer tasks and workloads is known as ______.

**Options:**
- A) Hypervisor
- B) Load balancing
- C) Elasticity
- D) Scalability

**Correct Answer:** B) Load balancing
