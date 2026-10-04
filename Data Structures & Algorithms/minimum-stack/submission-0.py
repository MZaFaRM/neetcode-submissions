class MinStack:

    def __init__(self):
        self.stack = []
        self.min_curr = -1

    def push(self, val: int) -> None:
        self.stack.append((val, self.min_curr))

        if val <= self.stack[self.min_curr][0]:
            self.min_curr = len(self.stack) - 1

    def pop(self) -> None:
        _, self.min_curr = self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[self.min_curr][0]
