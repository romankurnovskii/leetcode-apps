# Random



## 1. Two Sum [Easy]
https://leetcode.com/problems/two-sum/

### Explanation

## Two Sum [Easy]

https://leetcode.com/problems/two-sum/

## Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
```

Constraints:
```
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
```

---

## Explanation

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

## 2. Add Two Numbers [Medium]
https://leetcode.com/problems/add-two-numbers/

### Explanation

## Add Two Numbers [Medium]

https://leetcode.com/problems/add-two-numbers/

## Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

Constraints:
```
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```

---

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

## 11. Container With Most Water [Medium]
https://leetcode.com/problems/container-with-most-water/

### Explanation

## 11. Container With Most Water [Medium]

https://leetcode.com/problems/container-with-most-water/

## Description
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

Example 2:
```
Input: height = [1,1]
Output: 1

Constraints:
```
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
```

> **Hint:**  Use two pointers, one at each end, and move the pointer with the shorter line inward.

### Explanation

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

## 151. Reverse Words in a String [Medium]
https://leetcode.com/problems/reverse-words-in-a-string

### Explanation

## 151. Reverse Words in a String [Medium]

https://leetcode.com/problems/reverse-words-in-a-string

## Description
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Examples**
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

**Constraints**
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

## Hint
Split the string into words, reverse the list, and join them back.

## Explanation
Let's think of the sentence as a row of blocks, each block being a word. To reverse the sentence, we break it into blocks, flip the order, and stick them back together.

We do this because splitting and reversing is much easier than trying to move words around in the original string. Python's split and join functions make this super efficient, and by removing extra spaces, we make sure the result is clean and matches the requirements.

This approach is both simple and effective, making it a great example of using built-in tools to solve a problem quickly.

### Solution

```python
def reverseWords(s):
    words = s.strip().split()
    return " ".join(reversed(words))
```

## 238. Product of Array Except Self [Medium]
https://leetcode.com/problems/product-of-array-except-self

### Explanation

## 238. Product of Array Except Self [Medium]

https://leetcode.com/problems/product-of-array-except-self

## Description
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Examples**
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

**Constraints**

```
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
```

## Hint
Use two passes: one to calculate products to the left of each index, and one for the right.

## Explanation
We want to find the product of all numbers except the one at each position. If we used division, we could just multiply everything and divide by nums[i], but the problem says no division!

So, we use two passes. First, we go from left to right, building up the product of all numbers to the left of each index. We do this because it lets us know, for each position, what the product is before that number.

Then, we go from right to left, multiplying each answer by the product of all numbers to the right. This way, each answer[i] ends up being the product of everything except nums[i].

This approach is efficient because it only needs two passes and uses O(1) extra space (not counting the output array), making it perfect for large arrays.

### Solution

```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer
```

## 283. Move Zeroes [Easy]
https://leetcode.com/problems/move-zeroes/

### Explanation

## 283. Move Zeroes [Easy]

https://leetcode.com/problems/move-zeroes

## Description
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

**Examples**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]

**Constraints**
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

## Hint
Use two pointers: one to keep track of the current position to place a non-zero, and one to iterate through the array.

## Explanation
We use two pointers: one iterates through the array, and the other keeps track of where to place the next non-zero element. As we iterate, whenever we find a non-zero, we place it at the position of the first pointer and increment it. After all non-zeros are placed, we fill the rest of the array with zeros.

This approach ensures all non-zero elements retain their original order, and all zeros are moved to the end efficiently in a single pass.

### Solution

```python
def moveZeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
```

## 334. Increasing Triplet Subsequence [Medium]
https://leetcode.com/problems/increasing-triplet-subsequence

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

## 345. Reverse Vowels of a String [Easy]
https://leetcode.com/problems/reverse-vowels-of-a-string

### Explanation

## 345. Reverse Vowels of a String [Easy]

https://leetcode.com/problems/reverse-vowels-of-a-string

## Description
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

**Examples**
Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"

**Constraints**
- 1 <= s.length <= 3 * 10^5
- s consist of printable ASCII characters.

## Hint
Use two pointers to find vowels from both ends and swap them.

