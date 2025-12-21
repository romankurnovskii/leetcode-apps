from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current, open_count, close_count):
            # Base case: valid combination found
            if len(current) == 2 * n:
                res.append(current)
                return

            # Add opening parenthesis if we haven't used all
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add closing parenthesis if valid (more opens than closes)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
