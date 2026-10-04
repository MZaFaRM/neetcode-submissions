class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for num in nums:
            if hash_table.get(num, None):
                return True
            else:
                hash_table[num] = 1
        return False
         