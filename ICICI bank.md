# Interview Questions
*Total questions: 56*

---

## Table of Contents
- [Coding Questions](#coding-questions)
- [SQL & Database Questions](#sql--database-questions)
- [Quantitative Aptitude & Statistics](#quantitative-aptitude--statistics)
- [Theoretical & Computer Networks Questions](#theoretical--computer-networks-questions)
- [Software Engineering & Machine Learning](#software-engineering--machine-learning)

---

## Coding Questions

### Q1. NumPy Array Split and Dimension Expansion

**Topic:** `Python`, `NumPy`, `Arrays`  

What is the output of the following Python code?

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
result = np.split(arr, 2)
result = np.expand_dims(result, axis=0)
print(result)
```

**Answer/Solution:**
```python
[[[1 2 3]
  [4 5 6]]]
```
*Explanation:* `np.split(arr, 2)` splits the 1D array into two arrays of length 3: `[array([1, 2, 3]), array([4, 5, 6])]`. When passed to `np.expand_dims(..., axis=0)`, a new dimension is added at the first axis, wrapping it in an outer list.

---

### Q2. File I/O Truncation and Appending

**Topic:** `Python`, `File I/O`  

What is the output of the following Python code?

```python
with open('example.txt', 'w') as f:
    f.write('HackerEarth\n')

with open('example.txt', 'w') as f:
    f.write('Hacker_Earth\n')

with open('example.txt', 'a') as f:
    f.write('Programming\n')

with open('example.txt') as rt:
    d = rt.read()
    print(d)
```

**Answer/Solution:**
```
Hacker_Earth
Programming
```
*Explanation:* 
1. The first block opens `example.txt` in write mode (`'w'`), writing `"HackerEarth\n"`.
2. The second block opens `example.txt` in write mode (`'w'`) again, which truncates (clears) the file contents and writes `"Hacker_Earth\n"`.
3. The third block opens it in append mode (`'a'`), adding `"Programming\n"`.
4. Reading the file prints the remaining contents.

---

### Q3. Object Reference and Attribute Modification

**Topic:** `Python`, `OOP`, `Object References`  

What is the output of the following Python code?

*Scenario 1:*
```python
class Number:
    def __init__(self, number):
        self.number = number
        
    def addition(self, number2):
        return self.number * number2.number
        
    def display(self):
        return self.number
        
    def update(self, num):
        self.number = num

num1 = Number(10)
num2 = num1
num2.update(15)
num2 = Number(5)
print(num2.addition(num1))
```

*Scenario 2:*
```python
# (Alternate values found in screenshots)
num1 = Number(20)
num2 = num1
num2.update(10)
num2 = Number(5)
print(num2.addition(num1))
```

**Answer/Solution:**
- **Scenario 1 Output:** `75`
- **Scenario 2 Output:** `50`

*Explanation:* 
1. `num2 = num1` copies the reference of the first `Number` object. Both variables point to the same instance.
2. `num2.update(X)` changes the instance's `number` value to `X` (15 or 10). Both variables reflect this change.
3. `num2 = Number(5)` reassigns `num2` to a new instance with a value of `5`, while `num1` continues to point to the modified instance.
4. Calling `num2.addition(num1)` computes `5 * X`, yielding `75` or `50`.

---

### Q4. OpenCV Contour Drawing and Color Formats

**Topic:** `Python`, `OpenCV`, `Computer Vision`  

What is the output of the following Python code?

```python
import cv2

image = cv2.imread('image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('Image', image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**Answer/Solution:**
**Display the original image with contours drawn in green.**
*Explanation:* OpenCV uses BGR (Blue-Green-Red) color mapping, so the tuple `(0, 255, 0)` targets the green channel.

---

### Q5. Text Preprocessing: Tokenization and Stopwords Removal

**Topic:** `Python`, `NLP`, `NLTK`  

What is the output of the following Python code?

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Baseball is the most popular sport of USA. It is played between 2 teams of 9 players each."
tokens = word_tokenize(text.lower())
filtered_tokens = [token for token in tokens if token.isalpha() and token not in stopwords.words('english')]

print(filtered_tokens)
```

**Answer/Solution:**
```python
['baseball', 'popular', 'sport', 'usa', 'played', 'teams', 'players']
```
*Explanation:* NLTK's English stopword list contains terms like `is`, `the`, `most`, `of`, `it`, `between`, and `each`. Punctuation and numeric characters like `2` and `9` are removed by the `.isalpha()` check.

---

### Q6. Text Lemmatization with WordNetLemmatizer

**Topic:** `Python`, `NLP`, `NLTK`  

What is the output of the following Python code?

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

text = "I am running"
tokens = word_tokenize(text.lower())
lemmatized_tokens = [WordNetLemmatizer().lemmatize(token, pos='v') for token in tokens]

print(lemmatized_tokens)
```

**Answer/Solution:**
```python
['i', 'be', 'run']
```
*Explanation:* Setting the Part-of-Speech (`pos`) tag to `'v'` (verb) lemmatizes `"am"` to its root form `"be"`, and `"running"` to its base form `"run"`.

---

### Q7. Custom Class Decorator with Attribute Access Tracing

**Topic:** `Python`, `Decorators`, `OOP`  

What is the output of the following Python code?

```python
class Tracer:
    def __init__(self, aClass):
        self.aClass = aClass
        
    def __call__(self, *args):
        self.wrapped = self.aClass(*args)
        return self
        
    def __getattr__(self, attrname):
        print("Trace: " + attrname)
        return getattr(self.wrapped, attrname)

@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)

food = Spam()
food.display()
```

**Answer/Solution:**
```
Trace: display
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
```
*Explanation:* 
- `@Tracer` wraps the class `Spam`. Calling `Spam()` executes `Tracer.__call__`, returning the decorator instance containing the wrapped instance.
- Accessing `food.display` intercepts via `__getattr__`, prints `"Trace: display"`, and delegates to `Spam.display()`.

---

### Q8. Dictionary Key Lookup using get() method

**Topic:** `Python`, `Dictionaries`  

What is the output of the following Python code?

```python
d = {'fwa': 81, 269: '729', 'wds': '392', '629': '957'}
print(d.get('926'))
```

**Answer/Solution:**
`None`
*Explanation:* Unlike direct bracket access `d['926']` which throws a `KeyError`, the `.get()` method returns `None` (or a specified default value) when a key is not found.

---

### Q9. Custom Tuple Value Frequency Count

**Topic:** `Python`, `Tuple`  

What is the output of the following Python code?

```python
def My_Tuple(min1, t):
    min = 0
    for i in min1:
        if (i == t):
            min = min + 1
    return min

min1 = (15, 11, 5, 6, 8, 2, 4)
add = 5
add1 = 1
add2 = 7
print(My_Tuple(min1, add))
print(My_Tuple(min1, add1))
```

**Answer/Solution:**
```
1
0
```
*Explanation:* The function counts occurrences of `t` in `min1`. `5` occurs once, and `1` occurs zero times.

---

### Q10. Two-Sum Index Search using Hashing

**Topic:** `Python`, `Algorithms`, `Hash Map`  

What is the output of the following Python code?

```python
nums = [2, 7, 11, 15]
target = 9
d = {}
for i in range(len(nums)):
    if (target - nums[i] in d):
        print([d[target - nums[i]], i])
    else:
        d[nums[i]] = i
```

**Answer/Solution:**
```python
[0, 1]
```
*Explanation:* 
- At `i = 0`, `nums[0] = 2` is added to dict `d` as `d[2] = 0`.
- At `i = 1`, `nums[1] = 7`. The complement `9 - 7 = 2` is already in `d`. The program prints `[d[2], 1]` which is `[0, 1]`.

---

### Q11. Tuple Iteration and Element Access

**Topic:** `Python`, `Iterators`  

What is the output of the following Python code?

```python
t = ("Python", "language", "test")
iter_t = iter(t)
print(next(iter_t), end=' ')
print(next(iter_t), end=' ')
print(next(iter_t))
```

**Answer/Solution:**
```
Python language test
```

---

### Q12. Iterator Conversion to Tuple

**Topic:** `Python`, `Iterators`  

What is the output of the following Python code?

```python
L = ["HackerEarth", "Python", "Test"]
iteraL = iter(L)
next(iteraL)
print(tuple(next(iteraL)))
```

**Answer/Solution:**
```python
('P', 'y', 't', 'h', 'o', 'n')
```
*Explanation:* `next(iteraL)` advances past `"HackerEarth"`. The second `next(iteraL)` returns `"Python"`, which `tuple()` converts to a sequence of individual character elements.

---

### Q13. Abstract Classes and Class Instantiation in Python

**Topic:** `Python`, `OOP`, `Abstract Classes`  

What is the output of the following Python code?

```python
from abc import ABCMeta, abstractmethod
class MetaClass(metaclass=ABCMeta):
    def __init__(self):
        self.s = 842
    @abstractmethod
    def demo(num): pass
    
class DemoClass(MetaClass):
    def __init__(num):
        num.n = 824
        pass
        
class SuperDemoClass(DemoClass):
    def demo(num):
        super().__init__()
        print(num.n)
        
s = SuperDemoClass()
s.demo()
```

**Answer/Solution:**
```
824
```
*Explanation:* `SuperDemoClass` is instantiated since it implements the abstract method `demo`. When `s.demo()` is called, `super().__init__()` triggers `DemoClass.__init__(s)`, setting the attribute `n = 824`, which is printed.

---

### Q14. Dynamic Attributes in Python Classes

**Topic:** `Python`, `OOP`, `Attributes`  

What is the output of the following Python code?

```python
class student:
    def __init__(self, regd_no, grades):
        self.regd_no = regd_no
        self.grades = grades
    def display(self):
        print("Regd no : ", self.regd_no, ", Grade: ", self.grades)
        
student1 = student(42, 'S')
student1.age = 7
student2 = student(33, 'S')
student2.age = 9
print(hasattr(student2, 'age'))
```

**Answer/Solution:**
`True`

---

### Q15. Multi-level Class Inheritance and Method Overriding

**Topic:** `Python`, `OOP`, `Inheritance`  

What is the output of the following Python code?

```python
class MainClass:
    def s1(self):
        return 20
        
class Super(MainClass):
    def s1(self):
        return 30
    def s2(self):
        return 40
        
class Sub(Super):
    def s2(self):
        return 20
        
var = MainClass()
var2 = Super()
var3 = Sub()
print(var.s1() + var2.s2() + var3.s2())
```

**Answer/Solution:**
`80`
*Explanation:* 
- `var.s1()` resolves to `MainClass.s1()` $\rightarrow 20$.
- `var2.s2()` resolves to `Super.s2()` $\rightarrow 40$.
- `var3.s2()` resolves to `Sub.s2()` $\rightarrow 20$.
- Sum = $20 + 40 + 20 = 80$.

---

### Q16. Pandas Offset Operations with MonthBegin and WeekOfMonth

**Topic:** `Python`, `Pandas`, `DateTime`  

What is the output of the following Python code?

```python
from pandas.tseries.offsets import MonthBegin
from pandas.tseries.offsets import WeekOfMonth
from datetime import datetime

offset1 = MonthBegin(n=4)
offset2 = WeekOfMonth(week=3, weekday=1)
dt = datetime(2022, 8, 22)

new_dt = dt + offset1 + offset2
print(new_dt)
```

**Answer/Solution:**
```
2022-12-27 00:00:00
```
*Explanation:* 
1. `dt + MonthBegin(4)` moves the date forward to the 4th MonthBegin. Since Aug 22 is not a MonthBegin, `MonthBegin(1)` is Sep 1. Thus, `MonthBegin(4)` lands on Dec 1, 2022.
2. `offset2 = WeekOfMonth(week=3, weekday=1)` specifies the 4th Tuesday of the month (since `week` is 0-indexed and `weekday=1` is Tuesday).
3. The 4th Tuesday of December 2022 is December 27, 2022.

---

### Q17. Exception Raising in Custom Classes

**Topic:** `Python`, `Exception Handling`  

Analyze the structure and describe the behavior of the following Python code.

```python
class Hello(Exception):
    def __init__(this, arg):
        this.message = arg + " was not allowed in python! "

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def addition(self, a, b):
        a = a + b
        raise Hello("Addition")
        return a
        
    def multiplication(self, a, b):
        a = a * b
        raise Hello("multiplication")
        return a

obj = A(5, 10)
```

**Answer/Solution:**
Calling either `obj.addition()` or `obj.multiplication()` will raise a custom exception of type `Hello` with the respective messages:
- `"Addition was not allowed in python! "`
- `"multiplication was not allowed in python! "`

---

### Q18. C++ Try/Catch and Exception Handling

**Topic:** `C++`, `Exception Handling`  

What is the output of the following C++ code given the input `2 6`?

```cpp
#include <iostream>
using namespace std;
int main(){
    int var1=40, var2=80;
    try{
        cin>>var1>>var2;
        if(var2==0){
            throw var2;
        }
        else{
            cout << var2 % var1;
        }
    }
    catch(exception e){
        e.what();
    }
    return 0;
}
```

**Answer/Solution:**
`0`
*Explanation:* `var1` reads `2` and `var2` reads `6`. Since `var2 != 0`, the `else` block executes, printing `6 % 2` which evaluates to `0`.

---

### Q19. C++ Dynamic Memory Allocation and nothrow

**Topic:** `C++`, `Memory Allocation`  

What is the output of the following C++ code?

```cpp
#include <iostream>
using namespace std;
int main ()
{
    int n = 5;
    int *q = new(nothrow) int[n];
    if (!q)
        cout << "Allocation of memory failed\n";
    else
    {
        for (int i = 0; i < n; i++)
            q[i] = i+1;
        for (int i = 0; i < n; i++)
            cout << q[i] << " ";
    }
    delete[] q;
    return 0;
}
```

**Answer/Solution:**
```
1 2 3 4 5 
```

---

### Q20. Java Variable Shadowing and super Keyword

**Topic:** `Java`, `OOP`, `Inheritance`  

What is the output of the following Java code?

```java
public class Main {
    public static void main(String[] args) {
        B b = new B();
        b.display();
    }
}
class A {
    int x = 5;
}
class B extends A {
    int x = 10;
    void display() {
        System.out.println(x + " " + super.x);
    }
}
```

**Answer/Solution:**
```
10 5
```
*Explanation:* `x` refers to the variable defined in the local scope of class `B` (`10`), while `super.x` forces the compiler to resolve to the variable `x` defined in the base class `A` (`5`).

---

### Q21. Java Abstract Classes and Constructor Call Chains

**Topic:** `Java`, `OOP`, `Abstract Classes`  

What is the output of the following Java code?

```java
class Hackerearth
{
    public static void main(String []args)
    {
        hack2 h = new hack2();
        h.hack_method();
        h.hack_method2();
    }
}

abstract class hack1
{
    hack1()
    {
        System.out.println("hello");
    }
    abstract void hack_method();
    void hack_method2()
    {
        System.out.println("hi");
    }
}

class hack2 extends hack1
{
    void hack_method()
    {
        System.out.println("hackerearth");
    }
}
```

**Answer/Solution:**
```
hello
hackerearth
hi
```
*Explanation:* Instantiating `hack2` triggers a call to its base constructor `hack1()`, which prints `"hello"`. Then `h.hack_method()` calls the overridden method in `hack2` to print `"hackerearth"`, and `h.hack_method2()` calls the inherited method from `hack1` to print `"hi"`.

---

### Q22. Java Single Inheritance Resolution

**Topic:** `Java`, `OOP`, `Inheritance`  

Observe the following Java code and select the appropriate modification to get the output `Good`.

```java
public class Main extends Hack2{
    public static void main(String args[]){
        Main obj = new Main();
        obj.print1();
    }
}
class Hack1{
    void print1(){
        System.out.println("Good");
    }
}
class Hack2{
    void print2(){
        System.out.println("Morning");
    }
}
```

**Answer/Solution:**
**Replace `class Main extends Hack2` with `class Main extends Hack1`.**
*Explanation:* Java does not support multiple class inheritance (so extending both is syntax error). To call the `print1()` method, `Main` must directly inherit from `Hack1`.

---

### Q23. Java Lambda Expression and Functional Interface

**Topic:** `Java`, `Lambdas`  

What is the output of the following Java code?

```java
interface Worker {
    void doWork(int x);
}

public class Main {
    public static void main(String[] args) {
        Worker worker = x -> {
            for (int i = 0; i < x; i++) {
                System.out.print(i + " ");
            }
        };
        worker.doWork(5);
    }
}
```

**Answer/Solution:**
```
0 1 2 3 4 
```

---

### Q24. Java Enum Class Custom Methods and Fields

**Topic:** `Java`, `Enum`  

What is the output of the following Java code?

```java
enum Currency {
    USD(1.18), EUR(1.0), JPY(132.17);
    
    private double rate;
    
    Currency(double rate) {
        this.rate = rate;
    }
    
    double convertToUSD(double amount) {
        return amount * rate;
    }
}

public class Main {
    public static void main(String[] args) {
        Currency currency = Currency.EUR;
        System.out.println(currency.convertToUSD(50));
    }
}
```

**Answer/Solution:**
`50.0`
*Explanation:* Since `Currency.EUR` is initialized with a `rate` of `1.0`, `50 * 1.0` returns the `double` value `50.0`.

---

### Q25. Go Interface Implementation

**Topic:** `Go`, `Interfaces`  

What is the output of the following Go code?

```go
package main

import "fmt"

type I interface {
    M()
}

type T struct {
    S string
}

func (t T) M() {
    fmt.Println(t.S)
}

func main() {
    var i I = T{"hello"}
    i.M()
}
```

**Answer/Solution:**
`hello`

---

### Q26. Android ListView Adapter Binding

**Topic:** `Android`, `Java`, `UI Components`  

Which option correctly replaces the placeholder line `/**Line A**/` to bind the adapter to the ListView?

```java
public class MainActivity extends Activity {
    ListView simpleList;
    String animalList[] = {"Lion", "Tiger", "Monkey", "Elephant", "Dog", "Cat", "Camel"};
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        simpleList = (ListView) findViewById(R.id.simpleListView);
        
        ArrayAdapter<String> arrayAdapter = new ArrayAdapter<String>(this, R.layout.activity_list_view, R.id.textView, animalList);
        
        /**Line A**/
    }
}
```

**Answer/Solution:**
```java
simpleList.setAdapter(arrayAdapter);
```

---

## SQL & Database Questions

### Q27. SQL Inner Join with Aggregation

**Topic:** `SQL`, `Joins`  

You are given two tables:

**Table: Brand**
| BID | BName |
|---|---|
| 10 | Asus |
| 11 | Vivo |
| 12 | MI |
| 13 | Moto |

**Table: Item**
| PID | PName | Price | CID |
|---|---|---|---|
| 301 | PC | 60000 | 12 |
| 302 | Mouse | 5000 | 11 |
| 303 | Mobile | 10000 | 13 |
| 304 | Printer | 25000 | 10 |

Write and evaluate the query to fetch the average price of items under each brand name.

**Answer/Solution:**
```sql
SELECT AVG(Price) AS AvgPrice, Brand.BName
FROM Item INNER JOIN Brand
ON Item.CID = Brand.BID
GROUP BY Brand.BName;
```

**Output:**
| BName | AvgPrice |
|---|---|
| Asus | 25000 |
| Vivo | 5000 |
| MI | 60000 |
| Moto | 10000 |

*(Note: The raw source screenshot contains a syntax error because it misses the `GROUP BY Brand.BName` clause).*

---

### Q28. Oracle DATE format-mask

**Topic:** `Oracle`, `SQL`  

In Oracle SQL, what format-mask is used to format `sysdate` to output `WEDNESDAY,SEPTEMBER 16 2002 06:11PM`?

**Answer/Solution:**
`DAY,MONTH DD YYYY HH:MIAM`

---

### Q29. SQL Server Storage Selection: varchar vs nvarchar

**Topic:** `SQL Server`, `Database Design`  

Bob is working as a data warehouse developer in an IT company that maintains massive data. He chooses to use `varchar` in the destination database instead of the source data type of `nvarchar`. Identify the correct reason why he chose that.

**Answer/Solution:**
**To improve data performance.**
*Explanation:* `varchar` stores non-Unicode characters using 1 byte per character, whereas `nvarchar` stores Unicode using 2 bytes. For datasets containing mostly English characters, `varchar` saves 50% storage space, fits more records per data page, minimizes database memory usage, and decreases disk I/O, yielding superior query performance.

---

### Q30. SQL Server Database Size Limits in Express Edition

**Topic:** `SQL Server`, `Database Administration`  

What is the maximum size of a single database allowed in Microsoft SQL Server Express edition?

**Answer/Solution:**
`10 GB`
*(Note: Prior to SQL Server 2008 R2, the limit was 4 GB).*

---

### Q31. PySpark DESCRIBE DATABASE Output Metadata

**Topic:** `PySpark`, `Databases`  

Which details are returned by the `DESCRIBE DATABASE` statement in PySpark?

**Answer/Solution:**
**Database name and Database location** (and optional description/properties).

---

### Q32. SQL Server Checkpoint Process

**Topic:** `SQL Server`, `Database Administration`  

What is the primary purpose of the Checkpoint Process in SQL Server?

**Answer/Solution:**
**To reduce recovery time in the event of unexpected shutdown.**
*Explanation:* Checkpoints write dirty data and log pages from the buffer cache onto the physical disk, reducing the duration of transaction recovery during database startup.

---

## Quantitative Aptitude & Statistics

### Q33. Basic Ratio Division Problem

**Topic:** `Mathematics`, `Ratios`  

In a city, there is one school. This school has 23,400 students. If the ratio of students studying in Mathematics, Physics, and Chemistry is 8:3:7, what is the approximate number of students studying Mathematics and Physics?

**Answer/Solution:**
`14300`
*Calculation:*
- Total ratio units = $8 + 3 + 7 = 18$
- Total students = $23,400$
- Value of 1 unit = $23,400 / 18 = 1,300$
- Mathematics + Physics units = $8 + 3 = 11$
- Total students = $11 \times 1,300 = 14,300$

---

### Q34. Mean and Standard Deviation of a Dataset

**Topic:** `Statistics`, `Mean`, `Standard Deviation`  

Find the mean and population standard deviation for the following dataset: `[14, 29, 34, 48, 59, 67]`.

**Answer/Solution:**
- **Mean:** `41.83`
- **Standard Deviation:** `18.10`

*Calculation:*
- Mean $\mu = \frac{14+29+34+48+59+67}{6} = \frac{251}{6} \approx 41.83$
- Population Variance $\sigma^2 = \frac{\sum (x_i - \mu)^2}{n} \approx \frac{1966.83}{6} \approx 327.81$
- Population Standard Deviation $\sigma \approx \sqrt{327.81} \approx 18.10$

---

### Q35. Mean and Standard Deviation of a Binomial Distribution

**Topic:** `Statistics`, `Binomial Distribution`  

In a population, nine out of ten people are getting affected by a virus. Obtain the mean and standard deviation of the number of people getting affected out of 150 people.

**Answer/Solution:**
- **Mean:** `135`
- **Standard Deviation:** `3.674`

*Calculation:*
- Trials $n = 150$, Probability $p = 0.9$, $q = 1 - p = 0.1$
- Mean $\mu = n \cdot p = 150 \times 0.9 = 135$
- Standard Deviation $\sigma = \sqrt{n \cdot p \cdot q} = \sqrt{150 \times 0.9 \times 0.1} = \sqrt{13.5} \approx 3.674$

---

### Q36. Pie Chart Difference Problem

**Topic:** `Mathematics`, `Data Interpretation`  

A pie chart mentions the distribution of 34,000 total students who took courses in different fields:
- B.Ed: `18%`
- B.Tech: `30%`
- Pharmacy: `7%`
- MBA: `13%`
- MBBS: `6%`
- B.Sc: `26%`

Find the difference between B.Sc students and B.Ed students.

**Answer/Solution:**
`2720`
*Calculation:*
- Percentage difference = $26\% - 18\% = 8\%$
- Number of students = $8\% \text{ of } 34,000 = 0.08 \times 34,000 = 2,720$

---

## Theoretical & Computer Networks Questions

### Q37. PySpark Frequent Itemset Mining Module

**Topic:** `PySpark`, `Machine Learning`  

Which of the following modules will you use to mine frequent itemsets in PySpark?

**Answer/Solution:**
`fpm` (Frequent Pattern Mining, under `pyspark.ml.fpm`).

---

### Q38. Tkinter Custom Shape Creation

**Topic:** `Python`, `GUI`, `Tkinter`  

John is developing a GUI application using Tkinter in Python. He wants to create a canvas item with a custom shape, such as a star or a polygon. Which method should he use?

**Answer/Solution:**
`create_polygon()`

---

### Q39. JSP Base Class

**Topic:** `Java`, `JSP`  

In JSP, which of the following is the base class of all classes?

**Answer/Solution:**
`java.lang.Object`

---

### Q40. R Poisson Distribution Inverse CDF Function

**Topic:** `R Programming`, `Probability`  

In R, which function do you use to evaluate the inverse cumulative distribution function for the Poisson distribution?

**Answer/Solution:**
`qpois`

---

### Q41. C++ Pure Virtual Functions

**Topic:** `C++`, `OOP`  

Which of the following statements about pure virtual functions is true?

**Answer/Solution:**
**They must be overridden in a concrete derived class.**
*Explanation:* Declaring a pure virtual function (`= 0`) makes a class abstract, meaning it cannot be instantiated directly. Derived classes must override this method to become concrete classes.

---

### Q42. Transformer Models Adaptability Statements

**Topic:** `Machine Learning`, `Deep Learning`  

Evaluate the following statements regarding the adaptability of Transformer models:
1. Transformer models are restricted to natural language processing tasks and cannot be adapted for other sequential data types.
2. The architecture of Transformers allows for transfer learning, where a model trained on one task can be adapted for another task with minimal changes.
3. The self-attention mechanism in Transformers is more computationally efficient than RNNs for long sequences.

Which statements are correct?

**Answer/Solution:**
**Only 2 is correct** (or **2 and 3 are correct**, depending on interpretation).
- Statement 1 is False (Transformers are widely used in Computer Vision, Audio, etc.).
- Statement 2 is True (transfer learning/fine-tuning is standard).
- Statement 3 is technically False in terms of computational operation complexity ($O(n^2 \cdot d)$ vs $O(n \cdot d^2)$) for very long sequences, but True in terms of training time due to parallel processing capabilities.

---

### Q43. NLP Semantic vs Syntactic Analysis

**Topic:** `Machine Learning`, `NLP`  

In Machine Learning, you are working on natural language processing. Which analysis is used to understand the meaning and interpretation of words, signs, and sentence structure?

**Answer/Solution:**
**Semantic analysis**
*Explanation:* Syntactic analysis focuses on grammar and syntax rules, while semantic analysis focuses on meaning.

---

### Q44. Python Iterator Advantages

**Topic:** `Python`, `Iterators`  

In Python 3, which of the following represents the advantages of using iterators:
1. Enables you to produce cleaner code.
2. Has the ability to work with infinite sequences.
3. Saves memory because, at a time, only one element is stored in the memory unlike in lists or tuples.

**Answer/Solution:**
**All of these**

---

### Q45. RTL Data Path and Clock Period

**Topic:** `Computer Architecture`, `RTL`  

In Register-Transfer Level (RTL) design, you are given a conceptual data path:
`[Register q output] -> [Routing network] -> [Functional unit] -> [Routing network] -> [Register d input]`.
What is the relationship between the clock period ($T_{clk}$) and the propagation delay ($T_{dp}$)?

**Answer/Solution:**
$$T_{clk} \ge T_{cq} + T_{dp} + T_{setup}$$
where:
- $T_{cq}$ is the clock-to-q propagation delay of the source register.
- $T_{dp}$ is the maximum propagation delay of the combinational circuit data path.
- $T_{setup}$ is the setup time of the destination register.
The maximum clock rate is $f_{clk, max} = \frac{1}{T_{clk, min}}$.

---

### Q46. Linux DNS Command for Forward and Reverse Lookups

**Topic:** `Linux`, `Computer Networks`  

Which Linux command is helpful for finding the IP address of a domain and also finding the hostname by providing the IP address?

**Answer/Solution:**
`nslookup`

---

### Q47. Confluence Collaboration and Page Templates

**Topic:** `Software Engineering`, `Project Management`  

What is one way a product manager can use Confluence to gather feedback and share work in progress with the team?

**Answer/Solution:**
**Creating a page template** that includes background information, company details, and problem observations.

---

### Q48. IPv4 Logical Address Size

**Topic:** `Computer Networks`  

What is the logical address size of IPv4?

**Answer/Solution:**
`32-bit`

---

### Q49. WPA2 Security Protocol Target

**Topic:** `Computer Networks`, `Security`  

Which of the following does the WPA2 protocol secure?

**Answer/Solution:**
`Wi-Fi`

---

### Q50. Dynamic DNS Purpose

**Topic:** `Computer Networks`, `DNS`  

Which system allows customers to refresh their DNS entry automatically as their IP address changes?

**Answer/Solution:**
**Dynamic DNS (DDNS)**

---

### Q51. Subnet Network Address Calculation

**Topic:** `Computer Networks`  

Given a host with the IP address `172.16.66.0/21`, what is the network address (Subnet ID)?

**Answer/Solution:**
`172.16.64.0`
*Calculation:*
- Subnet mask for `/21` is `255.255.248.0` (21 bits are 1s: `11111111.11111111.11111000.00000000`).
- Performing bitwise AND on the third octet: `66 (01000010)` AND `248 (11111000)` = `64 (01000000)`.
- Network Address = `172.16.64.0`.

---

### Q52. ICMP Packet Validity Statements

**Topic:** `Computer Networks`, `Protocols`  

Evaluate the following statements regarding ICMP packets:
1. ICMP ensures datagram conveyance.
2. ICMP can provide hosts with information about network problems.
3. ICMP is encapsulated inside IP datagrams.
4. ICMP is encapsulated inside UDP datagrams.

Which statements are correct?

**Answer/Solution:**
**2 and 3**
- Statement 2 is True (it reports errors/network issues).
- Statement 3 is True (ICMP is encapsulated inside IP datagrams with protocol field set to 1).
- Statement 1 is False (ICMP does not ensure delivery).
- Statement 4 is False (not encapsulated in UDP).

---

### Q53. Unified Diagnostic Services (UDS) Request Types

**Topic:** `Automotive Protocols`, `UDS`  

In Unified Diagnostic Services (UDS) over CAN, what are the two main types of request addressing modes sent by the diagnostic tester?

**Answer/Solution:**
**Physical UDS (one-to-one)** and **Functional UDS (one-to-many)**.

---

## Software Engineering & Machine Learning

### Q54. SAP Coding Guidelines

**Topic:** `Software Engineering`, `ABAP`  

Identify the correct coding guidelines for SAP development from the following:
A. Follow proper naming conventions for variables, functions, and classes.
B. Minimize the use of global variables and prefer local variables.
C. Avoid using hard-coded values and utilize constants or config parameters.
D. Use inline comments extensively for every line of code.
E. Implement error and exception handling mechanisms.
F. Write lengthy and complex code for better performance.

**Answer/Solution:**
**A, B, C, and E**
- D is incorrect (over-commenting every line harms readability).
- F is incorrect (simple, modular, and maintainable code is preferred).

---

### Q55. Agile Scrum Sprint Goal SMART Criteria

**Topic:** `Software Engineering`, `Scrum`  

What should a project manager do to ensure the team sets and understands the sprint goal and how success will be measured?

**Answer/Solution:**
Ensure that the sprint goal is **specific, measurable, attainable, relevant, and time-bound (SMART)**.

---

### Q56. Agile User Story Definition

**Topic:** `Software Engineering`, `Scrum`  

Which of the following best describes a user story?

**Answer/Solution:**
**A high-level description of a feature from an end-user perspective.**
