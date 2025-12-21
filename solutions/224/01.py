class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "+":
                res += sign * num
                num = 0
                sign = 1
            elif char == "-":
                res += sign * num
                num = 0
                sign = -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ")":
                res += sign * num
                num = 0
                res *= stack.pop()  # pop sign
                res += stack.pop()  # pop previous result

        return res + sign * num
