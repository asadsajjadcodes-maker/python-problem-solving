# 🔢 Problem 04: Second Largest Number

## 🧠 Problem

Given a list of integers, find the **second largest unique number**.

---

## 💡 Approach

* Convert list to a set to remove duplicates
* Sort the unique elements
* Reverse the list to get descending order
* Select the second element

---

## 🧮 Implementation

```python
arr = [int(x) for x in input().split()]
unique_numbers = sorted(set(arr), reverse=True)
print(unique_numbers[1])
```

---

## 🧪 Example

Input:
3 4 5 6 7 3 2 2

Output:
6

---

## 🧠 What I Learned

* Using `set()` to remove duplicates
* Sorting lists
* Extracting specific values

---

## 🏷️ Tags

* Lists
* Sorting
* Set

---

## 🚀 Status

✅ Completed
