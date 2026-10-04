class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        hash_table = {num: i for i, num in enumerate(nums)}

        i = -1
        while i < n:
            i += 1
            key = target - nums[i]
            j = hash_table.get(key, None)
            if j is not None and j != i:
                return [i, j]