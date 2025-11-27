# LeetCode Top 150

Problem list from official https://leetcode.com/studyplan/top-interview-150

## 274. H-Index [Medium]
https://leetcode.com/problems/h-index/

### Explanation

## 274. H-Index [Medium]

https://leetcode.com/problems/h-index

## Description
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `iᵗʰ` paper, return *the researcher's h-index*.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

**Examples**

```tex
Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
```

**Constraints**
```tex
- n == citations.length
- 1 <= n <= 5000
- 0 <= citations[i] <= 1000
```

## Explanation

### Strategy
Let's restate the problem: You're given an array representing the number of citations for each paper a researcher has published. You need to find the maximum value `h` such that the researcher has at least `h` papers with at least `h` citations each.

This is a **sorting problem** that requires understanding the definition of h-index and finding the optimal value efficiently.

**What is given?** An array of integers representing citation counts for each paper.

**What is being asked?** Find the maximum h-index value that satisfies the h-index definition.

**Constraints:** The array can be up to 5000 elements long, with citation counts ranging from 0 to 1000.

**Edge cases:** 
- Array with all zeros
- Array with all high citation counts
- Array with single element
- Array with mixed citation counts

**High-level approach:**
The solution involves understanding the h-index definition and using sorting to efficiently find the maximum valid h value.

**Decomposition:**
1. **Sort the array**: Arrange citations in descending order to easily check h-index conditions
2. **Iterate through sorted array**: Check each position as a potential h-index
3. **Verify h-index condition**: Ensure at least h papers have at least h citations
4. **Return maximum valid h**: Find the largest h that satisfies the condition

**Brute force vs. optimized strategy:**
- **Brute force**: Try each possible h value and check if it satisfies the condition. This takes O(n²) time.
- **Optimized**: Sort the array and use a single pass to find the h-index. This takes O(n log n) time.

### Steps
Let's walk through the solution step by step using the first example: `citations = [3,0,6,1,5]`

**Step 1: Sort the array in descending order**
- Original: `[3,0,6,1,5]`
- Sorted: `[6,5,3,1,0]`

**Step 2: Check each position as potential h-index**
- Position 0: `h = 1`, check if `citations[0] >= 1` ✓ (6 >= 1)
- Position 1: `h = 2`, check if `citations[1] >= 2` ✓ (5 >= 2)
- Position 2: `h = 3`, check if `citations[2] >= 3` ✓ (3 >= 3)
- Position 3: `h = 4`, check if `citations[3] >= 4` ✗ (1 < 4)

**Step 3: Find the maximum valid h**
- The largest h where `citations[h-1] >= h` is 3
- At position 2 (0-indexed), we have `h = 3` and `citations[2] = 3 >= 3`

**Step 4: Verify the h-index condition**
- We need at least 3 papers with at least 3 citations
- Papers with ≥3 citations: 6, 5, 3 (3 papers) ✓
- Remaining papers: 1, 0 (≤3 citations) ✓
- H-index is 3

**Why this works:**
After sorting in descending order, the array position `i` (0-indexed) represents `h = i + 1`. For a position to be a valid h-index, we need `citations[i] >= h`. The largest valid h is our answer.

> **Note:** The key insight is that after sorting, we can directly check each position as a potential h-index. The sorting makes it easy to verify the h-index condition in a single pass.

**Time Complexity:** O(n log n) - dominated by sorting the array  
**Space Complexity:** O(1) - we only use a constant amount of extra space (excluding the sorted array if we modify the input)

### Solution

```python
def hIndex(citations):
    """
    Calculate the h-index for a researcher based on their paper citations.
    
    Args:
        citations: List[int] - Array of citation counts for each paper
        
    Returns:
        int - The researcher's h-index
    """
    # Handle edge cases
    if not citations:
        return 0
    
    # Sort citations in descending order
    citations.sort(reverse=True)
    
    # Check each position as a potential h-index
    for i in range(len(citations)):
        # h-index is i + 1 (1-indexed)
        h = i + 1
        
        # Check if citations[i] >= h
        # If not, we've found our answer
        if citations[i] < h:
            return i
        
        # If we reach the end, the h-index is the length of the array
        if i == len(citations) - 1:
            return h
    
    # This line should never be reached
    return 0
```

## 42. Trapping Rain Water [Hard]
https://leetcode.com/problems/trapping-rain-water/

### Explanation

## 42. Trapping Rain Water [Hard]

https://leetcode.com/problems/trapping-rain-water

## Description
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Examples**

```text
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints**
```text
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
```

## Explanation

### Strategy
Let's restate the problem: You're given an array representing the heights of walls in a landscape. When it rains, water gets trapped between these walls. Your job is to calculate how much water can be trapped.

This is a **two-pointer and dynamic programming problem** that requires understanding how water trapping works in real life.

**What is given?** An array of non-negative integers representing wall heights.

**What is being asked?** Calculate the total amount of water that can be trapped between the walls.

**Constraints:** The array can be quite large (up to 20,000 elements), so we need an efficient solution. All heights are non-negative.

**Edge cases:** 
- If the array has less than 3 elements, no water can be trapped (need at least 3 walls to form a container)
- If all heights are the same, no water can be trapped
- If heights are strictly increasing or decreasing, no water can be trapped

**High-level approach:**
The key insight is that for any position, the amount of water that can be trapped depends on the **minimum** of the highest wall to its left and the highest wall to its right. Water can only be trapped up to the height of the shorter of these two walls.

Think of it like this: at any point, water will rise to the level of the lower "dam" on either side. If you're in a valley between two mountains, the water level is limited by the shorter mountain.

**Decomposition:**
1. **Precompute left and right maximums**: For each position, find the highest wall to its left and right
2. **Calculate trapped water**: For each position, the trapped water is the minimum of left and right max, minus the current height (if positive)
3. **Sum up all trapped water**: Add up the water trapped at each position

**Brute force vs. optimized strategy:**
- **Brute force**: For each position, scan left and right to find maximums. This takes O(n²) time.
- **Optimized**: Precompute left and right maximums in two passes, then calculate water in one pass. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`

**Step 1: Understand the visualization**
Imagine this array as a landscape:
```
    ■
    ■   ■     ■
  ■ ■ ■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■
0 1 0 2 1 0 1 3 2 1 2 1
```

**Step 2: Precompute left maximums**
We'll create an array `left_max` where `left_max[i]` is the highest wall to the left of position `i` (including position `i` itself).

```
height:    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left_max:  [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
```

How we calculate this:
- `left_max[0] = height[0] = 0` (no walls to the left)
- `left_max[1] = max(left_max[0], height[1]) = max(0, 1) = 1`
- `left_max[2] = max(left_max[1], height[2]) = max(1, 0) = 1`
- `left_max[3] = max(left_max[2], height[3]) = max(1, 2) = 2`
- And so on...

**Step 3: Precompute right maximums**
Similarly, create `right_max` where `right_max[i]` is the highest wall to the right of position `i` (including position `i` itself).

```
height:     [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
right_max:  [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
```

How we calculate this (from right to left):
- `right_max[11] = height[11] = 1` (no walls to the right)
- `right_max[10] = max(right_max[11], height[10]) = max(1, 2) = 2`
- `right_max[9] = max(right_max[10], height[9]) = max(2, 1) = 2`
- And so on...

**Step 4: Calculate trapped water at each position**
For each position `i`, the water trapped is:
```
water[i] = min(left_max[i], right_max[i]) - height[i]
```

