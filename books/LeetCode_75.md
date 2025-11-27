# LeetCode 75

Problem list from official https://leetcode.com/studyplan/leetcode-75/

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

## 142. Linked List Cycle II [Medium]
https://leetcode.com/problems/linked-list-cycle-ii/

### Explanation

Given the `head` of a linked list, return *the node where the cycle begins. If there is no cycle, return* `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

**Example 1:**

```sh
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:**

```sh
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:**

```sh
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

**Constraints:**
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Explanation

### Strategy

This is a **two-pointer problem** that extends the cycle detection problem to find the starting node of the cycle. The key insight is to use Floyd's Cycle-Finding Algorithm in two phases: first to detect the cycle, then to find its starting point.

**Key observations:**
- If there's a cycle, we can find the meeting point using fast/slow pointers
- The distance from head to cycle start equals the distance from meeting point to cycle start
- We can use this mathematical relationship to find the cycle start
- This approach uses O(1) space, which is optimal

**High-level approach:**
1. **Phase 1 - Detect cycle**: Use fast/slow pointers to find meeting point
2. **Phase 2 - Find cycle start**: Use two pointers from head and meeting point
3. **Return result**: The node where these pointers meet is the cycle start

### Steps

Let's break down the solution step by step:

**Phase 1: Detect the cycle**
- Use fast and slow pointers to find the meeting point
- If no meeting point is found, return null (no cycle)

**Phase 2: Find the cycle start**
- Reset slow pointer to head
- Move both pointers one step at a time
- The node where they meet is the cycle start

**Mathematical proof:**
- Let `F` be the distance from head to cycle start
- Let `C` be the cycle length
- Let `a` be the distance from cycle start to meeting point
- When fast and slow meet: `slow` has traveled `F + a`, `fast` has traveled `F + a + n*C`
- Since fast moves twice as fast: `2(F + a) = F + a + n*C`
- Simplifying: `F + a = n*C`
- Therefore: `F = n*C - a`
- This means the distance from head to cycle start equals the distance from meeting point to cycle start

**Example walkthrough:**
Let's trace through the first example:

```sh
head = [3,2,0,-4], pos = 1 (cycle from -4 back to 2)

Phase 1 - Detect cycle:
slow = 3, fast = 2
slow = 2, fast = 0
slow = 0, fast = 2
slow = -4, fast = 0
slow = 2, fast = 2 (meeting point found!)

Phase 2 - Find cycle start:
slow = 3 (reset to head), fast = 2 (meeting point)
slow = 2, fast = 0
slow = 0, fast = -4
slow = -4, fast = 2 (they meet at node 2!)

Result: Return node with value 2
```

> **Note:** This algorithm is optimal because it uses O(1) space and O(n) time. The mathematical proof ensures that the two pointers will meet at the cycle start after the second phase.

**Time Complexity:** O(n) - we visit each node at most twice  
**Space Complexity:** O(1) - we only use two pointers regardless of input size

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.next = None
```

## 334. Increasing Triplet Subsequence [Medium]
https://leetcode.com/problems/increasing-triplet-subsequence/

### Explanation

## 334. Increasing Triplet Subsequence [Medium]

https://leetcode.com/problems/increasing-triplet-subsequence

## Description
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

**Examples**
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

**Constraints**

```
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
```

## Hint
Track the smallest and second smallest values as you iterate.

## Explanation
Let's imagine you're looking for three numbers in order, each bigger than the last. We keep track of the smallest number we've seen so far, and then the next smallest after that. If we find a number bigger than both, we know we have a triplet!

We do this because it's much faster than checking every possible combination. By updating our two smallest values as we go, we make sure we're always ready to spot a valid triplet as soon as it appears.

This approach is efficient and uses only constant extra space, making it perfect for large arrays.

### Solution

```python
def increasingTriplet(nums):
    first = second = float("inf")
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False
```

## 1431. Kids With the Greatest Number of Candies [Easy]
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

### Explanation

## 1431. Kids With the Greatest Number of Candies [Easy]

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

## Description
There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i`th kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

**Examples**

```text
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

**Constraints**

```text
- n == candies.length
- 2 <= n <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
```

## Hint
For each kid, check if their candies plus `extraCandies` is at least as much as the current maximum.

## Explanation
First, you want to know the highest number of candies any kid currently has. This is important because you need a reference point to see if giving extra candies to a kid will make them "the greatest."

For each kid, you add the `extraCandies` to their current amount. You do this because you want to see if, after the bonus, they can reach or beat the current maximum. If they do, you mark them as `True` in our answer list; otherwise, False.

You only need to find the maximum once, and then just compare each kid's total to it. Don't need to recalculate the maximum for every kid.

### Solution

```python
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Find the current maximum
    return [(c + extraCandies) >= max_candies for c in candies]
