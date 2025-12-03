# Problem 287: Find the Duplicate Number
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/find-the-duplicate-number/

## Explanation

### Strategy (The "Why")

The problem asks us to find the duplicate number in an array of $n+1$ integers where each integer is in $[1, n]$ and exactly one number appears twice.

**1.1 Constraints & Complexity:**

- **Input Constraints:** Array length is $n+1$ where $1 \leq n \leq 10^5$, and values are in $[1, n]$.
- **Time Complexity:** $O(n)$ - Floyd's cycle detection requires at most two passes through the array.
- **Space Complexity:** $O(1)$ - We only use constant extra space for two pointers.
- **Edge Case:** The duplicate can appear more than twice, but the problem guarantees exactly one duplicate.

**1.2 High-level approach:**

The goal is to find the duplicate without modifying the array and using only constant space. We treat the array as a linked list where `nums[i]` points to `nums[nums[i]]`, creating a cycle. The duplicate is the entrance to the cycle.

![Floyd's Cycle Detection](https://assets.leetcode.com/static_assets/others/duplicate-number-cycle.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use a hash set to track seen numbers. This takes $O(n)$ time and $O(n)$ space.
- **Optimized (Floyd's Cycle Detection):** Treat array as linked list, use tortoise and hare to find cycle, then find cycle entrance. This takes $O(n)$ time and $O(1)$ space.
- **Emphasize the optimization:** Floyd's algorithm achieves $O(1)$ space by using the array itself as the linked list structure, eliminating the need for extra storage.

**1.4 Decomposition:**

1. **Find Intersection:** Use slow and fast pointers to find where they meet in the cycle.
2. **Find Entrance:** Reset slow pointer to start, move both one step at a time until they meet. The meeting point is the duplicate.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `nums = [1,3,4,2,2]`.

Treat as linked list: `1 → 3 → 2 → 4 → 2 → 4 → ...` (cycle: 2 → 4 → 2)

**2.2 Start Detection:**

Initialize `slow = fast = nums[0] = 1`.

**2.3 Trace Walkthrough:**

**Phase 1: Find Intersection**
| Step | slow | fast | Action |
|------|------|------|--------|
| 0 | 1 | 1 | Start |
| 1 | nums[1]=3 | nums[nums[1]]=nums[3]=2 | Move |
| 2 | nums[3]=2 | nums[nums[2]]=nums[4]=2 | Move |
| 3 | nums[2]=4 | nums[nums[2]]=nums[4]=2 | Move |
| 4 | nums[4]=2 | nums[nums[2]]=nums[4]=2 | **Meet at 2** |

**Phase 2: Find Entrance**
| Step | slow | fast | Action |
|------|------|------|--------|
| 0 | nums[0]=1 | 2 | Reset slow to start |
| 1 | nums[1]=3 | nums[2]=4 | Move |
| 2 | nums[3]=2 | nums[4]=2 | **Meet at 2** |

**2.4 Result:**

The duplicate is `2`, which is the entrance to the cycle.

**2.5 Return Result:**

The function returns `2`.

> **Note:** The key insight is that the array indices and values form a linked list with a cycle. The duplicate number creates the cycle, and Floyd's algorithm finds where the cycle starts.

