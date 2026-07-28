# Interview Questions

*Total questions: 2*

---

## Table of Contents

1. [Coding Questions](#coding-questions)

---

## Coding Questions

### Q1. URL Query String Builder

`[Latest]`

**Topic:** `Implementation`, `String Parsing`, `URL Encoding`

#### Description
Your web application needs to build URL query strings from user filters and search parameters. Different pages manually construct these strings, leading to bugs: spaces encoded inconsistently, parameters in random order making caching difficult, and nested objects causing crashes.

Implement the `build_query` function that takes a `params` dictionary and returns a properly formatted URL query string.
- Sort parameters alphabetically by key.
- Percent-encode keys and values using standard URL encoding (specifically with `+` for spaces).
- Join key-value pairs with `&`.
- Skip any parameter with a `None` value.
- Convert booleans to lowercase string representations (`"true"` or `"false"`).
- Raise a `ValueError` if any key is not a string, or if any value is a nested structure (list, dict).

#### Function Parameters
- `params`: A dictionary mapping string keys to values of type `str`, `int`, `float`, `bool`, or `None`.

#### Returns
- `str`: The URL query string with parameters sorted by key, percent-encoded, and joined with `&`. Returns an empty string if no valid parameters remain.
- Raises `ValueError` if any key is not a string or if any value is a nested structure (`list`, `dict`).

#### Constraints
- $0 \le \text{number of parameters} \le 1500$
- $1 \le \text{length of each key} \le 64$ characters
- $0 \le \text{length of each stringified value} \le 2000$ characters (before encoding)
- Total JSON input size $\le 100,000$ characters

#### Sample Cases

**Sample Case 0**
- **Input:**
  - `dict = {"q": "hello world", "lang": "en", "page": 2}`
- **Output:**
  `lang=en&page=2&q=hello+world`
- **Explanation:**
  Parameters are sorted alphabetically by key (`lang`, `page`, `q`). The space in `"hello world"` is encoded as `+`, and pairs are joined with `&`.

**Sample Case 1**
- **Input:**
  - `dict = {"meta": {"a": 1}}`
- **Output:**
  `ValueError`
- **Explanation:**
  The value for `"meta"` is a nested dictionary, which is not allowed. A `ValueError` must be raised.

#### Python Solution
```python
import urllib.parse
import json
import sys

def build_query(params: dict) -> str:
    res = []
    for k in sorted(params.keys()):
        if not isinstance(k, str):
            raise ValueError("Keys must be strings")
        v = params[k]
        if isinstance(v, (dict, list)):
            raise ValueError("Nested structures are not allowed")
        if v is None:
            continue
        if isinstance(v, bool):
            v_str = "true" if v else "false"
        elif isinstance(v, (int, float, str)):
            v_str = str(v)
        else:
            raise ValueError("Unsupported parameter value type")
        res.append(f"{urllib.parse.quote_plus(k)}={urllib.parse.quote_plus(v_str)}")
    return "&".join(res)
```

---

### Q2. Markdown Checklist Parser

`[Latest]`

**Topic:** `Implementation`, `Class Design`, `String Parsing`

#### Description
A development team uses markdown checklists to track project tasks across code reviews, deployments, and sprints. The team needs a tool to programmatically update task status and generate progress reports.

Build a class `MarkdownChecklist` that parses markdown checklist items, updates task statuses, queries individual task states, and calculates completion metrics. The system should handle duplicate task names and ignore malformed entries.

#### Class Methods
- `__init__(lines)`: Initialize with a list of markdown lines containing checklist items.
- `markDone(taskText)`: Mark the first pending task with the given name as completed. Raise a `ValueError` if not found or already completed.
- `markUndone(taskText)`: Mark the first completed task with the given name as pending. Raise a `ValueError` if not found or already pending.
- `getStatus(taskText)`: Return the status of the first matching task (`"completed"` or `"pending"`). Raise a `ValueError` if not found.
- `getCompletedCount()`: Return the total number of completed tasks.
- `getPendingCount()`: Return the total number of pending tasks.

#### Input Parsing Details
- Valid list items start with `-` or `*` (with optional leading whitespace), followed by a space, followed by a status marker `[ ]`, `[x]`, or `[X]`, followed by a space, and then the task name.
- Task names are case-sensitive.
- Malformed lines should be ignored.

#### Constraints
- $1 \le n, q \le 10^3$ where $n$ is the number of markdown lines and $q$ is the number of operations.
- Task names are case-sensitive.
- Markers `[x]` and `[X]` are case-insensitive (both represent completed status).

#### Sample Cases

**Sample Case 0**
- **Input:**
  ```
  5
  - [ ] Write tests
  - [x] Update docs
  * [ ] Deploy app
  * [ ] Review PR
  - [X] Send report
  7
  getPendingCount
  getCompletedCount
  markDone Review PR
  getCompletedCount
  getStatus Write tests
  markUndone Update docs
  getCompletedCount
  ```
- **Output:**
  ```
  3
  2
  3
  pending
  2
  ```
- **Explanation:**
  - Initially, 3 tasks are pending (`"Write tests"`, `"Deploy app"`, `"Review PR"`) and 2 are completed (`"Update docs"`, `"Send report"`).
  - Calling `getPendingCount` returns `3`.
  - Calling `getCompletedCount` returns `2`.
  - Marking `"Review PR"` as done increases completed count to `3`.
  - Checking `"Write tests"` returns `"pending"`.
  - Marking `"Update docs"` undone reduces completed count to `2`.

**Sample Case 1**
- **Input:**
  ```
  3
  - [ ] Write code
  - [ ] Review PR
  - [x] Deploy
  3
  markDone Write code
  getCompletedCount
  getPendingCount
  ```
- **Output:**
  ```
  2
  1
  ```

#### Python Solution
```python
class MarkdownChecklist:
    def __init__(self, lines: list[str]) -> None:
        self.tasks = []
        for line in lines:
            line = line.rstrip('\r\n')
            s_line = line.lstrip()
            if not s_line or s_line[0] not in ('-', '*'):
                continue
            if len(s_line) < 2 or not s_line[1].isspace():
                continue
            rem = s_line[1:].lstrip()
            if len(rem) < 4 or not rem.startswith('['):
                continue
            marker = rem[1]
            if marker not in (' ', 'x', 'X') or rem[2] != ']':
                continue
            if not rem[3].isspace():
                continue
            name = rem[4:].strip()
            if name:
                completed = marker.lower() == 'x'
                self.tasks.append({"name": name, "completed": completed})

    def markDone(self, taskText: str) -> None:
        for task in self.tasks:
            if task["name"] == taskText and not task["completed"]:
                task["completed"] = True
                return
        raise ValueError("Task not found or already completed")

    def markUndone(self, taskText: str) -> None:
        for task in self.tasks:
            if task["name"] == taskText and task["completed"]:
                task["completed"] = False
                return
        raise ValueError("Task not found or already pending")

    def getStatus(self, taskText: str) -> str:
        for task in self.tasks:
            if task["name"] == taskText:
                return "completed" if task["completed"] else "pending"
        raise ValueError("Task not found")

    def getCompletedCount(self) -> int:
        return sum(1 for t in self.tasks if t["completed"])

    def getPendingCount(self) -> int:
        return sum(1 for t in self.tasks if not t["completed"])
```

