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
            if L <= R:
                i += 1
                result += max(L - height[i], 0)
                L = max(L, height[i])
            else:
                j -= 1
                result += max(R - height[j], 0)
                R = max(R, height[j])

        return result

            

            
                


