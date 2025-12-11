## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to design a data structure that can record exam scores with timestamps and efficiently calculate the total score for exams taken within a time range.

**1.1 Constraints & Complexity:**

* **Input Size:** At most 10^5 calls to record() and totalScore(), with times and scores between 1 and 10^9.
* **Time Complexity:** O(log n) for totalScore() using binary search, O(1) amortized for record().
* **Space Complexity:** O(n) - We store times, scores, and prefix sums, where n is the number of records.
* **Edge Case:** If no exams exist in the time range, return 0.

**1.2 High-level approach:**

The goal is to maintain sorted lists of times and scores, along with prefix sums for efficient range sum queries. We use binary search to find the range of indices that fall within the query time range.

![Visualization showing sorted times with prefix sums for range queries]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** For each totalScore() call, iterate through all records and sum those in the time range. This is O(n) per query.
* **Optimized (Binary Search + Prefix Sum):** Maintain sorted times and prefix sums. Use binary search to find the range bounds in O(log n), then use prefix sums to calculate the sum in O(1). This is O(log n) per query.
* **Why it's better:** Binary search reduces query time from O(n) to O(log n), and prefix sums allow O(1) sum calculation once we know the range.

**1.4 Decomposition:**

1. Maintain three arrays: times (sorted), scores, and prefix_sum.
2. In record(), append the time and score, and update the prefix sum.
3. In totalScore(), use binary search to find the left bound (first time >= startTime) and right bound (first time > endTime).
4. If left >= right, return 0 (no exams in range).
5. Otherwise, return prefix_sum[right] - prefix_sum[left].

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example from the problem:
* `record(1, 98)`
* `totalScore(1, 1)`
* `record(5, 99)`
* `totalScore(1, 5)`

We initialize:
* `times = []`
* `scores = []`
* `prefix_sum = [0]`

**2.2 Start Recording:**

We record exams and update our data structures.

**2.3 Trace Walkthrough:**

| Step | Operation       | times | scores  | prefix_sum | Result                            |
| ---- | --------------- | ----- | ------- | ---------- | --------------------------------- |
| 1    | record(1,98)    | [1]   | [98]    | [0,98]     | -                                 |
| 2    | totalScore(1,1) | [1]   | [98]    | [0,98]     | 98 (prefix_sum[1]-prefix_sum[0])  |
| 3    | record(5,99)    | [1,5] | [98,99] | [0,98,197] | -                                 |
| 4    | totalScore(1,5) | [1,5] | [98,99] | [0,98,197] | 197 (prefix_sum[2]-prefix_sum[0]) |

At step 4, binary search finds left=0 (first time >= 1) and right=2 (first time > 5), so we return prefix_sum[2] - prefix_sum[0] = 197.

**2.4 Increment and Loop:**

Each record() call appends to the arrays and updates prefix sums. Each totalScore() call uses binary search to find the range.

**2.5 Return Result:**

After processing queries, we return the sum of scores in the specified time range using prefix sums.
