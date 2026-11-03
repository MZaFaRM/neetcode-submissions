class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        for i in tokens:
            isdigit = False
            if len(i) <= 1:
                isdigit = i in numbers
            else:
                isdigit = i[1] in numbers

            if isdigit:
                token = int(i)
                stack.append(token)
            else:
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
        return stack[-1]
        