class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        n = len(nums)
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        bucket = [[] for i in range(len(nums))]
        for key, value in freq.items():
            bucket[value-1].append(key)

        output = []
        i = n-1
        while i >= 0:
            if k == 0:
                break
            elif not bucket[i]:
                i -= 1
                continue
            output.append(bucket[i].pop())
            k -= 1
        return output