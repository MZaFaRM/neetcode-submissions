class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = dict()
        for l in s:
            seens[l] = seens.get(l, 0) + 1
        for l in t:
            if l not in seens:
                return False
            seens[l] -= 1
            if seens[l] == 0:
                seens.pop(l)
        return len(seens) == 0
            