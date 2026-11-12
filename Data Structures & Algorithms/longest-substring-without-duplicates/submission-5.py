class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        seen = set()
        i = 0
        j = 0
        L = 0

        while j < n:
            if s[j] in seen:
                L = max(L, len(seen))
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
            seen.add(s[j])
            j += 1
        return max(L, len(seen))
            