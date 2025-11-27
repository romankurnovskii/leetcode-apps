# Problem 3683: Earliest Time to Finish One Task

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/earliest-time-to-finish-one-task/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the earliest time when at least one task completes. Each task has a start time and a duration, so we calculate when each task finishes and find the minimum finish time.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most 100 tasks, and each start time and duration is at most 100.
- **Time Complexity:** $O(n)$ where $n$ is the number of tasks. We iterate through each task once to calculate its finish time.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space to store the minimum finish time.
- **Edge Case:** If all tasks have the same start time and duration, they all finish at the same time, which is the answer.

**1.2 High-level approach:**

The goal is to compute the finish time for each task (start time + duration) and return the minimum finish time.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Calculate all finish times, store them in an array, then find the minimum. This is $O(n)$ time and $O(n)$ space.
- **Optimized Strategy:** Calculate each finish time and immediately compare it with the current minimum, updating the minimum as needed. This is $O(n)$ time and $O(1)$ space.
- **Optimization:** We trade the need for an array by keeping only the minimum value, reducing space complexity from $O(n)$ to $O(1)$.

**1.4 Decomposition:**

1. Initialize a result variable to track the minimum finish time (start with a very large value).
2. Iterate through each task in the input array.
3. For each task, calculate its finish time by adding the start time and duration.
4. Compare the finish time with the current minimum and update the minimum if the finish time is smaller.
5. Return the minimum finish time found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `tasks = [[1,6],[2,3]]`.

- Task 1: starts at time 1, takes 6 units → finishes at time 1 + 6 = 7
- Task 2: starts at time 2, takes 3 units → finishes at time 2 + 3 = 5

We initialize `res = float('inf')` to represent an initially very large value that will be replaced by the first finish time we calculate.

**2.2 Start Checking:**

We begin iterating through the tasks array, starting with the first task.

**2.3 Trace Walkthrough:**

| Task | Start ($s_i$) | Duration ($t_i$) | Finish Time ($s_i + t_i$) | Current `res` | Action |
|------|---------------|-------------------|---------------------------|---------------|--------|
| 1    | 1             | 6                 | 7                         | $\infty$      | Update `res = min(∞, 7) = 7` |
| 2    | 2             | 3                 | 5                         | 7             | Update `res = min(7, 5) = 5` |

**2.4 Increment and Loop:**

After processing each task, we move to the next task in the array until all tasks have been processed.

**2.5 Return Result:**

After processing all tasks, `res` contains the minimum finish time, which is 5. This is the earliest time at which at least one task is finished.