But only if this value is positive (we can't have negative water).

Let's calculate for a few positions:
- Position 0: `min(0, 3) - 0 = 0` (no water trapped)
- Position 1: `min(1, 3) - 1 = 0` (no water trapped)
- Position 2: `min(1, 3) - 0 = 1` (1 unit of water trapped)
- Position 3: `min(2, 3) - 2 = 0` (no water trapped)
- Position 4: `min(2, 3) - 1 = 1` (1 unit of water trapped)
- Position 5: `min(2, 3) - 0 = 2` (2 units of water trapped)

**Step 5: Sum up all trapped water**
```
water = [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]
total = 0 + 0 + 1 + 0 + 1 + 2 + 1 + 0 + 0 + 1 + 0 + 0 = 6
```

> **Note:** The key insight is that water can only be trapped up to the height of the lower "dam" on either side. This is why we take the minimum of the left and right maximums.

**Time Complexity:** O(n) - we make three passes through the array  
**Space Complexity:** O(n) - we store two additional arrays of size n

### Solution

```python
def trap(height):
    """
    Calculate the amount of water that can be trapped between walls.
    
    Args:
        height: List[int] - Array representing wall heights
        
    Returns:
        int - Total amount of water trapped
    """
    # Handle edge cases
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    
    # Step 1: Precompute left maximums
    # left_max[i] = highest wall to the left of position i (including i)
    left_max = [0] * n
    left_max[0] = height[0]
    
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Step 2: Precompute right maximums
    # right_max[i] = highest wall to the right of position i (including i)
    right_max = [0] * n
    right_max[n-1] = height[n-1]
    
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Step 3: Calculate trapped water at each position
    res = 0
    for i in range(n):
        # Water trapped = min(left_max, right_max) - current_height
        # But only if positive (can't have negative water)
        water = min(left_max[i], right_max[i]) - height[i]
        if water > 0:
            res += water
    
    return res
```

## 125. Valid Palindrome [Easy]
https://leetcode.com/problems/valid-palindrome/

### Explanation

## 125. Valid Palindrome [Easy]

https://leetcode.com/problems/valid-palindrome

## Description
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or *`false`* otherwise.*

**Examples**

```tex
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints**
```tex
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters
```

## Explanation

### Strategy
Let's restate the problem: You're given a string that may contain letters, numbers, spaces, and punctuation marks. You need to determine if it's a palindrome after cleaning it up (removing non-alphanumeric characters and converting to lowercase).

This is a **two-pointer problem** that involves string preprocessing and then checking for palindrome properties.

**What is given?** A string that may contain various characters including letters, numbers, spaces, and punctuation.

**What is being asked?** Determine if the cleaned string (only alphanumeric characters, all lowercase) is a palindrome.

**Constraints:** The string can be up to 200,000 characters long and contains only printable ASCII characters.

**Edge cases:** 
- Empty string (should return true)
- String with only non-alphanumeric characters (should return true)
- Single character (should return true)
- String with mixed case and punctuation

**High-level approach:**
The solution involves two main steps:
1. **Preprocessing**: Clean the string by removing non-alphanumeric characters and converting to lowercase
2. **Palindrome check**: Use two pointers to check if the cleaned string reads the same forward and backward

**Decomposition:**
1. **Clean the string**: Remove all non-alphanumeric characters and convert to lowercase
2. **Initialize pointers**: Place one pointer at the start and one at the end
3. **Compare characters**: Move pointers inward while comparing characters
4. **Return result**: Return true if all characters match, false otherwise

**Brute force vs. optimized strategy:**
- **Brute force**: Create a new cleaned string and then check if it equals its reverse. This takes O(n) time and O(n) space.
- **Optimized**: Use two pointers to check palindrome property in-place. This takes O(n) time and O(1) space.

### Steps
Let's walk through the solution step by step using the first example: `s = "A man, a plan, a canal: Panama"`

**Step 1: Preprocessing**
- Remove all non-alphanumeric characters: spaces, commas, colons
- Convert all letters to lowercase
- Result: `"amanaplanacanalpanama"`

**Step 2: Initialize pointers**
- `left = 0` (points to the first character: 'a')
- `right = 24` (points to the last character: 'a')

**Step 3: Compare characters**
- `s[left] = 'a'`, `s[right] = 'a'`
- `'a' == 'a'` ✓, so move both pointers inward
- `left = 1`, `right = 23`

**Step 4: Continue comparison**
- `s[left] = 'm'`, `s[right] = 'm'`
- `'m' == 'm'` ✓, so move both pointers inward
- `left = 2`, `right = 22`

**Step 5: Continue until pointers meet**
- Continue this process, comparing characters at both ends
- Move pointers inward after each successful comparison
- Stop when `left >= right`

**Step 6: Check result**
- If we reach the middle without finding a mismatch, it's a palindrome
- In this case, all characters match, so return `true`

**Why this works:**
A palindrome reads the same forward and backward. By using two pointers that start at opposite ends and move inward, we can efficiently check this property. If at any point the characters don't match, we know it's not a palindrome. If we reach the middle with all characters matching, it must be a palindrome.

> **Note:** The key insight is that we don't need to create a new cleaned string. We can process the original string character by character, skipping non-alphanumeric characters and converting case on-the-fly.

**Time Complexity:** O(n) - we process each character at most once  
**Space Complexity:** O(1) - we only use a constant amount of extra space for the pointers

### Solution

```python
def isPalindrome(s):
    """
    Check if a string is a palindrome after removing non-alphanumeric characters
    and converting to lowercase.
    
    Args:
        s: str - Input string that may contain various characters
        
    Returns:
        bool - True if the cleaned string is a palindrome, False otherwise
    """
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    # Use two pointers to check palindrome property
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # If pointers haven't crossed, compare characters
        if left < right:
            # Convert to lowercase and compare
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
    
    # If we reach here, all characters matched
    return True
```

## 167. Two Sum II - Input Array Is Sorted [Medium]
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

### Explanation

## 167. Two Sum II - Input Array Is Sorted [Medium]

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

## Description
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index₁]` and `numbers[index₂]` where `1 ≤ index₁ < index₂ ≤ numbers.length`.

Return *the indices of the two numbers, *`index₁`* and *`index₂`*, **added by one** as an integer array *`[index₁, index₂]`* of length 2.*

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

**Examples**

```text
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index₁ = 1, index₂ = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index₁ = 1, index₂ = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index₁ = 1, index₂ = 2. We return [1, 2].
```

**Constraints**
```text
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution
```

## Explanation

### Strategy
Let's restate the problem: You're given a sorted array of numbers and a target sum. You need to find two different numbers in the array that add up to the target, and return their 1-indexed positions.

This is a **two-pointer problem** that takes advantage of the fact that the array is already sorted.

**What is given?** A sorted array of integers and a target sum.

**What is being asked?** Find two numbers that add up to the target and return their 1-indexed positions.

**Constraints:** The array is sorted, there's exactly one solution, and you must use only constant extra space.

**Edge cases:** 
- The array has at least 2 elements (guaranteed by constraints)
- All numbers are within a reasonable range (-1000 to 1000)
- There's exactly one solution (no need to handle multiple solutions)

**High-level approach:**
Since the array is sorted, we can use two pointers - one at the beginning and one at the end. We can then move these pointers based on whether the current sum is too small or too large compared to the target.

Think of it like this: if you're looking for two numbers that add up to a target, and the array is sorted, you can start with the smallest and largest numbers. If their sum is too small, you need a larger number, so move the left pointer right. If their sum is too large, you need a smaller number, so move the right pointer left.

**Decomposition:**
1. **Initialize pointers**: Place one pointer at the start and one at the end
2. **Calculate current sum**: Add the numbers at both pointer positions
3. **Compare with target**: 
   - If sum equals target, we found our answer
   - If sum is too small, move left pointer right
   - If sum is too large, move right pointer left
4. **Return result**: Convert to 1-indexed format

**Brute force vs. optimized strategy:**
- **Brute force**: Check every possible pair of numbers. This takes O(n²) time.
- **Optimized**: Use two pointers and take advantage of the sorted order. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `numbers = [2,7,11,15]`, `target = 9`

**Step 1: Initialize pointers**
- `left = 0` (points to the first element: 2)
- `right = 3` (points to the last element: 15)

**Step 2: Calculate current sum**
- Current sum = `numbers[left] + numbers[right] = 2 + 15 = 17`

**Step 3: Compare with target**
- `17 > 9` (target), so the sum is too large
- We need a smaller number, so move the right pointer left
- `right = 2` (now points to 11)

**Step 4: Calculate new sum**
- Current sum = `numbers[left] + numbers[right] = 2 + 11 = 13`

**Step 5: Compare with target**
- `13 > 9` (target), so the sum is still too large
- Move the right pointer left again
- `right = 1` (now points to 7)

**Step 6: Calculate new sum**
- Current sum = `numbers[left] + numbers[right] = 2 + 7 = 9`

**Step 7: Found the solution!**
- `9 == 9` (target), so we found our answer
- The numbers are at positions `left = 0` and `right = 1`
- Convert to 1-indexed: `[1, 2]`

**Why this works:**
Since the array is sorted, when we move the left pointer right, we get larger numbers. When we move the right pointer left, we get smaller numbers. This allows us to efficiently search for the target sum by adjusting our search space.

> **Note:** The key insight is that since the array is sorted, we can use the two-pointer technique to efficiently find the target sum. This is much more efficient than checking every possible pair.

**Time Complexity:** O(n) - we visit each element at most once  
**Space Complexity:** O(1) - we only use a constant amount of extra space for the pointers

### Solution

```python
def twoSum(numbers, target):
    """
    Find two numbers in the sorted array that add up to the target.
    
    Args:
        numbers: List[int] - Sorted array of integers (1-indexed)
        target: int - Target sum to find
        
    Returns:
        List[int] - 1-indexed positions of the two numbers that sum to target
    """
    # Initialize two pointers
    left = 0
    right = len(numbers) - 1
    
    # Use two-pointer technique since array is sorted
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Found the solution, return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, move left pointer right to get larger numbers
            left += 1
        else:
            # Sum is too large, move right pointer left to get smaller numbers
            right -= 1
    
    # This line should never be reached since there's exactly one solution
    return []
```

## 11. Container With Most Water [Medium]
https://leetcode.com/problems/container-with-most-water/

### Explanation

## 11. Container With Most Water [Medium]

https://leetcode.com/problems/container-with-most-water/

## Description

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Examples:

```raw
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
```

> **Hint:**  Use two pointers, one at each end, and move the pointer with the shorter line inward.

## Explanation

Imagine the array as a row of sticks of different heights. You want to pick two sticks that, together with the x-axis, can hold the most water. The area is determined by the shorter stick and the distance between them. Start with the two ends and move the pointer pointing to the shorter stick inward, always looking for a bigger area.

This approach is efficient because it checks all possible pairs in linear time, always keeping the best answer found so far.

### Solution

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        max_area = max(max_area, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

## 15. 3Sum [Medium]
https://leetcode.com/problems/3sum/

### Explanation

## 15. 3Sum [Medium]

https://leetcode.com/problems/3sum

## Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Examples**

```tex
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**Constraints**
```tex
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
```

## Explanation

### Strategy
Let's restate the problem: You're given an array of integers and need to find all unique triplets that sum to zero. This is a classic **three-pointer problem** that builds upon the two-sum concept.

This is a **sorting + two-pointer problem** that requires careful handling of duplicates and efficient searching.

**What is given?** An array of integers that may contain duplicates.

**What is being asked?** Find all unique triplets that sum to zero, avoiding duplicate combinations.

**Constraints:** The array can be up to 3000 elements long, with values ranging from -100,000 to 100,000.

**Edge cases:** 
- Array with all zeros
- Array with many duplicates
- Array with no valid triplets
- Array with exactly 3 elements

**High-level approach:**
The solution involves three main steps:
1. **Sort the array**: This allows us to use two-pointer technique efficiently
2. **Fix one element**: Iterate through each unique element as the first number
3. **Two-pointer search**: Use two pointers to find pairs that sum to the negative of the fixed element

**Decomposition:**
1. **Sort the array**: Enables efficient two-pointer searching and helps avoid duplicates
2. **Iterate through unique elements**: Fix each element as the first number in the triplet
3. **Two-pointer search**: Use left and right pointers to find pairs that sum to the target
4. **Handle duplicates**: Skip duplicate elements to avoid duplicate triplets
5. **Return results**: Collect all valid triplets

**Brute force vs. optimized strategy:**
- **Brute force**: Check all possible combinations of three numbers. This takes O(n³) time.
- **Optimized**: Sort the array and use two-pointer technique for each fixed element. This takes O(n²) time.

### Steps
Let's walk through the solution step by step using the first example: `nums = [-1,0,1,2,-1,-4]`

**Step 1: Sort the array**
- Original: `[-1,0,1,2,-1,-4]`
- Sorted: `[-4,-1,-1,0,1,2]`

**Step 2: Fix first element and search for pairs**
- Fix `nums[0] = -4`
- Target for two-pointer search: `0 - (-4) = 4`
- Use two pointers: `left = 1`, `right = 5`
- `nums[left] + nums[right] = -1 + 2 = 1 < 4`, so move left pointer right
- `left = 2`, `nums[left] + nums[right] = -1 + 2 = 1 < 4`, so move left pointer right
- `left = 3`, `nums[left] + nums[right] = 0 + 2 = 2 < 4`, so move left pointer right
- `left = 4`, `nums[left] + nums[right] = 1 + 2 = 3 < 4`, so move left pointer right
- `left = 5`, but `left >= right`, so no valid pair found for `-4`

**Step 3: Fix next unique element**
- Fix `nums[1] = -1` (first occurrence)
- Target for two-pointer search: `0 - (-1) = 1`
- Use two pointers: `left = 2`, `right = 5`
- `nums[left] + nums[right] = -1 + 2 = 1 == 1`, found a triplet: `[-1,-1,2]`
- Move pointers: `left = 3`, `right = 4`
- `nums[left] + nums[right] = 0 + 1 = 1 == 1`, found another triplet: `[-1,0,1]`
- Continue until pointers cross

**Step 4: Skip duplicates**
- When moving to the next element, skip if it's the same as the previous one
- This prevents duplicate triplets

**Step 5: Continue for all elements**
- Repeat the process for each unique element
- Collect all valid triplets

**Why this works:**
By sorting the array, we can efficiently search for pairs using two pointers. For each fixed element `a`, we need to find pairs `b` and `c` such that `b + c = -a`. The two-pointer technique allows us to find these pairs in O(n) time for each fixed element, giving us an overall O(n²) solution.

> **Note:** The key insight is that sorting the array not only enables efficient searching but also helps us avoid duplicates by skipping identical elements.

**Time Complexity:** O(n²) - we iterate through each element and for each, we do a two-pointer search  
**Space Complexity:** O(1) - we only use a constant amount of extra space (excluding the output array)

### Solution

```python
def threeSum(nums):
    """
    Find all unique triplets in the array which gives the sum of zero.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        List[List[int]] - List of unique triplets that sum to zero
    """
    # Handle edge cases
    if len(nums) < 3:
        return []
    
    # Sort the array to enable two-pointer technique
    nums.sort()
    result = []
    
    # Iterate through each element as the first number in the triplet
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Use two pointers to find pairs that sum to -nums[i]
        left = i + 1
        right = len(nums) - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers
                left += 1
                right -= 1
                
            elif current_sum < target:
                # Sum is too small, move left pointer right
                left += 1
            else:
                # Sum is too large, move right pointer left
                right -= 1
    
    return result
```

## 289. Game of Life [Medium]
https://leetcode.com/problems/game-of-life/

### Explanation

## 289. Game of Life [Medium]

https://leetcode.com/problems/game-of-life

## Description
According to [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: **live** (represented by a `1`) or **dead** (represented by a `0`). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the `m x n` grid `board`. In this process, births and deaths occur **simultaneously**.

Given the current state of the `board`, **update** the `board` to reflect its next state.

**Note** that you do not need to return anything.

**Examples**

```tex
Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```

**Constraints**
```tex
- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] is 0 or 1
```

**Follow up:**
- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

## Explanation

### Strategy
Let's restate the problem: You're given a 2D grid representing the current state of Conway's Game of Life, where each cell is either alive (1) or dead (0). You need to update the board to the next generation based on specific rules about cell survival and reproduction.

This is a **simulation problem** that requires careful handling to update all cells simultaneously without interfering with the calculation of other cells.

**What is given?** An m x n grid where each cell is either 0 (dead) or 1 (live).

**What is being asked?** Update the board to the next generation based on the Game of Life rules.

**Constraints:** The grid can be up to 25x25, and all cells contain only 0 or 1.

**Edge cases:** 
- Grid with all dead cells
- Grid with all live cells
- Single row or column
- Grid with live cells on borders

**High-level approach:**
The solution involves using a two-pass approach where we first mark cells with their next state using special values, then convert these markers to the final states.

**Decomposition:**
1. **First pass**: Mark cells with their next state using special values (2 for live→dead, 3 for dead→live)
2. **Second pass**: Convert special values to final states (2→0, 3→1)
3. **Count neighbors**: For each cell, count its eight neighbors to determine its fate

**Brute force vs. optimized strategy:**
- **Brute force**: Create a copy of the board and update it. This takes O(mn) space.
- **Optimized**: Use special values to mark next states in-place. This takes O(1) space.

### Steps
Let's walk through the solution step by step using the first example: `board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]`

**Step 1: First pass - mark cells with next state**
- For each cell, count its eight neighbors
- Apply Game of Life rules and mark with special values:
  - `2` = currently live, will die (live→dead)
  - `3` = currently dead, will live (dead→live)
  - `0` = currently dead, will stay dead
  - `1` = currently live, will stay live

**Step 2: Count neighbors for each cell**
- For cell `board[0][1] = 1` (live):
  - Neighbors: `[0,0,1,0,0,1,1,1]` = 4 live neighbors
  - Rule 3: More than 3 live neighbors → dies
  - Mark as `2` (live→dead)

- For cell `board[1][2] = 1` (live):
  - Neighbors: `[1,0,1,1,1,0,0,0]` = 4 live neighbors
  - Rule 3: More than 3 live neighbors → dies
  - Mark as `2` (live→dead)

**Step 3: Second pass - convert special values**
- Convert `2` → `0` (dead)
- Convert `3` → `1` (live)
- Final board: `[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]`

**Why this works:**
By using special values (2 and 3) to mark the next state, we can update the board in-place without losing information about the current state. The two-pass approach ensures all cells are updated simultaneously as required.

> **Note:** The key insight is using special values to represent both current and next states, allowing us to solve the problem in-place while maintaining the requirement that all cells update simultaneously.

**Time Complexity:** O(mn) - we visit each cell twice  
**Space Complexity:** O(1) - we only use a constant amount of extra space

### Solution

```python
def gameOfLife(board):
    """
    Update the board to the next generation of Conway's Game of Life.
    This is done in-place using O(1) space.
    
    Args:
        board: List[List[int]] - The board to update in-place
        
    Returns:
        None - Modifies the board in-place
    """
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    
    # First pass: mark cells with their next state using special values
    # 2 = currently live, will die (live→dead)
    # 3 = currently dead, will live (dead→live)
    for i in range(m):
        for j in range(n):
            live_neighbors = countLiveNeighbors(board, i, j, m, n)
            
            if board[i][j] == 1:  # Currently live
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 2  # Mark as live→dead
            else:  # Currently dead
                if live_neighbors == 3:
                    board[i][j] = 3  # Mark as dead→live
    
    # Second pass: convert special values to final states
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0  # Convert live→dead to dead
            elif board[i][j] == 3:
                board[i][j] = 1  # Convert dead→live to live
