## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** a, b, and c can be up to 10^9.
* **Time Complexity:** O(log(max(a,b,c))) - We process each bit position, and the number of bits is logarithmic in the value.
* **Space Complexity:** O(1) - We only use a constant amount of extra space.
* **Edge Case:** If a OR b already equals c, return 0 (no flips needed).

**1.2 High-level approach:**

The goal is to find the minimum number of bit flips needed to make (a OR b) equal to c. We check each bit position and determine how many flips are needed.

![Bit manipulation showing how each bit position is checked and flipped]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Try all possible combinations of bit flips. This is exponential.
* **Optimized (Bit-by-bit Check):** Check each bit position independently. For each position, if (a_bit OR b_bit) != c_bit, calculate the minimum flips needed. This is O(log(max(a,b,c))) time.
* **Why it's better:** Bit positions are independent, so we can process them separately and sum the flips needed.

**1.4 Decomposition:**

1. Initialize result counter to 0.
2. While any of a, b, or c is non-zero:
   - Extract the least significant bit of each.
   - Check if (a_bit OR b_bit) equals c_bit.
   - If not, calculate flips needed:
     - If c_bit is 1: flip one of a or b (1 flip).
     - If c_bit is 0: flip both a and b if they're both 1 (2 flips), or flip the one that's 1 (1 flip).
   - Right-shift all numbers.
3. Return total flips.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: a = 2 (binary 10), b = 6 (binary 110), c = 5 (binary 101)

We initialize:
* `res = 0`

**2.2 Start Checking/Processing:**

We enter a while loop while any number is non-zero.

**2.3 Trace Walkthrough:**

| Bit Pos | a_bit | b_bit | c_bit | a OR b | Match? | Flips Needed | res |
|---------|-------|-------|-------|--------|-------|--------------|-----|
| 0 | 0 | 0 | 1 | 0 | No | 1 (set a or b) | 1 |
| 1 | 1 | 1 | 0 | 1 | No | 2 (clear both) | 3 |
| 2 | 0 | 1 | 1 | 1 | Yes | 0 | 3 |

**2.4 Increment and Loop:**

After processing each bit, we right-shift all numbers and continue.

**2.5 Return Result:**

After processing all bits, `res = 3` is returned.

