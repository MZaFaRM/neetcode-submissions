class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        result = 0

        while i < j:
            difference = j - i
            if heights[i] < heights[j]:
                smallest = heights[i]
            else:
                smallest = heights[j]

            area = difference * smallest

            if area > result:
                result = area

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return result