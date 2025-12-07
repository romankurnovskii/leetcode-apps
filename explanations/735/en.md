## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** Asteroids array can have up to 10^4 elements.
* **Time Complexity:** O(n) - Each asteroid is processed once, where n is the length of asteroids.
* **Space Complexity:** O(n) - In the worst case, the stack stores all asteroids.
* **Edge Case:** If all asteroids move in the same direction, no collisions occur.

**1.2 High-level approach:**

The goal is to simulate asteroid collisions where positive values move right, negative values move left. When two asteroids moving toward each other collide, the smaller one explodes. If equal, both explode.

![Stack simulation showing asteroid collisions]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Repeatedly scan the array to find and resolve collisions until no more occur. This could be O(n^2).
* **Optimized (Stack):** Use a stack to process asteroids. When a negative asteroid encounters a positive one on the stack, resolve the collision. This is O(n) time.
* **Why it's better:** The stack approach processes collisions in one pass, avoiding multiple scans.

**1.4 Decomposition:**

1. Use a stack to store surviving asteroids.
2. For each asteroid:
   - If it's positive or stack is empty, push it.
   - If it's negative and stack top is positive, check collision:
     - If stack top is smaller, pop it and continue checking.
     - If equal, pop stack top and don't add current.
     - If stack top is larger, don't add current.
3. Return the stack as result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: asteroids = [5,10,-5]

We initialize:
* `res = []` (stack to store surviving asteroids)

**2.2 Start Checking/Processing:**

We iterate through each asteroid.

**2.3 Trace Walkthrough:**

| Asteroid | res (before) | Condition | Action | res (after) |
|----------|--------------|-----------|--------|------------|
| 5 | [] | Positive | Push 5 | [5] |
| 10 | [5] | Positive | Push 10 | [5,10] |
| -5 | [5,10] | Negative, top positive | 10 > 5, don't add -5 | [5,10] |

**2.4 Increment and Loop:**

After processing each asteroid, we move to the next one.

**2.5 Return Result:**

After processing all asteroids, `res = [5,10]` is returned.

