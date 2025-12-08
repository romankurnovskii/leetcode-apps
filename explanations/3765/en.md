## Explanation

### Strategy (The "Why")

**Restate the problem:** A number is a "Complete Prime Number" if every prefix and every suffix of the number is prime. We need to check if a given number satisfies this condition.

**1.1 Constraints & Complexity:**
- Input size: `1 <= num <= 10^9`
- **Time Complexity:** O(d * sqrt(n)) where d is the number of digits, as we check primality for each prefix and suffix
- **Space Complexity:** O(d) to store the string representation
- **Edge Case:** Single-digit numbers are complete prime only if they are prime themselves

**1.2 High-level approach:**
We convert the number to a string, then check if all prefixes (from left) and all suffixes (from right) are prime numbers.

![Prime checking visualization](https://assets.leetcode.com/static_assets/others/prime-checking.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all prefixes and suffixes for primality, which is what we do
- **Optimized Strategy:** Use efficient primality testing (trial division up to sqrt(n)), achieving reasonable performance
- **Emphasize the optimization:** We only need to check divisors up to sqrt(n) for primality testing

**1.4 Decomposition:**
1. Convert the number to a string to access individual digits
2. Check all prefixes: from first digit, first two digits, ..., all digits
3. Check all suffixes: from last digit, last two digits, ..., all digits
4. Return true only if all prefixes and suffixes are prime

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `num = 23`
- Convert to string: `s = "23"`

**2.2 Start Checking:**
We check all prefixes first, then all suffixes.

**2.3 Trace Walkthrough:**

| Type | Substring | Value | Is Prime? |
|------|-----------|-------|-----------|
| Prefix | "2" | 2 | Yes |
| Prefix | "23" | 23 | Yes |
| Suffix | "3" | 3 | Yes |
| Suffix | "23" | 23 | Yes |

**2.4 Increment and Loop:**
After checking all prefixes and suffixes, we verify all are prime.

**2.5 Return Result:**
All prefixes and suffixes are prime, so the result is `true`.
