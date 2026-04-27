# 📅 Problem 02: Leap Year Checker

## 🧠 Problem

Determine whether a given year is a leap year.

---

## 💡 Logic

A year is considered a leap year if:

* It is divisible by 4 AND not divisible by 100
* OR it is divisible by 400

---

## 🧮 Implementation

```python
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```

---

## ⏱ Complexity

* Time: O(1)
* Space: O(1)

---

## 🧪 Examples

| Input | Output          |
| ----- | --------------- |
| 2024  | Leap Year       |
| 1900  | Not a Leap Year |
| 2000  | Leap Year       |

---

## 🧠 What I Learned

* Writing clean boolean conditions
* Using functions for reusable logic
* Real-world calendar rules

---

## 🏷️ Tags

* Math
* Conditions
* Logic

---

## 🚀 Status

✅ Completed
