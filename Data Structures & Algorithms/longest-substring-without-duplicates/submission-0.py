class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        j = 0
        subset = set()
        
        for i in range(len(s)):
            if s[i] not in subset:
                subset.add(s[i])
            else:
                while s[i] in subset:
                    subset.remove(s[j])
                    j += 1
                subset.add(s[i])

            longest = max(len(subset), longest) 
        return longest
        