```

## 205. Isomorphic Strings [Easy]
https://leetcode.com/problems/isomorphic-strings/

### Explanation

## 205. Isomorphic Strings [Easy]

https://leetcode.com/problems/isomorphic-strings

## Description

Given two strings `s` and `t`, *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Examples**

```tex
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
- Mapping 'e' to 'a'.
- Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
```

**Constraints**
```tex
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character
```

## Explanation

### Strategy
Let's restate the problem: You're given two strings of equal length, and you need to determine if they are isomorphic. Two strings are isomorphic if there's a one-to-one mapping between characters that can transform one string into the other.

This is a **hash table problem** that requires tracking character mappings in both directions to ensure the isomorphism property.

**What is given?** Two strings `s` and `t` of equal length.

**What is being asked?** Determine if the strings are isomorphic (can be transformed into each other via character replacement).

**Constraints:** The strings can be up to 50,000 characters long and contain any valid ASCII character.

**Edge cases:** 
- Empty strings
- Single character strings
- Strings with all identical characters
- Strings with complex character mappings

**High-level approach:**
The solution involves using two hash maps to track character mappings in both directions, ensuring that the mapping is consistent throughout both strings.

**Decomposition:**
1. **Check length equality**: If strings have different lengths, they can't be isomorphic
2. **Create mapping dictionaries**: Track character mappings from s to t and from t to s
3. **Iterate through characters**: Check each character pair for mapping consistency
4. **Verify isomorphism**: Ensure no conflicts in the mapping

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible character mappings. This is extremely inefficient.
- **Optimized**: Use hash tables to track mappings in a single pass. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `s = "egg"`, `t = "add"`

**Step 1: Initialize mapping dictionaries**
- `s_to_t = {}` (maps characters from s to t)
- `t_to_s = {}` (maps characters from t to s)

**Step 2: Check first character pair**
- `s[0] = 'e'`, `t[0] = 'a'`
- Check if 'e' is already mapped: No
- Check if 'a' is already mapped: No
- Add mappings: `s_to_t['e'] = 'a'`, `t_to_s['a'] = 'e'`

**Step 3: Check second character pair**
- `s[1] = 'g'`, `t[1] = 'd'`
- Check if 'g' is already mapped: No
- Check if 'd' is already mapped: No
- Add mappings: `s_to_t['g'] = 'd'`, `t_to_s['d'] = 'g'`

**Step 4: Check third character pair**
- `s[2] = 'g'`, `t[2] = 'd'`
- Check if 'g' is already mapped: Yes, to 'd'
- Verify consistency: `s_to_t['g'] == 'd'` ✓
- Check if 'd' is already mapped: Yes, to 'g'
- Verify consistency: `t_to_s['d'] == 'g'` ✓

**Step 5: Result**
- All character pairs are consistent
- Strings are isomorphic: `true`

**Why this works:**
By maintaining mappings in both directions, we ensure that:
1. No character in `s` maps to multiple characters in `t`
2. No character in `t` is mapped to by multiple characters in `s`
3. The mapping is consistent throughout both strings

> **Note:** The key insight is using bidirectional mapping to ensure the isomorphism property. We need to check both that each character in s maps to exactly one character in t, and that each character in t is mapped to by exactly one character in s.

**Time Complexity:** O(n) - we visit each character once  
**Space Complexity:** O(k) - where k is the number of unique characters (bounded by ASCII character set)

### Solution

```python
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    # Create mapping dictionaries for both directions
    s_to_t = {}
    t_to_s = {}
    
    # Check each character pair
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Check if char_s is already mapped
        if char_s in s_to_t:
            # Verify the mapping is consistent
            if s_to_t[char_s] != char_t:
                return False
        else:
            # Check if char_t is already mapped to by another character
            if char_t in t_to_s:
                return False
            
            # Add new mapping
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
    
    return True
