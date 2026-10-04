class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * len(nums)
        i = 1
        while i < n:
            output[i] = nums[i-1] * output[i-1]
            i += 1

        i = n - 2
        k = nums[-1]
        while i >= 0:
            output[i] = output[i] * k
            k *= nums[i]
            i -= 1
        return output