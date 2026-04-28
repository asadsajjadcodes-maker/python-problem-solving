# 📦 Problem 03: List Comprehensions

## 🧠 Problem

Given integers x, y, z, and n, generate all possible coordinates [i, j, k] such that:

* 0 ≤ i ≤ x
* 0 ≤ j ≤ y
* 0 ≤ k ≤ z
* i + j + k ≠ n

---

## 💡 Approach

* Use nested loops to generate all combinations
* Use list comprehension for clean and compact code
* Apply a condition to exclude combinations where the sum equals n

---

## 🧮 Implementation

```python
[[i, j, k] 
 for i in range(x + 1) 
 for j in range(y + 1) 
 for k in range(z + 1) 
 if i + j + k != n]
```

---



---

## 🧪 Example

Input:
x = 1, y = 1, z = 1, n = 2

Output:
[[0,0,0], [0,0,1], [0,1,0], [1,0,0], [1,1,1]]

---

## 🧠 What I Learned

* List comprehensions
* Nested loops in a single line
* Filtering conditions

---

## 🏷️ Tags

* Lists
* Comprehensions
* Loops

---

## 🚀 Status

✅ Completed