```

## 290. Word Pattern [Easy]
https://leetcode.com/problems/word-pattern/

### Explanation

## 290. Word Pattern [Easy]

https://leetcode.com/problems/word-pattern

## Description
Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`. Specifically:

- Each letter in `pattern` maps to **exactly** one unique word in `s`.
- Each unique word in `s` maps to **exactly** one letter in `pattern`.
- No two letters map to the same word, and no two words map to the same letter.

**Examples**

```tex
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
- 'a' maps to "dog".
- 'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Constraints**
```tex
- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '
- s does not contain any leading or trailing spaces
- All the words in s are separated by a single space
```

## Explanation

### Strategy
Let's restate the problem: You're given a pattern string (like "abba") and a string of words (like "dog cat cat dog"), and you need to determine if the words follow the same pattern. This means there should be a one-to-one mapping between letters in the pattern and words in the string.

This is a **hash table problem** that requires tracking bidirectional mappings between pattern characters and words, similar to the isomorphic strings problem but with words instead of individual characters.

**What is given?** A pattern string and a string of space-separated words.

**What is being asked?** Determine if the words follow the same pattern as the given pattern string.

**Constraints:** The pattern can be up to 300 characters, and the string can be up to 3000 characters with words separated by single spaces.

**Edge cases:** 
- Pattern and words have different lengths
- Empty pattern or empty string
- Pattern with repeated characters
- String with repeated words

**High-level approach:**
The solution involves using two hash maps to track character-to-word and word-to-character mappings, ensuring that the bijection property is maintained.

**Decomposition:**
1. **Split the string into words**: Convert the space-separated string into a list of words
2. **Check length consistency**: If pattern length doesn't match word count, return false
3. **Create mapping dictionaries**: Track character-to-word and word-to-character mappings
4. **Verify bijection**: Ensure each character maps to exactly one word and vice versa

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible mappings. This is extremely inefficient.
- **Optimized**: Use hash tables to track mappings in a single pass. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `pattern = "abba"`, `s = "dog cat cat dog"`

**Step 1: Split the string into words**
- `s = "dog cat cat dog"`
- `words = ["dog", "cat", "cat", "dog"]`

**Step 2: Check length consistency**
- `pattern.length = 4`
- `words.length = 4`
- Lengths match ✓

**Step 3: Initialize mapping dictionaries**
- `char_to_word = {}` (maps pattern characters to words)
- `word_to_char = {}` (maps words to pattern characters)

**Step 4: Check first character-word pair**
- `pattern[0] = 'a'`, `words[0] = "dog"`
- Check if 'a' is already mapped: No
- Check if "dog" is already mapped: No
- Add mappings: `char_to_word['a'] = "dog"`, `word_to_char["dog"] = 'a'`

**Step 5: Check second character-word pair**
- `pattern[1] = 'b'`, `words[1] = "cat"`
- Check if 'b' is already mapped: No
- Check if "cat" is already mapped: No
- Add mappings: `char_to_word['b'] = "cat"`, `word_to_char["cat"] = 'b'`

**Step 6: Check third character-word pair**
- `pattern[2] = 'b'`, `words[2] = "cat"`
- Check if 'b' is already mapped: Yes, to "cat"
- Verify consistency: `char_to_word['b'] == "cat"` ✓
- Check if "cat" is already mapped: Yes, to 'b'
- Verify consistency: `word_to_char["cat"] == 'b'` ✓

**Step 7: Check fourth character-word pair**
- `pattern[3] = 'a'`, `words[3] = "dog"`
- Check if 'a' is already mapped: Yes, to "dog"
- Verify consistency: `char_to_word['a'] == "dog"` ✓
- Check if "dog" is already mapped: Yes, to 'a'
- Verify consistency: `word_to_char["dog"] == 'a'` ✓

**Step 8: Result**
- All character-word pairs are consistent
- Pattern is followed: `true`

**Why this works:**
By maintaining mappings in both directions, we ensure that:
1. Each character in the pattern maps to exactly one word
2. Each word maps to exactly one character
3. The bijection property is maintained throughout the pattern

> **Note:** The key insight is using bidirectional mapping to ensure the bijection property. This is similar to the isomorphic strings problem but operates on words instead of individual characters.

**Time Complexity:** O(n) - we visit each character/word once  
**Space Complexity:** O(k) - where k is the number of unique characters/words

### Solution

```python
def wordPattern(pattern, s):
    """
    Determine if the string s follows the given pattern.
    
    Args:
        pattern: str - The pattern string to match against
        s: str - The string of space-separated words
        
    Returns:
        bool - True if s follows the pattern, False otherwise
    """
    # Split the string into words
    words = s.split()
    
    # Check if pattern length matches word count
    if len(pattern) != len(words):
        return False
    
    # Create mapping dictionaries for both directions
    char_to_word = {}  # maps pattern characters to words
    word_to_char = {}  # maps words to pattern characters
    
    # Check each character-word pair
    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]
        
        # Check if char is already mapped
        if char in char_to_word:
            # Verify the mapping is consistent
            if char_to_word[char] != word:
                return False
        else:
            # Check if word is already mapped to by another character
            if word in word_to_char:
                return False
            
            # Add new mapping
            char_to_word[char] = word
            word_to_char[word] = char
    
    return True
