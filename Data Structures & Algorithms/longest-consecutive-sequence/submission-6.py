class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        largest = 0

        for n in nums:
            if n - 1 in hash_nums:
                continue
            else:
                length = 1
                i = n + 1
                while i in hash_nums:
                    length += 1
                    i += 1
                if length > largest:
                    largest = length
        return largest

            