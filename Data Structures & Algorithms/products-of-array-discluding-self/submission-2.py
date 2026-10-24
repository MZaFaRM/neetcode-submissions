class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = nums.copy()

        result[0] = 1
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        mul = 1
        for i in range(n-2, -1, -1):
            mul *= nums[i+1]
            result[i] *= mul
        
        return result