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

## 21. Merge Two Sorted Lists [Easy]
https://leetcode.com/problems/merge-two-sorted-lists/

### Explanation

## Explanation

### Strategy (The "Why")

Given two sorted linked lists `list1` and `list2`, we need to merge them into one sorted list and return the head of the merged list.

**1.1 Constraints & Complexity:**

- **Input Size:** The total number of nodes can be up to $50$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of the two lists. We visit each node exactly once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for the dummy node and pointers.
- **Edge Case:** If one list is empty, return the other list. If both are empty, return `null`.

**1.2 High-level approach:**

The goal is to merge two sorted linked lists into one sorted list.

We use a dummy node to simplify edge cases and a current pointer to build the merged list. We compare nodes from both lists and attach the smaller one to the result, then move the pointer of the list we took from.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert both lists to arrays, merge the arrays, then convert back to a linked list. This takes $O(n + m)$ time and $O(n + m)$ space.
- **Optimized Strategy (Two Pointers):** Use two pointers to traverse both lists simultaneously, building the merged list in-place. This takes $O(n + m)$ time and $O(1)$ space.
- **Why it's better:** The two-pointer approach uses $O(1)$ extra space instead of $O(n + m)$ for arrays, while maintaining the same time complexity.

**1.4 Decomposition:**

1. Create a dummy node to simplify edge cases.
2. Initialize a current pointer at the dummy node.
3. While both lists have nodes, compare the values and attach the smaller node to the result.
4. Move the pointer of the list we took from.
5. Attach the remaining nodes from the non-empty list.
6. Return the head of the merged list (dummy.next).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $list1 = [1,2,4]$, $list2 = [1,3,4]$

We initialize:
- `dummy = ListNode(0)`
- `current = dummy`

**2.2 Start Merging:**

We begin comparing nodes from both lists.

**2.3 Trace Walkthrough:**

| Step | list1.val | list2.val | Compare | Attach | current.next | list1/list2 After |
|------|-----------|-----------|---------|--------|--------------|-------------------|
| 1 | 1 | 1 | Equal | list1 | 1 | list1 = 2 |
| 2 | 2 | 1 | 2 > 1 | list2 | 1 | list2 = 3 |
| 3 | 2 | 3 | 2 < 3 | list1 | 2 | list1 = 4 |
| 4 | 4 | 3 | 4 > 3 | list2 | 3 | list2 = 4 |
| 5 | 4 | 4 | Equal | list1 | 4 | list1 = null |
| 6 | null | 4 | - | list2 | 4 | list2 = null |

**2.4 Final Result:**

After merging: $[1,1,2,3,4,4]$

**2.5 Return Result:**

We return the head of the merged list: $[1,1,2,3,4,4]$

> **Note:** The dummy node simplifies the code by providing a starting point. Without it, we'd need special handling for the first node. The key is to always attach the smaller node and move the corresponding pointer forward.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes
        current.next = list1 if list1 else list2
        
        return dummy.next
```

## 25. Reverse Nodes in k-Group [Hard]
https://leetcode.com/problems/reverse-nodes-in-k-group/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The linked list has $n$ nodes where $1 \leq k \leq n \leq 5000$.
* **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We visit each node exactly once.
* **Space Complexity:** $O(n/k)$ for the recursion stack, which is $O(n)$ in the worst case when $k = 1$.
* **Edge Case:** If the number of nodes is not a multiple of $k$, the remaining nodes at the end stay in their original order.

**1.2 High-level approach**

The goal is to reverse nodes in groups of $k$. We reverse each group of $k$ nodes, then recursively process the remaining list. If there are fewer than $k$ nodes remaining, we leave them unchanged.

![Linked list reversal in groups showing how k nodes are reversed at a time]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Convert the linked list to an array, reverse groups in the array, then rebuild the list. This uses $O(n)$ extra space.
* **Optimized (In-Place Reversal):** Reverse groups of $k$ nodes in-place using pointer manipulation. This uses $O(1)$ extra space (excluding recursion stack) and maintains the linked list structure.

**1.4 Decomposition**

1. Check if there are at least $k$ nodes remaining.
2. If yes, reverse the first $k$ nodes.
3. Recursively process the remaining list.
4. Connect the reversed group with the result of the recursive call.
5. If fewer than $k$ nodes remain, return the list as is.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $head = [1,2,3,4,5]$, $k = 2$.

The linked list: `1 -> 2 -> 3 -> 4 -> 5 -> None`

**2.2 Start Checking/Processing**

We first check if there are at least $k$ nodes. For the first call, we have 5 nodes, which is more than 2.

**2.3 Trace Walkthrough**

**First group (nodes 1-2):**
1. Count nodes: We have 5 nodes, so we can reverse a group of 2.
2. Reverse nodes 1-2:
   - Before: `1 -> 2 -> 3 -> 4 -> 5`
   - After: `2 -> 1 -> 3 -> 4 -> 5`
3. Recursively process remaining: `3 -> 4 -> 5`

**Second group (nodes 3-4):**
1. Count nodes: We have 3 nodes, so we can reverse a group of 2.
2. Reverse nodes 3-4:
   - Before: `3 -> 4 -> 5`
   - After: `4 -> 3 -> 5`
3. Recursively process remaining: `5`

**Remaining (node 5):**
1. Count nodes: We have 1 node, which is less than 2.
2. Return as is: `5`

**Final result:** `2 -> 1 -> 4 -> 3 -> 5`

**2.4 Increment and Loop**

The reversal process:
1. Use a helper function to reverse a segment from `start` to `end` (exclusive).
2. The helper reverses the segment by:
   - Setting `prev = None`
   - For each node, save `next`, point `curr.next` to `prev`, move `prev` and `curr` forward
3. After reversing $k$ nodes, recursively call on the remaining list.
4. Connect the reversed head with the result of recursion.

**2.5 Return Result**

After processing all groups, the list becomes `[2,1,4,3,5]`:
* Group 1: `[1,2]` → `[2,1]`
* Group 2: `[3,4]` → `[4,3]`
* Remaining: `[5]` → `[5]`

The final result is `2 -> 1 -> 4 -> 3 -> 5`.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a linked list segment
        def reverse_segment(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Count nodes to check if we have enough for a group
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            # Reverse the first k nodes
            reversed_head = reverse_segment(head, curr)
            # Recursively reverse the rest
            head.next = self.reverseKGroup(curr, k)
            return reversed_head
        
        # Not enough nodes, return as is
        return head
```

