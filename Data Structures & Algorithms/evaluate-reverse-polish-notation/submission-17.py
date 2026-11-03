class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in {"+", "*", "/", "-"}:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    r = a + b
                elif i == '-':
                    r = a - b
                elif i == '*':
                    r = a * b
                elif i == '/':
                    r = int(a / b)
                stack.append(r)
            else:
                token = int(i)
                stack.append(token)
        return stack[-1]
        