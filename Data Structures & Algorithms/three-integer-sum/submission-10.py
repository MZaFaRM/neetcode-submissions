class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        n = len(nums)

        for k in range(n - 2):
            if k != 0 and nums[k] == nums[k-1]:
                continue

            i, j = k + 1, n - 1

            target = -nums[k]
            while i < j:
                nums1 = nums[i]
                nums2 = nums[j]
                sum = nums1 + nums2

                if sum == target:
                    result.append([nums1, nums2, -target])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif sum < target:
                    i += 1
                else:
                    j -= 1

        
        return result



        