```

## 345. Reverse Vowels of a String [Easy]
https://leetcode.com/problems/reverse-vowels-of-a-string/

### Explanation

## 345. Reverse Vowels of a String [Easy]

https://leetcode.com/problems/reverse-vowels-of-a-string

## Description
Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Examples**

```text
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Input: s = "leetcode"
Output: "leotcede"
```

**Constraints**

```text
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
```

## Explanation

### Strategy
- **Type:** String, Two Pointers
- **Given:** A string `s`
- **Asked:** Reverse only the vowels in `s`, keeping all other characters in their original positions

#### What does "reverse vowels" mean?
- Only the vowels ('a', 'e', 'i', 'o', 'u', both lowercase and uppercase) should be reversed in order. All other characters stay in place.

Ro reverse only the vowels in the string efficiently, you can use **two pointers**: one starting from the left, one from the right. You *move* each pointer until it finds a vowel. When both pointers are at vowels, you *swap* them.

You do this because it lets you reverse the vowels in-place, without affecting the other characters. Using two pointers is efficient and avoids unnecessary work, especially for long strings.

You keep moving the pointers toward each other, swapping vowels as you go, until they meet in the middle. This ensures every vowel is swapped exactly once, making the solution both correct and efficient.

#### High-Level Plan
1. Use two pointers: one starting from the left, one from the right.
2. Move each pointer until it finds a vowel.
3. When both pointers are at vowels, swap them.
4. Move the pointers toward each other and repeat until they meet.

### Steps

Let's walk through an example: s = "IceCreAm"

1. Vowels in s: ['I', 'e', 'e', 'A']
2. Start with pointers at the beginning and end.
3. Swap 'I' (start) with 'A' (end): "AceCreIm"
4. Move pointers inward, swap 'e' with 'e' (no visible change)
5. Continue until pointers meet
6. Result: "AceCreIm"

> **Note:**
> - Using two pointers is efficient and avoids unnecessary work, especially for long strings.
> - You only need to check for vowels and swap them; all other characters remain unchanged.

- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(n)

### Solution

```python
def reverseVowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)
```

## 1732. Find the Highest Altitude [Easy]
https://leetcode.com/problems/find-the-highest-altitude/

### Explanation

## 1732. Find the Highest Altitude [Easy]

https://leetcode.com/problems/find-the-highest-altitude

## Description
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

**Examples**
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

**Constraints**
- n == gain.length
- 1 <= n <= 100
- -100 <= gain[i] <= 100

## Hint
Track the running sum and keep the maximum seen so far.

## Explanation
Let's imagine you're on a bike ride, and you start at sea level (altitude 0). Each number in the gain array tells you how much you go up or down at each step. We keep track of our current altitude as we go, and always remember the highest point we've reached so far.

We do this because it lets us find the maximum altitude in a single pass, without having to store all the altitudes. By updating the highest altitude as we go, we make our solution efficient and easy to understand.

### Solution

```python
def largestAltitude(gain):
    altitude = 0
    max_altitude = 0
    for g in gain:
        altitude += g
        max_altitude = max(max_altitude, altitude)
    return max_altitude
```

## 605. Can Place Flowers [Easy]
https://leetcode.com/problems/can-place-flowers/

### Explanation

## 605. Can Place Flowers [Easy]

https://leetcode.com/problems/can-place-flowers

## Description
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and `false` otherwise.

**Examples**
```text
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

**Constraints**
```text
1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
```

## Explanation

### Strategy
- **Type:** Array, Greedy
- **Given:** An array `flowerbed` of 0s and 1s, and an integer `n`
- **Asked:** Can you plant `n` new flowers in the flowerbed without any two flowers being adjacent?

#### What does "adjacent" mean?
- No two flowers (1s) can be next to each other. You can only plant at a 0 if both neighbors (or edges) are 0.

