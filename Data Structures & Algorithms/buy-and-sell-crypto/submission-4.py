class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        i = 0
        j = 1
        P = 0
        while j < n:
            s = prices[j]
            b = prices[i]
            P = max(P, s - b)
            if s < b:
                i = j
            j += 1
        return P