```

## 242. Valid Anagram [Easy]
https://leetcode.com/problems/valid-anagram/

### Explanation

Given two strings `s` and `t`, return `true` if `t` is an [anagram](https://en.wikipedia.org/wiki/Anagram) of `s`, and `false` otherwise.

**Examples**

```tex
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
```

**Constraints**
```tex
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters
```

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Explanation

### Strategy
Let's restate the problem: You're given two strings, and you need to determine if one is an anagram of the other. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

This is a **character counting problem** that can be solved using hash tables to track the frequency of each character in both strings.

**What is given?** Two strings `s` and `t` of potentially different lengths.

**What is being asked?** Determine if `t` is an anagram of `s`.

**Constraints:** The strings can be up to 50,000 characters long and contain only lowercase English letters.

**Edge cases:** 
- Strings of different lengths
- Empty strings
- Strings with repeated characters
- Strings with all identical characters

**High-level approach:**
The solution involves counting the frequency of each character in both strings and comparing them. If the character counts match exactly, the strings are anagrams.

**Decomposition:**
1. **Check length equality**: If strings have different lengths, they can't be anagrams
2. **Count characters in first string**: Use a hash table to track character frequencies
3. **Decrement counts for second string**: For each character in the second string, decrement its count
4. **Verify all counts are zero**: If any count is not zero, the strings are not anagrams

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible permutations of one string. This takes O(n!) time.
- **Optimized**: Use character counting with hash tables. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `s = "anagram"`, `t = "nagaram"`

**Step 1: Check string lengths**
- `s.length = 7`, `t.length = 7`
- Lengths match ✓

**Step 2: Initialize character count dictionary**
- `char_count = {}`

**Step 3: Count characters in first string (s)**
- `s = "anagram"`
- `char_count['a'] = 3` (appears 3 times)
- `char_count['n'] = 1` (appears 1 time)
- `char_count['g'] = 1` (appears 1 time)
- `char_count['r'] = 1` (appears 1 time)
- `char_count['m'] = 1` (appears 1 time)

**Step 4: Decrement counts for second string (t)**
- `t = "nagaram"`
- `t[0] = 'n'`: `char_count['n'] = 1 - 1 = 0`
- `t[1] = 'a'`: `char_count['a'] = 3 - 1 = 2`
- `t[2] = 'g'`: `char_count['g'] = 1 - 1 = 0`
- `t[3] = 'a'`: `char_count['a'] = 2 - 1 = 1`
- `t[4] = 'r'`: `char_count['r'] = 1 - 1 = 0`
- `t[5] = 'a'`: `char_count['a'] = 1 - 1 = 0`
- `t[6] = 'm'`: `char_count['m'] = 1 - 1 = 0`

**Step 5: Verify all counts are zero**
- All character counts are now 0
- The strings are anagrams: `true`

**Why this works:**
By counting characters in the first string and then decrementing for the second string, we ensure that:
1. Both strings contain the same characters
2. Each character appears the same number of times in both strings
3. The final count of 0 for all characters confirms the anagram property

> **Note:** The key insight is using character frequency counting to verify that both strings contain exactly the same characters with the same frequencies. This is much more efficient than trying to find permutations.

**Time Complexity:** O(n) - we visit each character once in each string  
**Space Complexity:** O(k) - where k is the number of unique characters (bounded by the character set size)

### Solution

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        
        char_count[char] -= 1
        
        # If count becomes negative, strings are not anagrams
        if char_count[char] < 0:
            return False
    
    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return False
    
    return True
```

