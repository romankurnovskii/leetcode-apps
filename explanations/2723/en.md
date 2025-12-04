## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** Two promises that resolve with numbers.
- **Time Complexity:** O(1) - we wait for both promises and add their values.
- **Space Complexity:** O(1) - constant space.
- **Edge Case:** Promises might resolve at different times.

**1.2 High-level approach:**
The goal is to return a new promise that resolves with the sum of two input promises. We use `Promise.all()` to wait for both promises, then add their resolved values.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - Promise.all() is the standard approach.
- **Optimized Strategy:** Use async/await with Promise.all() for clean code.

**1.4 Decomposition:**
1. Wait for both promises to resolve using Promise.all().
2. Extract the resolved values.
3. Add them together.
4. Return the sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `promise1` resolves to 2, `promise2` resolves to 5. We want to return a promise that resolves to 7.

**2.2 Start Checking:**
We await both promises and add their values.

**2.3 Trace Walkthrough:**

| Step | Operation | Result |
|------|-----------|--------|
| 1 | await Promise.all([promise1, promise2]) | [2, 5] |
| 2 | val1 = 2, val2 = 5 | - |
| 3 | res = 2 + 5 | 7 |

**2.4 Increment and Loop:**
Not applicable - this is a single async operation.

**2.5 Return Result:**
Return a promise that resolves to `res = 7`.

