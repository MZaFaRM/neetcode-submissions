class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sum = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_sum:
                return [hash_sum[diff], i]
            hash_sum[n] = i


        