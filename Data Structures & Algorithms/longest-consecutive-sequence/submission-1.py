class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0
        for num in store:
            if (num - 1) not in store:
                curr = num + 1
                while (curr) in store:
                    curr += 1
                longest = max(curr - num, longest)
        return longest