class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        
        for asteroid in asteroids:
            while res and asteroid < 0 < res[-1]:
                if res[-1] < -asteroid:
                    res.pop()
                    continue
                elif res[-1] == -asteroid:
                    res.pop()
                break
            else:
                res.append(asteroid)
        
        return res