## 1. Two Sum [Easy]
https://leetcode.com/problems/two-sum/

### Explanation

To solve the Two Sum problem, we want to find two numbers in the array that add up to a given target. The most efficient way is to use a hash map (dictionary) to store the numbers we have seen so far and their indices. As we iterate through the array, for each number, we check if the complement (target - current number) exists in the hash map. If it does, we have found the solution. Otherwise, we add the current number and its index to the hash map. This approach has O(n) time complexity.

## Hint

Try using a hash map to keep track of the numbers you have seen so far and their indices.

## Points

- Time complexity: O(n) using a hash map.
- Brute-force solution is O(n^2) and not efficient for large arrays.
- There is always exactly one solution, and you may not use the same element twice.
- Be careful with duplicate numbers in the array.

### Solution

```python
def two_sum(nums, target):
    """Find two numbers that add up to target using a hash map for O(n) time complexity."""
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
```

## 128. Longest Consecutive Sequence [Medium]
https://leetcode.com/problems/longest-consecutive-sequence/

### Explanation

## 128. Longest Consecutive Sequence [Medium]

https://leetcode.com/problems/longest-consecutive-sequence

## Description
Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

**Examples**

```tex
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
```

**Constraints**
```tex
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given an unsorted array of integers, and you need to find the length of the longest sequence of consecutive integers. The challenge is to do this in O(n) time, which means we can't sort the array (as sorting takes O(n log n) time).

This is a **hash table problem** that requires finding sequences of consecutive numbers efficiently by using the properties of consecutive sequences.

**What is given?** An unsorted array of integers that can be very large (up to 100,000 elements).

**What is being asked?** Find the length of the longest sequence of consecutive integers.

**Constraints:** The array can be up to 100,000 elements long, with values ranging from -10⁹ to 10⁹.

**Edge cases:** 
- Empty array
- Array with single element
- Array with all identical elements
- Array with no consecutive sequences

**High-level approach:**
The solution involves using a hash set to quickly check if numbers exist, then for each number, expanding in both directions to find the complete consecutive sequence.

**Decomposition:**
1. **Convert array to hash set**: For O(1) lookup time
2. **Find sequence starting points**: Look for numbers that are the start of a consecutive sequence
3. **Expand sequences**: For each starting point, expand in both directions to find the complete sequence
4. **Track maximum length**: Keep track of the longest sequence found

**Brute force vs. optimized strategy:**
- **Brute force**: Sort the array and find consecutive sequences. This takes O(n log n) time.
- **Optimized**: Use hash set and expand sequences from starting points. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `nums = [100,4,200,1,3,2]`

**Step 1: Convert array to hash set**
- `nums = [100,4,200,1,3,2]`
- `num_set = {100, 4, 200, 1, 3, 2}`

**Step 2: Find sequence starting points**
- For each number, check if it's the start of a consecutive sequence
- A number is a starting point if `num - 1` is NOT in the set
- Starting points: `[100, 200, 1]` (because 99, 199, and 0 are not in the set)

**Step 3: Expand sequences from starting points**
- **Starting point 100**: 
  - Check if 101 exists: No
  - Sequence length: 1
- **Starting point 200**: 
  - Check if 201 exists: No
  - Sequence length: 1
- **Starting point 1**: 
  - Check if 2 exists: Yes
  - Check if 3 exists: Yes
  - Check if 4 exists: Yes
  - Check if 5 exists: No
  - Sequence: [1, 2, 3, 4]
  - Sequence length: 4

**Step 4: Track maximum length**
- Maximum sequence length found: 4
- Result: 4

**Why this works:**
By identifying starting points (numbers that don't have a predecessor in the set), we ensure that we only expand each sequence once. This gives us O(n) time complexity because:
1. We visit each number at most twice (once when checking if it's a starting point, once when expanding sequences)
2. Each number is part of at most one sequence
3. The total work is bounded by O(n)

> **Note:** The key insight is identifying starting points of consecutive sequences and expanding from there. This avoids redundant work and ensures O(n) time complexity.

**Time Complexity:** O(n) - we visit each number at most twice  
**Space Complexity:** O(n) - we need to store the hash set

### Solution

```python
def longestConsecutive(nums):
    if not nums:
        return 0
    
    # Convert array to hash set for O(1) lookup
    num_set = set(nums)
    max_length = 0
    
    # For each number, check if it's the start of a consecutive sequence
    for num in num_set:
        # A number is a starting point if num - 1 is NOT in the set
        if num - 1 not in num_set:
            current_length = 1
            current_num = num
            
            # Expand the sequence by checking consecutive numbers
            while current_num + 1 in num_set:
                current_length += 1
                current_num += 1
            
            # Update maximum length if current sequence is longer
            max_length = max(max_length, current_length)
    
    return max_length
```

## 228. Summary Ranges [Easy]
https://leetcode.com/problems/summary-ranges/

### Explanation

## 228. Summary Ranges [Easy]

https://leetcode.com/problems/summary-ranges

## Description
You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Examples**

```tex
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

**Constraints**
```tex
- 0 <= nums.length <= 20
- -2^31 <= nums[i] <= 2^31 - 1
- All the values of nums are unique
- nums is sorted in ascending order
```

## Explanation

### Strategy
Let's restate the problem: You're given a sorted array of unique integers, and you need to create a summary of consecutive ranges. The goal is to represent consecutive sequences as ranges (e.g., "0->2") and single numbers as themselves (e.g., "7").

This is an **array traversal problem** that requires identifying consecutive sequences and formatting them appropriately.

**What is given?** A sorted array of unique integers (up to 20 elements).

**What is being asked?** Create a list of ranges that cover all numbers exactly, representing consecutive sequences as ranges and single numbers as themselves.

**Constraints:** The array is small (up to 20 elements), sorted, and contains unique values.

