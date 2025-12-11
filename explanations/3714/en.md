## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the length of the longest substring where all distinct characters appear the same number of times. The string contains only 'a', 'b', and 'c'.

**1.1 Constraints & Complexity:**

* **Input Size:** The string `s` can have up to 10^5 characters, consisting only of 'a', 'b', and 'c'.
* **Time Complexity:** O(n) - We build prefix sums in one pass, then iterate through all prefix positions once, using hash map lookups in O(1).
* **Space Complexity:** O(n) - We store prefix sums in an array of size n+1, and a hash map that can store up to O(n) entries.
* **Edge Case:** If all characters are the same, the entire string is balanced with length n.

**1.2 High-level approach:**

The goal is to use prefix sums to efficiently find substrings where character frequencies are balanced. For a balanced substring S[i:j], the differences in prefix counts must be equal. We use hash maps to track the first occurrence of each (difference pattern, remaining count) combination.


**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Check all possible substrings by fixing start and end positions, then count character frequencies for each. This is O(n^2) time, which is too slow for n <= 10^5.
* **Optimized (Prefix Sum + Hash Map):** Build prefix sums for 'a', 'b', and 'c'. For balanced substrings, the differences between prefix counts must match. We use hash maps to find the earliest position with matching differences. This is O(n) time.
* **Why it's better:** By using prefix sums and hash maps, we avoid checking all substrings and can find valid ranges in O(1) time per position.

**1.4 Decomposition:**

1. Build prefix sum arrays for 'a', 'b', and 'c' where P[i] = (a_i, b_i, c_i) represents counts up to position i.
2. For each prefix position, check multiple cases: all 3 characters balanced, pairs balanced, or single character runs.
3. For each case, calculate the required difference pattern and check if we've seen it before.
4. Track the maximum length found across all cases.
5. Return the maximum length.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "abbac"`

We initialize:
* `P = [[0,0,0], [1,0,0], [1,1,0], [1,2,0], [2,2,0], [2,2,1]]` (prefix sums)
* `res = 0`
* `first = {}` (hash map for first occurrence)

**2.2 Start Checking:**

We iterate through each prefix position i from 0 to n.

**2.3 Trace Walkthrough:**

| Step | i   | (a,b,c) | Case | Key          | Check first | res |
| ---- | --- | ------- | ---- | ------------ | ----------- | --- |
| 1    | 0   | (0,0,0) | All  | ("abc",0,0)  | i=0 stored  | 0   |
| 2    | 1   | (1,0,0) | All  | ("abc",1,1)  | i=1 stored  | 0   |
| 3    | 2   | (1,1,0) | All  | ("abc",0,1)  | i=2 stored  | 0   |
| 4    | 3   | (1,2,0) | All  | ("abc",-1,1) | i=3 stored  | 0   |
| 5    | 4   | (2,2,0) | All  | ("abc",0,2)  | Found i=2   | 2   |
| 6    | 4   | (2,2,0) | ab   | ("ab",0,0)   | Found i=0   | 4   |

At step 6, we find that positions 0 and 4 have the same (a-b, c) = (0, 0), meaning substring s[0:4] = "abba" is balanced for 'a' and 'b'.

**2.4 Increment and Loop:**

For each prefix position, we check all 7 cases (all 3, 3 pairs, 3 singles) and update the maximum length.

**2.5 Return Result:**

After processing all positions, we return `res = 4`, representing the length of the longest balanced substring.
