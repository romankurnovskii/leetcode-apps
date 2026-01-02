class Solution:
    def evaluate(self, expression: str) -> int:
        stack = []
        i = 0
        n = len(expression)

        while i < n:
            if expression[i] == " ":
                i += 1
                continue

            if expression[i] == "(":
                stack.append("(")
                i += 1
            elif expression[i] == ")":
                values = []
                while stack and stack[-1] != "(":
                    values.append(stack.pop())

                if stack:
                    stack.pop()

                if values:
                    op = values.pop()
                    if op == "+":
                        res = sum(values)
                    elif op == "-":
                        res = (
                            values[0] - sum(values[1:])
                            if len(values) > 1
                            else -values[0]
                        )
                    elif op == "*":
                        res = 1
                        for v in values:
                            res *= v
                    else:
                        res = values[0] if values else 0
                    stack.append(res)

                i += 1
            elif expression[i].isdigit() or expression[i] == "-":
                num_str = ""
                if expression[i] == "-":
                    num_str = "-"
                    i += 1
                while i < n and expression[i].isdigit():
                    num_str += expression[i]
                    i += 1
                stack.append(int(num_str))
            else:
                i += 1

        return stack[0] if stack else 0
