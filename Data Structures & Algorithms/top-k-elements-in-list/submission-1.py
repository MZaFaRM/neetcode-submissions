from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_lists = [[] for n in range(len(nums))]
        for key, value in freq.items():
            freq_lists[value - 1].append(key)
        
        result = []

        for freq_list in reversed(freq_lists):
            if not freq_list:
                continue

            for n in reversed(freq_list):
                result.append(n)
                if len(result) >= k:
                    return result