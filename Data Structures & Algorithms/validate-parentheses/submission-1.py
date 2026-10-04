class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = {"[", "{", "("}
        for curr in s:
            if curr in o:
                stack.append(curr)
            elif len(stack) <= 0:
                return False
            else:
                last = stack.pop()
                if (last == "[" and curr == "]") or (last == "(" and curr == ")") or (last == "{" and curr == "}"):
                    pass
                else:
                    return False
        return not bool(stack)
        