Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

**Example 1:**
```text
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

**Example 2:**
```text
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```text
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:**
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Explanation

### Strategy

This is a **hash table problem** that requires grouping strings that are anagrams of each other. The key insight is to use a sorted version of each string as a key to group anagrams together.

**Key observations:**
- Anagrams have the same characters in different orders
- Sorting the characters gives us a unique key for each group of anagrams
- We can use a hash map to group strings by their sorted character representation
- All anagrams will have the same sorted key

**High-level approach:**
1. **Create a hash map**: Use sorted string as key, list of anagrams as value
2. **Process each string**: Sort the characters and use as key
3. **Group anagrams**: Add each string to the appropriate group
4. **Return result**: Return all groups as a list of lists

### Steps

Let's break down the solution step by step:

**Step 1: Initialize hash map**
- Create a dictionary to store groups: `groups = {}`

**Step 2: Process each string**
For each string in the input array:
- Sort the characters: `sorted_str = ''.join(sorted(s))`
- Use sorted string as key in hash map
- Add original string to the group

**Step 3: Return grouped anagrams**
- Return all values from the hash map as a list

**Example walkthrough:**
Let's trace through the first example:

```text
strs = ["eat","tea","tan","ate","nat","bat"]

Step 1: Process "eat"
sorted_str = "aet"
groups = {"aet": ["eat"]}

Step 2: Process "tea"
sorted_str = "aet"
groups = {"aet": ["eat", "tea"]}

Step 3: Process "tan"
sorted_str = "ant"
groups = {"aet": ["eat", "tea"], "ant": ["tan"]}

Step 4: Process "ate"
sorted_str = "aet"
groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}

Step 5: Process "nat"
sorted_str = "ant"
groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}

Step 6: Process "bat"
sorted_str = "abt"
groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}

Result: Return [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

> **Note:** The key insight is that anagrams have the same characters, so sorting them gives us a unique identifier. This approach is efficient because we only need to sort each string once, and hash map operations are O(1) on average.

**Time Complexity:** O(n * k log k) where n is the number of strings and k is the maximum length of any string  
**Space Complexity:** O(n * k) to store all strings in the hash map 