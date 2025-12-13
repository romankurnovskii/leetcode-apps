## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** Array length can be up to 10⁵, and values can range from -10⁶ to 10⁶.
  * **Time Complexity:** O(n) - We make a single pass through the array to partition elements.
  * **Space Complexity:** O(n) - We create three lists to store elements (less, equal, greater).
  * **Edge Case:** All elements equal to pivot results in returning the original array.

**High-level approach**
We partition the array into three groups: elements less than pivot, elements equal to pivot, and elements greater than pivot. We maintain the relative order within each group, then combine them.

**Brute force vs. optimized strategy**

  * **Brute Force:** Sort the array - but this doesn't maintain relative order of elements within groups.
  * **Optimized Strategy:** Use three separate lists to collect elements in a single pass, preserving relative order.

**Decomposition**

1.  **Create Three Lists:** Initialize lists for elements less than, equal to, and greater than pivot.
2.  **Partition Elements:** Iterate through the array and place each element into the appropriate list.
3.  **Combine Lists:** Concatenate the three lists in order: less, equal, greater.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `nums = [9, 12, 5, 10, 14, 3, 10]` and `pivot = 10`.
    We create three empty lists: `less = []`, `equal = []`, `greater = []`.

2.  **Start Processing:**
    We iterate through each element in `nums`.

3.  **Trace Walkthrough:**
    
    | Element | Comparison | Action | less | equal | greater |
    |---------|-------------|--------|------|-------|---------|
    | 9 | 9 < 10 | Add to less | [9] | [] | [] |
    | 12 | 12 > 10 | Add to greater | [9] | [] | [12] |
    | 5 | 5 < 10 | Add to less | [9, 5] | [] | [12] |
    | 10 | 10 == 10 | Add to equal | [9, 5] | [10] | [12] |
    | 14 | 14 > 10 | Add to greater | [9, 5] | [10] | [12, 14] |
    | 3 | 3 < 10 | Add to less | [9, 5, 3] | [10] | [12, 14] |
    | 10 | 10 == 10 | Add to equal | [9, 5, 3] | [10, 10] | [12, 14] |

4.  **Combine:**
    `res = less + equal + greater = [9, 5, 3] + [10, 10] + [12, 14] = [9, 5, 3, 10, 10, 12, 14]`

5.  **Return Result:**
    Return the combined array `[9, 5, 3, 10, 10, 12, 14]`.