## 19. Remove Nth Node From End of List [Medium]
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

### Explanation

## Explanation

### Strategy (The "Why")

Given the head of a linked list and an integer $n$, we need to remove the $n$-th node from the end of the list and return the head.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be between $1$ and $30$.
- **Value Range:** Node values are between $1$ and $100$.
- **Time Complexity:** $O(L)$ where $L$ is the length of the list. We make one pass through the list.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If we need to remove the head node ($n$ equals the list length), we need special handling. Using a dummy node simplifies this.

**1.2 High-level approach:**

The goal is to remove the $n$-th node from the end of a linked list.

![Remove Nth Node](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

We use two pointers: a fast pointer and a slow pointer. We move the fast pointer $n+1$ steps ahead, then move both pointers together. When fast reaches the end, slow will be at the node before the one to remove.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** First pass to count the length, second pass to find and remove the $(L-n+1)$-th node from the beginning. This takes two passes.
- **Optimized Strategy (Two Pointers):** Use two pointers with a gap of $n+1$ nodes. Move both together until the fast pointer reaches the end. This takes one pass.
- **Why it's better:** The two-pointer approach is more elegant and requires only one pass through the list, though both approaches have the same time complexity.

**1.4 Decomposition:**

1. Create a dummy node pointing to the head (to handle edge cases).
2. Initialize two pointers (fast and slow) at the dummy node.
3. Move the fast pointer $n+1$ steps ahead.
4. Move both pointers together until fast reaches the end.
5. Remove the node after slow (which is the $n$-th node from the end).
6. Return the head (via dummy.next).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: head = $[1,2,3,4,5]$, $n = 2$

We initialize:
- `dummy = ListNode(0)`, `dummy.next = head`
- `fast = dummy`, `slow = dummy`

**2.2 Start Processing:**

We move the fast pointer $n+1 = 3$ steps ahead.

**2.3 Trace Walkthrough:**

| Step | Fast Position | Slow Position | Action |
|------|---------------|---------------|--------|
| Initial | dummy | dummy | - |
| After moving fast 3 steps | node 4 | dummy | Fast is 3 steps ahead |
| Move both together | node 5 | node 1 | Continue... |
| Move both together | null | node 3 | Fast reached end |

When fast is null, slow is at node 3 (the node before node 4, which is the 2nd from end).

**2.4 Remove Node:**

- `slow.next = slow.next.next` removes node 4
- Result: $[1,2,3,5]$

**2.5 Return Result:**

We return `dummy.next` which points to the new head $[1,2,3,5]$.

> **Note:** The dummy node is crucial because it handles the edge case where we need to remove the head node. Without it, we'd need special handling for that case.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Two pointers: fast and slow
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next
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

## 104. Maximum Depth of Binary Tree [Easy]
https://leetcode.com/problems/maximum-depth-of-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the tree can be between $0$ and $10^4$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Edge Case:** If the tree is empty (root is null), return 0.

**1.2 High-level approach:**

The goal is to find the maximum depth of a binary tree.

![Maximum Depth](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

We use recursion: the maximum depth of a tree is 1 plus the maximum of the depths of its left and right subtrees.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree to find the depth.
- **Optimized Strategy (Recursion):** Recursively compute the depth of left and right subtrees, then return 1 plus the maximum. This is the natural and efficient approach.
- **Why it's better:** Recursion naturally follows the tree structure. Each node's depth depends only on its children's depths, creating optimal substructure.

**1.4 Decomposition:**

1. Base case: if the root is null, return 0.
2. Recursively find the maximum depth of the left subtree.
3. Recursively find the maximum depth of the right subtree.
4. Return 1 (for current node) plus the maximum of the two subtree depths.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[3,9,20,null,null,15,7]$

The tree structure:
```
    3
   / \
  9   20
     /  \
    15   7
```

**2.2 Start Recursion:**

We begin from the root node (value 3).

**2.3 Trace Walkthrough:**

| Node | Left Depth | Right Depth | Max Depth | Return Value |
|------|------------|--------------|-----------|--------------|
| 3 | ? | ? | - | Compute... |
| 9 | 0 (null) | 0 (null) | 0 | $0 + 1 = 1$ |
| 20 | ? | ? | - | Compute... |
| 15 | 0 (null) | 0 (null) | 0 | $0 + 1 = 1$ |
| 7 | 0 (null) | 0 (null) | 0 | $0 + 1 = 1$ |
| 20 | 1 | 1 | 1 | $1 + 1 = 2$ |
| 3 | 1 | 2 | 2 | $2 + 1 = 3$ |

**2.4 Recursion Flow:**

- Root (3): left depth = 1, right depth = 2, return $max(1, 2) + 1 = 3$
- Node 9: both children null, return $0 + 1 = 1$
- Node 20: left depth = 1, right depth = 1, return $max(1, 1) + 1 = 2$

**2.5 Return Result:**

We return 3, which is the maximum depth of the tree.

> **Note:** The recursive approach naturally handles the tree structure. The depth of each node is computed from its children's depths, working from the leaves upward to the root.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        # Recursively find max depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return max depth plus 1 for current node
        return max(left_depth, right_depth) + 1
```

## 100. Same Tree [Easy]
https://leetcode.com/problems/same-tree/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to determine if two binary trees are structurally identical and have the same node values.

**1.1 Constraints & Complexity:**

- **Input Constraints:** Both trees have at most 100 nodes, and node values are in the range $[-10^4, 10^4]$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once, where $n$ is the minimum number of nodes in the two trees.
- **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In the worst case (skewed tree), $h = n$, giving $O(n)$ space.
- **Edge Case:** Both trees are empty (both roots are `None`), which should return `True`.

**1.2 High-level approach:**

The goal is to check if two trees have the same structure and values by comparing them node by node recursively. We compare the root values, then recursively check left and right subtrees.

![Binary tree comparison](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert both trees to arrays using traversal, then compare arrays. This requires $O(n)$ time and $O(n)$ space for storing both arrays.
- **Optimized (Recursive Comparison):** Compare nodes directly during traversal without storing intermediate results. This uses $O(n)$ time but only $O(h)$ space for the recursion stack.
- **Emphasize the optimization:** By comparing nodes directly during traversal, we can short-circuit early if we find a mismatch, potentially avoiding full tree traversal.

**1.4 Decomposition:**

1. **Base Cases:** If both nodes are `None`, return `True`. If only one is `None`, return `False`.
2. **Value Comparison:** Check if the current nodes have the same value.
3. **Recursive Check:** Recursively check if left subtrees match and right subtrees match.
4. **Combine Results:** Return `True` only if values match and both subtrees match.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `p = [1,2,3]`, `q = [1,2,3]`.

Both trees have the same structure and values.

**2.2 Start Comparison:**

We begin at the root nodes of both trees.

**2.3 Trace Walkthrough:**

| Node Pair | p.val | q.val | Match? | Left Check | Right Check | Result |
|-----------|-------|-------|--------|------------|-------------|--------|
| Root (1, 1) | 1 | 1 | Yes | Check (2, 2) | Check (3, 3) | Continue |
| Left (2, 2) | 2 | 2 | Yes | Check (None, None) | Check (None, None) | True |
| Right (3, 3) | 3 | 3 | Yes | Check (None, None) | Check (None, None) | True |

**2.4 Recursive Unwinding:**

- Both left subtrees (2, 2) match: both have value 2 and no children.
- Both right subtrees (3, 3) match: both have value 3 and no children.
- Root nodes (1, 1) match.

**2.5 Return Result:**

Since all nodes match in structure and value, the function returns `True`.

> **Note:** The algorithm short-circuits: if any node comparison fails, the entire function returns `False` immediately without checking remaining nodes.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are None
        if not p and not q:
            return True
        
        # One is None, the other is not
        if not p or not q:
            return False
        
        # Both exist, check values and recursively check children
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## 101. Symmetric Tree [Easy]
https://leetcode.com/problems/symmetric-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to check whether it is a mirror of itself (symmetric around its center).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $1000$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$.
- **Edge Case:** An empty tree is symmetric. A tree with only one node is symmetric.

**1.2 High-level approach:**

The goal is to determine if a binary tree is symmetric (mirror of itself).

We use recursion to check if the left and right subtrees are mirrors of each other. Two trees are mirrors if their roots have the same value, and the left subtree of one is a mirror of the right subtree of the other, and vice versa.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must check the mirror property.
- **Optimized Strategy (Recursion):** Use recursion to check if left and right subtrees are mirrors. This is the standard and efficient approach.
- **Why it's better:** Recursion naturally checks the mirror property by comparing corresponding nodes in the left and right subtrees.

**1.4 Decomposition:**

1. Define a helper function that checks if two trees are mirrors.
2. Two trees are mirrors if:
   - Both are null (base case: true).
   - One is null and the other is not (false).
   - Both roots have the same value, and:
     - Left subtree of first is mirror of right subtree of second.
     - Right subtree of first is mirror of left subtree of second.
3. Check if root's left and right subtrees are mirrors.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,2,2,3,4,4,3]$

The tree structure:
```
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

We initialize:
- Call `is_mirror(root.left, root.right)`

**2.2 Start Checking:**

We begin checking if left and right subtrees are mirrors.

**2.3 Trace Walkthrough:**

| left | right | left.val | right.val | Check | Result |
|------|-------|----------|-----------|-------|--------|
| 2 | 2 | 2 | 2 | Equal ✓ | Check children |
| 3 | 3 | 3 | 3 | Equal ✓ | Both null ✓ |
| 4 | 4 | 4 | 4 | Equal ✓ | Both null ✓ |
| 4 | 4 | 4 | 4 | Equal ✓ | Both null ✓ |
| 3 | 3 | 3 | 3 | Equal ✓ | Both null ✓ |

**2.4 Explanation:**

- Root's left (2) and right (2) have same value ✓
- Left's left (3) and right's right (3) are mirrors ✓
- Left's right (4) and right's left (4) are mirrors ✓

**2.5 Return Result:**

We return `True` because the tree is symmetric.

> **Note:** The key insight is that a tree is symmetric if its left and right subtrees are mirrors. Two trees are mirrors if their roots match and the left of one mirrors the right of the other (and vice versa).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and 
                    is_mirror(left.left, right.right) and 
                    is_mirror(left.right, right.left))
        
        if not root:
            return True
        
        return is_mirror(root.left, root.right)
```

## 105. Construct Binary Tree from Preorder and Inorder Traversal [Medium]
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to construct a binary tree from its preorder and inorder traversal arrays.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 3000$, values in $[-3000, 3000]$, all values are unique.
- **Time Complexity:** $O(n)$ - We visit each node once. The hash map lookup is $O(1)$.
- **Space Complexity:** $O(n)$ - Hash map for inorder indices takes $O(n)$, recursion stack takes $O(h)$ where $h$ is tree height.
- **Edge Case:** Empty arrays return `None`.

**1.2 High-level approach:**

The goal is to reconstruct the tree using the property that in preorder, the root comes first, and in inorder, the root separates left and right subtrees.

![Tree Construction](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each root, search for it in inorder array linearly. This takes $O(n^2)$ time.
- **Optimized (Hash Map):** Use a hash map to store inorder indices for $O(1)$ lookup. This takes $O(n)$ time.
- **Emphasize the optimization:** The hash map reduces the time complexity from $O(n^2)$ to $O(n)$ by eliminating linear searches.

**1.4 Decomposition:**

1. **Build Hash Map:** Create a map from values to their inorder indices.
2. **Recursive Build:** Use preorder to get root, use inorder to split left/right subtrees.
3. **Calculate Ranges:** Determine preorder and inorder ranges for left and right subtrees.
4. **Return Root:** Build and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`.

Hash map: `{9:0, 3:1, 15:2, 20:3, 7:4}`

**2.2 Start Building:**

Root is `preorder[0] = 3`. Find its position in inorder: `inorder[1] = 3`.

**2.3 Trace Walkthrough:**

| Root | Preorder Range | Inorder Range | Left Size | Left Subtree | Right Subtree |
|------|----------------|---------------|-----------|--------------|---------------|
| 3 | [0:4] | [0:4] | 1 | pre[1:2], in[0:0] | pre[2:5], in[2:4] |
| 9 | [1:2] | [0:0] | 0 | None | None |
| 20 | [2:5] | [2:4] | 1 | pre[3:4], in[2:2] | pre[4:5], in[3:4] |
| 15 | [3:4] | [2:2] | 0 | None | None |
| 7 | [4:5] | [3:4] | 0 | None | None |

**2.4 Complete Construction:**

Tree structure: `3` (root) with left child `9` and right child `20`. `20` has left child `15` and right child `7`.

**2.5 Return Result:**

The function returns the root node of the constructed tree.

> **Note:** The key insight is that preorder gives us the root, and inorder tells us how many nodes are in the left subtree, allowing us to split the preorder array correctly.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Create a map for O(1) lookup of inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            # Root is the first element in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find root position in inorder
            root_idx = inorder_map[root_val]
            
            # Calculate sizes of left and right subtrees
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

## 106. Construct Binary Tree from Inorder and Postorder Traversal [Medium]
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to construct a binary tree from its inorder and postorder traversal arrays.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 3000$, values in $[-3000, 3000]$, all values are unique.
- **Time Complexity:** $O(n)$ - We visit each node once. The hash map lookup is $O(1)$.
- **Space Complexity:** $O(n)$ - Hash map for inorder indices takes $O(n)$, recursion stack takes $O(h)$.
- **Edge Case:** Empty arrays return `None`.

**1.2 High-level approach:**

The goal is to reconstruct the tree using the property that in postorder, the root comes last, and in inorder, the root separates left and right subtrees.

![Tree Construction](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each root, search for it in inorder array linearly. This takes $O(n^2)$ time.
- **Optimized (Hash Map):** Use a hash map to store inorder indices for $O(1)$ lookup. This takes $O(n)$ time.
- **Emphasize the optimization:** The hash map reduces the time complexity from $O(n^2)$ to $O(n)$ by eliminating linear searches.

**1.4 Decomposition:**

1. **Build Hash Map:** Create a map from values to their inorder indices.
2. **Recursive Build:** Use postorder to get root (last element), use inorder to split left/right subtrees.
3. **Calculate Ranges:** Determine inorder and postorder ranges for left and right subtrees.
4. **Return Root:** Build and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `inorder = [9,3,15,20,7]`, `postorder = [9,15,7,20,3]`.

Hash map: `{9:0, 3:1, 15:2, 20:3, 7:4}`

**2.2 Start Building:**

Root is `postorder[4] = 3`. Find its position in inorder: `inorder[1] = 3`.

**2.3 Trace Walkthrough:**

| Root | Inorder Range | Postorder Range | Left Size | Left Subtree | Right Subtree |
|------|---------------|-----------------|-----------|--------------|---------------|
| 3 | [0:4] | [0:4] | 1 | in[0:0], post[0:0] | in[2:4], post[1:3] |
| 9 | [0:0] | [0:0] | 0 | None | None |
| 20 | [2:4] | [1:3] | 1 | in[2:2], post[1:1] | in[3:4], post[2:2] |
| 15 | [2:2] | [1:1] | 0 | None | None |
| 7 | [3:4] | [2:2] | 0 | None | None |

**2.4 Complete Construction:**

Tree structure: `3` (root) with left child `9` and right child `20`. `20` has left child `15` and right child `7`.

**2.5 Return Result:**

The function returns the root node of the constructed tree.

> **Note:** Similar to problem 105, but here the root is the last element in postorder instead of the first in preorder.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # Create a map for O(1) lookup of inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None
            
            # Root is the last element in postorder
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # Find root position in inorder
            root_idx = inorder_map[root_val]
            
            # Calculate sizes of left and right subtrees
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(in_start, root_idx - 1, post_start, post_start + left_size - 1)
            root.right = build(root_idx + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
```

## 236. Lowest Common Ancestor of a Binary Tree [Medium]
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to find the lowest common ancestor (LCA) of two nodes in a binary tree. The LCA is the deepest node that has both nodes as descendants (a node can be a descendant of itself).

**1.1 Constraints & Complexity:**

- **Input Constraints:** The tree has $2 \leq n \leq 10^5$ nodes with unique values in $[-10^9, 10^9]$.
- **Time Complexity:** $O(n)$ - We may need to visit all nodes in the worst case.
- **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
- **Edge Case:** If one node is an ancestor of the other, return that ancestor node.

**1.2 High-level approach:**

The goal is to find the deepest node that is an ancestor of both target nodes. We use recursive DFS: if we find both nodes in a subtree, the current root is the LCA.

![Binary Tree LCA](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find paths to both nodes, then find the last common node in both paths. This requires storing paths and takes $O(n)$ time and $O(n)$ space.
- **Optimized (Recursive DFS):** Recursively search both subtrees. If both subtrees return non-null, the current root is the LCA. This takes $O(n)$ time and $O(h)$ space.
- **Emphasize the optimization:** The recursive approach finds the LCA in a single pass without storing paths, making it more space-efficient.

**1.4 Decomposition:**

1. **Base Case:** If root is `None` or equals `p` or `q`, return root.
2. **Recursive Search:** Recursively search left and right subtrees for `p` and `q`.
3. **Combine Results:** If both subtrees return non-null, root is the LCA. Otherwise, return whichever subtree found a node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 1`.

**2.2 Start Searching:**

Begin at root node `3`.

**2.3 Trace Walkthrough:**

| Node | Left Result | Right Result | Action |
|------|-------------|--------------|---------|
| 3 | Search left (5) | Search right (1) | Both found → Return 3 |
| 5 | Search left (6) | Search right (2) | Found p → Return 5 |
| 1 | Search left (0) | Search right (8) | Found q → Return 1 |

**2.4 Recursive Unwinding:**

- Node `5` returns itself (found `p`).
- Node `1` returns itself (found `q`).
- Node `3` receives both results, so it's the LCA.

**2.5 Return Result:**

The function returns node `3`, which is the LCA of nodes `5` and `1`.

> **Note:** The key insight is that if both left and right subtrees return non-null, the current root must be the LCA. If only one subtree returns non-null, that subtree contains the LCA.

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or root is p or q, return root
        if not root or root == p or root == q:
            return root
        
        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return non-None, root is the LCA
        if left and right:
            return root
        
        # Otherwise, return whichever side found p or q
        return left if left else right
```

## 199. Binary Tree Right Side View [Medium]
https://leetcode.com/problems/binary-tree-right-side-view/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to return the values of the nodes you can see when standing on the right side of the tree, ordered from top to bottom.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be up to $100$.
- **Value Range:** Node values are between $0$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level.
- **Edge Case:** If the tree is empty, return an empty list. If the tree has only one node, return that node's value.

**1.2 High-level approach:**

The goal is to find the rightmost node at each level of the tree.

![Right Side View](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

We use BFS (breadth-first search) level by level. For each level, we add the rightmost node (the last node processed at that level) to our result.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree.
- **Optimized Strategy (BFS):** Use BFS to process nodes level by level. For each level, track the last node processed, which is the rightmost node. This is the same as level-order traversal, but we only keep the last element of each level.
- **Why it's better:** BFS naturally processes nodes level by level from left to right, so the last node at each level is the rightmost node.

**1.4 Decomposition:**

1. If the tree is empty, return an empty list.
2. Initialize a queue with the root node.
3. While the queue is not empty:
   - Get the number of nodes at the current level.
   - Process all nodes at this level.
   - For the last node at each level (rightmost), add its value to the result.
   - Add all children to the queue for the next level.
4. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,2,3,null,5,null,4]$

The tree structure:
```
    1
   / \
  2   3
   \   \
    5   4
```

We initialize:
- `queue = deque([1])`
- `res = []`

**2.2 Start BFS:**

We begin processing level by level.

**2.3 Trace Walkthrough:**

| Level | Queue Before | Level Size | Process | Rightmost Node | res |
|-------|--------------|------------|---------|----------------|-----|
| 0 | [1] | 1 | Node 1 (last) | 1 | [1] |
| 1 | [2, 3] | 2 | Node 2, Node 3 (last) | 3 | [1, 3] |
| 2 | [5, 4] | 2 | Node 5, Node 4 (last) | 4 | [1, 3, 4] |

**2.4 Explanation:**

- Level 0: Only node 1 → add 1
- Level 1: Nodes 2 and 3 → add 3 (rightmost)
- Level 2: Nodes 5 and 4 → add 4 (rightmost)

**2.5 Return Result:**

We return `[1, 3, 4]`, which are the values of the rightmost nodes at each level.

> **Note:** The key is to identify the last node processed at each level during BFS. Since BFS processes nodes from left to right, the last node at each level is the rightmost node visible from the right side.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from collections import deque

class Solution:
    def rightSideView(self, root) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Add the rightmost node of each level
                if i == level_size - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
```

## 102. Binary Tree Level Order Traversal [Medium]
https://leetcode.com/problems/binary-tree-level-order-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to return the level-order traversal of its nodes' values (i.e., from left to right, level by level).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be up to $2000$.
- **Value Range:** Node values are between $-1000$ and $1000$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level, which is $O(n)$ in the worst case.
- **Edge Case:** If the tree is empty, return an empty list.

**1.2 High-level approach:**

The goal is to traverse the tree level by level, collecting values at each level.

![Level Order Traversal](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

We use BFS (breadth-first search) with a queue. We process nodes level by level, adding all nodes at the current level to a list before moving to the next level.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree.
- **Optimized Strategy (BFS with Queue):** Use a queue to process nodes level by level. For each level, process all nodes in the queue (which represents the current level), then add their children for the next level.
- **Why it's better:** BFS naturally processes nodes level by level. Using a queue ensures we process all nodes at one level before moving to the next.

**1.4 Decomposition:**

1. If the tree is empty, return an empty list.
2. Initialize a queue with the root node.
3. While the queue is not empty:
   - Get the number of nodes at the current level (queue size).
   - Process all nodes at this level, adding their values to a level list.
   - Add all children of these nodes to the queue for the next level.
   - Add the level list to the result.
4. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[3,9,20,null,null,15,7]$

The tree structure:
```
    3
   / \
  9   20
     /  \
    15   7
```

We initialize:
- `queue = deque([3])`
- `res = []`

**2.2 Start BFS:**

We begin processing level by level.

**2.3 Trace Walkthrough:**

| Level | Queue Before | Level Size | Process Nodes | Level List | Queue After |
|-------|--------------|------------|---------------|------------|-------------|
| 0 | [3] | 1 | 3 | [3] | [9, 20] |
| 1 | [9, 20] | 2 | 9, 20 | [9, 20] | [15, 7] |
| 2 | [15, 7] | 2 | 15, 7 | [15, 7] | [] |

**2.4 Final Result:**

After processing all levels:
- `res = [[3], [9, 20], [15, 7]]`

**2.5 Return Result:**

We return `[[3], [9, 20], [15, 7]]`, which represents the level-order traversal.

> **Note:** The key is to process all nodes at the current level before moving to the next. We do this by getting the queue size at the start of each iteration, which represents the number of nodes at the current level.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res
```

## 103. Binary Tree Zigzag Level Order Traversal [Medium]
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to return the zigzag level order traversal of a binary tree: left-to-right for even levels, right-to-left for odd levels.

**1.1 Constraints & Complexity:**

- **Input Constraints:** The tree has $0 \leq n \leq 2000$ nodes with values in $[-100, 100]$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level.
- **Edge Case:** Empty tree returns empty list.

**1.2 High-level approach:**

The goal is to traverse the tree level by level, alternating the direction at each level. We use BFS with a flag to track direction.

![Zigzag Traversal](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Do regular level-order traversal, then reverse every other level. This takes $O(n)$ time and $O(n)$ space.
- **Optimized (BFS with Direction Flag):** Use BFS and reverse the level list when needed based on a flag. This takes $O(n)$ time and $O(n)$ space.
- **Emphasize the optimization:** While complexity is the same, the direction flag approach is cleaner and more efficient than reversing after collection.

**1.4 Decomposition:**

1. **BFS Traversal:** Use a queue to process nodes level by level.
2. **Track Direction:** Use a boolean flag to alternate between left-to-right and right-to-left.
3. **Reverse When Needed:** For odd levels (right-to-left), reverse the level list before adding to result.
4. **Return Result:** Return the list of levels.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [3,9,20,null,null,15,7]`.

Initialize: `queue = [3]`, `left_to_right = True`, `res = []`

**2.2 Start Processing:**

Process level 0 (root).

**2.3 Trace Walkthrough:**

| Level | Queue Before | Level Values | Direction | After Reverse | Result |
|-------|--------------|--------------|-----------|---------------|--------|
| 0 | [3] | [3] | L→R | [3] | [[3]] |
| 1 | [9, 20] | [9, 20] | R→L | [20, 9] | [[3], [20, 9]] |
| 2 | [15, 7] | [15, 7] | L→R | [15, 7] | [[3], [20, 9], [15, 7]] |

**2.4 Complete Traversal:**

All levels processed: Level 0 (L→R), Level 1 (R→L), Level 2 (L→R).

**2.5 Return Result:**

The function returns `[[3], [20, 9], [15, 7]]`.

> **Note:** The direction alternates at each level: even levels (0, 2, ...) are left-to-right, odd levels (1, 3, ...) are right-to-left.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = [root]
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse if needed for zigzag
            if not left_to_right:
                level.reverse()
            
            res.append(level)
            left_to_right = not left_to_right
        
        return res
```

## 230. Kth Smallest Element in a BST [Medium]
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary search tree (BST) and an integer $k$, we need to find the $k$-th smallest element in the BST.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the BST can be up to $10^4$.
- **Value Range:** Node values are between $1$ and $10^4$.
- **Time Complexity:** $O(n)$ - We traverse all nodes in the BST using in-order traversal, which visits each node exactly once.
- **Space Complexity:** $O(n)$ - In the worst case (a skewed tree), the recursion stack can be $O(n)$ deep. Additionally, we store all node values in a list, which requires $O(n)$ space.
- **Edge Case:** If $k$ is 1, we return the smallest element. If $k$ equals the number of nodes, we return the largest element.

**1.2 High-level approach:**

The goal is to find the $k$-th smallest element in a BST.

![BST In-order Traversal](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

A key property of a BST is that an in-order traversal (left → root → right) visits nodes in ascending order. Therefore, the $k$-th element visited during an in-order traversal is the $k$-th smallest element.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Perform an in-order traversal to collect all node values in a list, then return the element at index $k-1$. This approach is straightforward and works correctly.
- **Optimized Strategy:** We can optimize by stopping the traversal once we've found the $k$-th element, using an iterative approach or early termination in recursion. However, for clarity and beginner-friendliness, we'll use the complete traversal approach.
- **Why it's better:** The brute force approach is actually quite efficient for this problem. A more optimized version would use iterative in-order traversal with early termination, but the complete traversal approach is easier to understand.

**1.4 Decomposition:**

1. Perform an in-order traversal of the BST (visit left subtree, then root, then right subtree).
2. Collect all node values in a list during the traversal.
3. Since in-order traversal of a BST produces values in sorted order, the list will be sorted.
4. Return the element at index $k-1$ (since $k$ is 1-indexed).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[3, 1, 4, null, 2]$, $k = 1$

The BST structure:
```
    3
   / \
  1   4
   \
    2
```

We initialize:
- An empty list `res = []` to store node values
- We'll perform in-order traversal starting from the root

**2.2 Start Traversing:**

We begin the in-order traversal from the root node (value 3).

**2.3 Trace Walkthrough:**

The in-order traversal visits nodes in this order:

| Step | Current Node | Action | List State |
|------|--------------|--------|------------|
| 1 | 3 (root) | Go to left child (1) | [] |
| 2 | 1 | Go to left child (null) | [] |
| 3 | null | Return (base case) | [] |
| 4 | 1 | Add 1 to list | [1] |
| 5 | 1 | Go to right child (2) | [1] |
| 6 | 2 | Go to left child (null) | [1] |
| 7 | null | Return (base case) | [1] |
| 8 | 2 | Add 2 to list | [1, 2] |
| 9 | 2 | Go to right child (null) | [1, 2] |
| 10 | null | Return (base case) | [1, 2] |
| 11 | 3 | Add 3 to list | [1, 2, 3] |
| 12 | 3 | Go to right child (4) | [1, 2, 3] |
| 13 | 4 | Go to left child (null) | [1, 2, 3] |
| 14 | null | Return (base case) | [1, 2, 3] |
| 15 | 4 | Add 4 to list | [1, 2, 3, 4] |
| 16 | 4 | Go to right child (null) | [1, 2, 3, 4] |
| 17 | null | Return (base case) | [1, 2, 3, 4] |

After traversal: `res = [1, 2, 3, 4]`

**2.4 Return Result:**

Since $k = 1$ (1-indexed), we return `res[0] = 1`, which is the 1st smallest element.

For $k = 3$, we would return `res[2] = 3`, which is the 3rd smallest element.

> **Note:** In-order traversal of a BST always produces values in ascending order because of the BST property: all values in the left subtree are less than the root, and all values in the right subtree are greater than the root.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        # In-order traversal to get elements in sorted order
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Return the k-th smallest element (1-indexed)
        return res[k - 1]
```

## 98. Validate Binary Search Tree [Medium]
https://leetcode.com/problems/validate-binary-search-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to determine if it is a valid binary search tree (BST). A BST is valid if for every node, all nodes in its left subtree are less than it, and all nodes in its right subtree are greater than it.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Edge Case:** An empty tree is a valid BST. A tree with only one node is a valid BST.

**1.2 High-level approach:**

The goal is to validate that a binary tree satisfies the BST property.

We use recursion with range validation. For each node, we check if its value is within the valid range (min_val, max_val). The range is updated as we traverse: left children must be less than the parent, right children must be greater than the parent.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each node, check if all nodes in its left subtree are less and all nodes in its right subtree are greater. This would be $O(n^2)$ time.
- **Optimized Strategy (Range Validation):** Use recursion with min and max bounds. Each node must be within its allowed range. This takes $O(n)$ time.
- **Why it's better:** The range validation approach reduces time complexity from $O(n^2)$ to $O(n)$ by passing down constraints instead of checking all descendants for each node.

**1.4 Decomposition:**

1. Define a recursive function that takes a node and its allowed range (min_val, max_val).
2. If the node is null, return true (base case).
3. Check if the node's value is within the range (strictly greater than min_val and strictly less than max_val).
4. Recursively validate left subtree with range (min_val, node.val).
5. Recursively validate right subtree with range (node.val, max_val).
6. Return true only if all checks pass.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[5,1,4,null,null,3,6]$

The tree structure:
```
    5
   / \
  1   4
     / \
    3   6
```

We initialize:
- Call `validate(root, -∞, +∞)`

**2.2 Start Validation:**

We begin validating from the root.

**2.3 Trace Walkthrough:**

| Node | min_val | max_val | node.val | Check | Result |
|------|---------|---------|----------|-------|--------|
| 5 | -∞ | +∞ | 5 | $-∞ < 5 < +∞$ | ✓ |
| 1 | -∞ | 5 | 1 | $-∞ < 1 < 5$ | ✓ |
| 4 | 5 | +∞ | 4 | $5 < 4 < +∞$ | ✗ |

**2.4 Explanation:**

- Root (5): Valid, within range (-∞, +∞)
- Left child (1): Valid, within range (-∞, 5)
- Right child (4): Invalid! It should be greater than 5, but 4 < 5

**2.5 Return Result:**

We return `False` because node 4 violates the BST property (it's in the right subtree of 5 but is less than 5).

> **Note:** The key insight is to pass down the allowed range for each node. A node's value must be strictly within its range, and we update the range for children: left children get (min_val, node.val) and right children get (node.val, max_val).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, min_val, max_val):
            # Empty tree is valid
            if not node:
                return True
            
            # Check if current node value is within valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
```

## 208. Implement Trie (Prefix Tree) [Medium]
https://leetcode.com/problems/implement-trie-prefix-tree/

### Explanation

## Explanation

### Strategy (The "Why")

We need to implement a Trie (prefix tree) data structure that supports inserting words, searching for complete words, and checking if any word starts with a given prefix.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of operations $N$ can be up to $3 \times 10^4$.
- **Value Range:** Words and prefixes consist of lowercase English letters only, with length between 1 and 2000.
- **Time Complexity:** 
  - `insert`: $O(m)$ where $m$ is the length of the word
  - `search`: $O(m)$ where $m$ is the length of the word
  - `startsWith`: $O(m)$ where $m$ is the length of the prefix
- **Space Complexity:** $O(ALPHABET\_SIZE \times N \times M)$ where $N$ is the number of words and $M$ is the average length. In practice, this is $O(\text{total characters in all words})$.
- **Edge Case:** Searching for an empty string should return false (unless an empty word was inserted). Checking prefix of empty string should return true if any word exists.

**1.2 High-level approach:**

The goal is to implement a Trie data structure that efficiently stores and retrieves words.

![Trie Structure](https://assets.leetcode.com/uploads/2021/04/28/trie-1.png)

A Trie is a tree-like data structure where each node represents a character. Words that share common prefixes share the same path in the tree. This makes prefix searches very efficient.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Store all words in a list. For search and prefix operations, iterate through all words checking each one. This takes $O(n \times m)$ time where $n$ is the number of words.
- **Optimized Strategy (Trie):** Use a tree structure where each node has children representing possible next characters. This allows us to search in $O(m)$ time regardless of how many words are stored.
- **Why it's better:** The Trie structure eliminates the need to check every word. We only traverse the path relevant to the word or prefix we're looking for, making it much more efficient for large datasets.

**1.4 Decomposition:**

1. Create a `TrieNode` class with a dictionary of children and a flag indicating if it's the end of a word.
2. Initialize the Trie with a root `TrieNode`.
3. For `insert`: Traverse the tree, creating nodes as needed, and mark the final node as an end-of-word.
4. For `search`: Traverse the tree following the word's characters. Return true only if we reach the end and the final node is marked as end-of-word.
5. For `startsWith`: Similar to search, but return true if we can traverse the entire prefix, regardless of whether it's a complete word.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example operations:
- `insert("apple")`
- `search("apple")` → returns true
- `search("app")` → returns false
- `startsWith("app")` → returns true
- `insert("app")`
- `search("app")` → returns true

We initialize:
- A root `TrieNode` with empty children dictionary
- `is_end = False` for all nodes initially

**2.2 Start Inserting:**

We begin by inserting "apple".

**2.3 Trace Walkthrough:**

**Insert "apple":**

| Step | Current Node | Character | Action | New Node Created? |
|------|--------------|-----------|--------|-------------------|
| 1 | root | 'a' | Create node for 'a' | Yes |
| 2 | a-node | 'p' | Create node for 'p' | Yes |
| 3 | p-node | 'p' | Create node for 'p' | Yes |
| 4 | p-node | 'l' | Create node for 'l' | Yes |
| 5 | l-node | 'e' | Create node for 'e', mark as end | Yes |

**Search "apple":**

| Step | Current Node | Character | Found? | Action |
|------|--------------|-----------|--------|--------|
| 1 | root | 'a' | Yes | Move to 'a' node |
| 2 | a-node | 'p' | Yes | Move to 'p' node |
| 3 | p-node | 'p' | Yes | Move to 'p' node |
| 4 | p-node | 'l' | Yes | Move to 'l' node |
| 5 | l-node | 'e' | Yes | Check is_end → true → Return true |

**Search "app":**

| Step | Current Node | Character | Found? | Action |
|------|--------------|-----------|--------|--------|
| 1 | root | 'a' | Yes | Move to 'a' node |
| 2 | a-node | 'p' | Yes | Move to 'p' node |
| 3 | p-node | 'p' | Yes | Check is_end → false → Return false |

**startsWith "app":**

| Step | Current Node | Character | Found? | Action |
|------|--------------|-----------|--------|--------|
| 1 | root | 'a' | Yes | Move to 'a' node |
| 2 | a-node | 'p' | Yes | Move to 'p' node |
| 3 | p-node | 'p' | Yes | All characters found → Return true |

**2.4 Insert "app" and Search Again:**

After inserting "app", the second 'p' node now has `is_end = true`. So searching "app" will now return true.

**2.5 Return Result:**

The Trie correctly handles all operations, allowing efficient word storage and prefix matching.

> **Note:** The key difference between `search` and `startsWith` is that `search` requires the final node to be marked as an end-of-word, while `startsWith` only requires that the path exists.

### Solution

```python
def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
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

## 23. Merge k Sorted Lists [Hard]
https://leetcode.com/problems/merge-k-sorted-lists/

### Explanation

## Explanation

### Strategy (The "Why")

Given an array of $k$ sorted linked lists, we need to merge all of them into one sorted linked list and return it.

**1.1 Constraints & Complexity:**

- **Input Size:** $k$ can be between $0$ and $10^4$, and the total number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-10^4$ and $10^4$.
- **Time Complexity:** $O(n \log k)$ where $n$ is the total number of nodes. We use a heap of size $k$, and each insertion/extraction takes $O(\log k)$ time. We do this for $n$ nodes.
- **Space Complexity:** $O(k)$ - We maintain a heap of size $k$.
- **Edge Case:** If the array is empty, return null. If all lists are empty, return null.

**1.2 High-level approach:**

The goal is to merge $k$ sorted linked lists into one sorted list.

We use a min heap to always get the smallest node among all lists. We add the first node from each list to the heap, then repeatedly extract the minimum, add it to the result, and add the next node from that list to the heap.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Merge lists one by one. This takes $O(kn)$ time where $n$ is the average list length.
- **Optimized Strategy (Min Heap):** Use a min heap to efficiently get the minimum node at each step. This takes $O(n \log k)$ time.
- **Why it's better:** The heap approach reduces time complexity by maintaining only $k$ nodes in the heap instead of comparing all $k$ lists at each step.

**1.4 Decomposition:**

1. Create a min heap and add the first node from each non-empty list.
2. Create a dummy node to simplify edge cases.
3. While the heap is not empty:
   - Extract the minimum node from the heap.
   - Add it to the result list.
   - If that node has a next node, add the next node to the heap.
4. Return the head of the merged list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $lists = [[1,4,5],[1,3,4],[2,6]]$

We initialize:
- `heap = [(1,0,node1), (1,1,node1), (2,2,node2)]`
- `dummy = ListNode(0)`
- `current = dummy`

**2.2 Start Merging:**

We begin extracting from the heap.

**2.3 Trace Walkthrough:**

| Step | Extract | current.next | Add to heap | heap After |
|------|---------|--------------|-------------|------------|
| 1 | (1,0) | 1 | (4,0) | [(1,1), (2,2), (4,0)] |
| 2 | (1,1) | 1 | (3,1) | [(2,2), (3,1), (4,0)] |
| 3 | (2,2) | 2 | (6,2) | [(3,1), (4,0), (6,2)] |
| 4 | (3,1) | 3 | (4,1) | [(4,0), (4,1), (6,2)] |
| ... | ... | ... | ... | ... |

**2.4 Final Result:**

After merging: $[1,1,2,3,4,4,5,6]$

**2.5 Return Result:**

We return the head of the merged list: $[1,1,2,3,4,4,5,6]$.

> **Note:** The key insight is to use a min heap to efficiently get the minimum node among all lists at each step. By maintaining only the current head of each list in the heap, we avoid storing all nodes and achieve $O(n \log k)$ time complexity.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Create a min heap
        heap = []
        
        # Add first node from each list to heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Create dummy node
        dummy = ListNode(0)
        current = dummy
        
        # Merge lists
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # Add next node from the same list if it exists
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
```
