class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        k = len(s) - 1
        s = s.lower()
        while True:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while k > 0 and not s[k].isalnum():
                k -= 1
            if k < i:
                return True
            elif s[i] == s[k]:
                i += 1
                k -= 1
            else:
                return False
        