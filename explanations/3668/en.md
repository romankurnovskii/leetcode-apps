## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= n <= 100`, `1 <= friends.length <= min(8, n)`.
- **Time Complexity:** O(n) where n is the length of order - we iterate through order once.
- **Space Complexity:** O(f) where f is the number of friends - we create a set and result list.
- **Edge Case:** All friends appear in order, or no friends appear.

**1.2 High-level approach:**
The goal is to return friends' IDs in their finishing order. We create a set of friends for O(1) lookup, then iterate through the order array and collect friends as we encounter them.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each friend, search through order to find its position - O(f*n) time.
- **Optimized Strategy:** Create a set for O(1) lookup, then single pass through order - O(n) time.

**1.4 Decomposition:**
1. Create a set from friends array for fast lookup.
2. Initialize an empty result list.
3. Iterate through the order array.
4. For each element in order, check if it's a friend.
5. If yes, add it to the result list.
6. Return the result list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `order = [3,1,2,5,4]`, `friends = [1,3,4]`. We create `friend_set = {1,3,4}` and `res = []`.

**2.2 Start Checking:**
We iterate through order and check membership in friend_set.

**2.3 Trace Walkthrough:**

| Element | In friend_set? | res |
|---------|----------------|-----|
| 3 | Yes | [3] |
| 1 | Yes | [3,1] |
| 2 | No | [3,1] |
| 5 | No | [3,1] |
| 4 | Yes | [3,1,4] |

**2.4 Increment and Loop:**
After checking each element, we move to the next until we've processed all elements in order.

**2.5 Return Result:**
Return `res = [3,1,4]`, which contains friends' IDs in their finishing order.

