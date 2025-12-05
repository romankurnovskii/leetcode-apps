class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        res = 0
        
        # Try all possible substrings
        for i in range(n):
            vowel_count = 0
            consonant_count = 0
            
            for j in range(i, n):
                if s[j] in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
                
                # Check if beautiful
                if vowel_count == consonant_count and (vowel_count * consonant_count) % k == 0:
                    res += 1
        
        return res
