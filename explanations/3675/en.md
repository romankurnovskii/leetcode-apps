## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to transform a string into all 'a' characters by repeatedly choosing a character and shifting all its occurrences forward by one in the circular alphabet (z wraps to a). We want the minimum number of operations.

**1.1 Constraints & Complexity:**

- **Input Size:** String length can be up to 5×10^5.
- **Time Complexity:** O(n) where n is the string length - we scan the string once.
- **Space Complexity:** O(1) - we only track the maximum distance.
- **Edge Case:** If the string already contains only 'a', the answer is 0.

**1.2 High-level approach:**

The goal is to find the character that requires the most operations to become 'a', as all characters must eventually become 'a' and operations can be done in parallel for the same character.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible operation sequences, which would be exponential.
- **Optimized Strategy:** Find the character farthest from 'a' in the circular alphabet. The distance is (ord('a') + 26 - ord(c)) % 26. This is O(n).
- **Optimization:** Since operations on different characters can be interleaved optimally, we only need to find the maximum distance.

**1.4 Decomposition:**

1. Initialize result to 0.
2. For each character in the string, calculate its distance from 'a' in the circular alphabet.
3. Keep track of the maximum distance found.
4. Return the maximum distance as the minimum number of operations needed.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "yz"`

- We need to find which character is farthest from 'a'.

**2.2 Start Processing:**

We iterate through each character and calculate its distance from 'a'.

**2.3 Trace Walkthrough:**

| Character | Distance Calculation | Distance | Max So Far |
|-----------|---------------------|----------|------------|
| 'y' | (ord('a') + 26 - ord('y')) % 26 = (97 + 26 - 121) % 26 = 2 | 2 | 2 |
| 'z' | (ord('a') + 26 - ord('z')) % 26 = (97 + 26 - 122) % 26 = 1 | 1 | 2 |

**2.4 Increment and Loop:**

The maximum distance is 2, which means we need 2 operations.

**2.5 Return Result:**

The result is 2: first change 'y' to 'z' (1 op), then change 'z' to 'a' (1 op). Since we can do all 'y' characters together and all 'z' characters together, the total is 2.

