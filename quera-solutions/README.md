# Quera Solutions

محل قرارگیری پاسخ‌های تمرینات سایت کوئرا.

This folder is my tracker for exercises solved on [Quera](https://quera.org).
Each solution is a single file that documents its own approach and
complexity, so the code and the reasoning live together.

## How to add a solution

1. Copy [`_template.py`](./_template.py) to `NNN_short_name.py`
   (for example `001_two_sum.py`).
2. Fill in the docstring: link, approach and **time / space complexity**.
3. Write `solve()` so it takes plain values and returns the answer. Keep the
   input and output handling in `main()`.
4. Run it locally with a few of your own examples, then submit it on Quera.
5. Add a row to the table below.

## Tracker

| # | Problem | Topic | Status | Time | Space | Solution |
| :-: | :--- | :--- | :---: | :---: | :---: | :--- |
| - | *No solutions yet. The first one goes here.* | - | - | - | - | - |

**Status legend:** ✅ accepted · 🔄 in progress · 💡 revisit later

## Complexity cheat sheet

`n` is the size of the input.

| Notation | Name | Typical example |
| :--- | :--- | :--- |
| `O(1)` | constant | dictionary lookup, list `append` (amortized) |
| `O(log n)` | logarithmic | binary search |
| `O(n)` | linear | one pass over a list |
| `O(n log n)` | linearithmic | `sorted()` |
| `O(n²)` | quadratic | nested loops over the same list |

Rule of thumb: count how many times the input is scanned for **time**, and how
much extra memory is allocated besides the input for **space**.
