from collections import defaultdict, Counter

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        # Count frequency of each character
        freq = Counter(s)
        
        # Group characters by their frequency
        # freq_group[k] = list of characters that appear exactly k times
        freq_group = defaultdict(list)
        for char, count in freq.items():
            freq_group[count].append(char)
        
        # Find the majority frequency group
        # We want the group with:
        # 1. Largest number of distinct characters
        # 2. If tied, higher frequency value
        max_size = 0
        best_freq = 0
        
        for k, chars in freq_group.items():
            size = len(chars)
            # If this group has more characters, or same size but higher frequency
            if size > max_size or (size == max_size and k > best_freq):
                max_size = size
                best_freq = k
        
        # Return all characters in the majority frequency group
        return ''.join(freq_group[best_freq])

