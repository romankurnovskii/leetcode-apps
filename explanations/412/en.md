## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** We need to process integers from 1 to n, where `1 <= n <= 10^4`.
- **Time Complexity:** O(n) - We iterate through each number from 1 to n exactly once.
- **Space Complexity:** O(n) - We create a result list of size n to store the output strings.
- **Edge Case:** When n = 1, we simply return `["1"]`.

**1.2 High-level approach:**
The goal is to generate a list of strings where numbers divisible by 3 are replaced with "Fizz", numbers divisible by 5 are replaced with "Buzz", and numbers divisible by both 3 and 5 are replaced with "FizzBuzz".

![FizzBuzz sequence visualization](https://assets.leetcode.com/static_assets/others/fizzbuzz.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check divisibility by 15 first, then by 3, then by 5, then use the number. This is the same as our optimized approach - there's no more efficient way to solve this problem.
- **Optimized Strategy:** Use conditional checks in the correct order (check for 15 first, then 3, then 5) to determine the appropriate string for each number.

**1.4 Decomposition:**
1. Iterate through numbers from 1 to n.
2. For each number, check if it's divisible by both 3 and 5 (i.e., divisible by 15).
3. If not, check if it's divisible by 3.
4. If not, check if it's divisible by 5.
5. Otherwise, use the number itself as a string.
6. Add the result to the output list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `n = 15`.

Initialize:
- `res = []` (empty list to store results)

**2.2 Start Checking:**
We iterate through numbers from 1 to 15.

**2.3 Trace Walkthrough:**

| i | Divisible by 3? | Divisible by 5? | Divisible by 15? | Result |
|---|-----------------|-----------------|------------------|--------|
| 1 | No | No | No | "1" |
| 2 | No | No | No | "2" |
| 3 | Yes | No | No | "Fizz" |
| 4 | No | No | No | "4" |
| 5 | No | Yes | No | "Buzz" |
| 6 | Yes | No | No | "Fizz" |
| 7 | No | No | No | "7" |
| 8 | No | No | No | "8" |
| 9 | Yes | No | No | "Fizz" |
| 10 | No | Yes | No | "Buzz" |
| 11 | No | No | No | "11" |
| 12 | Yes | No | No | "Fizz" |
| 13 | No | No | No | "13" |
| 14 | No | No | No | "14" |
| 15 | Yes | Yes | Yes | "FizzBuzz" |

**2.4 Increment and Loop:**
For each iteration, we check the conditions in order:
1. If `i % 3 == 0 and i % 5 == 0`: append "FizzBuzz"
2. Else if `i % 3 == 0`: append "Fizz"
3. Else if `i % 5 == 0`: append "Buzz"
4. Else: append `str(i)`

**2.5 Return Result:**
After processing all numbers from 1 to n, return the `res` list containing all the strings.

