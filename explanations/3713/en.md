## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the length of the longest substring where all distinct characters appear the same number of times.

**1.1 Constraints & Complexity:**

* **Input Size:** The string `s` can have up to 1000 characters, consisting of lowercase English letters.
* **Time Complexity:** O(n^2) - We check all possible substrings by fixing start and end positions, and use a Counter to track character frequencies in O(1) per operation.
* **Space Complexity:** O(n) - In the worst case, we store up to 26 distinct characters in the Counter.
* **Edge Case:** If all characters are the same, the entire string is balanced with length n.

**1.2 High-level approach:**

The goal is to check all possible substrings and find the longest one where all distinct characters have equal frequency. We use a Counter to track character counts as we extend substrings.

![Visualization showing balanced substring with equal character frequencies]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Check all possible substrings by fixing start and end positions, then count character frequencies for each. This is O(n^2) time, which is acceptable for n <= 1000.
* **Optimized (Same as brute force for this constraint):** The brute force approach is already optimal for the given constraints. We maintain a Counter as we extend substrings, avoiding redundant counting.
* **Why it's acceptable:** With n <= 1000, O(n^2) = 1 million operations is efficient enough.

**1.4 Decomposition:**

1. For each possible starting position i in the string.
2. Initialize an empty Counter to track character frequencies.
3. Extend the substring by moving the end position j from i to n-1.
4. Add each character to the Counter.
5. Check if all distinct characters have the same frequency, and update the maximum length.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "abbac"`

We initialize:
* `n = 5`
* `res = 0`

**2.2 Start Checking:**

We iterate through each starting position i from 0 to n-1.

**2.3 Trace Walkthrough:**

| Step | i   | j   | s[j] | char_count    | distinct_chars | counts  | Balanced? | res |
| ---- | --- | --- | ---- | ------------- | -------------- | ------- | --------- | --- |
| 1    | 0   | 0   | 'a'  | {a:1}         | ['a']          | [1]     | Yes       | 1   |
| 2    | 0   | 1   | 'b'  | {a:1,b:1}     | ['a','b']      | [1,1]   | Yes       | 2   |
| 3    | 0   | 2   | 'b'  | {a:1,b:2}     | ['a','b']      | [1,2]   | No        | 2   |
| 4    | 0   | 3   | 'a'  | {a:2,b:2}     | ['a','b']      | [2,2]   | Yes       | 4   |
| 5    | 0   | 4   | 'c'  | {a:2,b:2,c:1} | ['a','b','c']  | [2,2,1] | No        | 4   |

At step 4, we find the longest balanced substring "abba" with length 4, where both 'a' and 'b' appear twice.

**2.4 Increment and Loop:**

For each starting position i, we extend the substring by incrementing j, adding characters to the Counter and checking balance.

**2.5 Return Result:**

After checking all substrings, we return `res = 4`, representing the length of the longest balanced substring.
