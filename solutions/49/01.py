from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize hash map to store groups
        groups = {}

        # Process each string
        for s in strs:
            # Sort the characters to create a key
            sorted_str = "".join(sorted(s))

            # Add to the appropriate group
            if sorted_str in groups:
                groups[sorted_str].append(s)
            else:
                groups[sorted_str] = [s]

        # Return all groups
        return list(groups.values())
