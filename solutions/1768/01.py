class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        j = 0
        
        # Alternate between word1 and word2
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        # Append remaining characters from longer word
        res.extend(word1[i:])
        res.extend(word2[j:])
        
        return ''.join(res)
