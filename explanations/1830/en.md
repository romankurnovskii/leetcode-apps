## 1830. Count Good Meals [Medium]

https://leetcode.com/problems/count-good-meals

## Description
A **good meal** is a meal that contains **exactly two different food items** with a sum of deliciousness equal to a power of two.

You can pick **any** two different foods to make a good meal.

Given an array of integers `deliciousness` where `deliciousness[i]` is the deliciousness of the `iᵗʰ` item of food, return *the number of different **good meals** you can make from this list modulo* `10⁹ + 7`.

Note that items with different indices are considered different even if they have the same deliciousness value.

**Examples**

```tex
Example 1:
Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

Example 2:
Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
```

**Constraints**
```tex
- 1 <= deliciousness.length <= 10^5
- 0 <= deliciousness[i] <= 2^20
```

## Explanation

### Strategy
Let's restate the problem: You're given an array of food deliciousness values, and you need to count how many pairs of foods sum to a power of 2. A power of 2 is any number that can be written as 2ⁿ where n is a non-negative integer.

This is a **hash table problem** that requires finding pairs of numbers that sum to specific target values (powers of 2).

**What is given?** An array of integers representing food deliciousness, with values up to 2²⁰.

**What is being asked?** Count the number of pairs that sum to a power of 2.

**Constraints:** The array can be up to 100,000 elements long, with values up to 2²⁰.

**Edge cases:** 
- Empty array
- Single element array
- Array with all identical values
- Array with no valid pairs

**High-level approach:**
The solution involves generating all possible powers of 2 up to the maximum possible sum, then for each power, finding pairs of numbers that sum to it using a hash table.

**Decomposition:**
1. **Generate powers of 2**: Create all possible target sums up to 2 * max_deliciousness
2. **Use hash table**: Track frequency of each deliciousness value
3. **Find pairs**: For each power of 2, find pairs that sum to it
4. **Count combinations**: Handle duplicate values appropriately

**Brute force vs. optimized strategy:**
- **Brute force**: Check all possible pairs. This takes O(n²) time.
- **Optimized**: Use hash table to find pairs for each power of 2. This takes O(n * log max_val) time.

### Steps
Let's walk through the solution step by step using the first example: `deliciousness = [1,3,5,7,9]`

**Step 1: Generate powers of 2 up to maximum possible sum**
- Maximum possible sum: 2 * 9 = 18
- Powers of 2 up to 18: [1, 2, 4, 8, 16]

**Step 2: Create frequency hash table**
- `freq = {1: 1, 3: 1, 5: 1, 7: 1, 9: 1}`

**Step 3: Find pairs for each power of 2**
- **Target 1**: No pairs possible (all values ≥ 1)
- **Target 2**: No pairs possible (no two values sum to 2)
- **Target 4**: 
  - Check if 4 - 1 = 3 exists: Yes
  - Check if 4 - 3 = 1 exists: Yes
  - Check if 4 - 5 = -1 exists: No
  - Check if 4 - 7 = -3 exists: No
  - Check if 4 - 9 = -5 exists: No
  - Valid pairs: (1,3)
  - Count: 1

- **Target 8**:
  - Check if 8 - 1 = 7 exists: Yes
  - Check if 8 - 3 = 5 exists: Yes
  - Check if 8 - 5 = 3 exists: Yes
  - Check if 8 - 7 = 1 exists: Yes
  - Check if 8 - 9 = -1 exists: No
  - Valid pairs: (1,7), (3,5)
  - Count: 2

- **Target 16**:
  - Check if 16 - 1 = 15 exists: No
  - Check if 16 - 3 = 13 exists: No
  - Check if 16 - 5 = 11 exists: No
  - Check if 16 - 7 = 9 exists: Yes
  - Check if 16 - 9 = 7 exists: Yes
  - Valid pairs: (7,9)
  - Count: 1

**Step 4: Calculate total**
- Total good meals: 1 + 2 + 1 = 4

**Why this works:**
By generating all possible powers of 2 and using a hash table to find pairs efficiently, we can:
1. **Avoid brute force**: Don't need to check all O(n²) pairs
2. **Efficient lookup**: Hash table provides O(1) lookup time
3. **Complete coverage**: Check all possible target sums systematically

> **Note:** The key insight is that there are only a limited number of powers of 2 (at most 21 for the given constraints), so we can iterate through them efficiently. For each power, we use the hash table to find pairs in O(n) time.

**Time Complexity:** O(n * log max_val) - we iterate through powers of 2 and check each element  
**Space Complexity:** O(n) - we need to store the frequency hash table
