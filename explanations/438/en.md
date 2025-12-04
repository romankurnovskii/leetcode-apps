## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** String s and p have lengths between 1 and 3 * 10^4, and contain only lowercase English letters.
- **Time Complexity:** O(n) - We iterate through string s once with a sliding window, where n is the length of s.
- **Space Complexity:** O(1) - We use fixed-size dictionaries (at most 26 characters) for counting.
- **Edge Case:** If p is longer than s, return empty list.

**1.2 High-level approach:**
The goal is to find all starting indices of anagrams of string p in string s. We use a sliding window approach with character frequency counting to efficiently check if a window is an anagram of p.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each possible starting position, extract the substring and check if it's an anagram by sorting. This takes O(n * m log m) time where m is the length of p.
- **Optimized Strategy (Sliding Window with Frequency):** Use a sliding window with character frequency counting. Compare frequency maps instead of sorting. This takes O(n) time.
- **Emphasize the optimization:** Frequency counting avoids sorting and allows us to update the window in O(1) time by adjusting character counts.

**1.4 Decomposition:**
1. Count character frequencies in string p.
2. Use a sliding window of size len(p) over string s.
3. Maintain character frequencies for the current window.
4. When window size equals len(p), compare frequencies with p's frequencies.
5. If frequencies match, add the starting index to results.
6. Slide the window by removing left character and adding right character.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `s = "cbaebabacd"`, `p = "abc"`

Initialize:
- `p_count = {'a': 1, 'b': 1, 'c': 1}`
- `window_count = {}`
- `res = []`
- `left = 0`

**2.2 Start Checking:**
We iterate through s with a sliding window.

**2.3 Trace Walkthrough:**

| right | char | window_count | Window Size | Match? | Action |
|-------|------|--------------|-------------|--------|--------|
| 0 | 'c' | {'c':1} | 1 | No | Continue |
| 1 | 'b' | {'c':1,'b':1} | 2 | No | Continue |
| 2 | 'a' | {'c':1,'b':1,'a':1} | 3 | Yes | Add 0, remove 'c' |
| 3 | 'e' | {'b':1,'a':1,'e':1} | 3 | No | Remove 'b' |
| 4 | 'b' | {'a':1,'e':1,'b':1} | 3 | No | Remove 'a' |
| 5 | 'a' | {'e':1,'b':1,'a':1} | 3 | No | Remove 'e' |
| 6 | 'b' | {'b':1,'a':1,'b':1} | 3 | No | Remove 'b' |
| 7 | 'a' | {'a':1,'b':1,'a':1} | 3 | No | Remove 'a' |
| 8 | 'c' | {'b':1,'a':1,'c':1} | 3 | Yes | Add 6, remove 'b' |

**2.4 Return Result:**
After processing, `res = [0, 6]`, which are the starting indices of anagrams "cba" and "bac".

