class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        length = 0
        j = 0
        subset = set()
        
        for i in range(len(s)):
            if s[i] in subset:
                if length > longest:
                    longest = length

                while s[i] in subset:
                    subset.remove(s[j])
                    j += 1

            subset.add(s[i])
            length = len(subset)

        if length > longest: 
            return length
        else:
            return longest
        