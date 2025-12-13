## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** Array length can be up to 10⁵, and k can be up to the array length.
  * **Time Complexity:** O(n) - Each element is added and removed from the deque at most once.
  * **Space Complexity:** O(k) - The deque stores at most k indices.
  * **Edge Case:** When k equals the array length, we return a single maximum value.

**High-level approach**
We use a deque (double-ended queue) to maintain indices of elements in decreasing order. As we slide the window, we remove indices outside the window and indices whose values are smaller than the current element.

**Brute force vs. optimized strategy**

  * **Brute Force:** For each window position, scan all k elements to find the maximum. This is O(n*k).
  * **Optimized Strategy:** Use a deque to maintain a monotonic decreasing sequence. This allows O(1) access to the maximum and O(n) total time.

**Decomposition**

1.  **Initialize Deque:** Create a deque to store indices in decreasing order of their values.
2.  **Process Each Element:** For each element, remove outdated indices and smaller values.
3.  **Add Current Index:** Add the current index to the deque.
4.  **Record Maximum:** Once we have a full window, add the maximum to the result.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`.
    We initialize `dq = deque()` and `res = []`.

2.  **Start Processing:**
    We iterate through each index `i` from 0 to len(nums)-1.

3.  **Trace Walkthrough:**
    
    | i | nums[i] | Window | Deque (indices) | Max | Action |
    |---|---------|--------|-----------------|-----|--------|
    | 0 | 1 | [1] | [0] | - | Add index 0 |
    | 1 | 3 | [1,3] | [1] | - | Remove 0 (3>1), add 1 |
    | 2 | -1 | [1,3,-1] | [1,2] | 3 | Window full, max = nums[1] = 3 |
    | 3 | -3 | [3,-1,-3] | [1,2,3] | 3 | Remove outdated, max = 3 |
    | 4 | 5 | [-1,-3,5] | [4] | 5 | Remove all (5>all), max = 5 |
    | 5 | 3 | [-3,5,3] | [4,5] | 5 | Add 5, max = 5 |
    | 6 | 6 | [5,3,6] | [6] | 6 | Remove all (6>all), max = 6 |
    | 7 | 7 | [3,6,7] | [7] | 7 | Remove all (7>all), max = 7 |

4.  **Result:**
    After processing, `res = [3, 3, 5, 5, 6, 7]`

5.  **Return Result:**
    Return the result array `[3, 3, 5, 5, 6, 7]`.

