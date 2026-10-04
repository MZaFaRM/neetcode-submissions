class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for time, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                point, index = stack.pop()
                result[index] = time - index
            stack.append((temp, time))
        return result

        