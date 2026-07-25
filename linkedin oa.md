# Interview Questions
*Total questions: 3*

---

## Table of Contents
1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. Optimal Meeting Effectiveness

**Topic:** `greedy`, `sorting`  

**Question Wording:**  
A product manager has to organize $n$ meetings with different people. Meeting with each person results in an increase or decrease in the effectiveness index of the manager. The manager wants to organize the meetings such that the index remains positive for as many meetings as possible. Find the maximum number of meetings for which the effectiveness index is positive. The index at the beginning is 0.

Note: After the meetings begin, the index must remain above 0 to be positive.

**Function Description:**  
Complete the function `maxMeetings` in the editor.

`maxMeetings` has the following parameter:
* `int effectiveness[n]`: the increase or decrease effectiveness for each meeting.

**Returns:**  
* `int`: the maximum possible number of meetings while maintaining a positive index.

**Constraints:**  
* $1 \le n \le 10^5$
* $-10^9 \le effectiveness[i] \le 10^9$

**Example:**  
* **Input:** `effectiveness = [1, -20, 3, -2]`
* **Output:** `3`
* **Explanation:** One optimal meeting order is `[3, -2, 1, -20]`. The index is positive for the first three meetings, after which it is 3 - 2 + 1 - 20 = -18. So, the answer is 3. There is no way to have 4 meetings with a positive index.

**Sample Case 0:**  
* **Input:** `effectiveness = [-3, 0, 2, 1]`
* **Output:** `3`
* **Explanation:** One optimal rearrangement is `[2, 0, 1, -3]`.

**Python Solution:**  
```python
def maxMeetings(effectiveness):
    # Separate effectiveness values
    positives = [x for x in effectiveness if x > 0]
    zeros = [x for x in effectiveness if x == 0]
    negatives = [x for x in effectiveness if x < 0]
    
    # If there are no positive values, we can never start with a positive index (starts at 0)
    if not positives:
        return 0
        
    # Start by greedily using all non-negative numbers
    current_sum = sum(positives)
    count = len(positives) + len(zeros)
    
    # Sort negative numbers in descending order (least negative/closest to 0 first)
    negatives.sort(reverse=True)
    
    # Add negative values as long as the cumulative index remains strictly positive
    for val in negatives:
        if current_sum + val > 0:
            current_sum += val
            count += 1
        else:
            break
            
    return count
```

---

### Q2. Metro Land Festival Location

**Topic:** `math`, `greedy`, `median`  

**Question Wording:**  
Metro Land is a country located on a 2D plane. They are planning a summer festival for everyone in the country and would like to minimize the overall cost of travel for their citizens. Costs of travel are calculated as follows:
* A city is located at coordinates $(x, y)$.
* The festival is located at coordinates $(a, b)$.
* Cost of travel from a city to the festival = $|x - a| + |y - b|$ per person.

The festival can be held at any integral location in Metro Land. Find the optimal location for the festival, defined as the location with the minimal total travel cost assuming all people attend. Return the total travel cost for all citizens to attend the festival.

**Function Description:**  
Complete the function `minimizeCost` in the editor.

`minimizeCost` has the following parameters:
* `int numPeople[n]`: each `numPeople[i]` denotes the number of people in city $i$.
* `int x[n]`: each `x[i]` denotes the x coordinate of city $i$.
* `int y[n]`: each `y[i]` denotes the y coordinate of city $i$.

**Returns:**  
* `int`: the minimum cost of getting all the people to an optimal festival location.

**Constraints:**  
* $1 \le n \le 10^3$
* $1 \le x[i], y[i] \le 10^4$
* $1 \le numPeople[i] \le 50$

**Example:**  
* **Input:**
  * `numPeople = [1, 2]`
  * `x = [1, 3]`
  * `y = [1, 3]`
* **Output:** `4`
* **Explanation:** There is 1 person in City 0 located at $(1, 1)$ and 2 people in City 1 at $(3, 3)$. If the location for the festival is at $(3, 3)$:
  * Cost from City 0: $1 \times (|1 - 3| + |1 - 3|) = 4$
  * Cost from City 1: $2 \times (|3 - 3| + |3 - 3|) = 0$
  * Total travel cost = 4.

**Sample Case 0:**  
* **Input:**
  * `numPeople = [1, 1]`
  * `x = [1, 3]`
  * `y = [1, 1]`
* **Output:** `2`
* **Explanation:** City 0 is at $(1, 1)$ with 1 person, and City 1 is at $(3, 1)$ with 1 person. The optimal festival locations are $(1, 1)$, $(1, 2)$, or $(1, 3)$, each resulting in a total travel cost of 2.

