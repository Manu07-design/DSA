class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        operations = {
            "+": lambda a, b: b + a,
            "-": lambda a, b: b - a,
            "*": lambda a, b: b * a,
            "/": lambda a, b: int(float(b) / a)
        }

        for token in tokens:
            if token in operations:
                a = stack.pop()
                b = stack.pop()
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))

        return stack[-1]