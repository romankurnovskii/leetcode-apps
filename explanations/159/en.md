## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the length of the longest substring that contains at most two distinct characters. This means we can have 0, 1, or 2 different characters in our substring, but not 3 or more.

**1.1 Constraints & Complexity:**
- Input size: `1 <= s.length <= 10^5`
- **Time Complexity:** O(n) where n is the length of the string - each character is visited at most twice (once by right pointer, once by left pointer)
- **Space Complexity:** O(1) - we store at most 2 distinct characters in the hash map
- **Edge Case:** If the string has fewer than 2 distinct characters, return the entire string length

**1.2 High-level approach:**
We use a sliding window technique with two pointers. The right pointer expands the window to include new characters, and the left pointer shrinks it when we have more than two distinct characters. We track character frequencies using a hash map.

![Sliding window with two distinct characters](https://assets.leetcode.com/static_assets/others/sliding-window-two-distinct.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all possible substrings O(n²) and count distinct characters for each, which is O(n³) total.
- **Optimized Strategy:** Use sliding window to maintain a valid substring, expanding and contracting as needed. This is O(n) time.
- **Why it's better:** We avoid checking redundant substrings and process each character at most twice, making it much more efficient.

**1.4 Decomposition:**
1. Initialize two pointers (left and right) at the start of the string
2. Use a hash map to count character frequencies in the current window
3. Expand the window by moving the right pointer and updating counts
4. When we have more than 2 distinct characters, shrink the window by moving the left pointer
5. Track the maximum window size throughout the process

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `s = "eceba"`
- Initialize `left = 0`, `right = 0`, `res = 0`
- Initialize `char_count = {}` (empty hash map)

**2.2 Start Checking:**
We begin expanding the window by moving the right pointer.

**2.3 Trace Walkthrough:**

| Step | right | s[right] | char_count | Distinct | Action | left | res |
|------|-------|-----------|------------|----------|--------|-----|-----|
| 0 | 0 | 'e' | {'e':1} | 1 | Expand | 0 | 1 |
| 1 | 1 | 'c' | {'e':1,'c':1} | 2 | Expand | 0 | 2 |
| 2 | 2 | 'e' | {'e':2,'c':1} | 2 | Expand | 0 | 3 |
| 3 | 3 | 'b' | {'e':2,'c':1,'b':1} | 3 | Shrink | 1 | 3 |
| 3a | 3 | 'b' | {'e':1,'c':1,'b':1} | 3 | Shrink | 2 | 3 |
| 3b | 3 | 'b' | {'e':1,'b':1} | 2 | Expand | 2 | 3 |
| 4 | 4 | 'a' | {'e':1,'b':1,'a':1} | 3 | Shrink | 3 | 3 |
| 4a | 4 | 'a' | {'b':1,'a':1} | 2 | Expand | 3 | 3 |

**2.4 Increment and Loop:**
After processing each character, we increment the right pointer. If we need to shrink, we increment the left pointer until we have at most 2 distinct characters.

**2.5 Return Result:**
Return `res = 3`, which is the length of the longest substring with at most two distinct characters. In this case, "ece" or "ceb" both have length 3.

