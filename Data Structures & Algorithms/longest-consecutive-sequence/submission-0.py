class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) in store:
                continue

            seq = 1
            while (num + seq) in store:
                seq += 1
            
            longest = max(seq, longest)
        return longest