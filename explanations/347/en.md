## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Array length n is between 1 and 10^5, and values are between -10^4 and 10^4.
- **Time Complexity:** O(n) - We iterate through the array once to count frequencies, then iterate through buckets once.
- **Space Complexity:** O(n) - We use a dictionary to count frequencies and buckets array of size n+1.
- **Edge Case:** If k equals the number of unique elements, return all unique elements.

**1.2 High-level approach:**
The goal is to find the k most frequent elements in an array. We use bucket sort: count frequencies, then place numbers into buckets indexed by frequency, and collect the top k from the highest frequency buckets.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Count frequencies, then sort by frequency and take top k. This takes O(n log n) time.
- **Optimized Strategy (Bucket Sort):** Use bucket sort where each bucket index represents a frequency. This takes O(n) time since frequencies are bounded by n.
- **Emphasize the optimization:** Bucket sort eliminates the need for sorting, reducing time complexity from O(n log n) to O(n).

**1.4 Decomposition:**
1. Count the frequency of each number using a dictionary.
2. Create buckets where index represents frequency.
3. Place each number into its frequency bucket.
4. Iterate through buckets from highest to lowest frequency, collecting numbers until we have k elements.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `nums = [1,1,1,2,2,3]`, `k = 2`

Initialize:
- `count = {}` (empty dictionary)
- `buckets = [[] for _ in range(7)]` (7 buckets for frequencies 0-6)
- `res = []` (empty result list)

**2.2 Start Counting:**
Count frequencies: `count = {1: 3, 2: 2, 3: 1}`

**2.3 Trace Walkthrough:**

| Number | Frequency | Bucket Index | Bucket Contents |
|--------|-----------|--------------|-----------------|
| 1 | 3 | 3 | [1] |
| 2 | 2 | 2 | [2] |
| 3 | 1 | 1 | [3] |

After placing in buckets:
- `buckets[3] = [1]`
- `buckets[2] = [2]`
- `buckets[1] = [3]`

**2.4 Collect Top K:**
Iterate from bucket 3 down to bucket 1:
- Bucket 3: Add 1 to res → `res = [1]`
- Bucket 2: Add 2 to res → `res = [1, 2]` (k=2, done)

**2.5 Return Result:**
Return `[1, 2]` as the top 2 most frequent elements.

