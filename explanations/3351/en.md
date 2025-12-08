## Explanation

### Strategy (The "Why")

**Restate the problem:** We repeatedly remove the first occurrence of each letter from 'a' to 'z' until the string is empty. We need to return the string right before the last operation.

**1.1 Constraints & Complexity:**
- Input size: `1 <= s.length <= 5 * 10^5`
- **Time Complexity:** O(n) where n is the length of s, as we iterate once to count frequencies and find last positions
- **Space Complexity:** O(1) for the character set (26 letters), O(n) for storing last positions
- **Edge Case:** If all characters have the same frequency, the result contains all characters in order of last occurrence

**1.2 High-level approach:**
Before the last operation, only characters with maximum frequency remain. We find these characters and return them in the order of their last occurrence in the original string.

![String processing visualization](https://assets.leetcode.com/static_assets/others/string-processing.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Simulate all operations step by step, which would be O(n * 26) operations
- **Optimized Strategy:** Recognize that only max-frequency characters survive to the last operation, find their last positions, and return them in order
- **Emphasize the optimization:** By understanding the operation pattern, we can directly compute the result without simulation

**1.4 Decomposition:**
1. Count the frequency of each character
2. Find the maximum frequency
3. Identify all characters with maximum frequency
4. Find the last occurrence position of each max-frequency character
5. Sort these characters by their last position and return as a string

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `s = "aabcbbca"`
- Count frequencies: a=3, b=3, c=2
- Max frequency: 3
- Max frequency characters: ['a', 'b']

**2.2 Start Processing:**
We find the last occurrence of each max-frequency character.

**2.3 Trace Walkthrough:**

| Character | Frequency | Last Position | Sorted by Position |
|-----------|-----------|---------------|-------------------|
| 'a' | 3 | 7 | 'b' (pos 5) |
| 'b' | 3 | 5 | 'a' (pos 7) |

After sorting by last position: ['b', 'a']

**2.4 Increment and Loop:**
After processing all characters, we sort and build the result.

**2.5 Return Result:**
The result is "ba", which is the string right before the last operation removes these characters.