Let's imagine the flowerbed as a row of garden plots. You want to plant new flowers, but you can't put them right next to each other. So, for each empty spot, you check the spots to the left and right. If both are empty (or if you're at the edge), you can plant a flower there.

You do this because it's the only way to guarantee you never break the "no neighbors" rule. By checking each spot, you make sure you don't miss any possible planting locations.

You keep a count of how many flowers you've planted. If you reach the required number, you can stop early and return True. This helps us avoid unnecessary work and makes our solution efficient.

> Check each empty plot and see if both neighbors are empty (or out of bounds).

#### High-Level Plan
1. For each plot in the flowerbed, check if it is empty (0) and both neighbors are empty (or out of bounds).
2. If so, plant a flower there (set to 1) and decrease `n`.
3. If at any point `n` reaches 0, return True.
4. If you finish the loop and haven't planted enough, return False.

### Steps

Let's walk through an example: flowerbed = [1,0,0,0,1], n = 1

1. Start at index 0: already planted (1), skip.
2. Index 1: empty, but left is 1, can't plant.
3. Index 2: empty, left is 0, right is 0, can plant. Plant and set to 1, n becomes 0.
4. Since n == 0, return True.

> **Note:**
> - Always check both neighbors (or treat out-of-bounds as 0).
> - Stop early if n == 0 for efficiency.

- **Time Complexity:** O(m), where m is the length of flowerbed
- **Space Complexity:** O(1)

### Solution

```python
def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i-1] == 0)
            empty_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
```

## 1071. Greatest Common Divisor of Strings [Easy]
https://leetcode.com/problems/greatest-common-divisor-of-strings/

### Explanation

## 1071. Greatest Common Divisor of Strings [Easy]

https://leetcode.com/problems/greatest-common-divisor-of-strings

## Description
For two strings `s` and `t`, we say "t divides s" if and only if `s = t + t + ... + t` (i.e., t is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

**Examples**
```text
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

**Constraints**
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

> Try to find the greatest common divisor (GCD) of the lengths of the two strings, and check if the substring of that length divides both strings.

## Explanation

### Strategy
Let's restate the problem: Given two strings, find the largest string that can be repeated to form both strings exactly. This is a string manipulation problem with a mathematical twist (using the greatest common divisor, or GCD).

- **What is given?** Two strings, `str1` and `str2`.
- **What is being asked?** Find the largest string x such that both str1 and str2 are made by repeating x some number of times.
- **Constraints:** Both strings are non-empty, up to 1000 characters, and only contain uppercase English letters.
- **Edge cases:** If the strings cannot be built from the same repeating substring, the answer is an empty string.

Suppose you have two strings, and you want to find the biggest chunk that can be repeated to make both strings. Think of it like finding the biggest building block that fits perfectly into **both**.

First, you check if both strings can be built by repeating the same substring, because if they can't, there's no **common divisor** string. You do this by comparing `str1 + str2` and `str2 + str1` — if they're not the same, it means the order of repetition doesn't match, so no common divisor exists. This check is important because it quickly rules out impossible cases, saving you time and effort.

Next, you use the greatest common divisor (GCD) of the lengths of the two strings. You do this because the largest possible repeating substring must fit evenly into both strings, and the GCD gives you the largest length that divides both. This is a mathematical shortcut that ensures you only check the most promising candidate.

Finally, you take the substring of that length from the start of either string and check if repeating it forms both strings. This works because if a substring can build both strings by repetition, it must be the answer. 

**High-level plan:**
1. If `str1 + str2 != str2 + str1`, there is no common divisor string. Return "".
2. Otherwise, the answer is the substring of length gcd(len(str1), len(str2)) from the start of either string.

> Try to find the greatest common divisor (GCD) of the lengths of the two strings, and check if the substring of that length divides both strings.

### Steps
1. **Check for a valid repeating pattern:**
   - Concatenate `str1 + str2` and `str2 + str1`. If they are not equal, it means the two strings cannot be built from the same repeating substring. For example:
     - `str1 = "ABCABC", str2 = "ABC"` → `"ABCABCABC" == "ABCABCABC"` (valid)
     - `str1 = "LEET", str2 = "CODE"` → `"LEETCODE" != "CODELEET"` (invalid)

2. **Find the GCD of the lengths:**
   - If the pattern is valid, compute the greatest common divisor (GCD) of the lengths of str1 and str2. This gives the largest possible length for the repeating substring.
   - Example: `str1 = "ABABAB"` (length 6), `str2 = "ABAB"` (length 4). GCD(6, 4) = 2.

3. **Extract the substring:**
   - Take the substring of length GCD from the start of either string. This is the candidate for the greatest common divisor string.
   - Example: `str1 = "ABABAB", str2 = "ABAB"`. GCD = 2, so substring = "AB".

4. **Return the result:**
   - If the above checks pass, return the substring. Otherwise, return an empty string.

> The key insight is that if two strings are made by repeating the same substring, their concatenations in both orders must be equal. This is a quick way to check for a common divisor string.

### Solution

```python
def gcdOfStrings(str1, str2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if str1 + str2 != str2 + str1:
        return ""
    length = gcd(len(str1), len(str2))
    return str1[:length]
```

## 1768. Merge Strings Alternately [Easy]
https://leetcode.com/problems/merge-strings-alternately/

### Explanation

## 1768. Merge Strings Alternately [Easy]

https://leetcode.com/problems/merge-strings-alternately

## Description
You are given two strings, word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

**Examples**
```text
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a    b 
word2:     p    q   r   s
merged: a p b q  r   s

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

**Constraints**
```text
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
```

> In most cases, LeetCode Easy problems have a straightforward solution that can be derived from the description or the examples provided.

## Explanation
Imagine you have two strings, like two lines of colored beads. You want to make a new necklace by picking one bead from the first string, then one from the second, and keep going! If one string runs out, just add the rest from the other.

We use two pointers to keep track of our position in each string, because this lets us alternate letters easily and ensures we don't miss any. By appending the remaining part of the longer string at the end, we make sure no letters are left out—this is important for correctness, especially when the strings are different lengths.

**Example:**

word1 = "ab", word2 = "pqrs"  
- Take 'a' and 'p' → "ap"
- Take 'b' and 'q' → "apbq"
- word1 is done, so add the rest of word2: "rs"
- Final answer: "apbqrs"

We use a list to collect the letters because lists in Python are efficient for appending, and then join them at the end for the final string.

### Solution

```python
def mergeAlternately(word1, word2):
    res = []
    i = 0
    while i < len(word1) and i < len(word2):
        res.append(word1[i])
        res.append(word2[i])
        i += 1
    res.append(word1[i:])
    res.append(word2[i:])
    return "".join(res)
```

## 643. Maximum Average Subarray I [Easy]
https://leetcode.com/problems/maximum-average-subarray-i/

### Explanation

## 643. Maximum Average Subarray I [Easy]

https://leetcode.com/problems/maximum-average-subarray-i

## Description
Given an array consisting of n integers, find the contiguous subarray of length k that has the maximum average value. Return this value.

**Examples**
```text
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Input: nums = [5], k = 1
Output: 5.0
```

**Constraints**
```text
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4
```

## Hint
Use a sliding window to keep track of the sum of `k` elements.

## Explanation
Let's imagine the array as a long row of numbers. We want to find a group of `k` numbers in a row that, when averaged, gives us the biggest value. Instead of checking every possible group from scratch, we use a sliding window: we add the next number and remove the first number from the previous group.

We do this because it saves us from recalculating the sum for every window, making our solution much faster, especially for large arrays. By updating the sum as we slide the window, we always know the current total for the `k` numbers we're looking at.

This approach is efficient and perfect for problems where you need to look at all subarrays of a fixed size.

### Solution

```python
def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
```

## 1004. Max Consecutive Ones III [Medium]
https://leetcode.com/problems/max-consecutive-ones-iii/

### Explanation

## 1004. Max Consecutive Ones III [Medium]

https://leetcode.com/problems/max-consecutive-ones-iii

## Description
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

**Examples**
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1] -> flip two zeros

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

**Constraints**
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

## Hint
Use a sliding window to keep track of the number of zeros in the current window.

## Explanation
Let's imagine the array as a row of light switches, where 1 is on and 0 is off. We want to find the longest stretch of lights that can be on, if we're allowed to flip up to k switches from off to on.

We use a sliding window to keep track of the current stretch. Every time we add a new number, we check if we've flipped more than k zeros. If so, we move the left end of the window forward until we're back within our limit.

We do this because it lets us efficiently find the longest possible stretch without checking every possible subarray. By only moving the window when needed, we keep our solution fast and memory-efficient.

### Solution

```python
def longestOnes(nums, k):
    left = 0
    zeros = 0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
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

## 1657. Determine if Two Strings Are Close [Medium]
https://leetcode.com/problems/determine-if-two-strings-are-close/

### Explanation

## 1657. Determine if Two Strings Are Close [Medium]

https://leetcode.com/problems/determine-if-two-strings-are-close

## Description
Two strings are considered close if you can attain one from the other using the following operations:
- Operation 1: Swap any two existing characters (i.e., freely reorder the string).
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character (i.e., swap all a's with b's, and all b's with a's).
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

**Examples**
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

**Constraints**
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 contain only lowercase English letters.

## Hint
Operation 1 allows you to freely reorder the string. Operation 2 allows you to freely reassign the letters' frequencies.

## Explanation
To determine if two strings are close, you need to check two things:
1. Both strings must have the same set of unique characters. If one string has a character the other doesn't, you can't transform one into the other.
2. The frequency of each character (regardless of which character) must be the same in both strings. This is because you can swap the frequencies between characters using Operation 2, but you can't create or destroy frequencies.

This means you can sort the frequency counts of each string and compare them. If both the set of unique characters and the sorted frequency counts match, the strings are close.

### Solution

```python
def closeStrings(word1, word2):
    if set(word1) != set(word2):
        return False
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
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
