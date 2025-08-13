Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return *the number of unique elements in* `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
2. Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

```text
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**
```text
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```text
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

## Explanation

### Strategy

This is a **two-pointer array manipulation problem** that requires removing duplicates from a sorted array in-place. The key insight is that since the array is sorted, all duplicates of an element will be consecutive, making it easy to skip them.

**Key observations:**
- The array is sorted in non-decreasing order
- Duplicates appear consecutively in the array
- We need to maintain the relative order of elements
- We can use a two-pointer approach to efficiently remove duplicates

**High-level approach:**
1. **Use a slow pointer**: Points to the next position where we'll place a unique element
2. **Use a fast pointer**: Iterates through the array to find unique elements
3. **Skip duplicates**: When we find a duplicate, just increment the fast pointer
4. **Copy unique elements**: When we find a new unique element, copy it to the slow pointer position
5. **Return the count**: The slow pointer position at the end gives us the count of unique elements

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If the array is empty, return 0
- If the array has only one element, return 1

**Step 2: Initialize pointers**
- `slow`: Points to the next position where we'll place a unique element (starts at 1)
- `fast`: Iterates through the array to find unique elements (starts at 1)

**Step 3: Iterate through the array**
For each element at position `fast`:
- If `nums[fast] != nums[fast-1]`, it's a new unique element
  - Copy it to `nums[slow]` and increment `slow`
- If `nums[fast] == nums[fast-1]`, it's a duplicate
  - Skip it (just increment `fast`)

**Step 4: Return the result**
- The value of `slow` at the end gives us the count of unique elements
- The first `slow` elements of the array contain all the unique elements in order

**Example walkthrough:**
Let's trace through the second example:

```text
nums = [0,0,1,1,1,2,2,3,3,4]

Initial state:
slow = 1, fast = 1

Step 1: nums[1] = 0 == nums[0] = 0 (duplicate)
Skip, increment fast only
slow = 1, fast = 2

Step 2: nums[2] = 1 != nums[1] = 0 (new unique)
Copy 1 to nums[1], increment both
nums = [0,1,1,1,1,2,2,3,3,4], slow = 2, fast = 3

Step 3: nums[3] = 1 == nums[2] = 1 (duplicate)
Skip, increment fast only
slow = 2, fast = 4

Step 4: nums[4] = 1 == nums[3] = 1 (duplicate)
Skip, increment fast only
slow = 2, fast = 5

Step 5: nums[5] = 2 != nums[4] = 1 (new unique)
Copy 2 to nums[2], increment both
nums = [0,1,2,1,1,2,2,3,3,4], slow = 3, fast = 6

Continue this process...
Final result: Return slow = 5
Final array: [0,1,2,3,4,_,_,_,_,_]
```

> **Note:** The key insight is that since the array is sorted, we only need to compare each element with the previous one to detect duplicates. This makes the algorithm very efficient with O(n) time complexity.

**Time Complexity:** O(n) - we visit each element exactly once  
**Space Complexity:** O(1) - we modify the array in-place without extra space 