## Explanation

### Strategy (The "Why")

We need to implement a `RecentCounter` class that counts the number of recent requests within the past 3000 milliseconds. Each call to `ping(t)` adds a new request at time $t$ and returns the number of requests in the range $[t-3000, t]$.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of calls to `ping` can be up to $10^4$.
- **Value Range:** Time values $t$ are strictly increasing and between $1$ and $10^9$.
- **Time Complexity:** $O(1)$ amortized - Each `ping` operation is $O(1)$ amortized because each request is added once and removed at most once.
- **Space Complexity:** $O(n)$ where $n$ is the number of requests in the current 3000ms window. In the worst case, if all requests are within 3000ms, this is $O(n)$.
- **Edge Case:** If `ping` is called with times that are more than 3000ms apart, old requests are removed from the queue.

**1.2 High-level approach:**

The goal is to maintain a sliding window of requests within the past 3000ms.

![Recent Counter](https://assets.leetcode.com/uploads/2021/09/03/chrome_2021-09-03_10-30-58.png)

We use a queue (deque) to store request times. When a new request arrives, we remove all requests outside the 3000ms window, then add the new request and return the queue size.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Store all requests in a list and filter out old ones each time. This could be inefficient if we check all requests.
- **Optimized Strategy (Queue):** Use a deque to store requests. Since times are strictly increasing, we only need to remove from the front. This is efficient.
- **Why it's better:** The queue approach allows us to efficiently remove old requests from the front while adding new ones at the back. Since times are increasing, we never need to check the middle of the queue.

**1.4 Decomposition:**

1. Initialize an empty deque in the constructor.
2. In `ping(t)`:
   - Add the current time $t$ to the queue.
   - Remove all requests from the front that are older than $t - 3000$.
   - Return the size of the queue (number of requests in the window).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `ping(1)`, `ping(100)`, `ping(3001)`, `ping(3002)`

We initialize:
- `queue = deque()`

**2.2 Start Processing:**

We process each ping call.

**2.3 Trace Walkthrough:**

| Call | Time | Queue Before | Remove Old | Queue After | Return |
|------|------|--------------|------------|-------------|--------|
| `ping(1)` | 1 | [] | None | [1] | 1 |
| `ping(100)` | 100 | [1] | None ($1 \geq 100-3000$) | [1, 100] | 2 |
| `ping(3001)` | 3001 | [1, 100] | Remove 1 ($1 < 3001-3000$) | [100, 3001] | 2 |
| `ping(3002)` | 3002 | [100, 3001] | Remove 100 ($100 < 3002-3000$) | [3001, 3002] | 2 |

**2.4 Explanation:**

- `ping(1)`: Window $[1-3000, 1] = [-2999, 1]$, contains [1] → return 1
- `ping(100)`: Window $[100-3000, 100] = [-2900, 100]$, contains [1, 100] → return 2
- `ping(3001)`: Window $[3001-3000, 3001] = [1, 3001]$, contains [100, 3001] (1 is removed) → return 2
- `ping(3002)`: Window $[3002-3000, 3002] = [2, 3002]$, contains [3001, 3002] (100 is removed) → return 2

**2.5 Return Result:**

Each `ping` call returns the number of requests in the current 3000ms window.

> **Note:** Since times are strictly increasing, we only need to check and remove from the front of the queue. All requests in the queue are already in order, so we never need to check the middle or back.

