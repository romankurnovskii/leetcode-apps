## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to read n characters from a file using the read4 API, but the read function may be called multiple times. We must maintain state between calls to handle leftover characters from previous read4 calls that weren't fully consumed.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 1000` characters per read call
- **Time Complexity:** O(n) per read call - we process at most n characters per call
- **Space Complexity:** O(1) amortized - we use a queue that stores at most 4 characters at a time
- **Edge Case:** If read is called with n=0, return 0. If previous calls left characters in the queue, use them first

**1.2 High-level approach:**
We maintain a queue to store leftover characters from previous read4 calls. When read is called, we first consume characters from the queue, then call read4 if needed. Any extra characters from read4 are stored in the queue for future calls.

![Maintaining buffer between multiple read calls](https://assets.leetcode.com/static_assets/others/read4-multiple-calls.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Ignore previous state and start fresh each time, which would lose leftover characters and produce incorrect results.
- **Optimized Strategy:** Use a queue to buffer leftover characters between calls, ensuring we don't lose any data and minimize read4 calls.
- **Why it's better:** We correctly handle multiple calls by preserving state, and we avoid redundant read4 calls by reusing buffered characters.

**1.4 Decomposition:**
1. Initialize a queue in the constructor to store leftover characters
2. When read is called, first check if the queue has characters and use them
3. If more characters are needed, call read4 to get new characters
4. Store any extra characters from read4 (beyond what's needed) in the queue
5. Return the total number of characters read

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: First call `read(buf, 1)`, then `read(buf, 2)`, file contains "abc"
- Initialize `self.queue = []` in constructor
- First call needs 1 character, second call needs 2 characters

**2.2 Start Reading:**
We begin by checking the queue for leftover characters, then call read4 if needed.

**2.3 Trace Walkthrough:**

| Call | n | Queue Before | Action | read4() | Queue After | Return |
|------|---|--------------|--------|---------|------------|--------|
| 1 | 1 | [] | Call read4 | 4 chars: ['a','b','c',''] | ['b','c'] | 1 |
| 2 | 2 | ['b','c'] | Use queue first | - | [] | 2 |

**Detailed first call:**
- Queue is empty, call read4 → gets ['a','b','c',''] (3 valid chars)
- Need 1 char, take 'a' from read4 result
- Store remaining ['b','c'] in queue
- Return 1

**Detailed second call:**
- Queue has ['b','c'], take both
- Need 2 chars, have 2 in queue, perfect
- Return 2

**2.4 Increment and Loop:**
We continue processing characters from the queue and calling read4 until we've read n characters or reached EOF.

**2.5 Return Result:**
Return the total number of characters read (idx). The queue now contains any leftover characters for future read calls.

