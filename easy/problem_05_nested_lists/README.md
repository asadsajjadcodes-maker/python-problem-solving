# Problem 05 - Find Students With Second Lowest Score

## Problem Statement
Given the names and grades of students, store them in a list and print the names of students who have the second lowest grade.

If multiple students have the same second lowest grade, print their names in alphabetical order.

---

## Example Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

## Example Output
Berry
Harry

---

## Approach

1. Store all student names and scores in a list.
2. Extract all scores separately.
3. Remove duplicate scores using `set()`.
4. Sort the scores.
5. Find the second lowest score.
6. Find students matching that score.
7. Sort their names alphabetically.
8. Print the names.

---

## Concepts Used

- Lists
- Loops
- Conditional statements
- Sorting
- set()
- Nested lists

---

## Time Complexity

Sorting scores:
O(n log n)

Finding matching students:
O(n)

Overall:
O(n log n)

---

## What I Learned

- How to work with nested lists
- How to remove duplicate values
- How sorting helps solve ranking problems
- How to filter specific data from a dataset