## Explanation
We want to reverse only the vowels in the string. To do this efficiently, we use two pointers: one starting from the left, one from the right. We move each pointer until it finds a vowel. When both pointers are at vowels, we swap them.

We do this because it lets us reverse the vowels in-place, without affecting the other characters. Using two pointers is efficient and avoids unnecessary work, especially for long strings.

We keep moving the pointers toward each other, swapping vowels as we go, until they meet in the middle. This ensures every vowel is swapped exactly once, making the solution both correct and efficient.

### Solution

```python
def reverseVowels(s):
    vowels = set("aeiouAEIOU")
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
    return "".join(s)
```

## 392. Is Subsequence [Easy]
https://leetcode.com/problems/is-subsequence/

### Explanation

## 392. Is Subsequence [Easy]

https://leetcode.com/problems/is-subsequence

## Description
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

**Examples**
Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false

**Constraints**
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.

## Hint
Use two pointers to check if you can match all characters of s in t in order.

## Explanation
Let's imagine s as a list of items you want to find, and t as a long conveyor belt of items. You want to see if you can pick up all the items from s, in order, as they appear on the conveyor belt t. You use two pointers: one for s and one for t. Every time you see a match, you move the pointer for s forward. If you reach the end of s, it means you found all the items in order!

This approach is efficient because you only need to go through t once, and you never go back. It's perfect for checking subsequences quickly.

### Solution

```python
def isSubsequence(s, t):
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    return i == len(s)
```

## 443. String Compression [Medium]
https://leetcode.com/problems/string-compression

### Explanation

## 443. String Compression [Medium]

https://leetcode.com/problems/string-compression

## Description
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

**Examples**
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

**Constraints**
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

## Hint
Use two pointers: one for reading, one for writing.

## Explanation
We want to compress the string by replacing sequences of the same character with that character followed by the count. We use two pointers: one to read through the array, and one to write the compressed result.

We do this because it lets us modify the array in-place, which saves memory and meets the problem's requirements. By counting consecutive characters and writing the count only when needed, we keep the result as short as possible.

This approach is efficient and avoids creating extra arrays, making it suitable for large inputs.

### Solution

```python
def compress(chars):
    write = 0
    read = 0
    n = len(chars)
    while read < n:
        char = chars[read]
        count = 0
        while read < n and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1
        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1
    return write
```

## 605. Can Place Flowers [Easy]
https://leetcode.com/problems/can-place-flowers

### Explanation

## 605. Can Place Flowers [Easy]

https://leetcode.com/problems/can-place-flowers

## Description
You have a long flowerbed in which some plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

**Examples**
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

**Constraints**
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in the flowerbed.
- 0 <= n <= flowerbed.length

## Hint
Check each empty plot and see if both neighbors are empty (or out of bounds).

