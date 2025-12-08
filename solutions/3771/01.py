class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        
        # Prefix sums for damage
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + damage[i]
        
        # For each starting position i, calculate score
        res = 0
        for i in range(n):
            current_hp = hp
            score = 0
            for j in range(i, n):
                current_hp -= damage[j]
                if current_hp >= requirement[j]:
                    score += 1
            res += score
        
        return res
