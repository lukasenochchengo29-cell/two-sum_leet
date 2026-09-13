# LeetCode Python Solutions

This repository contains Python implementations for a set of LeetCode problems. Each file follows the standard LeetCode `Solution` class format and focuses on clear, efficient logic.

## Quick Start

The files are intended to be submitted to LeetCode or imported into a small test script. They do not include command-line input or output.

To check that every solution is valid Python, run:

```bash
python3 -m compileall .
```

## Problems Included

- [two-sum_leet.py](two-sum_leet.py) — Two Sum
- [valid-anagram.py](valid-anagram.py) — Valid Anagram
- [find-pivot-index.py](find-pivot-index.py) — Find Pivot Index
- [Running-Sum-of-1d-Array.py](Running-Sum-of-1d-Array.py) — Running Sum of 1D Array
- [Product-of-Array-Except-Self.py](Product-of-Array-Except-Self.py) — Product of Array Except Self
- [Contiguous-Array.py](Contiguous-Array.py) — Contiguous Array
- [Subarray-Sum-Equals-K.py](Subarray-Sum-Equals-K.py) — Subarray Sum Equals K
- [group-anagrams.py](group-anagrams.py) — Group Anagrams
- [top-k-frequent.py](top-k-frequent.py) — Top K Frequent Elements
- [maximum-sum-of-3-non-overlapping-subarrays.py](maximum-sum-of-3-non-overlapping-subarrays.py) — Maximum Sum of 3 Non-Overlapping Subarrays

## Complexity Guide

Let `n` be the number of input values. For string problems, `m` represents the total number of characters.

| Problem | Difficulty | Main technique | Time | Extra space |
| --- | --- | --- | --- | --- |
| [Two Sum](two-sum_leet.py) | Easy | Hash map lookup | O(n) | O(n) |
| [Valid Anagram](valid-anagram.py) | Easy | Character frequency map | O(m) | O(m) |
| [Find Pivot Index](find-pivot-index.py) | Easy | Total and running sums | O(n) | O(1) |
| [Running Sum of 1D Array](Running-Sum-of-1d-Array.py) | Easy | Cumulative sum | O(n) | O(n) |
| [Product of Array Except Self](Product-of-Array-Except-Self.py) | Medium | Prefix and suffix products | O(n) | O(1)* |
| [Contiguous Array](Contiguous-Array.py) | Medium | Prefix balance and hash map | O(n) | O(n) |
| [Subarray Sum Equals K](Subarray-Sum-Equals-K.py) | Medium | Prefix-sum frequency map | O(n) | O(n) |
| [Group Anagrams](group-anagrams.py) | Medium | Sorted-string grouping | O(m log m) | O(m) |
| [Top K Frequent Elements](top-k-frequent.py) | Medium | Frequency map and buckets | O(n) | O(n) |
| [Maximum Sum of 3 Non-Overlapping Subarrays](maximum-sum-of-3-non-overlapping-subarrays.py) | Hard | Sliding windows and dynamic programming | O(n) | O(n) |

\* `Product of Array Except Self` uses the returned list as output storage; its auxiliary space is O(1).

## Topics Covered

- Hash maps and frequency counts
- Prefix sums and cumulative arrays
- Sliding window techniques
- Sorting and grouping by transformed keys
- Efficient window optimization and greedy selection

## Notes

The solutions are written for practice and review, with emphasis on readability, correctness, and algorithmic clarity.

When adding a solution, keep the standard `Solution` class interface, use a descriptive filename, and add the problem to the table above with its technique and complexity.

