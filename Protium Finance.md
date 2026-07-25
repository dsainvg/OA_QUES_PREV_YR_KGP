# Interview Questions
*Total questions: 2*

---

## Table of Contents
- [SQL Questions](#sql-questions)

---

## SQL Questions

### Q1. Employee and Manager Salary Comparison

**Topic:** `SQL`, `Self Join`, `Conditional Logic`  

In this MySQL challenge, your query should identify employees who have a higher salary than their manager. Display each employee's `Name`, `Salary`, and `ManagerName`. If the employee does not have a manager, the `ManagerName` should be displayed as `"No Manager"`. The result should be ordered by the difference between the employee's and manager's salaries in descending order. Additionally, include a column titled `PromotionOpportunity` that indicates `"Yes"` if the employee's salary is higher than their manager's and `"No"` otherwise.

**Table Schema (maintable_0XQUK):**
- `ID` (INT)
- `Name` (VARCHAR)
- `Salary` (INT)
- `ManagerID` (INT)

```sql
SELECT 
    e.Name AS Name,
    e.Salary AS Salary,
    COALESCE(m.Name, 'No Manager') AS ManagerName,
    CASE 
        WHEN e.Salary > m.Salary THEN 'Yes'
        ELSE 'No'
    END AS PromotionOpportunity
FROM maintable_0XQUK e
LEFT JOIN maintable_0XQUK m ON e.ManagerID = m.ID
ORDER BY (e.Salary - COALESCE(m.Salary, 0)) DESC;
```

---

### Q2. SQL Department Budget Analysis

**Topic:** `SQL`, `Common Table Expressions (CTEs)`, `Window Functions`  

In this MySQL challenge, your task is to analyze the budget allocation within departments, identify the top earners, and assess potential areas for budget optimization. Construct a query that accomplishes the following objectives:

- **Department Budget Overview:** Generate a list of departments, represented by the `DivisionID`, along with the total salary (`TotalDivisionSalary`) allocated to each department.
- **Top Earners Insight:** For each department, identify the employee (`Name`) with the highest salary (`TopSalary`).
- **Budget Utilization Analysis:** Calculate the percentage (`SalaryUtilization`) of the total department budget that the top earner's salary represents. This should be represented as a percentage of the total salary for their respective department, rounded to 5 decimal places.
- **Underutilized Departments Detection:** Include a column titled `BudgetOptimizationPotential` that indicates `"Yes"` if the highest salary in the department is less than 50% of the total department salary, suggesting a potential for budget optimization, and `"No"` otherwise.

The result should include the following columns (ordered by `DivisionID` in ascending order):
- `DivisionID` (ID of the department)
- `TotalDivisionSalary` (Sum of salaries within the department)
- `Name` (Name of the employee with the highest salary in the department)
- `TopSalary` (The highest salary within the department)
- `SalaryUtilization` (Percentage of the total department salary that the top earner's salary represents rounded to 5 decimal places)
- `BudgetOptimizationPotential` (Indicates if there's a potential for budget optimization within the department based on the top earner's salary)

**Table Schema (maintable_7JTBU):**
- `DivisionID` (INT)
- `Name` (VARCHAR)
- `Salary` (INT)

#### Approach 1: Using Window Functions (Recommended)
```sql
WITH RankedEmployees AS (
    SELECT
        DivisionID,
        Name,
        Salary,
        SUM(Salary) OVER(PARTITION BY DivisionID) AS TotalDivisionSalary,
        ROW_NUMBER() OVER(PARTITION BY DivisionID ORDER BY Salary DESC, Name ASC) AS rn
    FROM maintable_7JTBU
)
SELECT
    DivisionID,
    TotalDivisionSalary,
    Name,
    Salary AS TopSalary,
    ROUND((Salary / TotalDivisionSalary) * 100, 5) AS SalaryUtilization,
    CASE
        WHEN Salary < 0.5 * TotalDivisionSalary THEN 'Yes'
        ELSE 'No'
    END AS BudgetOptimizationPotential
FROM RankedEmployees
WHERE rn = 1
ORDER BY DivisionID ASC;
```

#### Approach 2: Using Joins & Group By (Traditional)
```sql
WITH DepartmentBudget AS (
    SELECT
        DivisionID,
        SUM(Salary) AS TotalDivisionSalary
    FROM maintable_7JTBU
    GROUP BY DivisionID
),
TopEarners AS (
    SELECT
        e.DivisionID,
        e.Name,
        e.Salary AS TopSalary
    FROM maintable_7JTBU e
    JOIN (
        SELECT
            DivisionID,
            MAX(Salary) AS MaxSalary
        FROM maintable_7JTBU
        GROUP BY DivisionID
    ) t ON e.DivisionID = t.DivisionID AND e.Salary = t.MaxSalary
)
SELECT
    db.DivisionID,
    db.TotalDivisionSalary,
    te.Name,
    te.TopSalary,
    ROUND((te.TopSalary / db.TotalDivisionSalary) * 100, 5) AS SalaryUtilization,
    CASE
        WHEN te.TopSalary < 0.5 * db.TotalDivisionSalary THEN 'Yes'
        ELSE 'No'
    END AS BudgetOptimizationPotential
FROM DepartmentBudget db
JOIN TopEarners te ON db.DivisionID = te.DivisionID
ORDER BY db.DivisionID ASC;
```
