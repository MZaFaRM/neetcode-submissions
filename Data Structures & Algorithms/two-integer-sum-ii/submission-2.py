class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) - 1
        while i < n:
            diff = target - numbers[i]
            j = i + 1
            while j <= n and diff >= numbers[j]:
                if diff == numbers[j]:
                    return [i+1, j+1]
                else:
                    j += 1
            i += 1