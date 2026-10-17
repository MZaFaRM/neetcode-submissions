from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        char_map = defaultdict(int)
        for i in range(n):
            char_map[s[i]] += 1
            char_map[t[i]] -= 1
        
        return set(char_map.values()) == {0}