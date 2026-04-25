# 🔁 Problem 01: Swap Two Variables Without Third Variable

## 🧠 Problem Statement

Write a program to swap two variables without using a third variable.

---

## ✅ Solutions Implemented

### 1. Arithmetic Method

* Uses addition and subtraction
* Works because Python treats:

  * `True = 1`
  * `False = 0`

### 2. Bitwise XOR Method

* Uses XOR operator (`^`)
* Key properties:

  * `x ^ x = 0`
  * `x ^ 0 = x`

---

## 💻 Code Example

```python
# Method 1: Arithmetic
a = True
b = False

a = a + b
b = a - b
a = a - b

# Method 2: XOR
a = 0
b = -4

a = a ^ b
b = a ^ b
a = a ^ b
```

---

## 📚 Concepts Learned

* Boolean arithmetic in Python
* Bitwise operators
* In-place variable swapping

---



---

## 🚀 Status

✅ Completed
