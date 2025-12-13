## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** We have three arrays of length `n` where `1 <= n <= 100`. The arrays are small enough that we can use simple iteration.
  * **Time Complexity:** O(n log n) - We iterate through all coupons once (O(n)) and then sort them (O(n log n)). The sorting dominates the complexity.
  * **Space Complexity:** O(n) - We store valid coupons in a list for sorting.
  * **Edge Case:** Empty code strings or codes with special characters must be filtered out.

**High-level approach**
We need to validate coupons based on three conditions: code format, business line validity, and active status. Valid coupons are then sorted by business line priority and code name.

**Brute force vs. optimized strategy**

  * **Brute Force:** Check each coupon individually and sort the entire result set at the end. This is what we're doing, and it's efficient for the given constraints.
  * **Optimized Strategy:** Same approach - filter valid coupons and sort. The optimization comes from using a priority map for efficient business line ordering.

**Decomposition**

1.  **Create Priority Map:** Map business lines to their priority order for sorting.
2.  **Filter Valid Coupons:** Check each coupon for the three validation conditions.
3.  **Store with Priority:** Store valid coupons with their priority for sorting.
4.  **Sort and Return:** Sort by business line priority, then by code name, and return only the codes.

### Steps

1.  **Initialization & Example Setup:**
    Let's say we have:
    - `code = ["SAVE20", "", "PHARMA5", "SAVE@20"]`
    - `businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]`
    - `isActive = [true, true, true, true]`
    
    We create a priority map: `{"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}`

2.  **Start Checking:**
    Initialize `res = []` to store valid coupons with their priority.

3.  **Trace Walkthrough:**
    
    | Index | Code | Business Line | Is Active | Code Valid? | Business Line Valid? | Action |
    |-------|------|---------------|-----------|------------|---------------------|--------|
    | 0 | "SAVE20" | "restaurant" | true | Yes | Yes | Add (3, "SAVE20") |
    | 1 | "" | "grocery" | true | No (empty) | Yes | Skip |
    | 2 | "PHARMA5" | "pharmacy" | true | Yes | Yes | Add (2, "PHARMA5") |
    | 3 | "SAVE@20" | "restaurant" | true | No (@ char) | Yes | Skip |

4.  **Sort and Return:**
    After filtering, `res = [(2, "PHARMA5"), (3, "SAVE20")]`
    After sorting (already sorted by priority), we return `["PHARMA5", "SAVE20"]`

5.  **Return Result:**
    The final result is `["PHARMA5", "SAVE20"]` - sorted by business line priority (pharmacy before restaurant) and then by code name within each category.
