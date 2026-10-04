class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for op in tokens:
            if op in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                if op == "+":
                    stack.append(num1 + num2)
                elif op == "-":
                    stack.append(num1 - num2)
                elif op == "/":
                    stack.append(int(num1 / num2))
                elif op == "*":
                    stack.append(num1 * num2)
            else:
                stack.append(int(op))
        return stack[-1]
    