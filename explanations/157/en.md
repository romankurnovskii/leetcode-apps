## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to read n characters from a file using the read4 API, which reads exactly 4 characters at a time. We must handle cases where n might not be a multiple of 4, and we need to stop reading when we've read n characters or reached the end of the file.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 1000` characters to read
- **Time Complexity:** O(n) - we read at most n characters, and each read4 call reads up to 4 characters
- **Space Complexity:** O(1) - we use a fixed-size buffer of 4 characters
- **Edge Case:** If n is 0, we return 0 without reading. If the file has fewer than n characters, we return the actual number read

**1.2 High-level approach:**
We repeatedly call read4 to read 4 characters at a time, copying them to the destination buffer until we've read n characters or reached the end of the file. We handle partial reads when n is not a multiple of 4.

![Reading characters in chunks of 4](https://assets.leetcode.com/static_assets/others/read4-api.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Call read4 once for every character needed, which would be inefficient and incorrect since read4 reads 4 characters at a time.
- **Optimized Strategy:** Call read4 in a loop, reading 4 characters at a time and copying only what we need. This minimizes API calls.
- **Why it's better:** We make the minimum number of read4 calls needed, reading in optimal chunks of 4.

**1.4 Decomposition:**
1. Create a temporary buffer of size 4 to store characters from read4
2. Initialize a counter to track total characters read
3. Loop while we haven't read n characters yet
4. Call read4 to get up to 4 characters
5. Copy the minimum of (characters read, remaining needed) to the destination buffer
6. Update the total count and continue until done

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 5`, file contains "abcde"
- Initialize `buf4 = ['', '', '', '']` (temporary buffer)
- Initialize `total = 0` (characters read so far)

**2.2 Start Reading:**
We begin the loop to read characters until we've read n characters or reached EOF.

**2.3 Trace Walkthrough:**

| Iteration | total | n - total | read4() returns | buf4 | Copy to buf | total after |
|-----------|-------|-----------|------------------|------|-------------|--------------|
| 1 | 0 | 5 | 4 | ['a','b','c','d'] | buf[0:4] = ['a','b','c','d'] | 4 |
| 2 | 4 | 1 | 1 | ['e','','',''] | buf[4:5] = ['e'] | 5 |
| End | 5 | 0 | - | - | - | 5 |

**2.4 Increment and Loop:**
After each read4 call, we update total by the number of characters copied. We continue until total >= n or read4 returns 0 (EOF).

**2.5 Return Result:**
Return `total = 5`, which is the number of characters successfully read into the buffer. The buffer now contains ['a','b','c','d','e'].