**Edge cases:** 
- Empty array
- Single element array
- Array with no consecutive sequences
- Array with all consecutive sequences

**High-level approach:**
The solution involves traversing the array and identifying consecutive sequences. When we find a break in the sequence, we format the range appropriately and continue.

**Decomposition:**
1. **Handle edge cases**: Empty array returns empty list
2. **Initialize variables**: Track start of current range and result list
3. **Traverse array**: Look for consecutive sequences
4. **Format ranges**: Convert consecutive sequences to appropriate string format
5. **Handle final range**: Don't forget the last range when loop ends

**Brute force vs. optimized strategy:**
- **Brute force**: Check each possible range combination. This is inefficient.
- **Optimized**: Single pass through the array, identifying consecutive sequences as we go. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `nums = [0,1,2,4,5,7]`

**Step 1: Handle edge case**
- Array is not empty, continue

**Step 2: Initialize variables**
- `start = 0` (start of current range)
- `result = []` (list to store ranges)

**Step 3: Traverse array looking for consecutive sequences**
- `i = 0`: `nums[0] = 0`
  - Start new range: `start = 0`
- `i = 1`: `nums[1] = 1`
  - Check if consecutive: `1 == 0 + 1` ✓
  - Continue current range
- `i = 2`: `nums[2] = 2`
  - Check if consecutive: `2 == 1 + 1` ✓
  - Continue current range
- `i = 3`: `nums[3] = 4`
  - Check if consecutive: `4 == 2 + 1` ✗
  - Break in sequence! Format range [0,2] as "0->2"
  - Add to result: `result = ["0->2"]`
  - Start new range: `start = 3`
- `i = 4`: `nums[4] = 5`
  - Check if consecutive: `5 == 4 + 1` ✓
  - Continue current range
- `i = 5`: `nums[5] = 7`
  - Check if consecutive: `7 == 5 + 1` ✗
  - Break in sequence! Format range [4,5] as "4->5"
  - Add to result: `result = ["0->2", "4->5"]`
  - Start new range: `start = 5`

**Step 4: Handle final range**
- Loop ended, need to handle the last range [7,7]
- Since start == end (7 == 7), format as "7"
- Add to result: `result = ["0->2", "4->5", "7"]`

**Step 5: Return result**
- Final result: `["0->2","4->5","7"]`

**Why this works:**
By traversing the array once and checking for consecutive numbers, we can identify ranges efficiently. The key insights are:
1. A break in the sequence occurs when `nums[i] != nums[i-1] + 1`
2. Single numbers (where start == end) are formatted as "a"
3. Ranges (where start != end) are formatted as "a->b"

> **Note:** The key insight is identifying consecutive sequences by checking if each number is exactly one more than the previous number. This allows us to build ranges efficiently in a single pass.

**Time Complexity:** O(n) - we visit each element once  
**Space Complexity:** O(n) - we need to store the result list

### Solution

```python
def summaryRanges(nums):
    """
    Create a summary of ranges from a sorted array of unique integers.
    
    Args:
        nums: List[int] - Sorted array of unique integers
        
    Returns:
        List[str] - List of range strings
    """
    # Handle edge case
    if not nums:
        return []
    
    result = []
    start = 0
    
    # Traverse array looking for consecutive sequences
    for i in range(1, len(nums)):
        # Check if current number is consecutive to previous
        if nums[i] != nums[i-1] + 1:
            # Break in sequence, format the range
            if start == i - 1:
                # Single number
                result.append(str(nums[start]))
            else:
                # Range of numbers
                result.append(f"{nums[start]}->{nums[i-1]}")
            
            # Start new range
            start = i
    
    # Handle the final range
    if start == len(nums) - 1:
        # Single number
        result.append(str(nums[start]))
    else:
        # Range of numbers
        result.append(f"{nums[start]}->{nums[-1]}")
    
    return result
```

## 141. Linked List Cycle [Easy]
https://leetcode.com/problems/linked-list-cycle/

### Explanation

# 141. Linked List Cycle [Easy]

https://leetcode.com/problems/linked-list-cycle

## Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:**
```text
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:**
```text
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:**
```text
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.


**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Explanation

### Strategy

This is a **two-pointer problem** that requires detecting a cycle in a linked list. The key insight is to use Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm), which uses two pointers moving at different speeds.

**Key observations:**
- If there's a cycle, a fast pointer will eventually catch up to a slow pointer
- If there's no cycle, the fast pointer will reach the end (null)
- The fast pointer moves twice as fast as the slow pointer
- This approach uses O(1) space, which is optimal

**High-level approach:**
1. **Use two pointers**: Slow pointer (tortoise) and fast pointer (hare)
2. **Move pointers**: Slow moves 1 step, fast moves 2 steps
3. **Check for cycle**: If fast catches slow, there's a cycle
4. **Check for end**: If fast reaches null, there's no cycle

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If head is null or head.next is null, return false

**Step 2: Initialize pointers**
- `slow = head` (moves 1 step at a time)
- `fast = head.next` (moves 2 steps at a time)

**Step 3: Move pointers until they meet or reach end**
While `fast` is not null and `fast.next` is not null:
- Move slow pointer: `slow = slow.next`
- Move fast pointer: `fast = fast.next.next`
- If slow and fast meet, return true (cycle detected)

**Step 4: Return result**
- If you exit the loop, return false (no cycle)

**Example walkthrough:**
Let's trace through the first example:

```text
head = [3,2,0,-4], pos = 1 (cycle from -4 back to 2)

Initial state:
slow = 3, fast = 2

Step 1: slow = 2, fast = 0
Step 2: slow = 0, fast = 2
Step 3: slow = -4, fast = 0
Step 4: slow = 2, fast = 2 (they meet!)

Result: Return true (cycle detected)
```

> **Note:** Floyd's Cycle-Finding Algorithm is optimal because it uses O(1) space and O(n) time. The mathematical proof shows that if there's a cycle, the fast pointer will eventually catch the slow pointer within one cycle length.

**Time Complexity:** O(n) - in the worst case, you visit each node at most twice  
**Space Complexity:** O(1) - you only use two pointers regardless of input size

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.next = None
```

## 2. Add Two Numbers [Medium]
https://leetcode.com/problems/add-two-numbers/

### Explanation

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```text
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

Constraints:
```text
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```

## Explanation

The Add Two Numbers problem involves adding two numbers represented by linked lists, where each node contains a single digit and the digits are stored in reverse order. To solve this, we iterate through both linked lists, adding corresponding digits along with any carry from the previous addition. We create a new linked list to store the result. If one list is shorter, treat missing digits as 0. If there is a carry left after processing both lists, add a new node with the carry value.

## Hint

Use a dummy head node to simplify the code for building the result list. Remember to handle the carry at the end.

## Points

- Time complexity: O(max(m, n)), where m and n are the lengths of the two lists.
- Handle different lengths of input lists.
- Don’t forget to add a node if there is a carry left after the main loop.
- Each node contains a single digit (0-9).

### Solution

```python
def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## 61. Rotate List [Medium]
https://leetcode.com/problems/rotate-list/

### Explanation

Given the `head` of a linked list, rotate the list to the right by `k` places.

**Example 1:**
```text
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

![1](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

**Example 2:**
```text
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

