class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()
        n = len(nums)

        for k in range(n - 2):
            i, j = k + 1, n - 1

            target = -nums[k]
            while i < j:
                nums1 = nums[i]
                nums2 = nums[j]
                sum = nums1 + nums2

                if sum == target:
                    result.add((nums1, nums2, -target))
                    i += 1
                    j -= 1
                elif sum < target:
                    i += 1
                else:
                    j -= 1
        
        return [list(g) for g in result]



        