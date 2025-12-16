## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count subarrays where the minimum of the two ends is strictly greater than the maximum of all elements in between. A subarray must have length at least 3.

**1.1 Constraints & Complexity:**

- **Input Size:** `3 <= nums.length <= 10^5`, `nums[i] <= 10^9`, all elements are distinct
- **Time Complexity:** O(n) - Single pass with monotonic stack
- **Space Complexity:** O(n) - Stack can hold at most n indices
- **Edge Case:** Empty array or array with less than 3 elements returns 0

**1.2 High-level approach:**

A "bowl" subarray has the property that both endpoints are larger than all middle elements. We use a monotonic stack to efficiently find valid bowl subarrays. When we process each element as a potential right endpoint, we check if it can form bowls with elements in the stack.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all O(n²) subarrays of length >= 3, for each compute min(ends) and max(middle), then compare. This is O(n³) time.
- **Optimized (Monotonic Stack):** Use a decreasing stack. When we encounter an element that's >= stack top, we pop elements that can form bowls with current. This is O(n) time.
- **Why it's better:** The monotonic stack allows us to efficiently track potential left endpoints and count bowls without checking all pairs explicitly.

**1.4 Decomposition:**

1. Use a stack to maintain indices in decreasing order of values
2. For each element as right endpoint, pop elements from stack that are <= current
3. Each popped element forms a bowl with current if length >= 3
4. Check if current forms a bowl with stack top
5. Push current index to stack

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [2,5,3,1,4]`

- Initialize `res = 0` and empty stack
- Process each element from left to right

**2.2 Process Each Element:**

For each element at index `r` with value `val`:

**2.3 Pop Elements That Can Form Bowls:**

```python
while stack and nums[stack[-1]] <= val:
    l = stack.pop()
    if r - l + 1 >= 3:
        res += 1
```

When we pop an element at index `l`, it means `nums[l] <= val`. Since the stack maintains decreasing order, all elements between `l` and `r` are also <= `nums[l]` (otherwise they would have been popped earlier). This means `min(nums[l], nums[r]) = nums[l] > max(middle)`, forming a bowl.

**2.4 Check Bowl with Stack Top:**

```python
if stack and r - stack[-1] + 1 >= 3:
    res += 1
```

If stack is not empty, the top element is > `val`. Since stack maintains decreasing order, `min(nums[stack[-1]], nums[r]) = nums[r] > max(middle)`, forming a bowl.

**2.5 Push Current Index:**

```python
stack.append(r)
```

Add current index to maintain the decreasing order property.

**2.6 Return Result:**

After processing all elements, return the total count of bowl subarrays.

**Time Complexity:** O(n) - Each element is pushed and popped at most once  
**Space Complexity:** O(n) - Stack size

