## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the largest prime number ≤ n that can be expressed as the sum of one or more consecutive prime numbers starting from 2.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 5 * 10^5`
- **Time Complexity:** O(n log log n) for sieve + O(p²) for consecutive sums where p is number of primes
- **Space Complexity:** O(n) for the sieve array
- **Edge Case:** If n = 2, the answer is 2 itself

**1.2 High-level approach:**
We use the Sieve of Eratosthenes to find all primes up to n, then compute all consecutive prime sums starting from 2, and find the largest sum that is also prime.

![Prime sum visualization](https://assets.leetcode.com/static_assets/others/prime-sum.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check each number for primality individually, which is O(n * sqrt(n))
- **Optimized Strategy:** Use Sieve of Eratosthenes to mark all primes in O(n log log n), then compute consecutive sums
- **Emphasize the optimization:** The sieve allows us to check primality in O(1) time after preprocessing

**1.4 Decomposition:**
1. Use Sieve of Eratosthenes to find all primes up to n
2. Generate list of all primes
3. For each starting position, compute consecutive prime sums
4. Check if each sum is prime and ≤ n
5. Track the maximum such prime sum

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 20`
- Primes up to 20: [2, 3, 5, 7, 11, 13, 17, 19]

**2.2 Start Computing Sums:**
We compute consecutive sums starting from each prime.

**2.3 Trace Walkthrough:**

| Start | Consecutive Primes | Sum | Is Prime? | Is ≤ 20? | Max So Far |
|-------|-------------------|-----|-----------|----------|------------|
| 2 | [2] | 2 | Yes | Yes | 2 |
| 2 | [2,3] | 5 | Yes | Yes | 5 |
| 2 | [2,3,5] | 10 | No | Yes | 5 |
| 2 | [2,3,5,7] | 17 | Yes | Yes | 17 |
| 2 | [2,3,5,7,11] | 28 | No | No | 17 |

**2.4 Increment and Loop:**
We continue checking other starting positions, but the maximum from starting at 2 is 17.

**2.5 Return Result:**
The largest prime that is a consecutive prime sum is 17, which is the result.
