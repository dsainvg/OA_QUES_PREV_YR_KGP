*Total questions: 2*

---

## Table of Contents
- [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Bachata Dance Pairs

**Topic:** `Greedy`, `Sorting`, `Arrays`

Bachata is a style of social dance from the Dominican Republic which is now danced all over the world. Dancers are paired as couples to perform the dance, and to look visually appealing, the pair is usually made of people with similar height.

Alice runs a dance academy, and for her new Bachata batch, a lot of dancers have registered. She now has to pair them into couples, and decides that a couple can differ in height by no more than 2 inches. Any person who can't fit into such a couple has to leave. Alice wants to give higher priority to the participants with smaller height to form a couple. If more than one choice is available to form a couple, then the priority is given to participants arriving earlier i.e. 'first come first serve' principle is applied.

Write a program to help Alice form the pairs, given the number of participants $n$, and the name and height of each participant. Assume a unique solution exists.

Read the input from STDIN and print the output to STDOUT. Do not write arbitrary strings while reading the input or while printing, as these contribute to the standard output.

#### Constraints:
- $1 \le n \le 10000$
- $20 \le \text{height}[n] \le 200$
- Participant names are always unique.

#### Input Format:
- First line contains an integer $n$, determining the total number of participants.
- Each of the next $n$ lines contains the name and height (separated by a single whitespace) of one participant.

#### Output Format:
- Each line of output contains the two names (separated by a single white space) which form one pair.
- The pairs are printed in ascending order of heights i.e. within a pair the shorter participant's name comes first, and between two pairs, the pair with shorter first participant is printed first.
- If the heights are same, use "first come first serve" approach.

#### Sample Input 1:
```
4
Sam 60
Dan 52
Bob 54
Art 61
```

#### Sample Output 1:
```
Dan Bob
Sam Art
```

#### Explanation 1:
- Height difference of Dan and Bob: 54 and 52, which is 2.
- Height difference of Sam and Art: 61 and 60, which is 1.
- So the four of them can be coupled in the given way.
- Since Dan's height is lower than Bob, Dan is written first and then Bob. Similarly Sam is written before Art.
- Since Dan's height is lower than Sam, Dan's pair is printed first and then Sam's.

#### Sample Input 2:
```
7
Dan 60
Bob 52
Sam 54
Art 70
Kim 61
Jack 61
Jim 53
```

#### Sample Output 2:
```
Bob Jim
Dan Kim
```

#### Explanation 2:
- Art does not have anyone close in height, so Art is left out.
- Amongst Bob, Sam, and Jim, any two can form a pair. Since higher priority is given to shorter participants, Bob & Jim make a pair. Sam is left out as there is no one else for him to pair with.
- Amongst Dan, Kim, and Jack, any two can form a pair. Since higher priority is given to shorter participants, Dan is selected. Since Kim and Jack have the same height, the participant who arrived earlier is given priority (first come first serve approach). Hence Kim is selected to pair with Dan. Jack is left out as there is no one else for him to pair with.

```python
def perfectPair(name, height, n):
    # Convert height to integer list
    height = [int(h) for h in height]
    
    # Store each participant with original index to handle first-come first-served
    participants = [(name[i], height[i], i) for i in range(n)]
    
    # Sort primarily by height, secondarily by original arrival index
    participants.sort(key=lambda x: (x[1], x[2]))
    
    used = set()
    pairs = []
    
    # Greedily match from shortest to tallest
    for i in range(n):
        p_name, p_height, p_idx = participants[i]
        if p_idx in used:
            continue
        
        for j in range(i + 1, n):
            q_name, q_height, q_idx = participants[j]
            if q_idx in used:
                continue
            
            # Since list is sorted, if height difference exceeds 2, no more valid pairs can be formed for this p
            if q_height - p_height > 2:
                break
                
            # Form the pair
            used.add(p_idx)
            used.add(q_idx)
            # Since p is processed first and sorted by (height, index), p_name is the shorter/earlier participant
            pairs.append((p_name, q_name, p_height, p_idx))
            break
            
    # Sort pairs for output:
    # 1. Shorter first participant height
    # 2. First come first serve if heights are the same (original index of first participant)
    pairs.sort(key=lambda x: (x[2], x[3]))
    
    for p_name, q_name, _, _ in pairs:
        print(f"{p_name} {q_name}")
```

---

### Q2. Same Number Pairs

**Topic:** `Arrays`, `Hash Table`, `Counting`

Write a program to count the number of pairs of the same number that can be formed by using the elements of a given array `arr`. If any number is repeated an odd number of times, then the last remaining number will not be considered as a pair. Also, if there is no pair available in the given array, print `"No pairs found"`.

Read the input from STDIN and print the output to STDOUT. Do not print arbitrary strings anywhere in the program, as these contribute to the standard output and test cases will fail.

#### Constraints:
- $1 \le N \le 100,000$
- $1 \le \text{arr}[i] \le 10^9$
- If any number is repeated an odd number of times, then the remaining last number will not be considered as a pair.

#### Input Format:
- The first line of input should consist of an integer $N$.
- The second input line should consist of $N$ integers separated by a single white space.

#### Output Format:
- The only output line should display the counts of the pair of the same numbers in the given array. And, if there is no pair available in the given array, print `"No pairs found"`.

#### Sample Input 1:
```
11
6 1 6 5 1 2 8 2 9 2 4
```

#### Sample Output 1:
```
3
```

#### Explanation 1:
- The given array elements are `6, 1, 6, 5, 1, 2, 8, 2, 9, 2, 4`.
- The available pairs are `(6,6)`, `(1,1)`, and `(2,2)`. Though `2` is repeated 3 times, it is counted as 1 pair and the 3rd `2` remains uncounted. Therefore, it will print `3` as output.

#### Sample Input 2:
```
13
567 206 40 195 647 81 40 339 40 797 40
```

#### Sample Output 2:
```
2
```

#### Explanation 2:
- The given array elements are `567, 206, 40, 195, 647, 81, 40, 339, 40, 797, 40`.
- Among all elements, `40` appears 4 times in the given list and two pairs of `(40,40)` will be formed. Therefore, it will print `2` as output.

```python
def solve(n, arr):
    # arr is an array of n integers.
    from collections import Counter
    counts = Counter(arr)
    
    pair_count = 0
    for num, count_val in counts.items():
        pair_count += count_val // 2
        
    if pair_count == 0:
        return "No pairs found"
    return pair_count
```
