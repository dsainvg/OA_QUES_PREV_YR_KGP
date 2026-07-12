# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. String Program (minRemoval)

**Topic:** `strings`, `greedy`  

Alice is working on a system that processes text inputs from users. One of the requirements is that the text must not contain the substring `"ppp"` - three consecutive `'p'` characters. If this substring appears, the text is rejected.

To make the input text acceptable, Alice needs to remove characters in such a way that the substring `"ppp"` does not exist.

Your task is to help Alice find and return an integer value representing the minimum number of characters that need to be removed from the text to meet this requirement.

**Note:**
* The string only contains lowercase alphabetic characters.
* You can delete characters in random positions (not necessarily consecutive).

#### Input Specification
* `input1`: A string `S`, representing the text inputs from users.

#### Output Specification
* Return an integer value representing the minimum number of characters that need to be removed from the text to meet the above requirement.

#### Example 1
* **Input:** `pppiii`
* **Output:** `1`
* **Explanation:** Here the string `S` is `"pppiii"`. Since the string contains three consecutive p's or the substring `'ppp'`, if the first character is removed from the string, then it becomes `'ppiii'`. Now after removing 1 character, no such substring is there in the input text, so it will be accepted. Hence, `1` is returned as the output.

#### Example 2
* **Input:** `pppp`
* **Output:** `2`
* **Explanation:** Here the string `S` is `"pppp"`. Since the string contains three consecutive p's or the substring `'ppp'`, if we remove the first character from the string then it becomes `'ppp'`. Again, it contains substring `'ppp'`, so again the first character is removed. Now the string becomes `'pp'`. After removing 2 characters from string, no such substring is there in the input text, so it will be accepted. Hence, `2` is returned as the output.

#### Python 3 Solution
```python
def minRemoval(input1: str) -> int:
    ans = 0
    count = 0
    for char in input1:
        if char == 'p':
            count += 1
        else:
            if count >= 3:
                ans += count - 2
            count = 0
    if count >= 3:
        ans += count - 2
    return ans
```

#### Java Solution
```java
public class UserMainCode {
    public int minRemoval(String input1) {
        int ans = 0;
        int count = 0;
        for (int i = 0; i < input1.length(); i++) {
            char c = input1.charAt(i);
            if (c == 'p') {
                count++;
            } else {
                if (count >= 3) {
                    ans += (count - 2);
                }
                count = 0;
            }
        }
        if (count >= 3) {
            ans += (count - 2);
        }
        return ans;
    }
}
```

---

### Q2. Color Sandwich (colorSandwich)

**Topic:** `strings`, `parsing`  

Sam is a cook, and he has colored breads and stuffing with which he had made some sandwiches. A sandwich can be made by keeping multiple or no stuffing between two same-colored breads like: `qabcq` (where `abc` represents stuffing and `q` represents coloured bread). The sandwiches are placed one over the other represented by a string `S` where each character depicts either bread or the stuffing. Your task is to find and return a string value representing the colour of the breads used in all sandwiches.

#### Input Specification
* `input1`: A string `S` representing the sandwiches.

#### Output Specification
* Return a string value representing the colour of the breads used in all sandwiches.

#### Example 1
* **Input:** `qczcquu`
* **Output:** `qu`
* **Explanation:**
  * The first sandwich is `qczcq`: where bread is `q`, and the stuffing is `czc`.
  * The second sandwich is `uu`: where bread is `u` and no stuffing.
  The breads used for the sandwiches are `qu`. Hence `qu` is returned as the output.

#### Example 2
* **Input:** `yy`
* **Output:** `y`
* **Explanation:**
  * Here, the given order of sandwiches is `yy` which has only one sandwich where bread is `y` and no stuffing. Hence `y` is returned as the output.

#### Python 3 Solution
```python
def colorSandwich(input1: str) -> str:
    ans = []
    i = 0
    n = len(input1)
    while i < n:
        bread = input1[i]
        j = input1.find(bread, i + 1)
        if j == -1:
            break
        ans.append(bread)
        i = j + 1
    return "".join(ans)

# Alternative: If unique bread colors are required, use:
# def colorSandwichUnique(input1: str) -> str:
#     ans = []
#     seen = set()
#     i = 0
#     n = len(input1)
#     while i < n:
#         bread = input1[i]
#         j = input1.find(bread, i + 1)
#         if j == -1:
#             break
#         if bread not in seen:
#             ans.append(bread)
#             seen.add(bread)
#         i = j + 1
#     return "".join(ans)
```

#### Java Solution
```java
public class UserMainCode {
    public String colorSandwich(String input1) {
        StringBuilder ans = new StringBuilder();
        int i = 0;
        int n = input1.length();
        while (i < n) {
            char bread = input1.charAt(i);
            int j = input1.indexOf(bread, i + 1);
            if (j == -1) {
                break;
            }
            ans.append(bread);
            i = j + 1;
        }
        return ans.toString();
    }
}
```

---
