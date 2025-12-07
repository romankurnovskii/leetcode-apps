## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The senate string can have up to 10^4 characters.
* **Time Complexity:** O(n) - Each senator is processed at most once, where n is the length of senate.
* **Space Complexity:** O(n) - We use two queues to store senator indices.
* **Edge Case:** If senate has only one party, that party wins immediately.

**1.2 High-level approach:**

The goal is to simulate the voting process where each senator bans the next opposing senator. We use queues to track senators from each party and simulate rounds until one party has all remaining senators.

![Queue simulation showing how senators ban each other in rounds]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Simulate each round by iterating through the entire senate string, marking banned senators. This is inefficient.
* **Optimized (Queue-based):** Use two queues to track indices of Radiant and Dire senators. Compare indices to determine who bans whom, and add winners back with offset indices for next round. This is O(n) time.
* **Why it's better:** The queue approach efficiently tracks active senators and simulates rounds without redundant iterations.

**1.4 Decomposition:**

1. Separate senators into two queues based on party (R or D).
2. While both queues have senators, compare the front indices.
3. The senator with the smaller index bans the other (wins this round).
4. Add the winner back to their queue with an offset (index + n) for the next round.
5. Continue until one queue is empty.
6. Return the party of the remaining queue.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: senate = "RD"

We initialize:
* `r_queue = [0]` (Radiant at index 0)
* `d_queue = [1]` (Dire at index 1)
* `n = 2` (length of senate)

**2.2 Start Checking/Processing:**

We enter a while loop while both queues are non-empty.

**2.3 Trace Walkthrough:**

| Round | r_queue | d_queue | r_idx | d_idx | Winner | Action |
|-------|---------|---------|-------|-------|--------|--------|
| 1 | [0] | [1] | 0 | 1 | R (0 < 1) | r_queue = [2], d_queue = [] |

**2.4 Increment and Loop:**

After each comparison, the winner is added back with offset n, and we continue to the next round.

**2.5 Return Result:**

After round 1, d_queue is empty, so we return "Radiant".