## Explanation
Let's imagine the flowerbed as a row of garden plots. We want to plant new flowers, but we can't put them right next to each other. So, for each empty spot, we check the spots to the left and right. If both are empty (or if we're at the edge), we can plant a flower there.

We do this because it's the only way to guarantee we never break the "no neighbors" rule. By checking each spot, we make sure we don't miss any possible planting locations.

We keep a count of how many flowers we've planted. If we reach the required number, we can stop early and return True. This helps us avoid unnecessary work and makes our solution efficient.

### Solution

```python
def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
```

## 643. Maximum Average Subarray I [Easy]
https://leetcode.com/problems/maximum-average-subarray-i

### Explanation

## 643. Maximum Average Subarray I [Easy]

https://leetcode.com/problems/maximum-average-subarray-i

## Description
Given an array consisting of n integers, find the contiguous subarray of length k that has the maximum average value. Return this value.

**Examples**
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Input: nums = [5], k = 1
Output: 5.0

**Constraints**
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

## Hint
Use a sliding window to keep track of the sum of k elements.

## Explanation
Let's imagine the array as a long row of numbers. We want to find a group of k numbers in a row that, when averaged, gives us the biggest value. Instead of checking every possible group from scratch, we use a sliding window: we add the next number and remove the first number from the previous group.

We do this because it saves us from recalculating the sum for every window, making our solution much faster, especially for large arrays. By updating the sum as we slide the window, we always know the current total for the k numbers we're looking at.

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

## 1071. Greatest Common Divisor of Strings [Easy]
https://leetcode.com/problems/greatest-common-divisor-of-strings

### Explanation

## 1071. Greatest Common Divisor of Strings [Easy]

https://leetcode.com/problems/greatest-common-divisor-of-strings

## Description
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

**Examples**
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Input: str1 = "LEET", str2 = "CODE"
Output: ""

**Constraints**
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

## Hint
Try to find the greatest common divisor (GCD) of the lengths of the two strings, and check if the substring of that length divides both strings.

## Explanation
Suppose you have two strings, and you want to find the biggest chunk that can be repeated to make both strings. Think of it like finding the biggest building block that fits perfectly into both.

First, we check if both strings can be built by repeating the same substring, because if they can't, there's no common divisor string. We do this by comparing str1 + str2 and str2 + str1—if they're not the same, it means the order of repetition doesn't match, so no common divisor exists. This check is important because it quickly rules out impossible cases, saving us time and effort.

Next, we use the greatest common divisor (GCD) of the lengths of the two strings. We do this because the largest possible repeating substring must fit evenly into both strings, and the GCD gives us the largest length that divides both. This is a mathematical shortcut that ensures we only check the most promising candidate.

Finally, we take the substring of that length from the start of either string and check if repeating it forms both strings. This works because if a substring can build both strings by repetition, it must be the answer.

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

## 1207. Unique Number of Occurrences [Easy]
https://leetcode.com/problems/unique-number-of-occurrences/

### Explanation

## 1207. Unique Number of Occurrences [Easy]

https://leetcode.com/problems/unique-number-of-occurrences

## Description
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

**Examples**
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

**Constraints**
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

## Hint
Use a dictionary to count occurrences, then check if the counts are unique using a set.

## Explanation
We want to know if every number in the array appears a unique number of times. First, we count how many times each number appears using a dictionary. Then, we check if all those counts are different by putting them in a set.

We do this because using a dictionary makes counting fast and easy, and a set lets us quickly check for duplicates among the counts. This approach is efficient and avoids unnecessary loops.

### Solution

```python
def uniqueOccurrences(arr):
    from collections import Counter

    count = Counter(arr)
    return len(set(count.values())) == len(count)
```

## 1431. Kids With the Greatest Number of Candies [Easy]
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

### Explanation

## 1431. Kids With the Greatest Number of Candies [Easy]

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

## Description
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

**Examples**
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

**Constraints**
```
- n == candies.length
- 2 <= n <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
```

## Hint
For each kid, check if their candies plus extraCandies is at least as much as the current maximum.

## Explanation
First, we want to know the highest number of candies any kid currently has. This is important because we need a reference point to see if giving extra candies to a kid will make them "the greatest."

For each kid, we add the extraCandies to their current amount. We do this because we want to see if, after the bonus, they can reach or beat the current maximum. If they do, we mark them as True in our answer list; otherwise, False.

This approach is efficient because we only need to find the maximum once, and then just compare each kid's total to it. This saves us from recalculating the maximum for every kid, making our solution faster and cleaner.

### Solution

```python
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Find the current maximum
    return [(c + extraCandies) >= max_candies for c in candies]
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

## 1679. Max Number of K-Sum Pairs [Medium]
https://leetcode.com/problems/max-number-of-k-sum-pairs/

### Explanation

## 1679. Max Number of K-Sum Pairs [Medium]

https://leetcode.com/problems/max-number-of-k-sum-pairs

## Description
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

**Examples**
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

**Constraints**
```
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
```

## Hint
Use a hash map to count occurrences and find pairs efficiently.

## Explanation
Imagine you have a bag of numbers and you want to make as many pairs as possible that add up to k. For each number, check if you have seen its complement (k - number) before. If so, you can make a pair! Use a hash map to keep track of the numbers you have seen and how many are left.

This approach is efficient because it lets you find pairs in a single pass through the array.

### Solution

```python
def function_name(...):
    pass
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

## 1768. Merge Strings Alternately [Easy]
https://leetcode.com/problems/merge-strings-alternately

### Explanation

## 1768. Merge Strings Alternately [Easy]

https://leetcode.com/problems/merge-strings-alternately

## Description
You are given two strings, word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

**Examples**
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

**Constraints**
```text
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
```

## Hint
In most cases, LeetCode Easy problems have a straightforward solution that can be derived from the description or the examples provided.

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

## 1798. Maximum Number of Consecutive Values You Can Make [Medium]
https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make

### Explanation

## 1798. Maximum Number of Consecutive Values You Can Make [Medium]

https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make

## Description

You are given an integer array `coins` of length `n` which represents the `n` coins that you own. The value of the `i`th coin is `coins[i]`. You can **make** some value `x` if you can choose some of your `n` coins such that their values sum up to `x`.

Return the *maximum number of consecutive integer values that you **can** **make** with your coins **starting** from and **including** 0*.

Note that you may have multiple coins of the same value.

**Examples**

**Example 1:**

    Input: coins = [1,3]
    Output: 2
    Explanation: You can make the following values:
    - 0: take []
    - 1: take [1]
    You can make 2 consecutive integer values starting from 0.

**Example 2:**

    Input: coins = [1,1,1,4]
    Output: 8
    Explanation: You can make the following values:
    - 0: take []
    - 1: take [1]
    - 2: take [1,1]
    - 3: take [1,1,1]
    - 4: take [4]
    - 5: take [4,1]
    - 6: take [4,1,1]
    - 7: take [4,1,1,1]
    You can make 8 consecutive integer values starting from 0.

**Example 3:**

    Input: coins = [1,4,10,3,1]
    Output: 20

**Constraints**

```
coins.length == n
1 <= n <= 4 * 10^4
1 <= coins[i] <= 4 * 10^4
```

## Explanation

### Strategy

Let's restate the problem:
- You have a set of coins, each with a positive integer value.
- You can use any subset of these coins (including none) to make sums.
- What is the largest number of *consecutive* values (starting from 0) you can make?

Consecutive is 0, 1, 2, ... So when you have coins `[1,2,3]`:

    - sum of them is 6
    - consecutive sequence will be up to `6` starting from `0`: `0, 1, 2, 3, 4, 5, 6` 

**Type:** Array, Greedy, Sorting

**What is given:**
- An array of positive integers (the coin values).

**What is asked:**
- The maximum number of consecutive values (starting from 0) you can make by summing up any subset of the coins.

**Constraints/Edge Cases:**
- Coins can have repeated values.
- The array can be large (up to 40,000 elements).
- All coin values are at least 1.

**High-level plan:**
- Sort the coins in ascending order.
- Track the smallest value you *cannot* make yet (let's call it `res`, start at 1).
- For each coin:
    - If the coin is greater than `res`, you can't make `res` (or anything larger), so stop.
    - Otherwise, you can now make all values up to `res + coin - 1`, so update `res += coin`.
- Return `res`.

### Steps

Let's walk through an example: `coins = [1, 1, 1, 4]`

1. **Sort the coins:** `[1, 1, 1, 4]`
2. **Initialize `res = 1`** (the smallest value we can't make yet)
3. **First coin (1):**
    - 1 <= (sequence value 1), so we can make 1. Now we can make all values up to 1 + 1 - 1 = 1.
    - Update `res = 2`.
4. **Second coin (1):**
    - 1 <= (sequence value 2), so we can make 2. Now we can make up to 2 + 1 - 1 = 2.
    - Update `res = 3`.
5. **Third coin (1):**
    - 1 <= (sequence value 3), so we can make 3. Now we can make up to 3 + 1 - 1 = 3.
    - Update `res = 4`.
6. **Fourth coin (4):**
    - 4 <= (sequence value 4), so we can make 4. Now we can make up to 4 + 4 - 1 = 7.
    - Update `res = 8`.
7. **No more coins.**

So, we can make all values from 0 to 7 (8 values).

**Another example:** `coins = [1, 3]`
- Sort: [1, 3]
- res = 1
- First coin: 1 <= 1 → res = 2
- Second coin: 3 > 2 → stop
- Answer: 2

**Key insight:**
> If you ever encounter a coin that is greater than the smallest value you can't make yet, you can't fill the gap, so you must stop.

### Solution

```python
def getMaximumConsecutive(coins):
    res = 1
    for coin in sorted(coins):
        if coin > res:
            break
        res += coin
    return res
```

## 2215. Find the Difference of Two Arrays [Easy]
https://leetcode.com/problems/find-the-difference-of-two-arrays/

### Explanation

## 2215. Find the Difference of Two Arrays [Easy]

https://leetcode.com/problems/find-the-difference-of-two-arrays

## Description
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

**Examples**
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]

**Constraints**
- 1 <= nums1.length, nums2.length <= 1000
- -1000 <= nums1[i], nums2[i] <= 1000

## Hint
Use sets to efficiently find unique elements in each array.

## Explanation
Let's imagine you have two boxes of colored marbles (numbers). You want to find out which colors are only in the first box and which are only in the second. We use sets to quickly check for unique marbles in each box.

We do this because sets make it easy and fast to find differences—checking if something is in a set is much quicker than searching through a list. By converting the lists to sets, we can use set operations to get the answer efficiently.

### Solution

```python
def findDifference(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    return [list(set1 - set2), list(set2 - set1)]
```

## 2352. Equal Row and Column Pairs [Medium]
https://leetcode.com/problems/equal-row-and-column-pairs/

### Explanation

## 2352. Equal Row and Column Pairs [Medium]

https://leetcode.com/problems/equal-row-and-column-pairs

## Description
Given a 0-indexed n x n integer matrix grid, return the number of pairs (r_i, c_j) such that row r_i and column c_j are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

**Examples**
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

**Constraints**
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5

## Hint
We can use nested loops to compare every row against every column. Another loop is necessary to compare the row and column element by element. It is also possible to hash the arrays and compare the hashed values instead.

## Explanation
To count equal row and column pairs, we can compare each row with each column. For each row, we check if it matches any column by comparing their elements one by one. To make this efficient, we can use tuples or hashable representations of rows and columns and count their occurrences. If a row matches a column, we increment our answer.

This approach is efficient for n up to 200, and using hash maps or tuples makes the comparison fast and easy to implement.

### Solution

```python
def equalPairs(grid):
    n = len(grid)
    row_counts = Counter(tuple(row) for row in grid)
    col_counts = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
    return sum(row_counts[row] * col_counts[row] for row in row_counts)
```

## 2862. Maximum Element-Sum of a Complete Subset of Indices [Hard]
https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices

### Explanation

## 2862. Maximum Element-Sum of a Complete Subset of Indices (Hard)

https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices

## Description

You are given a **1-indexed** array `nums`. Your task is to select a **complete subset** from `nums` where every pair of selected indices multiplied is a perfect square, i.e., if you select `a_i` and `a_j`, `i * j` must be a perfect square.

Return the *sum* of the complete subset with the *maximum sum*.

**Examples**

**Example 1:**

    Input: nums = [8,7,3,5,7,2,4,9]
    Output: 16
    Explanation: We select elements at indices 2 and 8 and 2 * 8 is a perfect square.

**Example 2:**

    Input: nums = [8,10,3,8,1,13,7,9,4]
    Output: 20
    Explanation: We select elements at indices 1, 4, and 9. 1 * 4, 1 * 9, 4 * 9 are perfect squares.

**Constraints**

```text
1 <= n == nums.length <= 10^4
1 <= nums[i] <= 10^9
```

## Explanation

### Strategy

Let's restate the problem:
- You have a 1-indexed array `nums`.
- You want to select a subset of indices such that for every pair `(i, j)` in the subset, `i * j` is a perfect square.
- What is the maximum possible sum of the elements at those indices?

**Type:** Array, Math, Number Theory

**What is given:**
- An array of positive integers (the values).

**What is asked:**
- The maximum sum of a complete subset (as defined above).

**Constraints/Edge Cases:**
- Array can be large (up to 10,000 elements).
- All values are positive integers.

**High-level plan:**
- For each index, compute its "key" (the product of primes with odd exponents in its factorization).
- Group indices by key, sum the corresponding values, and return the maximum sum.
- Alternatively, for each possible starting index, consider the sequence `i * m^2` and sum the values.

### Steps

Let's walk through an example: `nums = [8, 7, 3, 5, 7, 2, 4, 9]`

1. For each index, compute its key:
    - Index 1: key = 1
    - Index 2: key = 2
    - Index 3: key = 3
    - Index 4: key = 1 (since 4 = 2^2)
    - ...
2. Group indices by key and sum the corresponding values:
    - key 1: indices 1, 4, ...
    - key 2: indices 2, ...
    - ...
3. The answer is the maximum sum among all groups.

> Indices with the same key can be grouped together, and their products will always be perfect squares.

### Solution

```python
def maximumSum(nums):
    count = Counter()
    for i in range(len(nums)):
        x, v = i + 1, 2
        while x >= v * v:
            while x % (v * v) == 0:
                x //= v * v
            v += 1
        count[x] += nums[i]
    return max(count.values())
```

## 3607. Power Grid Maintenance [Medium]
https://leetcode.com/problems/power-grid-maintenance

### Explanation

## 3607. Power Grid Maintenance [Medium]

https://leetcode.com/problems/power-grid-maintenance

## Description

You are given an integer `c` representing `c` power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing).

These stations are interconnected via `n` **bidirectional** cables, represented by a 2D array `connections`, where each element `connections[i] = [u_i, v_i]` indicates a connection between station `u_i` and station `v_i`. Stations that are directly or indirectly connected form a **power grid**.

Initially, **all** stations are online (operational).

You are also given a 2D array `queries`, where each query is one of the following two types:

- `[1, x]`: A maintenance check is requested for station `x`. If station `x` is online, it resolves the check by itself. If station `x` is offline, the check is resolved by the operational station with the smallest `id` in the same **power grid** as `x`. If **no** operational station exists in that grid, return -1.
- `[2, x]`: Station `x` goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type `[1, x]` in the **order** they appear.

**Note:** The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

**Examples**

**Example 1:**

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:
- Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
- Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
- Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
- Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
- Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
- Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.

**Example 2:**

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:
- There are no connections, so each station is its own isolated grid.
- Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
- Query [2,1]: Station 1 goes offline.
- Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.

**Constraints**
```text
1 <= c <= 10^5
0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)
connections[i].length == 2
1 <= u_i, v_i <= c
u_i != v_i
1 <= queries.length <= 2 * 10^5
queries[i].length == 2
queries[i][0] is either 1 or 2.
1 <= queries[i][1] <= c
```

## Explanation

### Strategy

Let's restate the problem:
- We have a set of power stations connected by cables, forming one or more power grids (connected components).
- Each station can go offline, but the grid structure does not change.
- For a maintenance check, if the station is online, it handles the check; if offline, the smallest online station in the same grid handles it (or -1 if none).

**Type:** Graph, Union Find, Heap, DFS, Ordered Set

**What is being asked?**
- Efficiently answer queries about which station can handle a maintenance check, considering online/offline status and grid structure.

**What is given?**
- Number of stations, connections, and a list of queries.

**Constraints/Edge Cases:**
- Up to 10^5 stations and 2*10^5 queries.
- Stations can go offline, but the grid structure is static.

**High-Level Plan:**
- Precompute connected components (power grids) using DFS or Union Find (DSU).
- For each component, maintain a data structure (set, heap, or sorted list) of online stations.
- For type 1 queries, if the station is online, return it; otherwise, return the smallest online station in its component, or -1 if none.
- For type 2 queries, mark the station as offline (remove from set/heap/list or mark in a boolean array).

### Steps

1. **Build the graph and find connected components:**
   - Use DFS or DSU to assign each station a component ID.
2. **For each component, track online stations:**
   - Use a set, heap, or sorted list for fast lookup of the smallest online station.
3. **Process queries:**
   - For `[1, x]`, if `x` is online, return `x`; else, return the smallest online station in the same component, or -1 if none.
   - For `[2, x]`, mark `x` as offline.

**Example Walkthrough:**

Suppose c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

- All stations are online and form a single grid.
- [1,3]: 3 is online → return 3
- [2,1]: 1 goes offline
- [1,1]: 1 is offline, smallest online in grid is 2 → return 2
- [2,2]: 2 goes offline
- [1,2]: 2 is offline, smallest online in grid is 3 → return 3

> **Note:** The grid structure is static; only online/offline status changes.

### Solution

```python
def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px


class Solution:
    def processQueries(self, n, connections, queries):
        dsu = DSU(n)
        online = [True] * (n + 1)
        for u, v in connections:
            dsu.union(u, v)
        component_heap = defaultdict(list)
        for station in range(1, n + 1):
            root = dsu.find(station)
            heapq.heappush(component_heap[root], station)
        result = []
        for typ, x in queries:
            if typ == 2:
                online[x] = False
            else:
                if online[x]:
                    result.append(x)
                else:
                    root = dsu.find(x)
                    heap = component_heap[root]
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    result.append(heap[0] if heap else -1)
        return result
```

## 3608. Minimum Time for K Connected Components [Medium]
https://leetcode.com/problems/minimum-time-for-k-connected-components

### Explanation

## 3608. Minimum Time for K Connected Components [Medium]

https://leetcode.com/problems/minimum-time-for-k-connected-components

## Description
You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [u_i, v_i, time_i] indicates an undirected edge between nodes u_i and v_i that can be removed at time_i.

You are also given an integer k.

Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t, the graph contains at least k connected components.

Return the minimum time t.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

## Examples

**Example 1**
Input:
n = 2
edges = [[0,1,3]]
k = 2

Output:
3

Explanation:
- Initially, there is one connected component {0, 1}.
- At time = 1 or 2, the graph remains unchanged.
- At time = 3, edge [0, 1] is removed, resulting in k = 2 connected components {0}, {1}. Thus, the answer is 3.

**Example 2**
Input:
n = 3
edges = [[0,1,2],[1,2,4]]
k = 3

Output:
4

Explanation:
- Initially, there is one connected component {0, 1, 2}.
- At time = 2, edge [0, 1] is removed, resulting in two connected components {0}, {1, 2}.
- At time = 4, edge [1, 2] is removed, resulting in k = 3 connected components {0}, {1}, {2}. Thus, the answer is 4.

**Example 3**
Input:
n = 3
edges = [[0,2,5]]
k = 2

Output:
0

Explanation:
- Since there are already k = 2 disconnected components {1}, {0, 2}, no edge removal is needed. Thus, the answer is 0.

## Constraints
```
- 1 <= n <= 10^5
- 0 <= edges.length <= 10^5
- edges[i] = [u_i, v_i, time_i]
- 0 <= u_i, v_i < n
- u_i != v_i
- 1 <= time_i <= 10^9
- 1 <= k <= n
- There are no duplicate edges.
```

## Explanation

**Intuition**

We want to find the minimum time t such that, after removing all edges with time <= t, the graph splits into at least k connected components. This is a classic application of binary search combined with union-find (DSU) to efficiently count components after edge removals.

**Approach**

1. **Binary Search:**
   - Sort all unique edge times and use binary search to find the smallest t such that the number of connected components is at least k after removing all edges with time <= t.
2. **Union-Find (DSU):**
   - For each candidate t, use union-find to connect all nodes with edges having time > t, then count the number of connected components.
3. **Edge Cases:**
   - If the initial graph already has at least k components, return 0.

### Solution

```python
def count_components(n, edges_by_time, t):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    for u, v, time in edges_by_time:
        if time > t:
            union(u, v)
    comps = set(find(i) for i in range(n))
    return len(comps)


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if k == n:
            return 0
        if not edges:
            return 0 if k <= n else -1
        edges_by_time = sorted(edges, key=lambda x: x[2])
        lo, hi = 0, max(e[2] for e in edges)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            comps = count_components(n, edges_by_time, mid)
            if comps >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## 3623. Count Number of Trapezoids I [Medium]
https://leetcode.com/problems/count-number-of-trapezoids-i

### Explanation

## 3623. Count Number of Trapezoids I [Medium]

https://leetcode.com/problems/count-number-of-trapezoids-i

## Description
You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `i`-th point on the Cartesian plane.

A **horizontal trapezoid** is a convex quadrilateral with **at least one pair** of horizontal sides (i.e., parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique **horizontal trapezoids** that can be formed by choosing any four distinct points from `points`.

Since the answer may be very large, return it **modulo** 10^9 + 7.

**Examples**

**Example 1:**

Input:
points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:
There are three distinct ways to pick four points that form a horizontal trapezoid:
- Using points [1,0], [2,0], [3,2], and [2,2].
- Using points [2,0], [3,0], [3,2], and [2,2].
- Using points [1,0], [3,0], [3,2], and [2,2].

![Trapezoid 1](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-6.png)
![Trapezoid 2](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-7.png)
![Trapezoid 3](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-8.png)

**Example 2:**

Input:
points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:
There is only one horizontal trapezoid that can be formed.

![Trapezoid Example 2](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png)

**Constraints**

```text
4 <= points.length <= 10^5
-10^8 <= x_i, y_i <= 10^8
All points are pairwise distinct.
```

## Explanation

### Strategy

Let's restate the problem:
- We are given a set of points on a 2D plane.
- We want to count the number of ways to pick 4 distinct points that form a convex quadrilateral with at least one pair of horizontal sides (i.e., two sides parallel to the x-axis).

**Type:** Geometry, Combinatorics, Hash Map

**What is being asked?**
- Count the number of unique horizontal trapezoids (convex quadrilaterals with at least one pair of horizontal sides) that can be formed from the given points.

**What is given?**
- A list of points, all distinct.

**Constraints/Edge Cases:**
- Large input size (up to 10^5 points).
- All points are distinct.

**Why is the naive approach too slow?**
- The naive approach groups points by y-coordinate, then for every pair of y-levels, multiplies the number of ways to pick 2 points from each. This is O(K^2) where K is the number of y-levels with at least 2 points. For large K, this is too slow and leads to TLE.

**Optimized Plan:**
- Instead of iterating over all pairs, use the mathematical identity:
  - The total number of unordered pairs of y-levels is C(K,2).
  - If we precompute the number of ways to pick 2 points from each y-level (call this list `pairs`), then the sum over all pairs is:
    - sum_{i<j} pairs[i] * pairs[j] = (total_sum^2 - sum_of_squares) // 2
  - Where total_sum = sum(pairs), sum_of_squares = sum(x*x for x in pairs).
- This reduces the time complexity to O(N + K), which is efficient for large inputs.

### Steps

1. **Group points by y-coordinate:**
   - Use a hash map to group all points with the same y.
2. **For each group, count the number of ways to pick 2 points:**
   - For a group of size c, the number of ways to pick 2 points is C(c, 2) = c * (c-1) // 2.
   - Only consider groups with at least 2 points.
3. **Sum up all C(c,2) values:**
   - Let `pairs` be the list of C(c,2) for each y-level with at least 2 points.
4. **Compute the total number of trapezoids:**
   - Use the formula: res = (total_sum^2 - sum_of_squares) // 2
   - Return res modulo 10^9 + 7.

> **Note:**
> - We only consider y-levels with at least 2 points.
> - The order of y-levels does not matter (unordered pairs).
> - This approach avoids the O(K^2) double loop and is much faster.

#### Example Walkthrough
Suppose points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
- y=0: [1,0], [2,0], [3,0] (3 points)
- y=2: [2,2], [3,2] (2 points)
- C(3,2) = 3, C(2,2) = 1
- pairs = [3, 1]
- total_sum = 4, sum_of_squares = 9 + 1 = 10
- res = (4*4 - 10) // 2 = (16 - 10) // 2 = 3

### Complexity Analysis
- **Time Complexity:** O(N + K), where N is the number of points and K is the number of y-levels with at least 2 points.
- **Space Complexity:** O(N) for storing the groups.

```text
| Step | Operation         | Count |
| ---- | ----------------- | ----- |
| 1    | Group points by y | N     |
| 2    | Compute C(c,2)    | K     |
| 3    | Math formula      | K     |
```

### Solution

```python
def countTrapezoids(points):
    y_groups = defaultdict(int)
    for x, y in points:
        y_groups[y] += 1
    pairs = []
    for c in y_groups.values():
        if c >= 2:
            pairs.append(c * (c - 1) // 2)
    total_sum = sum(pairs)
    sum_of_squares = sum(x * x for x in pairs)
    res = (total_sum * total_sum - sum_of_squares) // 2
    return res % MOD
```