![2](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

**Constraints:**
- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Explanation

### Strategy

This is a **linked list manipulation problem** that requires rotating a linked list to the right by k positions. The key insight is to find the new head position and break/reconnect the list appropriately.

**Key observations:**
- Rotating by k positions moves the last k nodes to the front
- If k is larger than the list length, we can use modulo to reduce it
- We need to find the new head position (length - k % length)
- We need to break the list at the new head position and reconnect

**High-level approach:**
1. **Find list length**: Count the number of nodes
2. **Normalize k**: Use `k % length` to handle large k values
3. **Find new head**: Calculate the position of the new head
4. **Break and reconnect**: Break the list and reconnect to form rotated list

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If head is null or head.next is null, return head
- If k is 0, return head

**Step 2: Find list length**
- Count the number of nodes in the list

**Step 3: Normalize k**
- Calculate `k = k % length` to handle large k values

**Step 4: Find new head position**
- Calculate `new_head_pos = length - k`

**Step 5: Break and reconnect**
- Find the node before the new head
- Break the list at that point
- Connect the end to the original head

**Example walkthrough:**
Let's trace through the first example:

```text
head = [1,2,3,4,5], k = 2

Step 1: Find length
length = 5

Step 2: Normalize k
k = 2 % 5 = 2

Step 3: Find new head position
new_head_pos = 5 - 2 = 3

Step 4: Find the node before new head
current = head, count = 0
current = 2, count = 1
current = 3, count = 2 (this is the node before new head)

Step 5: Break and reconnect
new_head = 4
current.next = None (break at 3)
last_node.next = head (connect 5 to 1)

Result: [4,5,1,2,3]
```

> **Note:** The key insight is that rotating by k positions is equivalent to moving the last k nodes to the front. We can achieve this by finding the new head position and breaking/reconnecting the list at the appropriate point.

**Time Complexity:** O(n) - we visit each node at most twice  
**Space Complexity:** O(1) - we only use a constant amount of extra space

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
```

## 146. LRU Cache [Medium]
https://leetcode.com/problems/lru-cache/

### Explanation

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Example 1:**

```raw
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Constraints:**
- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Explanation

### Strategy

This is a **design problem** that requires implementing an LRU (Least Recently Used) cache. The key insight is to combine a hash map for O(1) lookups with a doubly linked list for O(1) insertions/deletions to maintain the order of usage.

**Key observations:**

- We need O(1) time for both get and put operations
- We need to track the order of usage (most recently used to least recently used)
- When capacity is exceeded, we need to remove the least recently used item
- A hash map provides O(1) lookups, but doesn't maintain order
- A doubly linked list maintains order and allows O(1) insertions/deletions

**High-level approach:**

1. **Use a hash map**: For O(1) key-value lookups
2. **Use a doubly linked list**: To maintain usage order
3. **Combine both**: Hash map stores key -> node mappings
4. **Update order**: Move accessed items to front (most recently used)
5. **Evict LRU**: Remove from end when capacity exceeded

### Steps

Let's break down the solution step by step:

**Step 1: Design the data structure**

- `capacity`: Maximum number of items in cache
- `cache`: Hash map for key -> node mappings
- `head`: Dummy head node of doubly linked list
- `tail`: Dummy tail node of doubly linked list

**Step 2: Implement get operation**

- Check if key exists in hash map
- If not found, return -1
- If found, move node to front (most recently used)
- Return the value

**Step 3: Implement put operation**

- If key exists, update value and move to front
- If key doesn't exist:
  - Create new node
  - Add to front of list
  - Add to hash map
  - If capacity exceeded, remove LRU item (from end)

**Step 4: Helper methods**

- `_add_to_front(node)`: Add node to front of list
- `_remove_node(node)`: Remove node from list
- `_remove_lru()`: Remove least recently used item

**Example walkthrough:**

Let's trace through the example:

```raw
capacity = 2

put(1, 1): cache = {1=1}, list = [1]
put(2, 2): cache = {1=1, 2=2}, list = [2, 1]
get(1): return 1, list = [1, 2] (move 1 to front)
put(3, 3): cache = {1=1, 3=3}, list = [3, 1] (evict 2)
get(2): return -1 (not found)
put(4, 4): cache = {3=3, 4=4}, list = [4, 3] (evict 1)
get(1): return -1 (not found)
get(3): return 3, list = [3, 4]
get(4): return 4, list = [4, 3]
```

> **Note:** The doubly linked list with dummy head and tail nodes makes it easy to add/remove nodes at the beginning and end. The hash map provides O(1) access to any node, and the list maintains the order of usage.

**Time Complexity:** O(1) for both get and put operations  
**Space Complexity:** O(capacity) - we store at most capacity items

### Solution

```python
def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node mapping

        # Initialize doubly linked list with dummy nodes
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Check if key exists
        if key not in self.cache:
            return -1

        # Move node to front (most recently used)
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # If key exists, update value and move to front
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_front(node)
        else:
            # Create new node
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            # If capacity exceeded, remove LRU item
            if len(self.cache) > self.capacity:
                self._remove_lru()

    def _add_to_front(self, node):
        """Add node to front of list (after dummy head)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove node from list"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_lru(self):
        """Remove least recently used item (before dummy tail)"""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        del self.cache[lru_node.key]


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
```

## 148. Sort List [Medium]
https://leetcode.com/problems/sort-list/

### Explanation

Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

**Example 1:**

```tex
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

**Example 2:**

```tex
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Example 3:**

```tex
Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?

## Explanation

### Strategy

This is a **divide-and-conquer problem** that requires sorting a linked list in O(n log n) time and O(1) space. The key insight is to use merge sort, which naturally works well with linked lists and can be implemented in-place.

**Key observations:**
- We need O(n log n) time complexity for optimal sorting
- We need O(1) space complexity (no extra data structures)
- Merge sort is perfect for linked lists because we can split and merge in-place
- We can use the fast/slow pointer technique to find the middle

**High-level approach:**
1. **Find the middle**: Use fast/slow pointers to split the list
2. **Recursively sort**: Sort the left and right halves
3. **Merge sorted lists**: Merge the two sorted halves
4. **Return result**: Return the merged sorted list

### Steps

Let's break down the solution step by step:

**Step 1: Handle base cases**
- If head is null or head.next is null, return head (already sorted)

**Step 2: Find the middle of the list**
- Use fast/slow pointer technique
- Slow pointer moves 1 step, fast pointer moves 2 steps
- When fast reaches end, slow is at middle

**Step 3: Split the list**
- Set `mid = slow.next`
- Set `slow.next = None` to split the list

**Step 4: Recursively sort halves**

- Sort the left half: `left = sortList(head)`
- Sort the right half: `right = sortList(mid)`

**Step 5: Merge the sorted halves**

- Use a dummy node to simplify merging
- Compare nodes from both lists and link them in order

**Example walkthrough:**

Let's trace through the first example:

```tex
head = [4,2,1,3]

Step 1: Find middle
slow = 4, fast = 4
slow = 2, fast = 1
slow = 1, fast = 3
slow = 3, fast = null
middle = 3

Step 2: Split list
left = [4,2,1], right = [3]

Step 3: Recursively sort left
left = [4,2,1] → [1,2,4]

Step 4: Recursively sort right
right = [3] → [3]

Step 5: Merge [1,2,4] and [3]
result = [1,2,3,4]
```

> **Note:** Merge sort is ideal for linked lists because we can split and merge in-place without extra space. The fast/slow pointer technique efficiently finds the middle, and the merge step can be done by simply relinking nodes.

**Time Complexity:** O(n log n) - merge sort time complexity  
**Space Complexity:** O(log n) - recursion stack space (not O(1) due to recursion)

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the middle of the list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a dummy node to simplify merging
        dummy = ListNode(0)
        current = dummy

        # Merge the two sorted lists
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Attach remaining nodes
        if left:
            current.next = left
        if right:
            current.next = right

        # Return the merged list (skip dummy node)
        return dummy.next
```
