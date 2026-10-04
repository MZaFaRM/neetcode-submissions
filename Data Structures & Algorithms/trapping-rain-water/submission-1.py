class Solution:
    def trap(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_low = height[low]
        max_high = height[high]
        water = 0

        while low < high:
            if max_low < max_high:
                low += 1
                if height[low] > max_low:
                    max_low = height[low]
                else:
                    water += max_low - height[low]
            else:
                high -= 1
                if height[high] > max_high:
                    max_high = height[high]
                else:
                    water += max_high - height[high]
        return water