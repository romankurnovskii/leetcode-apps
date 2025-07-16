## 1207. Unique Number of Occurrences [Easy]

https://leetcode.com/problems/unique-number-of-occurrences

## Description
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

**Examples**
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

**Constraints**
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

## Hint
Use a dictionary to count occurrences, then check if the counts are unique using a set.

## Explanation
We want to know if every number in the array appears a unique number of times. First, we count how many times each number appears using a dictionary. Then, we check if all those counts are different by putting them in a set.

We do this because using a dictionary makes counting fast and easy, and a set lets us quickly check for duplicates among the counts. This approach is efficient and avoids unnecessary loops. 