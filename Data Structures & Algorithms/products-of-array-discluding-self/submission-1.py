class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left = [1]
        right = [1]
        result = []

        for i in range(1, n):
            left.append(nums[i-1] * left[-1])
            right.append(nums[n-i] * right[-1])

        result = []
        for i in range(n):
            result.append(left[i] * right[n-i-1])

        return result
        