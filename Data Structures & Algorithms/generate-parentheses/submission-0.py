class Solution(object):
    def generateParenthesis(self, n):
        self.result = []
        self.backtrack(n, n, [])
        return self.result

    def backtrack(self, left, right, current):
        if right == 0:
            self.result.append("".join(current))
            return
        if left > 0:
            current.append("(")
            self.backtrack(left-1, right, current)
            current.pop()
        if left < right:
            current.append(")")
            self.backtrack(left, right-1, current)
            current.pop()