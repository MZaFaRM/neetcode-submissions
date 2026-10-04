class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        len_stack = []
        lengths = {}
        for i, value in enumerate(heights):
            while len_stack and len_stack[-1][1] > value:
                length = len_stack.pop()
                lengths[length] = i - length[0]
            len_stack.append((i, value))
        
        n = len(heights)
        while len_stack:
            length = len_stack.pop()
            lengths[length] = n - length[0]

        print(lengths)
        for i, value in enumerate(reversed(heights)):
            while len_stack and len_stack[-1][1] > value:
                length = len_stack.pop()
                index = n - length[0] - 1, length[1]
                lengths[index] = (lengths[index] + (i - length[0] - 1)) * length[1]
            len_stack.append((i, value))
        
        n = len(heights)
        while len_stack:
            length = len_stack.pop()
            index = n - length[0] - 1, length[1]
            lengths[index] = (lengths[index] + (n - length[0] - 1)) * length[1]

        return max(lengths.values())


