class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        left = {"(", "{", "["}
        stack = []
        for l in s:
            if l in left:
                stack.append(l)
            else:
                if (len(stack) == 0) or (stack[-1] != pairs[l]):
                    return False
                else:
                    stack.pop()
                    
        return len(stack) == 0

