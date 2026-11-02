class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n <= 1:
            return 0

        i, j = 0, n-1

        L = height[i]
        R = height[j]

        result = 0

        while i < j:
            curr = i + 1
            while L <= R and i < j:
                result += max(L - height[curr], 0)
                L = max(L, height[curr])
                i = curr
                curr += 1
            
            curr = j - 1
            while R <= L and i < j:
                result += max(R - height[curr], 0)
                R = max(R, height[curr])
                j = curr
                curr -= 1

        return result

            

            
                


