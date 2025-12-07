## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** spells and potions arrays can have up to 10^5 elements each. success can be up to 10^10.
* **Time Complexity:** O(m log m + n log m) where m is potions length and n is spells length. Sorting takes O(m log m), and for each spell we do binary search O(log m).
* **Space Complexity:** O(1) excluding the result array, which is O(n).
* **Edge Case:** If all potions are too weak for a spell, return 0 for that spell.

**1.2 High-level approach:**

The goal is to count how many potions form successful pairs with each spell. A pair is successful if spell * potion >= success. We sort potions and use binary search to find the minimum potion strength needed.

![Binary search showing how we find the minimum potion strength for each spell]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** For each spell, check all potions. This is O(n * m) time.
* **Optimized (Sorting + Binary Search):** Sort potions once, then for each spell, use binary search to find the minimum potion strength needed. This is O(m log m + n log m) time.
* **Why it's better:** Binary search reduces the time per spell from O(m) to O(log m), making it much faster for large inputs.

**1.4 Decomposition:**

1. Sort the potions array.
2. For each spell:
   - Calculate target = ceil(success / spell).
   - Use binary search to find the leftmost potion >= target.
   - Count successful pairs = n - left_index.
3. Return the array of counts.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: spells = [5,1,3], potions = [1,2,3,4,5], success = 7

We initialize:
* Sort potions: [1,2,3,4,5] (already sorted)
* `res = []`

**2.2 Start Checking/Processing:**

We iterate through each spell.

**2.3 Trace Walkthrough:**

| Spell | Target (ceil(7/spell)) | Binary Search | Left Index | Successful Pairs |
|-------|------------------------|---------------|------------|------------------|
| 5 | ceil(7/5) = 2 | Find leftmost >= 2 | 1 (value 2) | 5-1=4 |
| 1 | ceil(7/1) = 7 | Find leftmost >= 7 | 5 (not found) | 5-5=0 |
| 3 | ceil(7/3) = 3 | Find leftmost >= 3 | 2 (value 3) | 5-2=3 |

**2.4 Increment and Loop:**

After processing each spell, we append the count to results.

**2.5 Return Result:**

After processing all spells, `res = [4,0,3]` is returned.

