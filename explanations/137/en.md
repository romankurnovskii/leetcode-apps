## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 3 \times 10^4$ elements. Each element appears exactly three times except one that appears once. Values are in the range $[-2^{31}, 2^{31} - 1]$.
- **Time Complexity:** $O(n)$ where $n$ is the number of elements. We traverse the array once.
- **Space Complexity:** $O(1)$ as we only use two integer variables to track bit states.
- **Edge Case:** If the array has only one element, return that element.

**1.2 High-level approach:**

The goal is to find the single element that appears once when all other elements appear three times. We use bit manipulation to track the state of each bit position. Since each number appears three times, we need to count bits modulo 3.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use a hash map to count occurrences, then find the element with count 1. This requires $O(n)$ space.
- **Optimized Strategy:** Use bit manipulation with two variables (`ones` and `twos`) to track bits that appear once and twice. This is $O(n)$ time and $O(1)$ space.
- **Why optimized is better:** The bit manipulation approach achieves $O(1)$ space complexity while maintaining linear time.

**1.4 Decomposition:**

1. Initialize `ones = 0` (bits appearing once) and `twos = 0` (bits appearing twice).
2. For each number, update `ones` and `twos` using XOR and AND operations.
3. The logic ensures that bits appearing three times are reset to 0, leaving only bits from the single element.
4. Return `ones` which contains the single element.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [2,2,3,2]`

We initialize:
- `ones = 0` (binary: `0000`)
- `twos = 0` (binary: `0000`)

**2.2 Start Checking:**

We process each number in the array, updating `ones` and `twos` to track bit states.

**2.3 Trace Walkthrough:**

| Number | Binary | ones before | twos before | ones after | twos after |
|--------|--------|-------------|-------------|------------|------------|
| 2 | 0010 | 0000 | 0000 | 0010 | 0000 |
| 2 | 0010 | 0010 | 0000 | 0000 | 0010 |
| 3 | 0011 | 0000 | 0010 | 0011 | 0010 |
| 2 | 0010 | 0011 | 0010 | 0001 | 0000 |

**Explanation:**
- First 2: appears once → `ones = 2`, `twos = 0`
- Second 2: appears twice → `ones = 0`, `twos = 2`
- 3: new number → `ones = 3`, `twos = 2`
- Third 2: completes triple → `ones = 1` (which is 3), `twos = 0`

**2.4 Increment and Loop:**

For each number `num`:
- `ones = (ones ^ num) & ~twos`: XOR adds the number to ones, but only if it's not in twos.
- `twos = (twos ^ num) & ~ones`: XOR adds the number to twos, but only if it's not in ones.

This ensures:
- First occurrence: number goes to `ones`.
- Second occurrence: number moves from `ones` to `twos`.
- Third occurrence: number is removed from both.

**2.5 Return Result:**

After processing all numbers, `ones = 3` (binary: `0011`), which is the single element that appears once. We return `3`.

