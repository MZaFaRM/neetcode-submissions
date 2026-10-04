class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            low = i+1
            high = n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    high -= 1
                    low += 1

                    while nums[low] == nums[low-1] and low < high:
                        low += 1
                        
                elif s < 0:
                    low += 1
                else:
                    high -= 1
        return result
            
