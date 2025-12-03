from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = {}
        
        # Count frequency of each word
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        res = []
        
        # Try each starting position
        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0
            
            # Check if substring matches all words
            while j < len(words):
                start_idx = i + j * word_len
                word = s[start_idx:start_idx + word_len]
                
                # If word not in words or seen too many times
                if word not in word_count:
                    break
                
                seen[word] = seen.get(word, 0) + 1
                
                # If we've seen this word more times than available
                if seen[word] > word_count[word]:
                    break
                
                j += 1
            
            # If we matched all words
            if j == len(words):
                res.append(i)
        
        return res