**Python Solution:**  
```python
def minimizeCost(numPeople, x, y):
    total_w = sum(numPeople)
    
    # Find the weighted median for x coordinate
    x_weighted = sorted(zip(x, numPeople))
    cum_w = 0
    best_x = x_weighted[0][0]
    for coord, weight in x_weighted:
        cum_w += weight
        if cum_w >= (total_w + 1) // 2:
            best_x = coord
            break
            
    # Find the weighted median for y coordinate
    y_weighted = sorted(zip(y, numPeople))
    cum_w = 0
    best_y = y_weighted[0][0]
    for coord, weight in y_weighted:
        cum_w += weight
        if cum_w >= (total_w + 1) // 2:
            best_y = coord
            break
            
    # Compute total cost at the optimal location (best_x, best_y)
    total_cost = 0
    for i in range(len(numPeople)):
        total_cost += numPeople[i] * (abs(x[i] - best_x) + abs(y[i] - best_y))
        
    return total_cost
```

---

### Q3. Round-Robin Load Balancer

**Topic:** `heap`, `priority-queue`, `simulation`  

**Question Wording:**  
Implement a prototype of a round-robin load-balancing algorithm.

There are $n$ servers indexed from 1 to $n$, and $m$ requests to be processed. The $i$-th request arrives at time `arrival[i]` and takes `burstTime[i]` time to execute. The load balancer assigns the request to the available server with the minimum index. A server that is assigned the $i$-th request is unavailable from time `arrival[i]` to `arrival[i] + burstTime[i]`. At `arrival[i] + burstTime[i]`, the server is available to serve a new request.

Given $n$, `arrival`, and `burstTime` for each request, find the index of the server that executes it. If no server is available at the time, the request is dropped, and -1 is reported. If multiple requests arrive at the same time, the one with the smaller index is assigned first.

**Function Description:**  
Complete the function `getServerIndex` in the editor.

`getServerIndex` has the following parameters:
* `int n`: the number of servers.
* `int arrival[m]`: the arrival time of requests.
* `int burstTime[m]`: the burst time of requests.

**Returns:**  
* `int[m]`: the index of the servers the requests are assigned to, or -1 if no server is available.

**Constraints:**  
* $1 \le n \le 10^5$
* $1 \le m \le 10^5$
* $1 \le arrival[i] \le 10^9$
* $1 \le burstTime[i] \le 10^9$

**Example:**  
* **Input:**
  * `n = 3`
  * `arrival = [2, 4, 1, 8, 9]`
  * `burstTime = [7, 9, 2, 4, 5]`
* **Output:** `[2, 1, 1, 3, 2]`
* **Explanation:**  
  * Request 3 (arrival=1, burst=2) arrives first. Server 1 is chosen. Busy until 3.
  * Request 1 (arrival=2, burst=7) arrives next. Server 2 is chosen. Busy until 9.
  * Request 2 (arrival=4, burst=9) arrives. Server 1 is available (free at 3). Server 1 chosen. Busy until 13.
  * Request 4 (arrival=8, burst=4) arrives. Server 3 is chosen. Busy until 12.
  * Request 5 (arrival=9, burst=5) arrives. Server 2 is available (free at 9). Server 2 chosen. Busy until 14.

**Sample Case 0:**  
* **Input:**
  * `n = 4`
  * `arrival = [3, 5, 1, 6, 8]`
  * `burstTime = [9, 2, 10, 4, 5]`
* **Output:** `[2, 3, 1, 4, 3]`

**Python Solution:**  
```python
import heapq

def getServerIndex(n, arrival, burstTime):
    m = len(arrival)
    result = [-1] * m
    
    # Store requests with their original index to preserve output ordering:
    # (arrival_time, original_index, burst_time)
    requests = []
    for i in range(m):
        requests.append((arrival[i], i, burstTime[i]))
        
    # Sort requests chronologically. Tie-breaking by original index
    requests.sort()
    
    # Min-heap of available servers (initially 1 to n)
    available_servers = list(range(1, n + 1))
    heapq.heapify(available_servers)
    
    # Min-heap of busy servers: stores tuples of (free_time, server_index)
    busy_servers = []
    
    for arr_time, orig_idx, burst in requests:
        # Free up all servers that finished processing at or before current arrival time
        while busy_servers and busy_servers[0][0] <= arr_time:
            _, server_idx = heapq.heappop(busy_servers)
            heapq.heappush(available_servers, server_idx)
            
        # Assign to the available server with the minimum index
        if available_servers:
            server_idx = heapq.heappop(available_servers)
            result[orig_idx] = server_idx
            heapq.heappush(busy_servers, (arr_time + burst, server_idx))
        else:
            result[orig_idx] = -1
            
    return result
```
