# 🔁 Problem 01: Swap Two Variables

## 🧠 Problem

Swap two variables without using a third variable.

---

## 💡 Approaches Implemented

### 1. Arithmetic Method

* Uses addition and subtraction
* Works with numeric values

---

### 2. XOR Method

* Uses bitwise operator (`^`)
* Based on properties:

  * x ^ x = 0
  * x ^ 0 = x

---

### 3. Pythonic Method (Best Practice)

* Uses tuple unpacking
* Most readable and recommended in Python

```python
a, b = b, a
```

---

### 4. Multiplication & Division Method

* Uses product and division
* ⚠️ Does NOT work if any value is 0 (division by zero issue)

---

## ⏱ Complexity

* Time: O(1)
* Space: O(1)

---

## 🧪 Example

Input:
a = 5, b = 10

Output:
a = 10, b = 5

---

## 🧠 What I Learned

* Multiple ways to solve the same problem
* Bitwise operations (XOR)
* Pythonic best practices
* Edge cases (division by zero)

---

## 🚀 Status

✅ Completed with 4 different approaches
