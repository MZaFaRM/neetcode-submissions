class Solution:
    def isValid(self, s: str) -> bool:
        v = {')': '(', '}': '{', ']':'['}
        n = ""
        for i in s:
            if i in v.values():
                n += i
            elif i in v.keys():
                try:
                    if v[i] != n[-1]:
                        return False
                    n = n[:-1]
                except IndexError:
                    return False
        if n:
            return False
        return True
        