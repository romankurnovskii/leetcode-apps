## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Capacity is between 1 and 10^4, keys are between 0 and 10^5, values are between 0 and 10^9. At most 2 * 10^5 calls to get and put.
- **Time Complexity:** O(1) average for both get and put operations - We use hash maps and ordered dictionaries for constant-time access.
- **Space Complexity:** O(capacity) - We store at most capacity key-value pairs.
- **Edge Case:** When capacity is 0, all operations return -1 or do nothing.

**1.2 High-level approach:**
The goal is to implement an LFU (Least Frequently Used) cache that evicts the least frequently used item when at capacity. For ties in frequency, we evict the least recently used item. We maintain frequency buckets using OrderedDict to track both frequency and recency.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Store (value, frequency, timestamp) for each key, and find minimum on eviction by scanning all keys. This takes O(capacity) time for eviction.
- **Optimized Strategy (Frequency Buckets with OrderedDict):** Use frequency buckets where each bucket is an OrderedDict maintaining insertion order. This allows O(1) access and O(1) eviction.
- **Emphasize the optimization:** By organizing keys by frequency and using OrderedDict for recency, we can find the LFU key in O(1) time.

**1.4 Decomposition:**
1. Maintain a dictionary mapping keys to their frequencies.
2. Maintain frequency buckets: each frequency maps to an OrderedDict of keys.
3. Track the minimum frequency currently in use.
4. For get: update frequency, move key to new frequency bucket.
5. For put: if at capacity, evict from min_freq bucket (FIFO), then add/update key.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's trace: `capacity = 2`, operations: `put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`, `get(2)`, `get(3)`, `put(4,4)`, `get(1)`, `get(3)`, `get(4)`

Initialize:
- `key_to_freq = {}`
- `freq_to_keys = {1: OrderedDict()}`
- `key_to_val = {}`
- `min_freq = 1`

**2.2 Start Processing:**
Process each operation step by step.

**2.3 Trace Walkthrough:**

| Operation | Key | Value | State After | min_freq |
|-----------|-----|-------|-------------|----------|
| put(1,1) | 1 | 1 | {1:1}, freq1={1} | 1 |
| put(2,2) | 2 | 2 | {1:1,2:2}, freq1={1,2} | 1 |
| get(1) | 1 | 1 | {1:2,2:1}, freq1={2}, freq2={1} | 1 |
| put(3,3) | 3 | 3 | Evict 2, {1:2,3:1}, freq1={3}, freq2={1} | 1 |
| get(2) | 2 | -1 | Not found | 1 |
| get(3) | 3 | 3 | {1:2,3:2}, freq2={1,3} | 2 |
| put(4,4) | 4 | 4 | Evict 1, {3:2,4:1}, freq1={4}, freq2={3} | 1 |
| get(1) | 1 | -1 | Not found | 1 |
| get(3) | 3 | 3 | {3:3,4:1}, freq1={4}, freq3={3} | 1 |
| get(4) | 4 | 4 | {3:3,4:2}, freq2={4}, freq3={3} | 2 |

**2.4 Return Result:**
Final sequence: `[null, null, null, 1, null, -1, 3, null, -1, 3, 4]`

