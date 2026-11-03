class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(0)

        elif val < self.stack[self.mins[-1]]:
            self.mins.append(len(self.stack) - 1)
        

    def pop(self) -> None:
        n = len(self.stack) - 1
        if n == self.mins[-1]:
            self.mins.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.mins[-1]]
        
