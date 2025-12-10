## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The integer `n` can be up to 10^9, but we only process its digits (at most 10 digits).
* **Time Complexity:** O(d^2) where d is the number of unique digits (at most 10), effectively O(1).
* **Space Complexity:** O(d) for storing digit frequencies, effectively O(1).
* **Edge Case:** When a digit appears only once, we cannot use it twice in the product.

**1.2 High-level approach:**

The goal is to find the maximum product of any two digits from the number. We need to consider all pairs of digits, but can only use the same digit twice if it appears more than once in the original number.

![Visualization showing digits extracted from a number and all possible pairs being considered]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Extract all digits, generate all pairs (including same digit twice), filter invalid pairs, find max. This is O(d^2) where d is number of digits.
* **Optimized (Frequency-based):** Count digit frequencies first, then only consider pairs where same-digit pairs are only allowed if frequency > 1. This is also O(d^2) but more efficient in practice.
* **Why it's better:** By checking frequencies upfront, we avoid generating invalid pairs and make the logic clearer.

**1.4 Decomposition:**

1. Extract all digits from the number and count their frequencies.
2. Get unique digits from the frequency map.
3. For each pair of unique digits, check if the pair is valid (same digit can only be used twice if frequency > 1).
4. Calculate the product for valid pairs and track the maximum.
5. Return the maximum product.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 124`

We initialize:
* Extract digits: `digits = [4, 2, 1]` (extracted in reverse order)
* Count frequencies: `digit_count = {1: 1, 2: 1, 4: 1}`
* `unique_digits = [1, 2, 4]`
* `res = 0`

**2.2 Start Checking:**

We iterate through all pairs of unique digits.

**2.3 Trace Walkthrough:**

| i   | j   | d1  | d2  | Same digit? | Frequency check | Product   | res |
| --- | --- | --- | --- | ----------- | --------------- | --------- | --- |
| 0   | 0   | 1   | 1   | Yes         | 1 > 1? No       | Skip      | 0   |
| 0   | 1   | 1   | 2   | No          | -               | 1 * 2 = 2 | 2   |
| 0   | 2   | 1   | 4   | No          | -               | 1 * 4 = 4 | 4   |
| 1   | 1   | 2   | 2   | Yes         | 1 > 1? No       | Skip      | 4   |
| 1   | 2   | 2   | 4   | No          | -               | 2 * 4 = 8 | 8   |
| 2   | 2   | 4   | 4   | Yes         | 1 > 1? No       | Skip      | 8   |

**2.4 Increment and Loop:**

We continue checking all pairs (i, j) where i <= j to cover all combinations.

**2.5 Return Result:**

After checking all valid pairs, we return `res = 8`, which is the maximum product (2 * 4).
